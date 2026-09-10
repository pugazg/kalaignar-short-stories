# HANDOVER — Kalaignar Short Stories Archive

## Repository

- repository: `pugazg/kalaignar-short-stories`
- branch: `main`
- permanent guides: `SHORT_STORY_PROCESSING_GUIDE.md`, `COLLECTION_SOURCE_GUIDE.md`, `HISTORICAL_TAMIL_GLYPH_TRANSCRIPTION_GUIDE.md`, `BATCH_TRANSCRIPTION_VERIFICATION_WORKFLOW.md`, `ENGLISH_TRANSLATION_GUIDE.md`

## LIVE MAIN IS AUTHORITATIVE

Fetch live `main` first. Controlling scans outrank contextual readings; no silent normalization.

## Batch execution workflow

Each physical batch is two separate durable activities: **Stage A direct transcription → commit/stop**, then **Stage B independent historical-glyph/source verification → commit/stop**.

## External hold

`நடுத்தெரு நாராயணி` remains **BLOCKED** while `வெள்ளிக்கிழமை` is incomplete.

## ACTIVE collection — 1976 `நளாயினி`

Controlling source: attached `TVA_BOK_0065574_நளாயினி_1976.pdf` — **78 scans**, **164,748,566 bytes**, fourth edition 1976, image-only, not committed; SHA-256 pending. The attached PDF itself is the sole controlling source unless the user explicitly requests external comparison.

Story inventory retains Story 8 heading **`மானம்`** from scan 73; never regress to `மனம்`.

## Active Story 4 — `நாட்டிய கலாராணி`

Workspace: `stories/naattiya-kalarani/`; physical range **scans 25–46 / printed 25–46**.

Durable state:

- source boundary / dedup: **PASS / PASS**;
- page records: **22/22**;
- direct first-pass transcription: **22/22 — COMPLETE — scans 25–46**;
- independent historical-glyph/source Stage B: **20/22 — scans 25–44**;
- verified: **20/22**;
- `needs-review`: **2/22 — scans 45–46**;
- not-started: **0/22**;
- blocked / unresolved blocking locations: **0 / 0**;
- Tamil assembly: **not started**.

P1 through P4 are fully closed. P5 scans 45–46 have completed **Stage A only**. The final page contains the source `வணக்கம், / இன்பசாகரன்.` block and two closing ornaments. P5 source-sensitive readings are documented in `stories/naattiya-kalarani/POSSIBLE_ERRORS_FOR_REVIEW.md`.

## Exact next activity — P5 Stage B only

Process only **scans 45–46 / printed pages 45–46** as **Stage B — independent historical-glyph/source verification**:

1. re-fetch live `main` and start from the committed P5 Stage-A records;
2. independently reopen the same two controlling scans;
3. compare committed text against source pixels; do not fully retranscribe;
4. explicitly check `ணா / ணை / ணொ / ணோ / லை / ளை / றா / றொ / றோ / னா / னை / னொ / னோ` plus every P5 queue entry;
5. use crops/enhancements only for actual ambiguity;
6. record corrections individually; never global-replace;
7. promote only fully closed pages to `verified`;
8. synchronize verification/current-state controls;
9. commit Stage B and stop/report.

Do **not** begin Story 8 `மானம்` in the same activity.
