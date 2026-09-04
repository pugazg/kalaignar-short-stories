# HANDOVER — Kalaignar Short Stories Archive

## Repository

- Repository: `pugazg/kalaignar-short-stories`
- Branch: `main`
- Story workflow: `SHORT_STORY_PROCESSING_GUIDE.md`
- Anthology workflow: `COLLECTION_SOURCE_GUIDE.md`
- Text-fidelity workflow: `TEXT_FIDELITY_CHECK_GUIDE.md`
- Text-fidelity tracker: `TEXT_FIDELITY_PROGRESS.md`
- Visual-fidelity workflow: `VISUAL_FIDELITY_CHECK_GUIDE.md`
- English-translation workflow: `ENGLISH_TRANSLATION_GUIDE.md`
- Source PDFs / renders / crops are **not** committed.

## Authoritative-state rule

Always fetch live `main` first and preserve newer durable work.

## Permanent source rules

- controlling scan first; no silent modernization of spelling, punctuation, grammar, sandhi, names or source anomalies;
- running headers/page numbers are furniture, not body text;
- `POSSIBLE_ERRORS_FOR_REVIEW.md` is a human-review queue, not proof of error;
- source-supported corrections propagate through page, assembly, audit/review and dependent layers;
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

## Closed Tamil source pass — கலைஞர் சொன்ன கதைகள்

Collection workspace: `collections/2008-kalaignar-sonna-kathaigal/`

Controlling source: `TVA_BOK_0065857_கலைஞர்_சொன்ன_கதைகள்.pdf`

- printed author: **டாக்டர் கலைஞர் மு. கருணாநிதி**;
- scanned edition: **Second Edition, December 2008**;
- source SHA-256: `1b2bf86892717776b1b3dc7fcb18dc146d5bfd0d60986509dc9cbbf5f235444b`;
- file size: **24,840,000 bytes**;
- PDF scans: **82**;
- contents entries: **40**;
- story text: scans **9–81 / printed 7–79**;
- scan **82**: verified back cover, no further story text;
- relation: **scan = printed page + 2**;
- canonical workspaces / Tamil source complete: **40 / 40**;
- Tamil source pending: **0 / 40**;
- blocked / unresolved source story text: **0**;
- English from this collection: **0 / 40**.

Nine TOC/opening-heading differences remain registered and must not be normalized: Stories **2, 11, 24, 27, 28, 29, 35, 36, 39**.

## Active phase — word-by-word text fidelity

The user explicitly authorized **text fidelity for every word** with **10 stories per iteration**.

Existing `verified` status is not proof in this phase. Every active story is re-read directly against the controlling scans, including words, joined/separated forms, punctuation, quotation marks, paragraph boundaries and physical page joins.

### Current progress

- total: **40**
- fidelity complete: **20 / 40**
- `PASS`: **8**
- `PASS — corrected`: **12**
- pending: **20 / 40**
- needs recheck: **0**
- unresolved fidelity issues among completed stories: **0**

### Completed fidelity iteration 1 — Stories 1–10

Stories **1–10** are closed. Stories **2, 3, 6 and 9** required source-supported corrections; Stories **1, 4, 5, 7, 8 and 10** passed unchanged.

### Completed fidelity iteration 2 — Stories 11–20

Stories **11–20** are closed. Stories **11 and 16** passed unchanged. Stories **12, 13, 14, 15, 17, 18, 19 and 20** are **PASS — corrected**.

Second-iteration recovered readings include:

- Story 12: `தொட்டாலும்` → **`தொடவும்`**;
- Story 13: `ஊடுருவல் செயலாளராக` → **`ஊடுதல் செயலாளராக`**;
- Story 14: first `காப்புமுற்றிருக்கிறது` → **`காப்புமுற்றிருக்கின்றது`**; later `காப்புமுற்றிருக்கிறது` remains source-faithful;
- Story 15: `உயர ஜாதிக்காரனுக்குக்` → **`உயர் ஜாதிக்காரனுக்குக்`**;
- Story 17: `போர் வீரனிடம்` → source **`போர் வீரன்படம்`** in `போர் வீரன்படம் பிரமாதமாக இருக்கிறது`;
- Story 18: `பேச்சை கேட்க` → **`பேச்சைக் கேட்க`**;
- Story 19: `என்னப்பா?` → **`என்னடா?`**;
- Story 20: `சென்னை.` → **`சென்னை,`** and `வில் நடுங்கியிருக்கும்;` → **`வில் நடுங்கியிருக்கும்.`**.

All affected page records, Tamil assemblies, audits and review queues are synchronized. Story-local `text-fidelity.md` records exist for Stories **1–20**.

## Exact next activity — text fidelity Stories 21–30

Process **all ten** stories in this iteration and stop after Story 30:

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

For every story:

1. re-fetch live `main` before source-dependent writes;
2. inspect every registered story span directly, including shared boundary material;
3. compare every word, spelling/sandhi form, punctuation, quotation boundary, paragraph and physical join;
4. verify the full phrase around every suspected mismatch;
5. propagate confirmed corrections through page, assembly, audit/review and `text-fidelity.md`;
6. if no mismatch exists, create `text-fidelity.md` with `PASS`;
7. update `TEXT_FIDELITY_PROGRESS.md` only after durable closure.

Story 20 closes above Story 21 on shared scan **43**; exclude already-closed Story-20 material. Story 30 closes above Story 31 on scan **66**; inspect the Story-31 heading only as the ending witness and do not begin Story 31 in this iteration.

## Phase guard

Text fidelity authorizes source-faithful Tamil correction only. It does not authorize modernization, adaptation, republication, Digital Library onboarding or English translation.
