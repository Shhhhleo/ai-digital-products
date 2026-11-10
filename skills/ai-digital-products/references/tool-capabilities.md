# What Synthesise, ListKit and Whop do, and who does it here

For Advaith's reference. Agents rarely need to load this file.

Sources: Iman's VIP and Main Sessions 1-3 (Advaith's notes), Workbooks 1-2, ListKit's and Whop's own docs (checked Nov 2026). Recheck vendor docs before relying on a detail; features change.

## Synthesise (Iman's specialised AI, bundled with Monetise at $1,995)

| What it does | Who does it here | How |
|---|---|---|
| Scans Google, Amazon and communities for high-demand, low-competition topics; returns 20 ranked profitable pockets | Whisky (Solo mode) | Discovery in build-pipeline.md |
| "Use your own pocket": shapes a rough idea into a pocket card | Whisky | Mode B card |
| Pocket card: promise, industry, niche, specific knowledge, problem solved, scores for Pain, Worsening, Purchasing Power, Speed | Whisky | Same fields, same formula |
| Analyses a creator's Instagram handle to find their niche and topic | Whisky | Finds the creators himself, then analyses each (the user never pastes a handle) |
| Finds the profitable pockets inside that creator's audience | Whisky | From reels, captions and comments |
| Builds a visceral transformation map | Whisky (draft), Ted (final) | Point A → Point B in the audience's words |
| Synthesises 150+ real sources into one cited, step-by-step solution | Ted | Step 2 of build-pipeline.md |
| Produces the product in any format (45-page e-book in about 40 min, other formats) | Mike (from Ted's content pack) | formats.md; Creative Claw for e-book graphics, Higgsfield for all other media and video (higgsfield-playbook.md) |
| Does the branding | Mike (product), Peter (website identity) | Step 4 and Step 5 |
| Generates store page content | Mike (store-copy.md), Luis (listing) | Step 7 |
| Suggests the price | Benji with the creator | deal-and-pricing.md |
| Generates store image and store cover | Mike | Step 4 |
| Claimed: trained on $155M of digital product sales, so it knows what sells | Partly replaced | Paid-supply checks (Whop, Gumroad, Etsy, Amazon) as live demand evidence. This is the one thing we cannot fully copy; real sales data from our own launches is the substitute, so log every result. |

## ListKit (cold email platform; Iman's "secret bonus")

| What it does | Who does it here | How |
|---|---|---|
| Lead database with AI search (hundreds of millions of B2B contacts, triple-verified emails) | Whisky | Instagram Explore + web search + the 4 filters; only emails creators published themselves |
| Builds the list of ~100 creators into a CSV | Whisky | creators.csv, validated by scripts/validate_creators.py |
| Sets up sending domains and inboxes configured for outreach | The user | One dedicated outreach inbox (references/outreach-email.md). Claude cannot create accounts. |
| Inbox warm-up and deliverability protection | Snippy | Gradual ramp, daily caps, plain-text, no links in email 1 |
| Generates 3-step email sequences, personalisation, templates | Snippy | Email 1 + 2 follow-ups, personalised per creator |
| Schedules and sends the campaign | Snippy | Day-by-day schedule, sent through the email connector after the user's yes |
| Unified inbox for replies | Snippy | Reply sorting into Interested / Question / Not now / No / Bounce |
| Done-for-you managed service | Not used | |

Cost note: ListKit's all-in-one bundle is listed at about $597/month. The free path above gives a lower sending volume but costs nothing; it is the right start for a 50-creator batch.

## Whop (where everything is hosted, sold and delivered)
From VIP Session 3, Main Session 3 and Whop's docs:
- Hosts every format: e-books, digital assets, video programmes, digital minds (apps).
- Payments: one-time, monthly or yearly subscriptions, free trials, instalments / buy now pay later, card, crypto; 100+ payment methods across 195 countries, chosen automatically for each buyer's location.
- Delivery: instant access on purchase; content apps gate files to the product.
- Dashboard: every sale live, on the phone too.
- Tracking links: clicks, purchases and revenue per link.
- Free to start; Whop takes fees per sale.
- Custom tools as iFrame apps inside the Whop.
- Revenue share: add a partner by email, Whop username or user ID; the % applies to all products in the business unless overridden per product (see whop-partner-setup.md). The split is calculated after Whop's fees, and the partner's share is deposited into their Whop balance automatically on each completed transaction. This is what makes the 50/50 creator deal hands-off.
- Affiliates: separate from revenue share; anyone can promote with a tracked link for a commission.
- Websites: Whop website apps on a free whop.site subdomain (used for Reset Lab's live sites).
- Synthesise can write the store page, price and store images; here Mike and Peter do it.

Who uses Whop: Luis (product, website deploy, split, payments, tracking, reports), through the Whop plugin, MCP or CLI first.

## Other tools the agents may use (Claude Code)
- Chrome integration (claude --chrome): Instagram browsing (Whisky), Whop dashboard only when the API can't (Luis).
- Email MCP: the outreach inbox (Snippy, Benji), only when signed in to the dedicated account.
- Notion: digital asset templates (Mike). Google Drive/Docs/Sheets: briefs and trackers if the user prefers.
- Creative Claw, HyperFrames, ElevenLabs, Gamma, Higgsfield: images, voice, slides, presenter video (Mike). Ask before spending paid credits.
- Vercel / Lovable are not needed; Whop hosts the sites.
