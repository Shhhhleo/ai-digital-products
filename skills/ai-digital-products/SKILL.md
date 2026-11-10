---
name: "ai-digital-products"
description: "AI digital product business run by a seven-agent team on Iman Gadzhi's Develop → Distribute → Deliver system, built for Claude Code. Whisky finds micro-creators and profitable pockets; Snippy emails creators (Solo: verifies the market); Benji agrees the 50/50 partnership and writes the brief; Ted synthesises 150+ sources; Mike builds the product in any format except digital minds plus ads and video (e-book graphics via Creative Claw, all else via Higgsfield); Peter builds the site; Luis leads throughout, evaluates twice and publishes on Whop. Solo mode works without a creator. Use whenever the user mentions AIC, Iman's challenge, profitable pockets, micro-creators, partnerships, ListKit, Synthesise, Whop, Higgsfield, Creative Claw, Reset Lab, a new digital product, a course, product ads, outreach, stand-up, or names an agent, even without saying 'skill'."
---

# AI Digital Products: the team

Iman's 3D system run by a team that works across days. State lives in files, so any session can pick up where the last one stopped.
Project folder: D:\AI Income Challenge. Read its CLAUDE.md first (folder map, live product IDs).

## The core idea (Main Session 3)
Hope marketing gives feast-or-famine income. Instead, put a specific product in front of predisposed buyers, rinse and repeat. Micro-creators (10K-100K followers, one topic) have loyal audiences and nothing to sell them. Partner with one, personalise the product to their audience, publish on Whop, which takes payment, delivers and splits the money. One partnership can change everything; most emails get ignored, which is normal.
The 5 unlocks, product promise and pocket score are in references/build-pipeline.md (top section).

## The team
| Agent | Runs as | Model | Job |
|---|---|---|---|
Order: Whisky → Snippy → Benji → Ted → Mike → Peter, with Luis working throughout.

| Agent | Runs as | Model | Partner mode | Solo mode (no creator) |
|---|---|---|---|---|
| Whisky | Subagent | sonnet | Finds 50-100 creators passing the 4 filters, light pocket card each | Finds 20+ pockets with raw evidence |
| Snippy | Subagent | haiku | Sorts, emails creators, follows up, sorts replies | Sorts and verifies pockets, competitor teardown, buyer keyword set, shortlist (no social media, no emails) |
| Benji | Subagent | sonnet | Talks to interested creators, format, 50/50 terms, brief | Picks the winner, buyer language, offer and price, brief; later buyer support and reviews |
| Ted | Subagent | inherit | 150+ source synthesis into the full content pack | same |
| Mike | Subagent | inherit | Builds the product in its format, media plan, all product media and sales assets | same |
| Peter | Subagent | inherit | Builds the sales website, hands it to Luis unpublished | same, plus search-friendly copy |
| Luis | Main session (lead) | your session model | Stand-ups and feedback, approvals queue, evaluates everything twice, publishes on Whop's free domain, runs the store | same, with a 30-day verdict |
Briefs: agents/<name>.md. Luis's brief is agents/luis.md and is read by the main session itself.

## First run in Claude Code (one-time setup)
1. Copy agents/whisky.md, snippy.md, benji.md, ted.md, mike.md, peter.md into D:\AI Income Challenge\.claude\agents\ so Claude Code can dispatch them as real subagents (each gets its own context and model). Do not copy luis.md.
2. Copy references/team-board.md's template to D:\AI Income Challenge\04 Creator Pipeline\TEAM-BOARD.md.
3. Chrome: start with `claude --chrome` or run /chrome (Whisky needs Instagram; the user is logged in).
   Media: Higgsfield and Creative Claw connectors signed in (check /mcp).
4. Email: an MCP connector signed in to the outreach inbox (check /mcp). Whop: the Whop plugin (`/plugin marketplace add whopio/plugins`, then `/plugin install whop@whop`) or its MCP server, so Luis works through the API instead of clicking the dashboard.
In Cowork or chat (rare): no subagent files; the session plays each role in turn, reading that agent's brief.

## How the team works together
Subagents cannot message each other live, so the team talks through one shared file and through Luis.
- TEAM-BOARD.md (04 Creator Pipeline): open tasks (owner, status, depends on, due), agent-to-agent messages, the Needs Advaith list, and decisions. Protocol in references/team-board.md.
- Every agent starts by reading the board: its tasks and messages addressed to it. It ends by updating its tasks, posting messages to whoever it needs (e.g. Ted → Benji: "ask the creator if they want cry-it-out mentioned at all") and adding anything that needs Advaith.
- Luis reads the whole board in every stand-up, answers or reassigns messages, gives feedback, and dispatches the next agents. Agents never wait on each other inside a session; they leave a message and stop.

## Working across days
No session runs for days. Each run does one chunk, saves a checkpoint, stops.
- Trigger: "Luis, stand-up" (daily), or a scheduled headless run (`claude -p "Luis: daily stand-up, read-only"` from Windows Task Scheduler). Scheduled runs only read, draft and report; anything that sends or publishes waits in the approvals queue for Advaith.
- Checkpoints: every long job writes progress.md in its folder (done, next step, files touched). Ted saves research in batches and content chapter by chapter; Mike saves the product section by section; Peter saves the site by section. A new session reads progress.md and continues; it never restarts finished work.
- Replies from creators arrive while nobody is running. Snippy and Benji pick them up at the next stand-up.

## Modes
- Partner mode (default): Whisky → Snippy → Benji → Ted → Mike → Peter, Luis throughout; the creator brings the audience.
- Solo mode: when Advaith says no partner ("solo", "no creator"). All seven still work (Solo column above). No social media and no emails: buyers come through Whop's marketplace and search, so Snippy's verification and keywords replace outreach.
- Single agent: "run Whisky", "Snippy check replies", "Benji update" runs that agent on the latest run.

## Defaults (no option questions)
Pick what Iman teaches, state it in one line, carry on.
- Run size: 50 creators while the outreach inbox is under 2 weeks old; up to 100 once it is warm (2+ weeks of sending, bounces under 5%). Whatever passes the filters within Whisky's search budget is the batch, even if short.
- Format: the best fit for the transformation from references/formats.md, any format except digital minds. A plain e-book alone is never the default; an e-book always ships with a companion asset.
- Price rises with complexity: simple $19-37, tools and audio $37-67, programmes and challenge kits $77-150, bundles up to $150 (references/formats.md).
- Split: 50/50 after Whop fees, paid automatically by Whop.
- Media rule: e-books get every image and graphic from Creative Claw; every other format's images, and all video for any product, come from Higgsfield. Mike prices everything in a media plan first (including Peter's website allowance); one yes per product covers that spend.

## Approvals (Advaith's yes in chat, collected by Luis in one queue)
1. Each email batch (Snippy): sending address, count, schedule, 3 samples.
2. Benji's replies to creators (batch-approve).
3. Anything signed, and any term other than 50/50.
4. Each product's media plan (credit totals for Creative Claw and Higgsfield).
5. Publishing and price: "Launch <product> at $<price>" covers Luis's whole launch run.
Never create accounts, enter passwords, bank, tax or ID details, or pay for anything. Emails go out as Advaith, Reset Lab; agent names stay internal.

## Usage budget (every agent follows this)
- Whop handles delivery to buyers once Luis attaches the files; no agent manages delivery.
- Read only the files a task needs; never re-read a reference already in context.
- Browser: read page text and the accessibility tree, not screenshots. Screenshot only for visual QA (hero, images, final pages).
- Whop: API or CLI first, the dashboard only when the API cannot do it.
- Whisky does a light card per creator; deep analysis happens only for creators who reply (Benji).
- Snippy fills one template with two personalised lines per creator, in one outbox.csv.
- Handoffs and board updates: 5 lines max. Reports to Advaith: short.
- No re-running finished work: check progress.md first.

## Folder layout
```
D:\AI Income Challenge\
  .claude\agents\                    whisky, snippy, benji, ted, mike
  04 Creator Pipeline\               (if 04 is taken, next free number; note it in CLAUDE.md)
    TEAM-BOARD.md
    contacts-master.csv              everyone ever found + status; do-not-contact list
    runs\<YYYY-MM-DD>-<seed>\01-whisky\creators.csv (Solo: pockets.csv, evidence.md), summary.md
                            \02-snippy\outbox.csv, replies.md, interested.csv (Solo: shortlist.md)
    partners\<handle>\conversation-log.md, deal-terms.md, agreement.md, product-brief.md
  03 Products\<Product name>\        content\ (Ted), product + media-plan.md (Mike), website\ (Peter), launch-report.md, store-ops.md (Luis)
```
CSV columns and the brief template: references/handoff-schemas.md. Validate Whisky's CSV with scripts/validate_creators.py.

## Honest expectations
Cold email replies run in single digits: 50 emails might give 0-3 interested creators. Plan on 0.1-1% of a creator's followers buying at launch. Distribution does most of the work in Iman's case studies, but the creator's name is on the product, so it must be genuinely good.
Solo mode has no borrowed audience and no social media, so traffic comes only from Whop's marketplace and search. Expect slower sales; Luis judges a Solo product after 30 days, not 7.

## Reference map (load on demand)
formats.md (catalogue, choosing, prices, delivery) · higgsfield-playbook.md (programmes, ads, motion graphics, short and long video, storyboards, models) · creative-claw-ebook.md (e-book graphics) · build-pipeline.md (proven build steps) · team-board.md · handoff-schemas.md · outreach-email.md · deal-and-pricing.md · whop-partner-setup.md · tool-capabilities.md (what Synthesise, ListKit and Whop do; for Advaith, agents rarely need it)
