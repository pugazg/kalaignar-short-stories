# HANDOVER — Kalaignar Short Stories Archive

## Repository

- repository: `pugazg/kalaignar-short-stories`
- branch: `main`
- permanent workflows: `SHORT_STORY_PROCESSING_GUIDE.md`, `COLLECTION_SOURCE_GUIDE.md`, `HISTORICAL_TAMIL_GLYPH_TRANSCRIPTION_GUIDE.md`, `ENGLISH_TRANSLATION_GUIDE.md`

## LIVE MAIN IS AUTHORITATIVE

Always fetch live `main` first and preserve newer durable state.

## Closed phases — preserve

- 1977 — Tamil/visual/English **37/37 PASS**
- 2008 — Tamil/visual/English **40/40 PASS**
- 2004 — Tamil/visual/English **34/34 PASS**
- 2009 new-story onboarding — **5/5 CLOSED**
- 2009 existing-canonical witness comparison — **11/11 CLOSED**
- supplemental English — **6/6 PASS / CLOSED**
- 1987 `கலைஞர் சொன்ன குட்டிக் கதைகள்` Tamil/source phase — **CLOSED**

## ACTIVE — 1987 English

Collection: `collections/1987-kalaignar-sonna-kuttik-kathaigal/`

Source: `TVA_BOK_0065566_கலைஞர்_சொன்ன_குட்டிக்_கதைகள்_1987.pdf` — 50 scans, 107,757,858 bytes, SHA-256 `29c986812f95c43105eec4b38fa9e02c3c4f66cf3c4e8a686b81dd28c1164f0f`, Second Edition 1987.

Tamil/source remains **25/25 CLOSED**, story-bearing scans **45/45 two-pass COMPLETE**, unresolved Tamil/source/glyph locations **0**.

## Authoritative corrections — do not revert

- Story 2 `அராபியக் கதை`
- Story 4 `நாராயணா ! நாராயணா !`
- Story 6 `மூளி மூக்குக்காரன்`
- Story 10 `இரு நிழல்கள்`, not `இரு நிகழ்வுகள்`
- Story 10 legacy directory `stories/iru-nigazhvugal/` remains for path continuity.

## Witness-only routing — preserve

- Story 2 `அராபியக் கதை` → 1987 witness-local English only; canonical 2008 Tamil/English unchanged.
- Story 11 `குருவி ராமேஸ்வரம்` → 1987 witness-local English only; canonical 2004 Tamil/English unchanged.

## English progress

User directive: **process 10 stories in each iteration**.

- source stories: **25**
- English PASS: **11 / 25**
- pending: **14 / 25**
- needs review: **0**

Completed:

- Story 1 `மன்னனும் குருவியும்!` — **PASS**
- Batch 01 Stories **2–11** — **10 / 10 PASS**
- batch record: `collections/1987-kalaignar-sonna-kuttik-kathaigal/ENGLISH_BATCH_01_STORIES_0002_0011.md`
- every Story 2–11 translation review: **PASS**
- physical source-page content-boundary alignment: **PASS 10/10**
- Tamil changed merely for translation: **No**

## Exact next activity — English Batch 02, Stories 12–21

Translate, review and synchronize these 10 stories in source order:

12. `சாமியாரும் பூக்காரியும்` — lower scan 24 → upper 25
13. `ஹஜ்ரத் அலியும் யூதனும்` — lower 25 → 26 → upper 27
14. `புகழேந்திப் புலவர் கதை` — lower 27 → 28
15. `மன மாற்றம்` — 29 → 30
16. `குறிக்கோள்` — 31 → upper 32
17. `பாலும் தண்ணீரும்` — lower 32 → 33 → upper 34
18. `ஜெயத்ரதனின் வீழ்ச்சி` — lower 34 → 35 → 36 → upper 37
19. `தெனாலிராமன் கதை` — lower 37 → 38 → upper 39
20. `வல்வில் ஓரி` — lower 39 → 40 → upper 41
21. `யசோதர காவியம்` — lower 41 → 42 → 43 → upper 44

For every story, use verified Tamil `pages/*.md` records to anchor English page markers to actual content transitions, create/update `TRANSLATION_REVIEW.md`, update story README and batch controls, and do not change Tamil unless translation exposes a genuinely source-proven defect that is reopened under the source workflow.

After Batch 02, the remaining final iteration will contain Stories **22–25** only.

Do not begin `நடுத்தெரு நாராயணி` while waiting for `வெள்ளிக்கிழமை` completion in the novels workflow.
