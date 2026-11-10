# Handoff schemas

## creators.csv (Whisky → Snippy)
Light card per creator. Column order matters for scripts/validate_creators.py.

| Column | Meaning |
|---|---|
| creator_id | <handle>-<YYYYMMDD> |
| handle | Instagram handle without @ |
| profile_url | https://www.instagram.com/<handle>/ |
| industry | e.g. Parenting |
| keyword_used | The Explore combo, e.g. "toddler sleep tips" |
| niche | One specific line |
| audience | One line: who follows them, stage of the problem |
| followers | Integer |
| median_views | Median of the last 10 reels, from the Reels grid |
| last_post_date | YYYY-MM-DD |
| selling_product | no / yes |
| selling_evidence | What the bio and link in bio showed |
| business_email | Exactly as published |
| email_source | bio / contact button / link in bio / website |
| language_country | e.g. English, US |
| top_pain | One line |
| evidence_link | One reel or post URL showing that pain |
| pocket_promise | I help [who] [result] in [time] without [hated method] |
| pain, worsening, purchasing_power, speed | 0-10 each |
| pocket_score | 0.4 x pain + 0.2 x (worsening + purchasing_power + speed), 1 decimal |
| suggested_format | ebook_bundle / pack / planner / notion_template / spreadsheet_tool / audio_programme / video_programme / challenge_kit / bundle |
| brand_safe | yes / no |
| found_date | YYYY-MM-DD |
| notes | Optional |

## contacts-master.csv (every agent updates it)
Columns: creator_id, handle, business_email, industry, run, status, status_date, notes.
Statuses: found → emailed → followup1 → followup2 → replied-interested / replied-question / not-now / opted-out / bounced / no-reply → negotiating → agreed → building → live → paused → ended.
opted-out is permanent across all runs.

## outbox.csv (Snippy)
creator_id, business_email, subject, body, send_day, sent_at, followup1_at, followup2_at, reply_category.

## interested.csv (Snippy → Benji)
creator_id, handle, business_email, reply_category, reply_date, reply_summary, thread_id.

## progress.md (any long job)
```
Job: <what>   Owner: <agent>   Updated: <date>
Done: <checkpoints finished>
Next: <the very next step>
Files: <paths touched>
Blockers: <none / message posted to X>
```

## pockets.csv (Whisky → Snippy, Solo mode)
pocket_id, who, stuck_situation, trigger, industry, pocket_promise, pain, worsening, purchasing_power, speed, pocket_score, evidence_links, notes.

## shortlist.md (Snippy → Benji, Solo mode)
Top 3 pockets, each with: verified demand numbers (paid products, price range, formats, review counts, search phrases), competitor teardown (3-5 products, promise, price, 1-3 star complaints), keyword set (10-15 phrases), positioning line.

## product-brief.md (Benji → Ted, both modes)
```
# Product brief: <working title>
Partner: <creator, @handle> | none (Solo)
Format: <one from formats.md> + companion asset (e-books)
On camera: creator's own footage | creator's likeness/voice with written consent | AI presenter | faceless
Media plan: 03 Products/<name>/media-plan.md (approved <date>, total credits)
Promise: I help [who] [result] in [time] without [hated method]
Audience: <who, stage, language, country>
Point A (their words): feels / fears / avoids / sees self
Point B: result / new self-image
Creator's method and signature tips: <list>
Never say or recommend: <list>
Must-cover audience questions: <list>
Length target: <pages / lessons and minutes / sessions / days / template scope>
Branding: by <creator> | <creator> x Reset Lab | Reset Lab
Price: <band>, launch price <$x>
Split: 50/50 after Whop fees (or as approved)
Launch window and creator posts: <dates, posts>
Creator's Whop account: <email/username>
Approvals: outline approved <date>; final approval needed before launch
```
