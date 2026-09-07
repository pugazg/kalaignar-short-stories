# HANDOVER — Kalaignar Short Stories Archive

## Repository

- repository: `pugazg/kalaignar-short-stories`
- branch: `main`
- workflows: `SHORT_STORY_PROCESSING_GUIDE.md`, `COLLECTION_SOURCE_GUIDE.md`, `HISTORICAL_TAMIL_GLYPH_TRANSCRIPTION_GUIDE.md`

## LIVE MAIN IS AUTHORITATIVE

Always fetch live `main` first and preserve newer durable state.

## Permanent source rules

- controlling scan first; no silent normalization;
- prove canonical identity before creating a new story workspace;
- preserve shared physical page boundaries;
- additional witnesses never overwrite controlling canonical editions;
- decode historical Tamil type by character identity, never by modern visual resemblance alone;
- never global-replace historical-looking forms;
- source PDFs / inspection crops are not committed.

## Mandatory two-pass historical-glyph rule

Every historical-Tamil page requires:

1. Pass 1 direct source-faithful transcription.
2. Pass 2: reopen the same physical page at native/high resolution and independently recheck  
   `ணா / ணை / ணொ / ணோ / லை / ளை / றா / றொ / றோ / னா / னை / னொ / னோ`
   plus suspicious old-type clusters.

Final `verified` requires both passes.

## Closed phases — preserve

- 1977 — Tamil/visual/English **37/37 PASS**
- 2008 — Tamil/visual/English **40/40 PASS**
- 2004 — Tamil/visual/English **34/34 PASS**
- 2009 new-story onboarding — **5/5 CLOSED**
- 2009 existing-canonical witness comparison — **11/11 CLOSED**
- supplemental English — **6/6 PASS / CLOSED**

Do not reopen these because of an older prompt.

## ACTIVE — 1987 `கலைஞர் சொன்ன குட்டிக் கதைகள்`

Workspace: `collections/1987-kalaignar-sonna-kuttik-kathaigal/`

Controlling source: `TVA_BOK_0065566_கலைஞர்_சொன்ன_குட்டிக்_கதைகள்_1987.pdf`

- 50 scans
- 107,757,858 bytes
- SHA-256 `29c986812f95c43105eec4b38fa9e02c3c4f66cf3c4e8a686b81dd28c1164f0f`
- Second Edition, 1987
- headings: **25 / 25 PASS**
- canonical identity: **25 / 25 COMPLETE**
- distinct: **23**
- witness-only: **2**

### Authoritative title corrections — do not revert

- Story 2 `அராபியக் கதை`
- Story 4 `நாராயணா ! நாராயணா !`
- Story 6 `மூளி மூக்குக்காரன்`
- Story 10 `இரு நிழல்கள்` — direct banner recheck; earlier `இரு நிகழ்வுகள்` was wrong

## Lexical/Glyph L1 — COMPLETE

- scans **5–19 = 15 / 15**
- unresolved: **0**

## Retrospective historical-glyph correction — CLOSED through scan 34

Durable record:
`collections/1987-kalaignar-sonna-kuttik-kathaigal/RETROSPECTIVE_GLYPH_REAUDIT_L1_L2_2026-09-07.md`

Important corrected identities include:

`சொன்னாராம்`, `பேசினார்கள்`, `நிலைமையை`, `பேசினான்`, `பின்னால்`, `வினவினான்`, `அவனா!`, `இட்டானாம்`, and Story-18 `பின்னாலிருந்து`.

`அந்நிலை` was rechecked and remains unchanged.

## Lexical/Glyph L2 — COMPLETE

Ledger:
`collections/1987-kalaignar-sonna-kuttik-kathaigal/LEXICAL_GLYPH_BATCH_L2_SCANS_0020_0034.md`

- scans **20–34 = 15 / 15 COMPLETE**
- Story 9: closed
- Story 10 `இரு நிழல்கள்`: closed
- Story 11: 1987 witness closed; 2004 canonical unchanged
- Stories 12–17: closed
- Story 18 `ஜெயத்ரதனின் வீழ்ச்சி`: lower scan 34 verified; **story-wide OPEN / PARTIAL**
- unresolved L2: **0**
- English: **not authorized**

## Exact next activity — Lexical/Glyph L3

Process **scans 35–49 inclusive = 15 physical scans**.

Routing:

- Story 18 `ஜெயத்ரதனின் வீழ்ச்சி`: 35 → 36 → upper 37
- Story 19 `தெனாலிராமன் கதை`: lower 37 → 38 → upper 39
- Story 20 `வல்வில் ஓரி`: lower 39 → 40 → upper 41
- Story 21 `யசோதர காவியம்`: lower 41 → 42 → 43 → upper 44
- Story 22 `காடு சென்ற குமணன்`: lower 44 → upper 45
- Story 23 `அகத்திணை அன்பு!`: lower 45 → upper 46
- Story 24 `தெனாலிராமன் பூனை`: lower 46 → 47 → upper 48
- Story 25 `குழந்தையும் கிளியும்`: lower 48 → 49

Use Pass 1 and then independent native/high-resolution Pass 2 on every physical scan. Do not reuse modern visual resemblance as Unicode identity.

Scan 50 is the already verified blank/damaged terminal leaf and is outside the 15-scan L3 batch.

Do not begin English. Do not begin `நடுத்தெரு நாராயணி` while waiting for `வெள்ளிக்கிழமை` completion in the novels workflow.
