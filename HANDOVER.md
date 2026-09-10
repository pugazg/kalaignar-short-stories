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
- direct first-pass transcription: **20/22 — scans 25–44**;
- independent historical-glyph/source Stage B: **20/22 — scans 25–44**;
- verified: **20/22**;
- `needs-review`: **0/22**;
- not-started: **2/22 — scans 45–46**;
- blocked / unresolved blocking locations: **0 / 0**;
- Tamil assembly: **not started**.

P1, P2, P3 and P4 are fully closed. P4 Stage B made **4 source/line-break corrections / 0 unresolved**: scan 40 `நடைபெற்றுத்` → `நடைபெறத்`; scan 40 `கலிதான்` → historical `கலைதான்`; scan 41 `ஆத் மாக்களில்` → `ஆத்மாக்களில்`; scan 41 `களி மண்` → `களிமண்`. Scan 45 has not been touched.

## Exact next activity — P5 Stage A only

Process only **scans 45–46 / printed pages 45–46** as **Stage A — direct transcription**:

1. re-fetch live `main`;
2. read each whole page directly from the attached controlling source and transcribe once;
3. preserve source wording, punctuation, spacing, paragraphing, page boundaries and clearly readable historical character identity;
4. do **not** run the systematic 13-family Stage B in this activity;
5. do not routinely crop/enhance or repeatedly reopen clear text; closer inspection only for genuine ambiguity;
6. keep scans 45–46 `needs-review` after Stage A;
7. synchronize Pass-1/current-state controls;
8. commit Stage A;
9. stop/report.

After that durable commit, P5 Stage B on scans 45–46 becomes next. Do **not** begin Story 8 `மானம்` in the same activity.
