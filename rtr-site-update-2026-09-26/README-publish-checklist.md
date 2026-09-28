# Room to Regulate site update — September 26, 2026

This folder is a ready-to-publish copy of the site with two additions: kids' activities links and the Survive story submission page. Nothing here has been published to the live Atoms site. Upload through your normal Atoms publishing workflow, keeping every file in the same root directory so relative links work.

Live pages were retrieved from roomtoregulate.atoms.world on September 26, 2026. Only the changes listed below were made; everything else in each page is unchanged.

## New pages and assets

| File | What it is |
| --- | --- |
| `share-your-story.html` | Survive story submission page (preview mode until a Formspree ID is added) |
| `kids-activities.html` | Hub linking to the three kids' activities |
| `Room_to_Regulate_Little_Missions_Ages_3_to_5.html` | Interactive activity, ages 3–5 |
| `Room_to_Regulate_Mini_Missions_Ages_6_to_9.html` | Interactive activity, ages 6–9 |
| `Room_to_Regulate_While_I_Figure_This_Out_Ages_6_to_9.pdf` | Printable kit, ages 6–9 |

## Changed pages

| Pages | Change |
| --- | --- |
| All 15 Survive essays (`survive-*.html`) | "Have a moment like this? Share your Survive story →" callout just above "Keep going," plus footer link |
| Every other page with a site footer (26 pages) | "Share your Survive story" link added to the footer |
| `site-index.html` | New "Share & take a breath" section linking to the story page and kids' activities |
| `resources-outsourcing-static.html`, `resources-outsourcing-personalized.html` | Kids' activity callout after the introduction, before the scenario tabs, plus footer link |
| `rtr-capacity-checkin.html`, `rtr-iep-letter-builder.html`, `rtr-senator-script.html`, `rtr-outsource-calculator.html` | Kids' activity callout near the start of each tool (these tools are not yet on the live site) |

All kids' activity callouts open `kids-activities.html` in a new tab so a half-finished form stays open.

## Before publishing

1. **Connect the story form.** Create a form in your own Formspree account and replace `REPLACE_WITH_FORM_ID` in the form's `action`. Until then, the submit button shows a preview message and nothing is sent.
2. **Add terms for the AI framework choice.** The form asks submitters to opt in or out of the "Room to Regulate AI-enabled framework." Publish plain-language terms for that framework, and link them from the opt-in, before collecting real submissions.
3. **Test on the published domain.** Submit one test story after publishing and confirm it arrives in your Formspree dashboard or email. If Atoms blocks custom JavaScript or outbound form posts, use the same markup with a native form POST, or embed a hosted form with the same questions and wording.
4. **Test every new link** on mobile and desktop: the story links on Survive essays and in footers, the kids' activity callouts, and all three activities, including the PDF download.

## Editorial workflow for submissions

1. Acknowledge each submission privately. Don't promise a response time until staffing supports it.
2. Discuss fit, how she wants to be named, and which child details to remove.
3. Agree in writing on fee, editing, byline, publication rights, and withdrawal point before drafting.
4. Send the edited version for explicit approval before publishing.
5. Don't paste submissions into public AI tools or share them with sponsors without separate permission.

## Notes

- `survive-1-chaos-ordinary-day.html` is live and linked from several pages but isn't listed in `site-index.html`. It received the same story callout and footer link. Add it to the index if it's meant to be public.
- The personalized outsourcing page still matches the static page except for metadata. The new callout doesn't change that.
- Add the same kids' activity callout to any future Solve tool pages.
