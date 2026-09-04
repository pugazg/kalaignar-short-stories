# HANDOVER — Kalaignar Short Stories Archive

## Repository

- Repository: `pugazg/kalaignar-short-stories`
- Branch: `main`
- Story workflow: `SHORT_STORY_PROCESSING_GUIDE.md`
- Collection workflow: `COLLECTION_SOURCE_GUIDE.md`
- Text-fidelity workflow/tracker: `TEXT_FIDELITY_CHECK_GUIDE.md` / `TEXT_FIDELITY_PROGRESS.md`
- 1977 visual workflow/tracker: `VISUAL_FIDELITY_CHECK_GUIDE.md` / `VISUAL_FIDELITY_PROGRESS.md`
- 2008 visual workflow/tracker: `collections/2008-kalaignar-sonna-kathaigal/VISUAL_FIDELITY_GUIDE.md` / `collections/2008-kalaignar-sonna-kathaigal/VISUAL_FIDELITY_PROGRESS.md`
- English workflow: `ENGLISH_TRANSLATION_GUIDE.md`
- 1977 English tracker: `ENGLISH_TRANSLATION_PROGRESS.md` — closed at **37 / 37**
- 2008 English tracker: `collections/2008-kalaignar-sonna-kathaigal/ENGLISH_TRANSLATION_PROGRESS.md`

## Authoritative-state rule

Always fetch live `main` first and preserve newer durable work. Source PDFs / renders / crops are not committed.

## Permanent source rules

- controlling scan first; no silent modernization or normalization;
- running headers and printed page numbers are page furniture, not body text;
- shared physical scans preserve exact story boundaries;
- source-supported textual corrections propagate through page, assembly, audit/review and dependent layers;
- `POSSIBLE_ERRORS_FOR_REVIEW.md` is a human-review queue, not proof of error.

## Closed 1977 anthology

`கலைஞர் கருணாநிதியின் சிறுகதைகள்` remains fully closed:

- Tamil source: **37 / 37 complete**;
- visual fidelity: **37 / 37 complete**;
- English translation/review: **37 / 37 complete**;
- final English structural/control QA: **PASS**;
- unresolved story text: **0**;
- scan **260**: verified back cover.

Story 29 `திடுக்கிடும் கதை` retains the later marker-only provenance correction. Obsolete Wave-2 pin `a9b333f12128686785ee981f97313a64af12e29b` must not be reused.

## 2008 collection — source / text / visual closed

Collection: **கலைஞர் சொன்ன கதைகள்**  
Workspace: `collections/2008-kalaignar-sonna-kathaigal/`  
Controlling source: `TVA_BOK_0065857_கலைஞர்_சொன்ன_கதைகள்.pdf`

- represented edition: **Second Edition, December 2008**;
- PDF scans: **82**;
- story text: scans **9–81 / printed pages 7–79**;
- scan **82**: verified back cover, no further story text;
- Tamil source: **40 / 40 complete**, 0 blocked / 0 unresolved;
- word-by-word text fidelity: **40 / 40 complete**;
- text-fidelity split: **19 PASS / 21 PASS — corrected**;
- visual fidelity: **40 / 40 complete**, all **40 PASS**.

Nine TOC/opening-heading differences remain registered and must not be normalized: Stories **2, 11, 24, 27, 28, 29, 35, 36, 39**.

## 2008 English translation — ACTIVE

The user explicitly authorized the English downstream phase after source/text/visual closure.

Current durable state:

- English translation complete: **1 / 40**;
- `PASS`: **1**;
- pending: **39 / 40**;
- `NEEDS REVIEW`: **0**;
- canonical Tamil changed during English work: **No**.

### Completed Story 1 — `அப்படித்தான் சிரிப்பேன்`

Workspace: `stories/appadithan-sirippen/`

- English file: `translations/en/appadithan-sirippen.md`;
- review: `TRANSLATION_REVIEW.md`;
- English title treatment: **Appadithan Sirippen**;
- source span: **scan 9 / printed 7 → top scan 10 / printed 8**;
- source markers: **9 → 10**, once and in order;
- physical page-boundary alignment: **PASS** — scan 9 ends inside the beggar's quoted reply at `“Yes!`; scan 10 resumes that same reply at `That is exactly how I laugh!”`;
- Story-2 material below the Story-1 ending ornament on shared scan 10: **excluded**;
- possible-error queue read: **Yes**;
- unusual Tamil forms were not silently normalized;
- final source-significant `*`: preserved;
- result: **PASS**.

Important marker syntax precedent for validator compatibility: use the exact marker form `<!-- source scan N; printed page M -->`. Put any boundary note in a separate HTML comment rather than adding fields inside the marker.

## Current exact next activity — 2008 Story 2 English

Process **one story only** under `ENGLISH_TRANSLATION_GUIDE.md` unless the user explicitly expands the batch.

Story 2:

- TOC title: **`ஐஸ்கட்டி`**;
- opening heading: **`ஐஸ் கட்டி`**;
- workspace: `stories/ice-katti/`;
- verified physical span: **lower scan 10 / printed page 8 → upper scan 11 / printed page 9**;
- title variance must be preserved and documented, not normalized.

Before translation, read completely:

1. `SHORT_STORY_PROCESSING_GUIDE.md`;
2. `COLLECTION_SOURCE_GUIDE.md`;
3. `ENGLISH_TRANSLATION_GUIDE.md`;
4. `collections/2008-kalaignar-sonna-kathaigal/ENGLISH_TRANSLATION_PROGRESS.md`;
5. `TEXT_FIDELITY_CHECK_GUIDE.md` and `TEXT_FIDELITY_PROGRESS.md`;
6. `collections/2008-kalaignar-sonna-kathaigal/VISUAL_FIDELITY_GUIDE.md` and `VISUAL_FIDELITY_PROGRESS.md`;
7. this `HANDOVER.md`;
8. `NEXT_CHAT_PROMPT.md`;
9. collection README, source metadata, story inventory and scan map;
10. Story-2 README, canonical Tamil assembly, all Story-2 page records, page map, audit, `POSSIBLE_ERRORS_FOR_REVIEW.md`, `text-fidelity.md` and `visual-fidelity.md`.

Translate from the verified canonical Tamil assembly, not from OCR. Check actual physical page-boundary alignment against verified Tamil page records, not marker numbering alone. Create the English file and `TRANSLATION_REVIEW.md`, synchronize story/collection/root controls, re-fetch live `main`, and advance the exact next target only after Story 2 is fully durable.

Modernization, adaptation, republication and Digital Library onboarding remain outside the current authorization.