# Outreach email: inbox, limits, templates, rules

## 1. The dedicated outreach inbox (the user sets this up)
Why separate: it protects the user's personal and school inboxes, keeps every creator thread in one place, and if anything gets flagged it is only this account.

Start (free): a new Gmail named for the business, e.g. advaith.resetlab@gmail.com. Then:
- Profile photo, display name "Advaith | Reset Lab", a short signature.
- Warm it by hand for 5-7 days before any cold email: send a few real emails to friends and get replies, subscribe to 2-3 newsletters, open and reply to them.
- Turn on 2-step verification.
Upgrade (when replies start or volume grows): a separate cheap domain (not resetlab's main site domain) plus a business mailbox, with SPF, DKIM and DMARC set up. Inbox placement and trust are much better, and it reads as a real business.

Connecting it (Claude Code): an email MCP server signed in to this outreach account (check /mcp). Gmail in the browser through the Chrome integration works as a fallback but costs far more usage. Snippy reads the connected address before every batch and stops if it is the personal or school account.

## 2. Sending limits (Snippy never exceeds these)
New free account:
- Week 1 of cold sending: max 10 per day.
- Week 2: max 20 per day.
- After that: max 30 per day.
Upgraded domain mailbox after 2 weeks of warm-up: start at 20 per day, ramp to 40.
Spread sends through the working day of the creator's time zone (roughly 9:00-17:00, Tue-Thu best), a few minutes apart. Never send all at once.
Run size follows the cap: 50 creators per run while the inbox is under 2 weeks old (about a week to send), up to 100 once it is warm (30 a day, about 4 days). That is correct, not slow: a burned inbox costs far more.
Stop all sending at the first spam warning, sending-limit message or bounce rate above 5%.

## 3. Email 1 (structure, not copy to paste)
Subject (short, lower case, about them): "your [niche] audience" / "idea for your followers" / "[the pain] product idea"
Body (80-130 words, plain text, no links, no attachments):
1. One specific line about their content: a reel, a repeated comment theme ("your comments are full of parents asking how to stop the 6pm meltdowns").
2. The idea in one sentence: a [format] that helps their audience [Point B] in [time] without [hated method], built from [150+] studies and their own method.
3. What they do: nothing except share it. We research, write, design, build the site, host, handle payments and delivery and support. No cost to them.
4. The split: 50/50 of every sale, paid to them automatically by Whop.
5. One easy question: "Want me to send you a one-page outline?"
Sign-off: Advaith, Reset Lab.
Last line: "Not for you? Just reply 'no' and I won't email again."

Example (parenting creator, adapt every time):
Subject: your toddler-sleep audience
Hi Maya, your bedtime-routine reels keep pulling the same comment: "this works until 2am, then what?" I'd love to build a short guide for your followers that gets toddlers sleeping through in 14 nights without cry-it-out, built from 150+ sleep studies plus your own routine. You wouldn't do any of the work: I research, write, design, build the sales page and handle payments and delivery. You'd just share it, and we split every sale 50/50, paid to you automatically through Whop. Want me to send a one-page outline?
Advaith, Reset Lab
Not for you? Just reply "no" and I won't email again.

## 4. Follow-ups (only if no reply of any kind)
Follow-up 1, 3 working days later, same thread, 2-3 lines: restate the outcome for their audience and the ask.
Follow-up 2, 7 working days after email 1, same thread, 1-2 lines, a graceful close: "Last note from me. If an outline for [promise] would help, just say and I'll send it."
Then stop. Each follow-up batch needs the user's yes.

## 5. Rules
- Only emails the creator published for business enquiries. No guessed, scraped or bought addresses.
- One creator, one thread; never email someone who said no; the opt-out is permanent across all runs (contacts-master.csv).
- Truthful subject lines, no fake "Re:", no fake urgency, no income promises.
- Identify the sender honestly: Advaith, Reset Lab. Emails are the user's, sent with his approval.
- US anti-spam rules (CAN-SPAM) expect a working opt-out and a valid postal address for commercial email; EU/UK rules expect a clear reason for contacting a business address and an easy opt-out. Keep the opt-out line in every email; once the business has a business or virtual mailbox address, add it to the signature. This is general information, not legal advice.
