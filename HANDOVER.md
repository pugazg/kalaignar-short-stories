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
- complete: **20 / 40**;
- `PASS`: **20**;
- `PASS — corrected`: **0**;
- pending: **20 / 40**;
- needs recheck: **0**;
- unresolved visual-fidelity issues: **0**;
- story-local `visual-fidelity.md`: **20 / 40**.

### Completed iteration 1 — Stories 1–10

Stories **1–10** were directly inspected across scans **9–27** and are all **PASS**. No Tamil wording or meaningful visual structure required correction.

### Completed iteration 2 — Stories 11–20

Stories **11–20** were directly inspected across scans **27–43** and are all **PASS**. No Tamil wording or meaningful visual structure required correction.

Important visual confirmations:

- Story 11's TOC `சாவிதான் இல்லை` / opening `சாவி தான் இல்லை` variance remains preserved;
- Story 15's short dialogue sequence remains separated as printed;
- Stories 18–20 preserve their narrative/dialogue paragraph structure and all physical joins;
- the recurring boxed sequence number, vertical gutter rule and opening title rule are collection-design furniture and remain outside canonical prose;
- every completed story preserves the centered single `*` ending ornament;
- printed page numbers / running headers remain excluded as page furniture.

## Exact next activity — visual fidelity Stories 21–30

Process **Stories 21–30 only** in one iteration:

21. `இதயம் பேசுகிறது` — lower scan **43 → upper 44**;
22. `புலிவால்` — lower **44 → upper 45**;
23. `தெரியாத பேச்சு` — lower **45 → 46 → upper 47**;
24. TOC `வெண்ணெய் உருகுது வெயிலில்!` / opening `வெண்ணெய் உருகுது வெயிலில்` — lower **47 → 48–53 → upper 54**;
25. `மாமியார் உடைத்தால் மட்டும் மண்சட்டியா?` — lower **54 → 55–59 → upper 60**;
26. `பொறுமைக்கு சான்று` — lower **60 → upper 61**;
27. TOC `எடுக்கவோ கோக்கவோ!` / opening `எடுக்கவோ கோக்கவோ` — lower **61 → upper 62**;
28. TOC `அந்த நாள் வந்திலை...` / opening `அந்த நாள் வந்திலை!` — lower **62 → 63 → upper 64**;
29. TOC `பனித் துளியில் பனைமரம்` / opening `பனித்துளியில் பனை மரம்` — lower **64 → upper 65**;
30. `பாரூர் போல...` — lower **65 → upper 66**.

Story 20 closes above Story 21 on shared scan **43**. Story 31 begins below Story 30 on shared scan **66**. Exclude adjacent-story material and stop after Story 30.

For every active story inspect all registered scans directly; check heading/title provenance, paragraph/dialogue structure, display or verse blocks, meaningful ornaments, collection-design furniture, page furniture and physical joins. Create `stories/<slug>/visual-fidelity.md`. Propagate a correction only when the source scan directly supports it.

## Phase guard

Visual fidelity does not authorize English translation, modernization, adaptation, republication or Digital Library onboarding. Do not open another downstream phase until visual fidelity is closed and the user explicitly authorizes the next phase.
