# What's Actually Changed — dynamic tracker handoff

Prepared September 28, 2026. This is a site-ready prototype and source-update pipeline. It has **not** been installed on the live Atoms site.

## Files

- `whats-changed.html` — replace the current `/whats-changed.html` page with this after review. It has search, topic/source filters, three views, source links, a source-refresh timestamp, and an offline preview snapshot.
- `source-updates.json` — automatically collected, source-linked headlines from selected feeds. Published as **From verified sources**, not as confirmed policy changes.
- `policy-updates.json` — editor-owned entries. Its 11 migrated August 2026 entries are marked `review_due` in a separate archive. No migrated assertion has been silently relabeled as current.
- `update_policy_sources.py` — fetches and deduplicates RSS from KFF Medicaid, Medicare, Affordable Care Act, state health policy, USDA FNA Newsroom, and USDA FNA Federal Register. These organizations/official agency are in or linked from the current Verified Resources ecosystem. Validates HTTPS domains; keeps the last good feed snapshot if one feed fails; refuses to overwrite the data if every feed fails.
- `policy-tracker-workflow/refresh-policy-sources.yml` — optional daily GitHub Actions schedule if the site source is maintained in GitHub.

## How updates become visible

1. A scheduled job runs `python3 update_policy_sources.py`, writes `source-updates.json`, and publishes that file alongside `whats-changed.html`.
2. On each visit, the page fetches the latest JSON. If previewed as a local HTML file or if fetching fails, it uses an embedded snapshot so the design remains reviewable; the embedded snapshot will not refresh itself.
3. Visitors see fresh headlines and dates in **From verified sources**, with a link to the original. The interface says explicitly that a newly posted source item does not establish a policy change.
4. An editor opens the primary document, checks whether the action is proposed, final, effective, stayed, or state-specific, checks date and impacted population, then writes a short entry in `policy-updates.json` with `stage`, `stageLabel`, `reviewedAt`, `effectiveDate` if known, `topic`, `geography`, `claim`, `summary`, and `sources`. Only then does it appear under **Reviewed changes**.
5. Review older entries after policy or implementation changes. Move outdated entries back to `review_due` when the source or effective date changes.

The source monitor currently covers selected KFF and USDA FNA feeds. It does **not** claim comprehensive coverage of IDEA, Medicaid waiver approvals, state regulations, court rulings, or every item in Verified Resources. Those need additional monitored feeds or manual review. A source feed can contain data releases and commentary, not only policy changes.

## Publication requirements

- The Atoms site currently serves static HTML. A browser-only page cannot reliably collect and classify all external feeds because of cross-origin restrictions; this design uses a separate scheduled job to fetch feeds and write JSON. Connect the repository's deploy pipeline to Atoms, or arrange another scheduled backend that uploads `source-updates.json` to the same directory each day. GitHub Actions by itself updates a repository; it does not publish to Atoms without that deployment connection.
- Keep `policy-updates.json` under editorial control. Do not let the scheduler rewrite it or let AI-generated summaries auto-publish as verified changes.
- For new policy entries, link to a primary source where available, plus an explanatory source when helpful. Include reviewed date and effective date separately. For state-specific items include the state explicitly.
- Test each JSON load, filtering, and a failed-source run in preview. Check the live page title and source-refresh timestamp after deployment.

## Editor entry shape (illustrative placeholders, not a policy claim)

```json
{
  "id": "unique-id",
  "topic": "Education and food assistance",
  "geography": "National",
  "stage": "reviewed",
  "stageLabel": "Proposed / Final / In effect / Stayed — choose one",
  "claim": "Question readers are asking",
  "summary": "Plain-language explanation approved by the editor",
  "reviewedAt": "YYYY-MM-DD",
  "effectiveDate": null,
  "sources": [{"label": "Official document", "url": "https://example.gov/document"}]
}
```
