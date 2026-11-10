# Higgsfield playbook (every non-e-book format, and all video)

Learned from Higgsfield's own MCP catalogue (Nov 2026): its workflow list, model catalogue, presets and tool contracts. Higgsfield changes often, so its own workflow files are the authority: before any multi-step job, load the matching workflow with `get_workflow_instructions({workflow:"<name>"})` and follow it. This file tells you which one, which model, and our house rules.

## Contents
1. House rules (credits, projects, batching, consent)
2. Routing: deliverable → Higgsfield workflow or preset
3. Pre-recorded programmes
4. Product ads
5. Motion graphics
6. Short-form video
7. Long-form video
8. Storyboards
9. Images, audio, finishing tools
10. Model cheat sheet

## 1. House rules
- Media plan first. Before generating, list every asset with its model and settings, price each with `get_cost:true` (image, video, audio, outpaint, upscale_image, reframe) or `ads_studio_quote`, add them up, and put the total in media-plan.md. Luis queues it; Advaith's one yes covers that plan. A run that will exceed the plan by more than 20% stops and re-asks.
- Never pass `use_unlim` unless Advaith asks to use free generations. Never buy credits or plans; if credits run out, say so and stop.
- One Higgsfield project per product: `get_preferences`, then `create_project` (name = product name), and pass its `folder_id` on every generation so all assets stay together.
- Two or more independent generations go through the batch tools (`generate_image_batch`, `generate_video_batch`, `generate_audio_batch`, max 12 per call), then `jobs_wait` (groups of 12), then one `show_generation_by_ids`. Single user-facing generations use the plain `generate_*` tool.
- On a timeout, never resubmit blindly: keep the job ids and check them first. Retries reuse the same references.
- Upload local files with `media_upload` → PUT → `media_confirm`, or `media_import_url` for web files; generations take media ids, not URLs.
- Real people: the creator's face or voice only with their written consent recorded in deal-terms.md (Soul training needs 5-20 of their photos; `create_voice` clones a voice). Never a likeness of anyone else. No brand, studio or character names in prompts.
- Posting: Higgsfield can publish to TikTok, but posting is public content in Advaith's or the creator's name. Only after an explicit yes, and normally the creator posts their own.
- Save every final asset's media id and URL in the product's media-plan.md (the asset ledger). Reuse ids instead of regenerating.

## 2. Routing
| Deliverable | Use |
|---|---|
| Video programme module, narrated, no presenter | workflow `faceless-video` (channel type Explainer) |
| Module or reel with an AI presenter talking to camera | `/shorts` preset (`get_preset_instructions`), or workflow `narration` to put a consenting person's photo in as the on-screen narrator |
| Editing the creator's own footage, captions, assembly | workflows `video-montage` (cuts, soundtrack, captions), `video-editing` (native motion graphics), reel effects such as `/captions`, `/katana-bold`, `/text-behind` |
| Static ad creatives with copy (Meta, Instagram) | workflow `ads-studio` |
| UGC video ads (review, tutorial, unboxing, website tour) | workflow `ugc-video` |
| One-click product video ad, 12-15 s | model `marketing_studio_video` (presets via Marketing Studio) |
| Story ad with characters | `/drama-ads` |
| Variants of one ad (new hook, market, language) | workflow `ad-multiplier`; `/marketing-hook-variants` |
| Product stills, mockups, banners | workflow `product-photoshoot`; presets `/hero-shot`, `/before-after`, `/benefits`, `/whats-inside`, `/three-reasons`, `/how-it-works`, `/saveable-tip`, `/swipe-opener`, `/reel-cover` |
| Video or reel thumbnail and cover | workflow `thumbnail-generation` |
| Consistent cast for a programme | workflow `character-sheet`, then Elements |
| Faceless "what if" shorts | `/content-factory` |
| Logo, brand kit, social graphics | workflow `brand-asset-creation` |
Not used: Higgsfield's website builder (Whop hosts our sites), 3D Jutsu, games, AI Influencer (unless a product needs a mascot).

## 3. Pre-recorded programmes
Structure (from the brief): 5-10 lessons in a set order, each one result, 2-6 minutes, each building on the last, plus a workbook PDF and a quick-start lesson.
- Faceless lessons: `faceless-video`, Explainer type. It locks one style key, an asset roster (characters, locations, props), one narrator voice and burned captions, and assembles in its own sandbox. Lessons are built from 10-second blocks; a 3-minute lesson is 18 blocks. Animated mode looks premium; Still pictures mode (one image per spoken line) costs far less, so use it for text-heavy lessons and animated mode for the lessons that show movement.
- Keep the whole programme one look: reuse the first lesson's style key, voice pair and assets (its printed "channel DNA") for every later lesson.
- Presenter lessons: the creator's own recordings if they want to be on camera (edit with `video-montage`); otherwise `/shorts` with an AI presenter or the creator's consented Soul, set to 16:9 for lessons.
- Voice: one `list_voices` pick (or the creator's consented cloned voice) locked for the whole programme.
- Languages: `dubbing` translates and lip-syncs a finished lesson into 18 languages, including Hindi; a cheap second edition.
- Delivery: finished MP4s to Whop's Courses app (Luis), workbook in the Content app.

## 4. Product ads (for our digital products)
A digital product needs a physical-looking stand-in: a tablet, laptop or phone showing the real cover and pages, a printed workbook on a desk, the planner open beside coffee.
- Stills: `product-photoshoot` or presets (`/hero-shot`, `/before-after`, `/in-hand`, `/on-desk`, `/flatlay`), with the real cover uploaded as the product image.
- Static ads with copy: `ads-studio` (add the product from its Whop page URL; quote; approve; generate).
- Video ads: `marketing_studio_video` 9:16 for reels; `ugc-video` for a creator-style review; `/drama-ads` for a story hook. Ad variants with `ad-multiplier`.
- Score before posting: `virality_predictor` on the finished video (hook strength, retention risk).

## 5. Motion graphics
- Animated titles, lower thirds, text cards, overlays on footage: workflow `video-editing` (Higgsedit).
- Talking-head effects (kinetic words, text behind the head, stat callouts): `/katana-bold`, `/text-behind`, `/glass-graph`, `/tier-list`, `/over-the-shoulder`, `/freeze-frame`.
- Explainer-style motion graphics as a look: `faceless-video` with the Editorial Motion Graphics style.
- After Effects-grade work (`/kinetic-typography`, `/logo-animation`, `/motion-bundle`, `/presentation-animation`, `/saas-animation`) needs After Effects installed locally (`/use-after-effects`); only if Advaith has it.

## 6. Short-form video (reels, Shorts, TikTok, 9:16)
- AI presenter reel up to about 2 minutes: `/shorts` (hook-first script, presenter, captions, motion design, music).
- Faceless explainer reel: `faceless-video` at 9:16, 30-60 s.
- Product teaser: `marketing_studio_video` at 9:16.
- Turn a 16:9 lesson into a vertical clip: `reframe` to 9:16.
- Cover: `/reel-cover` or `thumbnail-generation`. Check with `virality_predictor`.
Always pass `aspect_ratio:"9:16"` explicitly; some models default to 16:9.

## 7. Long-form video
- Narrated long-form (10+ minutes): `faceless-video` long-form direction (chapters, era map), or a programme of chained lessons.
- Individual cinematic shots: `seedance_2_5` (up to 30 s per shot, can edit or extend a clip), `cinematic_studio_video_4_0` (camera, lens, lighting, genre controls, up to 30 s), `cinematic_studio_3_0` (up to 15 s, 4K).
- Assemble shots, music and captions with `video-montage`; optional 4K finish with `upscale_video` (provider topaz, 2160p) on the final cut only.

## 8. Storyboards (before any expensive video)
1. Script → shot list (shot number, size, angle, action, line, duration).
2. Lock the cast and props: `character-sheet`, then save each as an Element (`manage_reference_elements` create) and put `<<<element_id>>>` in prompts for consistency. A real, consenting person: train a Soul (`show_characters` train, 5-20 photos; only `soul_2` / `soul_cinematic` use it).
3. One keyframe still per shot with `generate_image_batch` (`gpt_image_2_6` default; `nano_banana_pro` for 4K hero frames), same style words in every prompt.
4. Show the storyboard grid, approve or fix individual frames.
5. Animate from the approved keyframes as `start_image` (and `end_image` where useful): `seedance_2_5` with `draft:true` renders cheap 480p drafts; finalise only the approved drafts at 1080p with `draft_job_id` within 7 days. `minimax_h3` (2K, keyframes, many references) for faceless-style blocks; `kling3_0` for multi-shot clips with sound (needs a `start_image` when using Elements).

## 9. Images, audio, finishing tools
- Images: `gpt_image_2_6` (default, text and typography, editing, native GIF/SVG), `marketing_studio_image` (commercial), `nano_banana_pro` (4K renders), `soul_2` (portraits, editorial), `seedream_5_5`.
- Finishing: `upscale_image` (2K/4K), `outpaint_image` (new aspect), `remove_background`, `reframe`, `upscale_video`.
- Voice: `generate_audio` with `seed_audio` (default) or `text2speech_v2` + `variant` (elevenlabs etc.); voices from `list_voices`. For timed narration use the `narration` workflow (it measures takes; never time-stretch).
- Music: `suno_music` (15-360 s; instrumental for beds). Sound effects: `mirelo_text_to_audio`.
- Audio programmes (guided sessions): narration + an instrumental bed, exported as MP3s.

## 10. Video model cheat sheet
| Model | Best for | Limits |
|---|---|---|
| seedance_2_5 | General default; reference-driven; edit and extend clips; drafts | 4-30 s, up to 1080p |
| kling3_0 | Multi-shot clips with audio, motion transfer | needs start_image with Elements |
| minimax_h3 | 2K blocks with keyframes and up to 7 image references (faceless engine) | 4-15 s, 2K |
| cinematic_studio_video_4_0 | Cinema-grade shots with camera, lens, light, era controls | 4-30 s, up to 1080p |
| cinematic_studio_3_0 | Premium cinematic shots | 4-15 s, up to 4K |
| marketing_studio_video | Product ads, UGC formats, hooks, avatars | 12-15 s, up to 1080p |
| seedance_2_0 | Consistent identity, multi-product, 4K | 4-15 s |
| minimax_h3_max, grok_video_v15_lite, seedance_2_0_mini | Cheap fast tests | 480-768p mostly |
Unsure which fits: `models_explore({action:"recommend", query:"<goal and inputs>"})`. Exact parameters: `models_explore({action:"get", model_id})`.
