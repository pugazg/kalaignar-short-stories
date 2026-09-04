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
- fidelity complete: **30 / 40**
- `PASS`: **15**
- `PASS — corrected`: **15**
- pending: **10 / 40**
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

### Completed fidelity iteration 3 — Stories 21–30

Stories **21–30** are closed. Stories **21, 22, 23, 26, 27, 29 and 30** passed unchanged. Stories **24, 25 and 28** are **PASS — corrected**.

Third-iteration recovered readings include:

- Story 24: source punctuation `எழுத்துத் தடை, பேச்சுத் தடை,`; `தூக்கி நிறுத்திய`; `கடிதங்கள் எழுதியே கழகத்தை காத்த`; `கடிதமாகத் தீட்டினேன்`; `தொடுவான்! துவளமாட்டான்.`; `கொண்டவனுக்குத் துணை`; `ஏராளமானப் பணியாட்கள் உண்டு!`; `மாற்றார் தலைகளைப் பந்தாடும்`; `தூங்கிடுவான்`; `சல்லாபத்`; `எழுதுகின்றார் - ஏசுகின்றார்`; `தொடங்குவதற்கு`; `மணப் பாறையா?`; `யாரையாவது, உதவிக்கு அழைக்கலாம் என்றாலோ`;
- Story 25: `தெய்வீகக் கடமையின்`; `புராணிகள் கூறுவர்`; `பெரிய பதவிகளில்`; `முதல்வராக அமர்ந்து அரசோச்சியவர்`; `வருத்தம் தெரிவித்த பிறகும்`; `தீர்ப்பையொட்டி`; `நரகலோகத்திற்குச் சில`; `ஒன்று போல`; `சொர்க்கத்தில் இருக்கலாம்`; `தீவிரமாகக்`; `சொர்க்கம் செல்பவனின்`; `வெளியாகும் வங்காள`; `கட்சியின் மீதும் கட்சித் தலைவர்கள் மீதும்`;
- Story 28: `பகைத்துப் போன புலவர்` → **`பதைத்துப் போன புலவர்`**.

All affected page records, Tamil assemblies, audits and review queues are synchronized. Story-local `text-fidelity.md` records exist for Stories **1–30**.

## Exact next activity — text fidelity Stories 31–40

Process the **final ten** stories in this phase:

31. `இராமனைப் பற்றி இராமன்` — lower scan **66 → 67–68 → upper 69**;
32. `மானும் பெருமானும்` — lower **69 → 70 → upper 71**;
33. `எழுச்சிக்கு அடையாளம்` — lower **71 → upper 72**;
34. `தலையும் நுனியும்` — lower **72 → upper 73**;
35. TOC `தும்... பம்... தீம்... தோம்` / opening `தும் பம் தீம் தோம்` — lower **73 → 74–75 → upper 76**;
36. TOC `நல்லவழியும் நல்ல வழியும்` / opening `நல்வழியும் நல்ல வழியும்` — lower **76 → upper 77**;
37. `நாக்குத் தமிழ் மணக்கும்` — lower **77 → 78 → upper 79**;
38. `நீதி தேவதையே!` — lower **79 → upper 80**;
39. TOC `நன்றி சொல்லும் நேரம்...` / opening `நன்றி சொல்லும் நேரம்` — lower **80 → upper 81**;
40. `பந்தலிலே பாகற்காய்` — lower **81**; scan **82** is the back-cover witness.

For every story:

1. re-fetch live `main` before source-dependent writes;
2. inspect every registered story span directly, including shared boundary material;
3. compare every word, spelling/sandhi form, punctuation, quotation boundary, paragraph and physical join;
4. verify the full phrase around every suspected mismatch;
5. propagate confirmed corrections through page, assembly, audit/review and `text-fidelity.md`;
6. if no mismatch exists, create `text-fidelity.md` with `PASS`;
7. update `TEXT_FIDELITY_PROGRESS.md` only after durable closure.

Story 30 closes above Story 31 on shared scan **66**; exclude already-closed Story-30 material. Story 40 closes on scan **81**. Inspect scan **82** only as the verified physical back-cover/final-boundary witness; there is no Story 41.

## Phase guard

Text fidelity authorizes source-faithful Tamil correction only. It does not authorize modernization, adaptation, republication, Digital Library onboarding or English translation.
