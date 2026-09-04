# HANDOVER — Kalaignar Short Stories Archive

## Repository

- Repository: `pugazg/kalaignar-short-stories`
- Branch: `main`
- Story workflow: `SHORT_STORY_PROCESSING_GUIDE.md`
- Collection workflow: `COLLECTION_SOURCE_GUIDE.md`
- Text-fidelity workflow/tracker: `TEXT_FIDELITY_CHECK_GUIDE.md` / `TEXT_FIDELITY_PROGRESS.md`
- 2008 visual workflow/tracker: `collections/2008-kalaignar-sonna-kathaigal/VISUAL_FIDELITY_GUIDE.md` / `VISUAL_FIDELITY_PROGRESS.md`
- English workflow: `ENGLISH_TRANSLATION_GUIDE.md`
- 1977 English tracker: `ENGLISH_TRANSLATION_PROGRESS.md` — closed at **37 / 37**
- 2008 English tracker: `collections/2008-kalaignar-sonna-kathaigal/ENGLISH_TRANSLATION_PROGRESS.md`

## LIVE MAIN IS AUTHORITATIVE

Always fetch live `main` first and preserve newer durable work. Source PDFs / renders / crops are not committed. Repository files reachable from live `main`, not chat memory or local preparation, are durable state.

## Permanent source / translation rules

- controlling scan first; no silent modernization or normalization;
- canonical verified Tamil is authoritative for English translation;
- running headers and printed page numbers are page furniture, not body text;
- shared physical scans preserve exact story boundaries;
- source-supported textual corrections propagate through page, assembly, audit/review and dependent layers;
- `POSSIBLE_ERRORS_FOR_REVIEW.md` is a human-review queue, not proof of error;
- English page markers must use exactly `<!-- source scan N; printed page M -->`;
- boundary notes belong in separate HTML comments;
- marker presence/order alone is insufficient: actual translated content boundaries must align to the verified Tamil page records.

## Closed 1977 anthology

`கலைஞர் கருணாநிதியின் சிறுகதைகள்` remains fully closed:

- Tamil source **37 / 37**;
- visual fidelity **37 / 37**;
- English translation/review **37 / 37**;
- final English structural/control QA **PASS**;
- unresolved story text **0**;
- scan **260** verified back cover.

Story 29 `திடுக்கிடும் கதை` retains the later marker-only provenance correction. Obsolete Wave-2 pin `a9b333f12128686785ee981f97313a64af12e29b` must not be reused.

## 2008 collection — source / text / visual CLOSED

Collection: **கலைஞர் சொன்ன கதைகள்**  
Workspace: `collections/2008-kalaignar-sonna-kathaigal/`  
Controlling source: `TVA_BOK_0065857_கலைஞர்_சொன்ன_கதைகள்.pdf`

- represented edition: **Second Edition, December 2008**;
- PDF scans: **82**;
- story text: scans **9–81 / printed pages 7–79**;
- scan **82**: verified back cover, no further story text;
- Tamil source: **40 / 40 complete**, 0 blocked / 0 unresolved;
- word-by-word text fidelity: **40 / 40 complete — 19 PASS / 21 PASS — corrected**;
- visual fidelity: **40 / 40 complete — all 40 PASS**.

Nine TOC/opening-heading differences remain registered and must not be normalized: Stories **2, 11, 24, 27, 28, 29, 35, 36, 39**.

## 2008 English translation — ACTIVE

Current durable state:

- English complete: **15 / 40**;
- `PASS`: **15**;
- pending: **25 / 40**;
- `NEEDS REVIEW`: **0**;
- canonical Tamil changed during English work: **No**.

Stories **1–4** remain individually closed as previously recorded.

### Completed expanded batch — Stories 5–14

The user explicitly expanded one activity to **10 stories**. Stories **5–14** are all **PASS**, with English files, `TRANSLATION_REVIEW.md`, synchronized story READMEs and verified physical page anchoring. Their existing source-sensitive control notes remain authoritative.

### Completed Story 15 — `ஒண்ணு குடுமா?`

Workspace: `stories/onnu-kuduma/`

- English: `translations/en/onnu-kuduma.md`;
- review: `TRANSLATION_REVIEW.md`;
- English title treatment: **Onnu Kuduma?**;
- source span: **lower scan 33 / printed 31 → scan 34 / printed 32 → upper scan 35 / printed 33**;
- source markers: **33 → 34 → 35**;
- physical page-boundary alignment: **PASS**;
- scan 33 contains only the opening Kalaivaanar / Udumalai Narayana Kavi statement and the English marker section matches that boundary;
- scan 34 contains the `Uthama Puthiran` social-reform passage and the complete mango/kiss comedy sequence;
- scan 35 contains only the final comedy reflection and `*`;
- source-colloquial `ஒண்ணு கொடுத்திடு` / `ஒண்ணு குடும்மா!` ambiguity is preserved with **“give him one”** in dialogue, while the title remains transliterated;
- `புல்கட்டு`, corrected `உயர் ஜாதிக்காரனுக்குக்`, and `ஆதிதிராவிடப் பெண்` were handled conservatively from verified Tamil;
- Story-14 / Story-16 adjacent material excluded: **Yes**;
- canonical Tamil changed during translation: **No**;
- result: **PASS**.

## Current exact next activity — Story 16 English

Return to the default **one story per activity** unless the user explicitly expands the batch again.

Story 16:

- title: **`அத்திரி பாச்சா`**;
- workspace: `stories/aththiri-paachaa/`;
- verified physical span: **lower scan 35 / printed page 33 → upper scan 36 / printed page 34**;
- Story 15 closes above the Story-16 heading on shared scan **35**;
- Story 17 **`செருப்போடு இரு`** begins below the Story-16 ending ornament on shared scan **36**.

Before Story-16 English work, read completely:

1. `SHORT_STORY_PROCESSING_GUIDE.md`;
2. `COLLECTION_SOURCE_GUIDE.md`;
3. `ENGLISH_TRANSLATION_GUIDE.md`;
4. `collections/2008-kalaignar-sonna-kathaigal/ENGLISH_TRANSLATION_PROGRESS.md`;
5. `TEXT_FIDELITY_CHECK_GUIDE.md` and `TEXT_FIDELITY_PROGRESS.md`;
6. `collections/2008-kalaignar-sonna-kathaigal/VISUAL_FIDELITY_GUIDE.md` and `VISUAL_FIDELITY_PROGRESS.md`;
7. this `HANDOVER.md`;
8. `NEXT_CHAT_PROMPT.md`;
9. collection README, source metadata, story inventory and scan map;
10. Story-16 README, canonical Tamil assembly, all Story-16 page records, page map, audit, `POSSIBLE_ERRORS_FOR_REVIEW.md`, `text-fidelity.md` and `visual-fidelity.md`.

Translate from the verified canonical Tamil assembly, not OCR. Check actual physical content-boundary alignment against the verified Story-16 page records. Create the English file and `TRANSLATION_REVIEW.md`, synchronize story/collection/root controls, re-fetch live `main`, and advance only after Story 16 is fully durable.

Modernization, adaptation, republication and Digital Library onboarding remain outside the current authorization.