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

1. **Pass 1:** direct source-faithful transcription, preserving wording/spelling/grammar/spacing/punctuation and marking uncertainty honestly.
2. **Pass 2:** only after Pass 1 exists, reopen the same page at native/high resolution and independently recheck `ணா / ணை / ணொ / ணோ / லை / ளை / றா / றொ / றோ / னா / னை / னொ / னோ` plus any suspicious old-type cluster.

Final `verified` requires both passes.

## Closed phases — preserve

- 1977 — Tamil/visual/English **37/37 PASS**.
- 2008 — Tamil/visual/English **40/40 PASS**.
- 2004 — Tamil/visual/English **34/34 PASS**.
- 2009 new-story onboarding — **5/5 CLOSED**.
- 2009 existing-canonical witness comparison — **11/11 CLOSED**.
- supplemental English — **6/6 PASS / CLOSED**.

Do not reopen these phases because of an older copied prompt.

## ACTIVE — 1987 `கலைஞர் சொன்ன குட்டிக் கதைகள்`

Workspace: `collections/1987-kalaignar-sonna-kuttik-kathaigal/`

Controlling source: `TVA_BOK_0065566_கலைஞர்_சொன்ன_குட்டிக்_கதைகள்_1987.pdf`

- scans: **50**
- size: **107,757,858 bytes**
- SHA-256: **`29c986812f95c43105eec4b38fa9e02c3c4f66cf3c4e8a686b81dd28c1164f0f`**
- represented edition: **Second Edition, 1987**
- headings: **25 / 25 native/high-resolution PASS**
- canonical identity: **25 / 25 COMPLETE**
- distinct identities: **23**
- witness-only identities: **2**

### Authoritative title corrections

Do not revert:

- Story 2 **`அராபியக் கதை`**;
- Story 4 **`நாராயணா ! நாராயணா !`** — historical `ணா`, spaces before `!` preserved;
- Story 6 **`மூளி மூக்குக்காரன்`**.

## Lexical/Glyph Batch L1 — COMPLETE

Durable ledger: `collections/1987-kalaignar-sonna-kuttik-kathaigal/LEXICAL_GLYPH_BATCH_L1_SCANS_0005_0019.md`.

Scans **5–19 = 15 / 15** are durably closed at the assigned physical-page level with Pass 1 + independent Pass 2.

- Story 1: full PASS.
- Story 2 `அராபியக் கதை`: full 1987 witness PASS for canonical `ஜாடி குட்டி போடுமா?`; canonical 2008 Tamil/English unchanged.
- Stories 3–8: full PASS.
- Story 9: lower scan 18 + scan 19 PASS; **full-story closure remains OPEN until upper scan 20**.
- unresolved L1 in-batch lexical/glyph locations: **0**.

Pass-2 findings retained in the ledger include Story-2 `இவனோ` / `அவனோ` (`னோ`), source `மறுமாள்`, Story-3 historical `னை`, and Story-4 historical `ணா`.

## Exact next activity — Lexical/Glyph Batch L2

Process **scans 20–34 inclusive = 15 physical scans**.

Authoritative routing:

- scan 20: upper Story 9 `கஜினி முகமதுவும் கவிஞர் பார்டோசியும்` ending; lower Story 10 `இரு நிகழ்வுகள்` begins;
- Story 10: lower 20 → 21 → 22 → upper 23;
- Story 11 `குருவி ராமேஸ்வரம்`: lower 23 → upper 24 — **1987 witness only** for the existing 2004 canonical story;
- Story 12 `சாமியாரும் பூக்காரியும்`: lower 24 → upper 25;
- Story 13 `ஹஜ்ரத் அலியும் யூதனும்`: lower 25 → 26 → upper 27;
- Story 14 `புகழேந்திப் புலவர் கதை`: lower 27 → 28;
- Story 15 `மன மாற்றம்`: 29 → 30;
- Story 16 `குறிக்கோள்`: 31 → upper 32;
- Story 17 `பாலும் தண்ணீரும்`: lower 32 → 33 → upper 34;
- Story 18 `ஜெயத்ரதனின் வீழ்ச்சி`: begins lower 34 and continues beyond L2.

For every physical scan, perform Pass 1 first and then the separate native/high-resolution Pass 2. Do not mark Story 18 complete at the L2 boundary.

English remains unauthorized.

Do not begin `நடுத்தெரு நாராயணி` while waiting for `வெள்ளிக்கிழமை` completion in the novels workflow.
