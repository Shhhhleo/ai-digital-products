# Whop with a creator partner: setup and the four Session 3 questions

Checked against docs.whop.com/affiliates/setup-rev-share in Nov 2026. If a screen differs, read the current doc page (or ask the Whop MCP) before clicking.

## The trap: the share % applies to every product
In the revenue share invite, "Share %" is the partner's percentage of all products in that business; "Products" overrides it per product. Inviting a creator at 50% inside Reset Lab would give them half of The Desk Body Reset and The GLP-1 Off-Ramp too. Two safe setups:
- Default: one Whop business per creator partnership, named for the creator's brand. Share % = 50 for the whole business. Their future products with us go in the same business and are split automatically. Clean dashboards, clean storefront for their audience.
- Alternative (creator doesn't mind the Reset Lab storefront): in Reset Lab, Share % = 0 and a product override of 50% on their product only. Check the overrides every time a product is added.

## The four questions

1. How do I publish the product along with the creator?
   Luis publishes it from the partnership's Whop business, with the creator's name and brand on the product, listing and website, and the creator added as the revenue share partner. The creator promotes it with their own tracking links. You own and run the store; they never touch the dashboard.

2. How do I make Whop work with the creator and me?
   The creator makes a free Whop account and gives Benji their email or username. Luis invites them as the revenue share partner. Whop then takes payment, delivers the product, and records every sale for both of you; the creator sees their earnings in their own Whop account.

3. How do I split each payment 50/50?
   Dashboard → Marketing → Affiliates → Share your revenue → add the creator (email, Whop username or user ID) → Share % 50 (or 0 with a 50% product override, per the trap above) → Invite. Whop calculates the split after its fees and, when each transaction completes, deposits the creator's portion into their Whop balance. No manual transfers.

4. "The second someone buys, they get it and we both get paid": how do I set that up?
   Three pieces, set once per product, before launch:
   a. Delivery: the Content app with the files attached, gated to this product. Access is instant at checkout.
   b. Payment: an active paid plan and one checkout link that every buy button uses (Step 7-B2).
   c. Split: the revenue share above, accepted by the creator.
   Each side withdraws from their own Whop balance to their own bank once their payout details are verified. You do your payout, identity and tax screens yourself; the creator does theirs.

## Luis's checklist
- [ ] Creator's Whop account recorded in deal-terms.md.
- [ ] Revenue share invite sent; share applies to their product(s) only; creator accepted.
- [ ] Creator is not also a standard affiliate on the same product (no double pay).
- [ ] Tracking links per channel sent to the creator via Benji.
- [ ] Payouts verified for the business; no banner blocking charges.
- [ ] Incognito checkout check and every buy button checked.
- [ ] After the first real sale, the creator's share shows in their balance; if not, pause promotion and fix.

## Revenue share vs affiliate
Revenue share: a fixed partner earning their % of every sale, however the buyer arrived. Use for the creator.
Affiliate: anyone with a tracked link earning a commission on sales through that link. Use for third-party promoters (store rate 30%).

## Money notes
The split follows net revenue, so refunds and chargebacks reduce both shares; the agreement says so. Each side handles its own taxes; finish Whop's tax details by the deadline it shows or payouts can pause.

## Tools for Luis
Whop plugin for Claude Code (`/plugin marketplace add whopio/plugins`, `/plugin install whop@whop`), the Whop MCP server (https://mcp.whop.com/mcp, browser sign-in), or the Whop CLI for websites. The API moves real money in production; test risky changes in Whop's sandbox first.
