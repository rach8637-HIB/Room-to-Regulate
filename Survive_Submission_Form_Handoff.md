# Survive story submission form — integration handoff

Preview: `share-your-story.html`. Use this as a new page at `/share-your-story.html` and add a link labeled **Share your Survive story** near Survive essays and in the site footer or navigation.

## Connect submissions

The HTML is complete visually and validates in the browser, but its form destination is intentionally unset. Create a form in your own Formspree account, then replace `REPLACE_WITH_FORM_ID` in the `<form action>` with the unique ID. Formspree documents the required action URL and named fields; test one submission in a preview environment and verify it appears in your dashboard/email before promoting the page. Use your account so you control access to submissions. Formspree's `_gotcha` field is included for basic spam filtering.

The page accepts a short story or a request to talk by email; it does not upload audio files. The email field is required to follow up. It explicitly does not add submitters to a marketing list. A story is never auto-published from the form.

## Editorial workflow

1. Acknowledge each submission privately; do not promise a response time until staffing supports it.
2. Discuss whether it is a fit, how the mom wants to be identified, and what child details to remove.
3. Agree on fee, editing, byline, publication rights, and withdrawal point in writing **before** drafting for publication.
4. Send the edited version for explicit approval before publishing.
5. Do not copy submissions into public AI tools or share with sponsors without separate permission.

## Important implementation check

The current site is hosted on Atoms and the form is not installed there yet. The preview's submit button will say it is a preview until a real form ID is supplied. If Atoms restricts custom JavaScript or outbound form submissions, use the same markup in an HTML page with a native POST, or embed a hosted form while keeping the exact questions and editorial language. An actual submit test on the published domain is required.

## AI framework choice — added September 26, 2026

After the story questions, the form now shows explicit **Opt in** and **Opt out** checkboxes with the approved copy. Client-side behavior makes them mutually exclusive and requires one before submission. The submitted fields are `ai_framework_opt_in=yes` or `ai_framework_opt_out=yes`; the receiving workflow must also enforce exactly one choice and record it with the submission. Never treat an unselected box as consent.

Opt-out means the story must not be sent through the AI-enabled framework for topic matching, summaries, drafting, embeddings, or actionable outputs. Keep the raw submission in an editorial review path that honors that choice. Opt-in is permission to discuss use in that framework, **not** permission to publish the story or an AI-generated output. The separate publication approval remains in place.

The phrase “terms of this framework” in the requested copy should link to a plain-language page before launch that explains what data is used, the AI providers involved, storage and retention, human review, withdrawal, and whether outputs can be published. The form copy alone does not supply those terms. Set and link them before accepting live submissions.
