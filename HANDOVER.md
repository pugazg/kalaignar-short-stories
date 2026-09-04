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
- relation: **scan = printed page + 2**.

### Collection source state

- contents: **40 / 40 transcribed**;
- TOC-derived ranges: **40 / 40 calculated**;
- story-opening scans: **40 / 40 visually checked**;
- canonical workspaces activated: **40 / 40**;
- Tamil source complete: **40 / 40**;
- Tamil source pending: **0 / 40**;
- completed-story blocked / unresolved story text: **0**;
- English from this collection: **0 / 40**.

The user's 10-story iteration instruction was followed through Stories 2–11, 12–21 and 22–31; the final source iteration contained the remaining nine Stories 32–40.

### Completed final iteration — Stories 32–40

32. `மானும் பெருமானும்` — lower 69 → 70 → upper 71 — PASS, 3/3;
33. `எழுச்சிக்கு அடையாளம்` — lower 71 → upper 72 — PASS, 2/2;
34. `தலையும் நுனியும்` — lower 72 → upper 73 — PASS, 2/2;
35. TOC `தும்... பம்... தீம்... தோம்` / opening `தும் பம் தீம் தோம்` — lower 73 → 74–75 → upper 76 — PASS, 4/4;
36. TOC `நல்லவழியும் நல்ல வழியும்` / opening `நல்வழியும் நல்ல வழியும்` — lower 76 → upper 77 — PASS, 2/2;
37. `நாக்குத் தமிழ் மணக்கும்` — lower 77 → 78 → upper 79 — PASS, 3/3;
38. `நீதி தேவதையே!` — lower 79 → upper 80 — PASS, 2/2;
39. TOC `நன்றி சொல்லும் நேரம்...` / opening `நன்றி சொல்லும் நேரம்` — lower 80 → upper 81 — PASS, 2/2;
40. `பந்தலிலே பாகற்காய்` — lower 81 — PASS, 1/1; scan 82 is the verified back-cover witness.

Story 39 closes above Story 40 on scan 81. Story 40 then closes on that same physical scan. Scan 82 contains no further story text.

### Title-variance register

Nine TOC/opening-heading differences are registered and must remain distinct:

1. #2 `ஐஸ்கட்டி` ↔ `ஐஸ் கட்டி`;
2. #11 `சாவிதான் இல்லை` ↔ `சாவி தான் இல்லை`;
3. #24 `வெண்ணெய் உருகுது வெயிலில்!` ↔ `வெண்ணெய் உருகுது வெயிலில்`;
4. #27 `எடுக்கவோ கோக்கவோ!` ↔ `எடுக்கவோ கோக்கவோ`;
5. #28 `அந்த நாள் வந்திலை...` ↔ `அந்த நாள் வந்திலை!`;
6. #29 `பனித் துளியில் பனைமரம்` ↔ `பனித்துளியில் பனை மரம்`;
7. #35 `தும்... பம்... தீம்... தோம்` ↔ `தும் பம் தீம் தோம்`;
8. #36 `நல்லவழியும் நல்ல வழியும்` ↔ `நல்வழியும் நல்ல வழியும்`;
9. #39 `நன்றி சொல்லும் நேரம்...` ↔ `நன்றி சொல்லும் நேரம்`.

## Exact next activity

The **Tamil source pass for the 2008 collection is closed**. There is no Story 41 and no further source transcription activity.

Before any future phase:

1. fetch live `main` and preserve newer durable work;
2. confirm the collection controls still agree at **40 / 40 complete, 0 pending**;
3. do **not** reopen closed Tamil text without new source evidence or a user correction;
4. do **not** automatically start English translation, visual-fidelity review, Digital Library onboarding, modernization, adaptation or republication merely because the source pass is complete.

A new downstream phase should begin only when the user explicitly requests or authorizes that phase. If English translation is selected later, follow `ENGLISH_TRANSLATION_GUIDE.md` and keep verified Tamil assemblies authoritative.

## Phase guard

The completed source-first processing of `கலைஞர் சொன்ன கதைகள்` does not itself authorize modernization, adaptation, republication, Digital Library onboarding, or changes to other repositories.