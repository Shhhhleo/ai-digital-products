# Build pipeline (proven on The Desk Body Reset and The GLP-1 Off-Ramp)

The detailed, tested steps the agents follow. Ted uses Step 2, Mike Steps 3-4, Peter Steps 5-6, Luis Steps 7-9 (and runs the two evaluation passes in agents/luis.md). Read only the steps for your role. In Partner mode the product is personalised to the creator and their audience; everything else stays the same.

## Contents
- The 5 unlocks and the product promise
- Pocket scoring (Synthesise's formula)
- Step 2: Synthesise the research (150+ sources)
- Step 3: Package the e-book
- Step 4: Listing images
- Step 5: Website identity brief
- Step 6: Sales website
- Step 7: Launch on Whop (A product, B website, B2 payments, C checks)
- Step 8: Distribute
- Step 9: Check results honestly
- Logging

## The 5 unlocks (the filter for every decision)
A product sells when it ticks all five, in order: Pain → Worsening pain → Transformation → Specificity → Speed.

1. Pain. The product must fix a real problem people already think about. A watermelon-cutting guide fails because nobody has that problem. Pain beats pleasure: people move about 2x harder away from pain than toward pleasure (toothache vs nicer teeth). Core pain areas: wealth, health, relationships.
2. Worsening pain. Sensitive → dull ache → throbbing → urgency. Urgency is where demand peaks.
3. Transformation. People pay to go from Point A to Point B, not for content. Map Point A (feels, fears, avoids, sees self) and Point B. Describe the problem better than they can and they trust you with the fix.
4. Specificity. Parents → dads → divorced dads with teenage sons. Specific enough to feel seen, common enough to have volume. No empty keywords ("busy moms").
5. Speed. 20 pages that fix it beat 200 that don't.

Product promise: I help [specific who, stuck in X] get to [Point B] in [time] without [method they hate].

Intrinsic vs borrowed value (VIP Session 3): intrinsic value comes from the product itself solving the problem; borrowed value comes from who stands behind it (a plain jersey vs a jersey signed by Ronaldo). A creator partnership adds borrowed value on top of a product that must already have intrinsic value. Never rely on the creator's name to carry a weak product.

## Pocket scoring (out of 10, Synthesise's formula)
- Pain (x0.4): how much and how often it hurts.
- Worsening (x0.2): getting worse now; a pain that peaked years ago scores 3 or less.
- Purchasing Power (x0.2): can and will this group pay? Broke or freebie-hunting groups score low.
- Speed (x0.2): fast visible result, and buildable quickly in the chosen format.
Overall = 0.4 x Pain + 0.2 x Worsening + 0.2 x Purchasing Power + 0.2 x Speed. Cap a sub-score at 6 if it rests only on inference.

Discovery (Solo mode, no topic): seed from wealth, health, relationships and everyday industries (parenting, study and exams, careers and job loss, money and debt, fitness and weight, sleep, desk-work pain, gaming, pets, small business, ageing, new parents, students, side hustles). Find current triggers with web search (last 12 months). Fan out to 20+ candidates as who x stuck situation x trigger. Drop anything failing Pain or Worsening. Check demand for the top 6-8 on Google, Amazon (1-3 star reviews show the gaps), communities and paid supply (Whop, Etsy, Gumroad). Rank and recommend #1. Card fields: promise, industry, niche, Point A → Point B, specific knowledge, problem solved, evidence with links (source-backed / user-reported / hypothesis), one cheap validation test.

## Step 2: Synthesise the research (150+ sources)
- PubMed works through WebFetch on SEARCH pages only (article pages hit a CAPTCHA; eutils, EuropePMC and OpenAlex are blocked):
  - List: https://pubmed.ncbi.nlm.nih.gov/?term=QUERY&filter=pubt.systematicreview&filter=pubt.metaanalysis&filter=pubt.randomizedcontrolledtrial&size=50 (size must be 10/20/50/100/200; no OR operators)
  - Abstracts: a simple topical query plus &format=abstract&size=10
  - One page at a time (rate limits). Retry later if blocked.
- For non-health topics, use credible sources (studies, government data, reputable guides) and cite each one.
- Collect 150+ unique sources into refs.py grouped by topic. Read about 10 key abstracts for dose and effect claims. Claim only what the source supports. Be honest when evidence is weak, and tell the user how many were read in depth vs cited by title.
- Health and finance: education and habits framing, a disclaimer, a red-flags page, never medical or financial advice.

## Step 3: Package the e-book (PDF formats: e-books, workbooks, planners, packs)
Every picture, diagram, chart and icon in an e-book comes from Creative Claw (creative-claw-ebook.md); this step only typesets. Other formats: references/formats.md and higgsfield-playbook.md.
Organise the book as the transformation: open with Point A in the reader's words, give a staged plan to Point B, and end with a retest that proves the change. Keep it short (unlock 5).
Build as HTML, then PDF with Playwright (A4, printBackground). Fonts installed locally: Inter and Inter Display.
Design rules:
- A4, body 11-12pt, line-height 1.4-1.5, 45-75 characters per line, two fonts max, contrast 4.5:1.
- Contents page, short intro, a "who it's for" line, one feature box or visual per page, a cover readable as a thumbnail.
- Trackers and worksheets (a logbook helps people stick with it): baseline test, daily tracker, Day-N retest, one-page cheat sheet.
- Numbered citations, with a reference list giving each source's ID.
- Check a pdftoppm contact sheet visually. Fix overflow: fixed-height reference pages with column-fill:auto, and a smaller chunk on the first page.
Save to `03 Products/<Name>/`: the PDF, references.csv, product-notes.md and a source/ folder.

## Step 4: Listing images
E-book products: made in Creative Claw (creative-claw-ebook.md). All other products: Higgsfield (higgsfield-playbook.md §4, product-photoshoot or presets, device mockups of the real product). Partner mode only: 3 story frames and one 9:16 launch reel from Higgsfield for the creator to post (Solo mode has no social media).
Every product gets its own fresh image set. Never reuse, copy or lightly edit another product's images, covers or mockups. Buyers read the text on images, judge the product from them, and notice when the look is off.
- Generate new for this product: cover or key visual, 16:9 hero, 1200x630 banner, 1080x1080 social, 3 story frames, "what's inside" image, and any in-product visuals.
- Every image shows this product's real title, promise and real page renders. No placeholder or leftover text from another product.
- Style follows this product's Step 5 identity brief (palette, fonts, mood), so the images match its website and differ from every other product.
- Check before upload: read every word on each image, compare against product-notes.md, and look at all images side by side with the previous product's set. If any could be mistaken for another product, redo it. Log the image set in brand-registry.md.
- Whop media slot: 16:9, so make 1920x1080. Banner: about 1.9:1, so make 1200x630 with text in the central safe zone. Never put a portrait cover in the media slot. Also make a 1080x1080 for social.
- Composed listing images (cover mockup + fanned real page renders + title + pills): for e-books build them with Creative Claw's render_html_image; for other formats with Higgsfield (gpt_image_2_6 using the real product renders as references).
- Every generation is in the approved media plan; download each final into the product folder (Cloudfront URLs may not download from a cloud workspace, so save through the tool's own download or media URL).
- Write to /mnt/user-data/outputs, then commit into the product's marketplace/ folder.

## Step 5: Website identity brief (before any code)
Every product site must look like it belongs to its own category, not to Reset Lab. Copy the last site's wiring (Whop config, Lenis/GSAP setup, build scripts), never its look.

1. Research the category. Web search 3-4 strong sites and brands in the product's niche (top competitors, Awwwards/Godly/Dribbble for the category, leading apps and brands buyers already trust). Note their palettes, type, imagery and mood. Buyers trust what looks native to their world.
2. Pick a palette that follows the category's proven pattern, then make it ours. Reference patterns:
   - Health and body: clinical calm (off-white, sage, deep teal) or warm wellness (cream, terracotta, olive).
   - Weight and metabolic: fresh and hopeful (warm white, coral, deep forest), never "diet ad" neon.
   - Money and debt: trust and control (ink navy, paper white, one sharp green or gold accent).
   - Careers and AI: editorial tech (near-black, electric accent like lime or ultraviolet, mono details).
   - Parenting and family: soft, warm, rounded (butter, peach, sky blue, dark plum text).
   - Study and exams: focused and bright (white, cobalt, highlighter yellow).
   - Sleep and stress: night calm (midnight blue, lavender, moon cream).
   - Gaming: dark, high contrast, saturated accent (black, acid green or hot magenta).
   Define 5-7 tokens: bg, surface, ink, muted, accent, accent-2, line. Check 4.5:1 text contrast.
3. Pick typography for the mood and use only what is needed: one display face + one text face (optionally a mono for data). Sources: Google Fonts or Fontshare, self-hosted woff2, subset, font-display: swap, preload only the hero weight. Example pairings: editorial (Fraunces / Inter), clinical (General Sans / Inter), warm (Recoleta-style serif such as Young Serif / DM Sans), tech (Space Grotesk / IBM Plex Mono), friendly (Bricolage Grotesque / Nunito Sans), luxury-trust (Instrument Serif / Geist).
   Type scale: fluid with clamp(). Body 17-19px, line-height 1.5-1.65, 60-75 characters per line. H1 clamp(44px, 7vw, 112px), tight tracking (-0.02 to -0.04em) on display only. Max 2 weights per family. Every size comes from the scale; no stray values.
4. Hero concept unique to the product: a metaphor drawn from the pain or transformation (e.g. spine straightening for desk pain, a scale needle settling for GLP-1, a debt bar shrinking). The hero format may differ: scroll-locked video, live three.js object, kinetic typography, photographic split, or illustrated scene. Choose what fits the product, not the last one.
5. Distinctness check: keep D:\AI Income Challenge\05 Website Kit\brand-registry.md with one row per site (product, palette hexes, fonts, hero format, layout signature). A new site must differ from every row on palette family, at least one font, and hero format or layout. If it collides, change it.
6. Write website-brief.md: palette, fonts, scale, hero concept, motion mood, 3 reference sites, and why they fit the buyer. Then build.

## Step 6: Sales website
Built in Claude Code in D:\AI Income Challenge (Opus 5.5, effort extra, ultracode on; confirm at session start). Folder: 03 Products/<Name>/website. Start from 05 Website Kit for wiring only, then apply the Step 5 brief: rewrite all :root tokens in src/index.css, font files and the type scale. Product details live in src/content.ts.

Page order (fixed): the pain → why it's there → how to make it go away → the product (what's inside, page previews, phases) → evidence → price → FAQs. Add a searchable science/references page.

Components: use what the brief needs. The kit's MetroHero, PolishedShader and input.tsx are options, not defaults. Pull other pieces from 21st.dev and restyle them to the tokens. Drop anything that does not serve the page.

Motion: smooth and purposeful, styled to the brief (calm products move slowly, tech products can snap). Lenis on the GSAP ticker, masked heading reveals, fade-rise reveals, scrubbed highlights, counters, one pinned section, hover micro-interactions. Respect prefers-reduced-motion. Lazy-load three.js.

### Hero sharpness rules (no blurry heroes)
The Desk Body Reset hero looked soft because the frames were low resolution and upscaled. Every hero must pass these:
- Video: the hero loop comes from Higgsfield (Peter's website allowance in Mike's media plan): minimax_h3 at 2K or cinematic_studio_3_0 at 4K, never a 720p clip stretched. Master at 2560x1440 or higher (3840x2160 for full-bleed); upscale_video (topaz, 2160p) only on the final loop if needed. Encode two files: H.264 MP4 (ffmpeg -c:v libx264 -preset slow -crf 18 -profile:v high -pix_fmt yuv420p -movflags +faststart) and AV1 or VP9 WebM (crf 28-32). Serve a 1280-wide version to phones with <source media>. Target under 6 MB desktop, 2.5 MB phone; cut length before cutting quality.
- Recording a three.js or HyperFrames scene: render with deviceScaleFactor 2 at 1440x810 or more (true 2880x1620 pixels), at 60fps, lossless capture first, compress last.
- Live three.js instead of video when possible: it is pixel-perfect at any size. renderer.setPixelRatio(Math.min(devicePixelRatio, 2)), antialias on, resize on window change, particle size scaled by pixel ratio, enough particles that the shape reads as solid lines (dense enough at 2x, not a dusty haze).
- No CSS blur, scale() above 1, or heavy filter on the hero media. Glow comes from additive blending or a crisp bloom pass, not blur on the whole frame.
- Poster frame: a sharp WebP/AVIF still at the master resolution, shown before the video loads.
- Text in the hero is real HTML text, never baked into video.
- Quality gate: Playwright screenshot of the hero at 1440x900 with deviceScaleFactor 2, crop at 100% and look at edges. If lines look fuzzy, smeared or pixelated, re-render. Repeat on iPhone 13.

Before handing to Luis: build passes and the hero gate passes. The full checks are Luis's two evaluation passes; don't duplicate them.

## Step 7: Launch on Whop (product + website, one run)
One go-ahead from the user covers the whole launch: "Launch <product> at $<price>". Ask once, then run start to finish. Never enter tax, bank or ID details.

A. Create the product (Whop plugin, MCP or API first, checked against Whop's docs; the dashboard through the Chrome integration only for steps the API can't do)
1. Dashboard fallback: whop.com/dashboard/<biz>/products/create. Real clicks and typing (React ignores form_input). Read pages with get_page_text rather than screenshots.
2. Name → Labels (type, Return) → Paid access → billing One-time, price, Done (verify it closed).
3. Headline + description: click, type, verify with JS the text landed.
4. Media: file_upload the 1920x1080 image to input[type=file], then "Use image".
5. Apps → Content. Growth tools: Show discount OFF, member count OFF. Button text "Get access", affiliate 30%.
6. FAQs: max 5, re-find the "Add FAQ" ref each time, include the refund policy.
7. Create product. Banner: edit → "Add banner image" → upload 1200x630 → Use image → Save → Save product.
8. Attach the PDF: open the Content iframe src (whop.com/core/app/launch/?redirect=...apps.whop.com/seller-product/exp_...) in a new tab, hook HTMLInputElement.click for type=file, then title, welcome line, /file, upload, Publish (confirm "Published!").
9. Content visibility = gated to this product only.
10. Capture the IDs: product URL, plan_id (from the checkout link), experience ID. Write them to whop-listing.md immediately.

B. Wire and publish the website
11. Put the checkout URL https://whop.com/checkout/<plan_id> into src/content.ts. Every buy button uses it; never a custom payment form.
12. Create a Whop website app for the product (dashboard, or `npx whop apps init`), keeping vite.config.ts with the whop() plugin and build.outDir "dist/client".
13. `npm run build` → dist/whop-build.zip. Deploy with `npx whop apps deploy --app <app_id> --preview`, check the preview, then deploy to production. Cowork fallback: upload the zip in a whop.com tab and call whop.com/api/v1 files → app_builds → promote with the logged-in session (see website/DEPLOY.md).
14. Link both ways: add the website URL to the Whop product description/links, and set the site's subdomain to the product slug.

B2. Payments must work (no launch without this)
A page full of visitors earns $0 if checkout is broken. Before the site goes live:
- Confirm the product has an active paid plan (One-time, correct price, visible, not archived, stock unlimited). If missing, create it in the product's pricing options.
- Create a dedicated checkout link: dashboard → More → Checkout links → new link for this product's plan. Name it "<product> – website". Use that URL (or https://whop.com/checkout/<plan_id>) in src/content.ts.
- Check the business can actually take money: Settings → payouts / verification. If identity, tax or payout setup is incomplete and blocks charges, stop and tell the user exactly which screen to finish (never enter those details).
- Open the checkout URL in a logged-out incognito tab: the price shows, card and UPI/other methods render, the Pay button is enabled. Do not pay.
- Click every buy button on the live site (desktop and phone) and confirm each lands on that same checkout. Grep the built site for any old or placeholder checkout URLs.
- Ask the user for one real test purchase from a second account (then refund it). Only a Succeeded row on the Payments page proves payments work.

C. Launch checks
15. Open the live site, click every buy button and confirm it lands on the right Whop checkout and price (do not pay). Confirm the dashboard shows the new build live.
16. Run the hero sharpness gate on the live URL.
17. Record the live site URL, app ID, build ID and product URL in product-notes.md, brand-registry.md and the AIC project doc.
18. Tell the user what only they can do: confirm tax details, make a test purchase from another account.

Rollback: Versions in the dashboard, or `npx whop apps builds promote <abld_id>`.

## Step 8: Distribute
- Partner mode: the creator's audience is the distribution. Benji agrees the launch posts (reel, stories, link in bio, then a monthly mention); Mike supplies the story frames, reel and captions; Luis gives each channel its own tracking link.
- Solo mode: no social media and no creator. Buyers arrive through Whop's marketplace (Discover) and search. Luis lists the product with Snippy's keyword set in the title and description; Peter's page carries the same phrases; the store's 30% affiliate rate stays on so anyone can promote it. Luis gives the verdict after 30 days.
- Benchmark against a proven product in the pocket. Copy the packaging (one villain, bonuses, guarantee), never the overclaiming.
- The infinite game: expect early products to make $0. Keep pulling the lever with new pockets.

## Step 9: Check results honestly
Verify sales on the Payments page (Succeeded count), not the Home balance. If views are coming in but Payments shows 0 across every tab (including Failed and Pending), nobody even reached a working checkout: rerun the B2 payment checks on every live product before blaming the offer. The Home chart shows a fake placeholder value while loading.

## Logging
After each step, update product-notes.md and whop-listing.md in the product folder and the AIC project doc. Report back in short plain language: what's live, the link, and the one or two things only the user can do.