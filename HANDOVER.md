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
- canonical workspaces activated: **21 / 40**;
- Tamil source complete: **21 / 40**;
- Tamil source pending: **19 / 40**;
- English from this collection: **0 / 40**;
- completed Story 1–21 text: **0 blocked / 0 unresolved**.

The user explicitly instructed: **process 10 stories in each iteration**. The first 10-story iteration was Stories 2–11 after Story 1 had been closed independently. The second 10-story iteration, **Stories 12–21, is now fully source-complete**.

### Completed second iteration — Stories 12–21

12. `கண்ணில் கால்` — scan 29 → upper 30 — PASS, 2/2;
13. `மயில் ராவணன்` — lower 30 → 31 — PASS, 2/2;
14. `ஜாடி குட்டி போடுமா?` — 32 → upper 33 — PASS, 2/2;
15. `ஒண்ணு குடுமா?` — lower 33 → 34 → upper 35 — PASS, 3/3;
16. `அத்திரி பாச்சா` — lower 35 → upper 36 — PASS, 2/2;
17. `செருப்போடு இரு` — lower 36 → upper 37 — PASS, 2/2;
18. `இடிக்குப் பின் மழை` — lower 37 → 38 → upper 39 — PASS, 3/3;
19. `நடக்குமா நடக்காதா?` — lower 39 → 40–41 → upper 42 — PASS, 4/4;
20. `கனியும் கணையும்` — lower 42 → upper 43 — PASS, 2/2;
21. `இதயம் பேசுகிறது` — lower 43 → upper 44 — PASS, 2/2.

Six TOC/opening-heading differences remain registered: #2, #11, #24, #28, #35 and #39. No title form is silently normalized.

## Exact next activity — third 10-story iteration, Stories 22–31

Process all ten and stop after Story 31 unless the user explicitly expands the batch:

22. `புலிவால்` — printed **42**, scan **44**, boundary **45**;
23. `தெரியாத பேச்சு` — printed **43–44**, scans **45–46**, boundary **47**;
24. TOC `வெண்ணெய் உருகுது வெயிலில்!` / opening `வெண்ணெய் உருகுது வெயிலில்` — printed **45–51**, scans **47–53**, boundary **54**;
25. `மாமியார் உடைத்தால் மட்டும் மண்சட்டியா?` — printed **52–57**, scans **54–59**, boundary **60**;
26. `பொறுமைக்கு சான்று` — printed **58**, scan **60**, boundary **61**;
27. `எடுக்கவோ கோக்கவோ!` — printed **59**, scan **61**, boundary **62**;
28. TOC `அந்த நாள் வந்திலை...` / opening `அந்த நாள் வந்திலை!` — printed **60–61**, scans **62–63**, boundary **64**;
29. `பனித் துளியில் பனைமரம்` — printed **62**, scan **64**, boundary **65**;
30. `பாரூர் போல...` — printed **63**, scan **65**, boundary **66**;
31. `இராமனைப் பற்றி இராமன்` — printed **64–66**, scans **66–68**, boundary **69**.

For every story: re-fetch live `main`; duplicate-check TOC/opening/documented forms; inspect controlling and next-boundary scans directly; preserve punctuation/paragraphs/non-text facts; create canonical workspace with pages, assembly, metadata, page map, audit and review queue; do not use OCR memory or inferred prose as a substitute for the source.

## Phase guard

The active collection authorizes source-first processing of `கலைஞர் சொன்ன கதைகள்`; it does not authorize modernization, adaptation, republication, Digital Library onboarding, or changes to other repositories.
