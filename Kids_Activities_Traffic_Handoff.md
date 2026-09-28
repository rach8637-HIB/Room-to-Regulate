# Kids’ activities links — site integration

Updated September 26, 2026. The companion folder/package contains `kids-activities.html`, the three activity assets, the updated `share-your-story.html`, four original toolkit HTML pages with activity callouts, and updated versions of the site's two outsourcing calculator pages. Keep these files in the **same site directory** so the relative links resolve.

## Placements

| Page | Placement | Callout |
| --- | --- | --- |
| Story submission (`share-your-story.html`) | Before the submission form | “Need a few minutes to tell your story? Start a short activity with your child, then come back here.” |
| Capacity check-in | Near the start of the tool | “Need a few minutes for this?” with activity link |
| IEP letter builder | Above the tool introduction | Same callout |
| Senator script | Above the tool introduction | Same callout |
| Outsource calculator | Above the tool introduction | Same callout |
| Public site's static and personalized outsourcing pages | After the introduction, before scenario tabs | Same callout; preserves the rest of the live HTML as retrieved September 26 |

All callouts open `kids-activities.html` in a separate tab, helping parents return to partially completed forms. The hub links to Little Missions (ages 3–5), Mini Missions (ages 6–9), and the optional printable 6–9 kit. The activities are free and do not require email capture. Parents are asked to start together and stay nearby; no guaranteed uninterrupted time is promised.

## Publishing checks

1. Publish `kids-activities.html`, both interactive HTML files, and the PDF at the root alongside the linked pages. Test each link on mobile and desktop.
2. Replace the four toolkit pages and the two public calculator pages only through the site's normal publishing workflow; these are prepared files, not changes to the live Atoms site.
3. `share-your-story.html` still requires a real form endpoint and framework terms before collecting submissions. Do not treat its preview mode as a working submission flow.
4. The personalized outsourcing page remains substantively the same as the static page except for metadata, as noted in the site discrepancy audit; the new activity callout does not resolve that issue.
5. Add the same short callout to any other Solve tool pages created later, pointing to `/kids-activities.html`.
