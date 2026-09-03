# HANDOVER — Kalaignar Short Stories Archive

## Repository

- Repository: `pugazg/kalaignar-short-stories`
- Branch: `main`
- Story workflow: `SHORT_STORY_PROCESSING_GUIDE.md`
- Anthology workflow: `COLLECTION_SOURCE_GUIDE.md`
- Visual-fidelity workflow: `VISUAL_FIDELITY_CHECK_GUIDE.md`
- English-translation workflow: `ENGLISH_TRANSLATION_GUIDE.md`
- Source PDFs / renders / crops are **not** committed.

## Authoritative-state rule

Always fetch live `main` first and preserve newer durable work.

## Permanent source rules

- controlling scan first; no silent modernization of spelling, punctuation, grammar, sandhi, names or source anomalies;
- running headers/page numbers are furniture, not body text;
- `POSSIBLE_ERRORS_FOR_REVIEW.md` is a human-review queue, not proof of error;
- source-supported corrections propagate through page, assembly, audit/review and dependent English layers;
- shared physical boundary scans preserve each story's exact source span;
- do not commit controlling PDFs or inspection artefacts.

## Closed 1977 anthology

`கலைஞர் கருணாநிதியின் சிறுகதைகள்` remains durably closed:

- Tamil source: **37 / 37 complete**, 0 blocked / 0 unresolved;
- visual fidelity: **37 / 37 complete**;
- English translation/review: **37 / 37 complete**;
- final English structural/control QA: **PASS**;
- scan **260**: verified back cover.

Story 29 `திடுக்கிடும் கதை` retains its later marker-only provenance correction. Canonical Tamil and English prose were unchanged; old Wave-2 pin `a9b333f12128686785ee981f97313a64af12e29b` is obsolete.

## Active collection — கலைஞர் சொன்ன கதைகள்

Collection workspace: `collections/2008-kalaignar-sonna-kathaigal/`

Controlling source: `TVA_BOK_0065857_கலைஞர்_சொன்ன_கதைகள்.pdf`

- printed author: **டாக்டர் கலைஞர் மு. கருணாநிதி**;
- scanned edition: **Second Edition, December 2008**;
- source SHA-256: `1b2bf86892717776b1b3dc7fcb18dc146d5bfd0d60986509dc9cbbf5f235444b`;
- file size: **24,840,000 bytes**;
- PDF scans: **82**;
- contents entries: **40**;
- story text: scans **9–81 / printed 7–79**;
- scan **82**: verified back cover;
- relation: **scan = printed page + 2**.

### Current collection state

- contents: **40 / 40 transcribed**;
- TOC-derived ranges: **40 / 40 calculated**;
- story-opening scans: **40 / 40 visually checked**;
- canonical workspaces activated: **31 / 40**;
- Tamil source complete: **31 / 40**;
- Tamil source pending: **9 / 40**;
- English from this collection: **0 / 40**;
- completed Story 1–31 text: **0 blocked / 0 unresolved**.

The user explicitly instructed: **process 10 stories in each iteration**. Stories 2–11 formed the first ten-story iteration after Story 1; Stories 12–21 formed the second; Stories 22–31 formed the third and are now fully source-complete. Only nine stories remain for the final source iteration.

### Completed third iteration — Stories 22–31

22. `புலிவால்` — lower 44 → upper 45 — PASS, 2/2;
23. `தெரியாத பேச்சு` — lower 45 → 46 → upper 47 — PASS, 3/3;
24. TOC `வெண்ணெய் உருகுது வெயிலில்!` / opening `வெண்ணெய் உருகுது வெயிலில்` — lower 47 → 48–53 → upper 54 — PASS, 8/8;
25. `மாமியார் உடைத்தால் மட்டும் மண்சட்டியா?` — lower 54 → 55–59 → upper 60 — PASS, 7/7;
26. `பொறுமைக்கு சான்று` — lower 60 → upper 61 — PASS, 2/2;
27. TOC `எடுக்கவோ கோக்கவோ!` / opening `எடுக்கவோ கோக்கவோ` — lower 61 → upper 62 — PASS, 2/2;
28. TOC `அந்த நாள் வந்திலை...` / opening `அந்த நாள் வந்திலை!` — lower 62 → 63 → upper 64 — PASS, 3/3;
29. TOC `பனித் துளியில் பனைமரம்` / opening `பனித்துளியில் பனை மரம்` — lower 64 → upper 65 — PASS, 2/2;
30. `பாரூர் போல...` — lower 65 → upper 66 — PASS, 2/2;
31. `இராமனைப் பற்றி இராமன்` — lower 66 → 67–68 → upper 69 — PASS, 4/4.

Eight TOC/opening-heading differences are registered: #2, #11, #24, #27, #28, #29, #35 and #39. No title form is silently normalized.

## Exact next activity — final source iteration, Stories 32–40

Process the remaining nine stories and stop after Story 40:

32. `மானும் பெருமானும்` — printed **67–68**, scans **69–70**, boundary **71**;
33. `எழுச்சிக்கு அடையாளம்` — printed **69**, scan **71**, boundary **72**;
34. `தலையும் நுனியும்` — printed **70**, scan **72**, boundary **73**;
35. TOC `தும்... பம்... தீம்... தோம்` / opening `தும் பம் தீம் தோம்` — printed **71–73**, scans **73–75**, boundary **76**;
36. `நல்லவழியும் நல்ல வழியும்` — printed **74**, scan **76**, boundary **77**;
37. `நாக்குத் தமிழ் மணக்கும்` — printed **75–76**, scans **77–78**, boundary **79**;
38. `நீதி தேவதையே!` — printed **77**, scan **79**, boundary **80**;
39. TOC `நன்றி சொல்லும் நேரம்...` / opening `நன்றி சொல்லும் நேரம்` — printed **78**, scan **80**, boundary **81**;
40. `பந்தலிலே பாகற்காய்` — printed **79**, scan **81**, boundary witness **82 / back cover**.

Story 31 closes above Story 32 on scan 69. For every story: re-fetch live `main`; duplicate-check TOC/opening/documented forms; inspect controlling and next-boundary scans directly; preserve punctuation/paragraphs/non-text facts; create canonical workspace with pages, assembly, metadata, page map, audit and review queue; do not use OCR memory or inferred prose as a substitute for the source.

## Phase guard

The active collection authorizes source-first processing of `கலைஞர் சொன்ன கதைகள்`; it does not authorize modernization, adaptation, republication, Digital Library onboarding, or changes to other repositories.
