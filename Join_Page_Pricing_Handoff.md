# Room to Regulate — Join page pricing handoff

Display the four cards in this order, including on mobile:

| Order | Card title | Price | Button text | Details |
| --- | --- | --- | --- | --- |
| 1 | Free Content | Free | Sign up here | Keep the existing free-content description and its one essay/catharsis benefit. Remove the three empty benefit rows. |
| 2 | Monthly | $14.99/month | Join Monthly | Keep this card's existing description and four benefits exactly as shown. |
| 3 | Annual | $120/year | Join for 1 full year | Keep the existing $120/year card's package information and benefits; change its current 'Free Content' title and 'Sign Up Here' button. |
| 4 | Founding annual | $180/year | Become a founding member | Keep the existing final card, including the Best value badge, package details, and benefits. |

## Exact edits to the current page

1. First card: change `Annual` to `Free Content`; change `Join for 1 full year` to `Sign up here`; delete the three empty feature-list items.
2. Second card: keep as is.
3. Third card: change `Free Content` to `Annual`; change `Sign Up Here` to `Join for 1 full year`.
4. Fourth card: keep as is.

The order already follows this sequence in the current markup. Preserve it on desktop and mobile.

## Copy issues to resolve before publishing

- Annual shows `$120/year` but says `$12/month`. The annual total equals $10/month. Confirm whether the annual price or description should change; this handoff preserves both as supplied.
- Founding annual shows `$180/year` and `$15/month`, which are consistent. The `Best value` badge may be misleading beside the lower-priced Annual plan if it is meant to signal lowest cost rather than extra benefits.
- The current button links point back to the Join page (`community.html`). Connect each to its actual sign-up or checkout destination before treating them as working sign-up buttons.

## Optional checkout donation and linked page

Add an optional **one-time** donation to The Shift Fund at checkout for all four packages, including Free Content if that signup has a checkout step. Default to no donation. Suggested buttons: $5, $10, $25, and Other amount, plus a clear No donation choice. Allow a custom positive amount. Show the donation as its own line in the order summary and receipt, separate from membership price; update the total before payment. Never preselect a paid amount. If the free signup has no payment step, offer the donation after signup without blocking free access.

Callout: **Want to give a little more? Add an optional donation to The Shift Fund.** [What is The Shift Fund?](shift-fund.html)

Build `shift-fund.html` and link this callout to it; a ready-to-integrate page is supplied separately. Add a return link from that page to Join. Avoid a tax-deductibility claim unless the legal status supports it.

**Decision needed before implementing annual checkout:** the existing Annual and Founding annual card descriptions already say they include $10 and $30 donations, respectively. Confirm whether those amounts are included in their listed prices and whether the optional checkout gift is additional. Label the optional amount as “additional donation” for those plans if their included donations remain.
