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

## 2008 collection — closed source and text fidelity

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
- English from this collection: **0 / 40**.

Nine TOC/opening-heading differences remain registered and must not be normalized: Stories **2, 11, 24, 27, 28, 29, 35, 36, 39**.

## Active phase — 2008 visual fidelity

Standing batch rule: **10 stories per iteration**.

### Current durable state

- total: **40**;
- complete: **30 / 40**;
- `PASS`: **30**;
- `PASS — corrected`: **0**;
- pending: **10 / 40**;
- needs recheck: **0**;
- unresolved visual-fidelity issues: **0**;
- story-local `visual-fidelity.md`: **30 / 40**.

### Completed iteration 1 — Stories 1–10

Stories **1–10** were directly inspected across scans **9–27** and are all **PASS**. No Tamil wording or meaningful visual structure required correction.

### Completed iteration 2 — Stories 11–20

Stories **11–20** were directly inspected across scans **27–43** and are all **PASS**. No Tamil wording or meaningful visual structure required correction.

### Completed iteration 3 — Stories 21–30

Stories **21–30** were directly inspected across scans **43–66**, including all shared-page boundaries, and are all **PASS**. No Tamil wording or meaningful visual structure required correction.

Important visual confirmations:

- Stories **24, 27, 28, 29** retain their registered TOC/opening-heading differences;
- Story 23's dialogue/narrative paragraph structure remains separated as printed;
- Story 24 preserves the long `உடன்பிறப்பே` letter structure and three-line Kuruntokai quotation;
- Story 28 preserves its four-line quoted verse;
- Story 30 preserves its three four-line poetic display blocks;
- all completed stories preserve the centered single `*` ending ornament;
- recurring boxed sequence numbers, vertical gutter rules and opening title rules remain collection-design furniture outside canonical prose;
- printed page numbers / running headers remain excluded as page furniture.

## Exact next activity — final visual fidelity Stories 31–40

Process **Stories 31–40 only** in one iteration:

31. `இராமனைப் பற்றி இராமன்` — lower scan **66 → 67–68 → upper 69**;
32. `மானும் பெருமானும்` — lower **69 → 70 → upper 71**;
33. `எழுச்சிக்கு அடையாளம்` — lower **71 → upper 72**;
34. `தலையும் நுனியும்` — lower **72 → upper 73**;
35. TOC `தும்... பம்... தீம்... தோம்` / opening `தும் பம் தீம் தோம்` — lower **73 → 74–75 → upper 76**;
36. TOC `நல்லவழியும் நல்ல வழியும்` / opening `நல்வழியும் நல்ல வழியும்` — lower **76 → upper 77**;
37. `நாக்குத் தமிழ் மணக்கும்` — lower **77 → 78 → upper 79**;
38. `நீதி தேவதையே!` — lower **79 → upper 80**;
39. TOC `நன்றி சொல்லும் நேரம்...` / opening `நன்றி சொல்லும் நேரம்` — lower **80 → upper 81**;
40. `பந்தலிலே பாகற்காய்` — lower scan **81**, with scan **82** used only as the verified back-cover / final-boundary witness.

Story 30 closes above Story 31 on shared scan **66**. Exclude Story-30 material. For each active story inspect all registered scans directly; check heading/title provenance, paragraph/dialogue structure, display or verse blocks, meaningful ornaments, collection-design furniture, page furniture and physical joins. Create `stories/<slug>/visual-fidelity.md`. Propagate a correction only when the source scan directly supports it.

After all ten are durably closed, synchronize the tracker and close the 2008 visual-fidelity phase. Do **not** automatically open English translation.

## Phase guard

Visual fidelity does not authorize English translation, modernization, adaptation, republication or Digital Library onboarding. Do not open another downstream phase until visual fidelity is closed and the user explicitly authorizes the next phase.
