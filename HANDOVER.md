# HANDOVER — Kalaignar Short Stories Archive

## Repository

- repository: `pugazg/kalaignar-short-stories`
- branch: `main`
- story workflow: `SHORT_STORY_PROCESSING_GUIDE.md`
- collection workflow: `COLLECTION_SOURCE_GUIDE.md`
- historical Tamil glyph workflow: `HISTORICAL_TAMIL_GLYPH_TRANSCRIPTION_GUIDE.md`
- English workflow: `ENGLISH_TRANSLATION_GUIDE.md`
- archive-wide closure history: `ARCHIVE_COMPLETION.md`

## LIVE MAIN IS AUTHORITATIVE

Always fetch live `main` first and preserve newer durable state.

## Permanent rules

- controlling scan first; no silent normalization;
- before creating any new story workspace, prove it is not already canonical under the same or an alternate title;
- preserve shared physical page boundaries exactly;
- additional witnesses never silently overwrite canonical controlling editions;
- historical Tamil typeforms are decoded by character identity, not modern visual resemblance;
- never global-replace historical-looking forms;
- source PDFs are not committed.

## New mandatory two-pass historical-glyph rule

For every potentially historical Tamil page:

1. **Pass 1 — initial transcription:** transcribe directly from the controlling scan, preserving source wording/spelling/grammar/spacing/punctuation and marking uncertainty honestly.
2. **Pass 2 — independent high-resolution glyph check:** after Pass 1 exists, reopen the same physical page at native/high resolution and recheck all 13 known historical families: `ணா / ணை / ணொ / ணோ / லை / ளை / றா / றொ / றோ / னா / னை / னொ / னோ`.

Final `verified` status requires both passes. A first-pass transcription alone is never enough.

## Closed phases — preserve

- 1977 — Tamil/visual/English **37/37 PASS**.
- 2008 — Tamil/visual/English **40/40 PASS**.
- 2004 — Tamil/visual/English **34/34 PASS**.
- 2009 new-story onboarding — **5/5 CLOSED**.
- 2009 existing-canonical witness comparison — **11/11 CLOSED**.
- supplemental English — **6/6 PASS / CLOSED**.

## ACTIVE — 1987 `கலைஞர் சொன்ன குட்டிக் கதைகள்`

Workspace: `collections/1987-kalaignar-sonna-kuttik-kathaigal/`

Controlling source: `TVA_BOK_0065566_கலைஞர்_சொன்ன_குட்டிக்_கதைகள்_1987.pdf`

Source identity:

- scans: **50**
- size: **107,757,858 bytes**
- SHA-256: **`29c986812f95c43105eec4b38fa9e02c3c4f66cf3c4e8a686b81dd28c1164f0f`**
- publisher: **செல்வகுமார் பதிப்பகம்**, மதுரை
- first edition: **1984**
- represented edition: **இரண்டாம் பதிப்பு — 1987**
- headings: **25 / 25 native/high-resolution PASS**

## Title / historical-glyph re-audit — authoritative

A complete high-resolution heading re-audit was completed on **2026-09-06**.

Three earlier title readings were corrected:

- Story 2: `அரசாபிமானக் கதை` → **`அராபியக் கதை`**;
- Story 4: `நாராயணு! நாராயணு!` → **`நாராயணா ! நாராயணா !`** — historical `ணா` decoding; source punctuation spacing preserved;
- Story 6: `முல்லை முத்துக்குமரன்` → **`மூளி மூக்குக்காரன்`**.

No other heading changed. Sensitive forms in `தென்னை`, `தெனாலிராமன்`, `அகத்திணை`, and `பூனை` were explicitly rechecked at high resolution.

Durable record: `collections/1987-kalaignar-sonna-kuttik-kathaigal/TITLE_GLYPH_REAUDIT_2026-09-06.md`.

## User-directed batching — 15 physical scans per iteration

Source/structure/canonical-identity review is complete:

- Batch 01: **6–20** — COMPLETE.
- Batch 02: **21–35** — COMPLETE.
- Batch 03: **36–50** — COMPLETE.

Durable records:

- `collections/1987-kalaignar-sonna-kuttik-kathaigal/BATCH_0001_SCANS_0006_0020.md`
- `collections/1987-kalaignar-sonna-kuttik-kathaigal/BATCH_0002_SCANS_0021_0035.md`
- `collections/1987-kalaignar-sonna-kuttik-kathaigal/BATCH_0003_SCANS_0036_0050.md`

The same 15-page rule now applies to lexical/historical-glyph closure.

## Full identity disposition — 25 / 25 COMPLETE

### Existing-canonical witnesses — 2

- Story 2 **`அராபியக் கதை`** → canonical `ஜாடி குட்டி போடுமா?`; 1987 witness only; lower 6 → upper 7.
- Story 11 `குருவி ராமேஸ்வரம்` → canonical 2004 story; 1987 witness only; lower 23 → upper 24.

No controlling canonical Tamil/English is changed from these witnesses.

### Positively distinct identities — 23

Story 1; Stories 3–10; Stories 12–25.

Resolved collision checks remain closed:

- Story 7 `சொர்க்கத்திற்குச் சென்றுவந்த அழகி!` ≠ 2004 `சொர்க்கத்திற்கு வந்தது எப்படி?`.
- Story 8 `புத்தர் உணர்த்திய உண்மை` ≠ 1977 `சித்தார்த்தன் சிலை`.
- Story 14 `புகழேந்திப் புலவர் கதை` ≠ 1977 `புகழேந்தி`.
- Story 21 `யசோதர காவியம்` ≠ canonical `அமிர்தமதி`.
- Story 19 `தெனாலிராமன் கதை` ≠ Story 24 `தெனாலிராமன் பூனை`.

Unresolved identity holds: **0**.

## Current lexical phase / exact next activity

Continue **Lexical/Glyph Batch L1 — scans 5–19 inclusive = 15 physical scans**.

Authoritative routing in this range:

- Story 1 `மன்னனும் குருவியும்!`: scan 5 → upper 6;
- Story 2 `அராபியக் கதை`: lower 6 → upper 7 — existing-canonical witness only;
- Story 3 `தென்னை மரத்தில் புல்`: lower 7 only;
- Story 4 `நாராயணா ! நாராயணா !`: 8 → 9 → upper 10;
- Story 5 `துறவியும் சீடர்களும்`: lower 10 → 11 → upper 12;
- Story 6 `மூளி மூக்குக்காரன்`: lower 12 → upper 13;
- Story 7 `சொர்க்கத்திற்குச் சென்றுவந்த அழகி!`: lower 13 → 14 → upper 15;
- Story 8 `புத்தர் உணர்த்திய உண்மை`: lower 15 → 16 → 17 → upper 18;
- Story 9 `கஜினி முகமதுவும் கவிஞர் பார்டோசியும்`: lower 18 → 19 → continues upper 20.

For every physical page: complete Pass 1 initial transcription, then complete Pass 2 independent native/high-resolution glyph audit before final `verified` status.

English remains unauthorized.

Do not begin `நடுத்தெரு நாராயணி` while waiting for `வெள்ளிக்கிழமை` completion in the novels workflow.
