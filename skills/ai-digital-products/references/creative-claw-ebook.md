# Creative Claw for e-books (the house rule)

Every image and graphic in an e-book product is designed and made through Creative Claw: the cover, every in-book illustration, diagram, chart, icon and visual, the listing images, the website's images, and social or story frames. Mike builds only the page layout and typesetting (HTML → PDF); anything that is a picture comes from Creative Claw. Video for an e-book product (ads, a website hero loop, launch reels) is video, so it goes to Higgsfield (references/higgsfield-playbook.md).

If Creative Claw is not connected, stop and tell Advaith (Claude Code: /mcp). Never fall back to another image tool for an e-book.

## Before generating
- Brand theme per product: `update_theme` with this product's palette, fonts and rules (from Peter's identity brief or Mike's style lock), then `get_theme` on every branded image so the set matches.
- Media plan: list every image, its tool and model, and price it with `estimate_generation`; add it to media-plan.md with `get_credits_balance`. One yes from Advaith covers the plan (via Luis).
- Read Creative Claw's own skill guidance once per task (creativeclaw-generate-image, and creativeclaw-render-html for exact layouts).

## What to use for each graphic
| Graphic | Tool and model |
|---|---|
| Cover (title must be exact) | `generate_image`, `image/nano-banana-pro` (best typography); verify every letter, regenerate if wrong |
| Chapter or section illustrations | `generate_image`, `image/nano-banana-2`, same style words and theme in every prompt |
| Diagrams, charts, infographics, labelled steps, trackers shown as visuals, comparison tables as images | `render_html_image` (exact text and numbers, rendered by Creative Claw) |
| Icon set | `generate_image` with `image/gpt-image-2.5-sunburst`, transparent background (`extras.background: "transparent"`) |
| Device or print mockups (tablet, phone, printed workbook) | `generate_image`, `image/nano-banana-pro`, the real cover uploaded as reference |
| Whop media 1920x1080, banner 1200x630, social 1080x1080, story 1080x1920, "what's inside" | `render_html_image` composing the real cover, real page renders and the title (exact sizes, exact words) |
| Website images (hero still, section art) | `generate_image` (nano-banana-2 or pro) or `render_html_image` for anything with words |

## Rules
- Every product gets its own fresh set. Never reuse another product's images.
- Text on images comes from product-notes.md, copied exactly. Read every word on every result before using it.
- Tag each approved asset (`update_asset` with the product name) and record its URL in media-plan.md.
- Keep the source aspect for edits; regenerate the smallest failing part rather than the whole image.
