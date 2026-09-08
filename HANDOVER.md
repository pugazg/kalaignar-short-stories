# HANDOVER — Kalaignar Short Stories Archive

## Repository

- repository: `pugazg/kalaignar-short-stories`
- branch: `main`
- permanent workflows: `SHORT_STORY_PROCESSING_GUIDE.md`, `COLLECTION_SOURCE_GUIDE.md`, `HISTORICAL_TAMIL_GLYPH_TRANSCRIPTION_GUIDE.md`, `ENGLISH_TRANSLATION_GUIDE.md`

## LIVE MAIN IS AUTHORITATIVE

Always fetch live `main` first and preserve newer durable state.

## Permanent source / phase rules

- controlling scan first; no silent normalization;
- prove canonical identity before creating a new story workspace;
- preserve shared physical page boundaries;
- additional witnesses never overwrite controlling canonical editions;
- decode historical Tamil type by character identity, never by modern visual resemblance alone;
- never global-replace historical-looking forms;
- source PDFs / inspection crops are not committed;
- **Tamil/source must be fully closed before English begins; once Tamil/source is fully closed, English is automatically the next activity unless the user explicitly pauses, redirects, defers or excludes it.**

## Closed phases — preserve

- 1977 — Tamil/visual/English **37/37 PASS**
- 2008 — Tamil/visual/English **40/40 PASS**
- 2004 — Tamil/visual/English **34/34 PASS**
- 2009 new-story onboarding — **5/5 CLOSED**
- 2009 existing-canonical witness comparison — **11/11 CLOSED**
- supplemental English — **6/6 PASS / CLOSED**
- 1987 `கலைஞர் சொன்ன குட்டிக் கதைகள்` Tamil/source phase — **CLOSED**

Do not reopen closed phases merely because of an older prompt.

## ACTIVE — 1987 `கலைஞர் சொன்ன குட்டிக் கதைகள்` English

Collection workspace:
`collections/1987-kalaignar-sonna-kuttik-kathaigal/`

Controlling source:
`TVA_BOK_0065566_கலைஞர்_சொன்ன_குட்டிக்_கதைகள்_1987.pdf`

- 50 scans
- 107,757,858 bytes
- SHA-256 `29c986812f95c43105eec4b38fa9e02c3c4f66cf3c4e8a686b81dd28c1164f0f`
- Second Edition, 1987
- headings: **25 / 25 PASS**
- canonical identity: **25 / 25 COMPLETE**
- distinct: **23**
- witness-only: **2**
- story-bearing scans **5–49 = 45 / 45 Pass 1 + independent Pass 2 COMPLETE**
- scan 50: verified blank/damaged terminal non-story leaf
- unresolved 1987 Tamil/source or historical-glyph locations: **0**

Final Tamil release record:
`collections/1987-kalaignar-sonna-kuttik-kathaigal/FINAL_TAMIL_SOURCE_RELEASE_AUDIT_2026-09-07.md`

English tracker:
`collections/1987-kalaignar-sonna-kuttik-kathaigal/ENGLISH_TRANSLATION_PROGRESS.md`

## Authoritative corrections — do not revert

- Story 2 `அராபியக் கதை`
- Story 4 `நாராயணா ! நாராயணா !`
- Story 6 `மூளி மூக்குக்காரன்`
- Story 10 `இரு நிழல்கள்` — not `இரு நிகழ்வுகள்`

Story 10 retains directory `stories/iru-nigazhvugal/` only for path continuity.

Historical/source-sensitive resolved forms include `சொன்னாராம்`, `பேசினார்கள்`, `நிலைமையை`, `பேசினான்`, `பின்னால்`, `வினவினான்`, `அவனா!`, `இட்டானாம்`, `பின்னாலிருந்து`, `மூன்றாண்டுகாலம்`, `பின்னாலே`, `மன்னா`, `நோஞ்சானை`, `அந்தநாள் வந்தில அருங்கவிப் புலவோய்`, `பெற்றுஉன்`, `அன்பில்லையே`, `நன்றாக`. `அந்நிலை` remains unchanged.

## Witness-only routing — preserve

- Story 2 `அராபியக் கதை` is the completed 1987 witness for canonical `ஜாடி குட்டி போடுமா?`; controlling 2008 Tamil/English remain unchanged. Its 1987 English is witness-local.
- Story 11 `குருவி ராமேஸ்வரம்` is the completed 1987 witness for the 2004 canonical; controlling 2004 Tamil/English remain unchanged. Its 1987 English is witness-local.

## English progress

User directive: **process 10 stories in each iteration**.

- source stories: **25**
- English PASS: **11 / 25**
- pending: **14 / 25**
- needs review: **0**

### Story 1 — `மன்னனும் குருவியும்!` — PASS

Workspace: `stories/mannanum-kuruviyum/`

- source span: scan **5 / printed 4 → upper scan 6 / printed 5**
- English title: **The King and the Sparrow!**
- translation: `translations/en/mannanum-kuruviyum.md`
- review: `TRANSLATION_REVIEW.md` — **PASS**
- physical source-page anchoring: **PASS**
- lower scan 6 / Story 2 excluded: **Yes**
- Tamil changed during translation: **No**

### Batch 01 — Stories 2–11 — PASS

Record:
`collections/1987-kalaignar-sonna-kuttik-kathaigal/ENGLISH_BATCH_01_STORIES_0002_0011.md`

- translated/reviewed: **10 / 10 PASS**
- physical source-page content-boundary alignment: **PASS 10/10**
- unresolved English review items: **0**
- Tamil changed merely for English fluency: **No**
- Story 2 controlling 2008 Tamil/English changed: **No**
- Story 11 controlling 2004 Tamil/English changed: **No**

## Exact next activity — English Batch 02, Stories 12–21

Process the next 10 stories in source order:

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

For each: use verified Tamil `pages/*.md` records for physical anchoring; translate the complete verified Tamil; create `TRANSLATION_REVIEW.md`; update story README; do not silently normalize source-odd wording; and reopen Tamil only if translation reveals a genuinely source-proven defect under the source workflow.

After Batch 02, the final English iteration contains Stories **22–25**.

Do not begin `நடுத்தெரு நாராயணி` while waiting for `வெள்ளிக்கிழமை` completion in the novels workflow.
