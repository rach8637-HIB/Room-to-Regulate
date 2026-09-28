# Room to Regulate — site discrepancy audit

Reviewed September 26, 2026. Scope: 44 HTML pages linked from the home page, full site index, and their internal links, plus `nav.js`. Findings reflect the public `roomtoregulate.atoms.world` site at review time. This is a content and link audit, not a verification of every article's research claims or a test of authenticated checkout.

## Fix before inviting people to join

| Priority | Location | What is inconsistent or broken | Exact fix |
| --- | --- | --- | --- |
| Critical | [Join page](https://roomtoregulate.atoms.world/community.html), four membership cards | The Free card is labeled `Annual`, while the $120/year card is labeled `Free Content`. Three empty benefits display in the Free card. Buttons carry the wrong labels. | Apply the agreed [pricing handoff](Join_Page_Pricing_Handoff.md): Free Content → Monthly → Annual → Founding annual, with the specified CTAs. |
| Critical | Join page, all four card buttons | All four card CTAs link to `community.html`, sending visitors back to the same page instead of signup or checkout. | Connect each CTA to its matching signup or checkout flow. Keep Free signup usable without payment. |
| Critical | Join page FAQ, “Can I cancel anytime?” | It says `Donations are tax deductible`. The approved checkout design deliberately leaves tax details to “Learn more,” and the earlier mockup said the opposite. | Remove the categorical claim from the Join FAQ. Put accurate, reviewed tax treatment on The Shift Fund page, then link to that page from checkout. Do not infer tax status from the mockup. |
| Critical | Checkout concept / The Shift Fund | The approved mockup says `100% goes to sponsored seats`, but the [home page](https://roomtoregulate.atoms.world/index.html) says the fund supports free access, advocacy content, **and policy work**; the Join page also says membership proceeds shape policy. These descriptions imply different uses of money. | Decide what the fund actually pays for and whether an optional `Sponsor a seat` gift is ring-fenced. Match the home, Join, checkout, fund page, and receipts to that decision. Avoid `100%` until the allocation is supportable. |
| Critical | [The Shift Fund URL](https://roomtoregulate.atoms.world/shift-fund.html) | This path currently serves the **home page** (title and hero), despite returning HTTP 200. The checkout “Learn more” link therefore cannot explain the fund on the live site. | Publish the drafted Shift Fund page at `/shift-fund.html` and verify its title, content, and checkout link on the live site. |
| High | Join page, Annual card | `$120/year` is paired with `$12/month`; $120 divided by 12 is $10. | Confirm whether price or explanatory monthly equivalent is intended; if $120/year is correct, write `Equivalent to $10/month, billed annually` and clarify the included $10 gift. |

## Clarify the membership promise

| Priority | Location | What needs alignment | Suggested action |
| --- | --- | --- | --- |
| High | Join page heading | `One membership. No tier maze.` and “we'll add options later” appear directly above four options. | Say `Choose how to join` or explain that Monthly and Annual are billing choices and Founding includes extras. |
| High | Founding annual card | `Everything in Standard Package` refers to a tier that does not exist by that name. | Replace with `Everything in the Annual membership` or name the paid core membership consistently. |
| High | Join page, Annual and Founding descriptions; checkout concept | The cards say $10 and $30 donations are included, while checkout adds a gift. The mockup labels gift buttons `+$5/mo`, suggesting a **recurring** gift; the prior handoff describes a **one-time** gift. | Decide whether gifts are included in annual prices, and whether optional gifts recur. Label any checkout gift `additional`, and show its billing frequency and total explicitly. |
| High | Join page, Monthly card and FAQ | Card says `Free Cancellation, any time`; FAQ says monthly payments are non-refundable. | State both plainly: `Cancel future renewals anytime. Payments already made are non-refundable`, if that is the actual policy. Have the final terms reviewed before launch. |
| Medium | Join page, `What members are actually saying` | Three quotes are presented as real member feedback, including `member since launch`, while signup flows currently loop back to the page. | Verify these are genuine, approved testimonials. If they are illustrative copy, remove the attribution or replace the section until actual feedback is available. |
| Medium | Join page, benefits | `Ask an Advocate, live` is promoted as a general membership feature, but it appears only on the Founding annual card; Monthly and Annual cards omit it. | State clearly which plans include the live sessions; align the overview with card benefits. |

## Navigation and content readiness

| Priority | Location | Finding | Suggested action |
| --- | --- | --- | --- |
| High | [The Room](https://roomtoregulate.atoms.world/the-room.html) | Eight video cards link to `#` and display `[Creator name]`, `[Video title — placeholder]`, or similar production text. | Publish vetted videos or hide the sample cards until ready; keep the page intro if useful. |
| Medium | [Home](https://roomtoregulate.atoms.world/index.html) hero | `Get the morning script, free` links to the Join page’s pricing section; it does not open or download a morning script. | Link directly to the resource or change the CTA to `Explore free content`. |
| Medium | [Full site index](https://roomtoregulate.atoms.world/site-index.html) | It publicly links to `Partner Card Disclosure — Example`, whose title identifies it as an internal brand partnership framework. | Remove the internal demo from public navigation or mark it clearly as a published example. |
| Medium | `resources-outsourcing-personalized.html` versus `resources-outsourcing-static.html` | The two pages have the **same body and calculator controls**. Only metadata differs. The personalized page claims ZIP, income, and spending personalization that the body does not offer. | Build the personalized inputs and calculation or remove that version/description and link to the static tool. |
| Medium | Site metadata | Pages declare canonical URLs on `roomtoregulate.org`, while the reviewed live pages are on `roomtoregulate.atoms.world`. The custom domain did not load from this audit environment, so its status could not be confirmed. | When publishing, verify the intended primary domain resolves and redirects consistently, then set canonical URLs to that domain. |

## Recommended sequence

1. Publish the corrected Join pricing and working signup destinations.
2. Decide fund allocation, included annual gifts, optional gift frequency, and tax wording; align checkout and all site copy.
3. Publish `/shift-fund.html` and verify the “Learn more” link.
4. Remove public placeholders and correct the misleading resource links.
5. Recheck the membership promises, testimonials, and domain metadata before launch.

No changes to the live Atoms site were made during this audit.
