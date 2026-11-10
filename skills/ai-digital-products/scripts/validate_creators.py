#!/usr/bin/env python3
"""Validate Whisky's creators.csv before Snippy uses it.

Checks every row against Iman's 4 filters, the schema, the pocket score
formula, duplicates, and the do-not-contact list in contacts-master.csv.

Usage:
    python validate_creators.py creators.csv [--master contacts-master.csv]
        [--target 50] [--write-pass passed.csv]

Failing rows are dropped, never padded. However many pass is the batch.
Exit code 0 when at least one row passes, 1 otherwise.
"""
import argparse
import csv
import re
import sys
from datetime import date, datetime

REQUIRED = [
    "creator_id", "handle", "profile_url", "industry", "keyword_used", "niche",
    "audience", "followers", "median_views", "last_post_date",
    "selling_product", "selling_evidence", "business_email", "email_source",
    "language_country", "top_pain", "evidence_link", "pocket_promise",
    "pain", "worsening", "purchasing_power", "speed", "pocket_score",
    "suggested_format", "brand_safe", "found_date", "notes",
]
FOLLOWERS = (10_000, 100_000)
VIEWS = (50_000, 200_000)
FORMATS = {"ebook_bundle", "pack", "planner", "notion_template",
           "spreadsheet_tool", "audio_programme", "video_programme",
           "challenge_kit", "bundle"}
BLOCKING_STATUSES = {"opted-out", "bounced"}
EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[A-Za-z]{2,}$")


def to_int(value):
    return int(str(value).replace(",", "").replace("_", "").strip())


def to_float(value):
    return float(str(value).strip())


def load_master(path):
    handles, emails = {}, {}
    if not path:
        return handles, emails
    try:
        with open(path, newline="", encoding="utf-8-sig") as f:
            for row in csv.DictReader(f):
                h = (row.get("handle") or "").lower().lstrip("@")
                e = (row.get("business_email") or "").lower()
                s = (row.get("status") or "").strip()
                if h:
                    handles[h] = s
                if e:
                    emails[e] = s
    except FileNotFoundError:
        print(f"note: master list {path} not found, treating as empty")
    return handles, emails


def check_row(row, master_handles, master_emails, seen_h, seen_e):
    errs = []
    missing = [c for c in REQUIRED if not str(row.get(c, "")).strip()
               and c not in ("notes", "selling_evidence")]
    if missing:
        errs.append("missing: " + ", ".join(missing))

    handle = (row.get("handle") or "").lower().lstrip("@")
    email = (row.get("business_email") or "").strip().lower()

    # Filter 1: views
    try:
        v = to_int(row["median_views"])
        if not VIEWS[0] <= v <= VIEWS[1]:
            errs.append(f"filter 1 views: median {v:,} outside 50K-200K")
    except (KeyError, ValueError):
        errs.append("filter 1 views: median_views not a number")
    # Filter 2: followers
    try:
        fl = to_int(row["followers"])
        if not FOLLOWERS[0] <= fl <= FOLLOWERS[1]:
            errs.append(f"filter 2 followers: {fl:,} outside 10K-100K")
    except (KeyError, ValueError):
        errs.append("filter 2 followers: not a number")
    # Filter 3: not already selling
    if (row.get("selling_product") or "").strip().lower() != "no":
        errs.append("filter 3: already selling a product (or not checked)")
    # Filter 4: business email
    if not EMAIL_RE.match(email):
        errs.append("filter 4: no valid business email")

    # Score formula
    try:
        p, w, pp, s = (to_float(row[k]) for k in
                       ("pain", "worsening", "purchasing_power", "speed"))
        for name, val in zip(("pain", "worsening", "purchasing_power", "speed"),
                             (p, w, pp, s)):
            if not 0 <= val <= 10:
                errs.append(f"{name} out of 0-10")
        expected = round(0.4 * p + 0.2 * (w + pp + s), 1)
        given = round(to_float(row["pocket_score"]), 1)
        if abs(expected - given) > 0.05:
            errs.append(f"pocket_score {given} should be {expected}")
    except (KeyError, ValueError):
        errs.append("scores not numeric")

    if (row.get("suggested_format") or "").strip() not in FORMATS:
        errs.append("suggested_format must be one of: " + ", ".join(sorted(FORMATS)))
    if (row.get("brand_safe") or "").strip().lower() != "yes":
        errs.append("not brand safe")

    # Activity: posted in the last 14 days (warning-level, still an error to fix)
    try:
        last = datetime.strptime(row["last_post_date"].strip(), "%Y-%m-%d").date()
        found = datetime.strptime(row["found_date"].strip(), "%Y-%m-%d").date()
        if (found - last).days > 14:
            errs.append(f"inactive: last post {last}, more than 14 days before {found}")
    except (KeyError, ValueError):
        errs.append("dates must be YYYY-MM-DD")

    # Duplicates and do-not-contact
    if handle in seen_h:
        errs.append("duplicate handle in this file")
    if email and email in seen_e:
        errs.append("duplicate email in this file")
    for key, book in ((handle, master_handles), (email, master_emails)):
        status = book.get(key)
        if status in BLOCKING_STATUSES:
            errs.append(f"do not contact: master status {status}")
        elif status:
            errs.append(f"already in contacts-master ({status})")
    seen_h.add(handle)
    if email:
        seen_e.add(email)
    return list(dict.fromkeys(errs))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("csv")
    ap.add_argument("--master")
    ap.add_argument("--target", type=int, default=50)
    ap.add_argument("--write-pass")
    a = ap.parse_args()

    with open(a.csv, newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        cols = reader.fieldnames or []
        rows = list(reader)

    absent = [c for c in REQUIRED if c not in cols]
    if absent:
        print("schema error, missing columns: " + ", ".join(absent))
        sys.exit(1)

    mh, me = load_master(a.master)
    seen_h, seen_e = set(), set()
    passed, failed = [], []
    for i, row in enumerate(rows, start=2):
        errs = check_row(row, mh, me, seen_h, seen_e)
        (failed if errs else passed).append((i, row, errs))

    for i, row, errs in failed:
        print(f"FAIL line {i} @{row.get('handle','?')}: " + "; ".join(errs))

    passed.sort(key=lambda t: float(t[1]["pocket_score"]), reverse=True)
    print(f"\n{len(passed)} passed, {len(failed)} failed, target {a.target}")
    if passed:
        top = ", ".join(f"@{r['handle']} ({r['pocket_score']})" for _, r, _ in passed[:5])
        print("top by pocket score: " + top)

    if a.write_pass and passed:
        with open(a.write_pass, "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=cols)
            w.writeheader()
            for _, r, _ in passed:
                w.writerow(r)
        print(f"wrote passing rows to {a.write_pass}")

    if len(passed) < a.target:
        print(f"{len(passed)} of {a.target}: that is the batch (search budget rule, do not widen)")
    sys.exit(0 if passed else 1)


if __name__ == "__main__":
    main()
