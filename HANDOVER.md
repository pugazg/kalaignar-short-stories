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

- Story 2 `அராபியக் கதை` is the completed 1987 witness for canonical `ஜாடி குட்டி போடுமா?`; controlling 2008 Tamil/English remain unchanged.
- Story 11 `குருவி ராமேஸ்வரம்` is the completed 1987 witness for the 2004 canonical; controlling 2004 Tamil/English remain unchanged.
- During 1987 English, these two stories must receive **witness-local English**, not replacement canonical English.

## English progress

- source stories: **25**
- English PASS: **1 / 25**
- pending: **24 / 25**
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

## Exact next activity — English Story 2 `அராபியக் கதை`

Use the verified 1987 witness workspace:

`stories/jaadi-kutti-poduma/witnesses/1987-kalaignar-sonna-kuttik-kathaigal/`

Source span:
- lower scan **6 / printed 5** → upper scan **7 / printed 6**

This is **witness-local English**. Do not alter the canonical 2008 English for `ஜாடி குட்டி போடுமா?`.

Before writing, read:

1. `ENGLISH_TRANSLATION_GUIDE.md`;
2. `SHORT_STORY_PROCESSING_GUIDE.md`;
3. `COLLECTION_SOURCE_GUIDE.md`;
4. this handover and `NEXT_CHAT_PROMPT.md`;
5. collection English tracker;
6. witness README;
7. `sections/arabiyak-kathai.md`;
8. witness pages / boundary records;
9. witness `HISTORICAL_GLYPH_AUDIT.md`;
10. witness `VARIANT_COMPARISON.md` and any audit/review controls.

Translate the complete verified 1987 witness into a witness-local `translations/en/` path, create a witness-local translation review, preserve lower-scan-6 → upper-scan-7 physical anchoring, synchronize tracker and handover controls, and stop after Story 2 unless the user explicitly expands the batch.

Do not begin `நடுத்தெரு நாராயணி` while waiting for `வெள்ளிக்கிழமை` completion in the novels workflow.
