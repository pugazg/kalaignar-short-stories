# HANDOVER — Kalaignar Short Stories Archive

## Repository

- repository: `pugazg/kalaignar-short-stories`
- branch: `main`
- permanent guides: `SHORT_STORY_PROCESSING_GUIDE.md`, `COLLECTION_SOURCE_GUIDE.md`, `HISTORICAL_TAMIL_GLYPH_TRANSCRIPTION_GUIDE.md`, `BATCH_TRANSCRIPTION_VERIFICATION_WORKFLOW.md`, `ENGLISH_TRANSLATION_GUIDE.md`

## LIVE MAIN IS AUTHORITATIVE

Fetch live `main` first. Controlling scans outrank contextual readings; no silent normalization.

## External hold

`நடுத்தெரு நாராயணி` remains **BLOCKED** while `வெள்ளிக்கிழமை` is incomplete.

## ACTIVE collection — 1976 `நளாயினி`

Controlling source: attached `TVA_BOK_0065574_நளாயினி_1976.pdf` — **78 scans**, **164,748,566 bytes**, fourth edition 1976, image-only, not committed; SHA-256 pending. The attached PDF itself is the sole controlling source unless the user explicitly requests external comparison.

## Closed Story 4 — `நாட்டிய கலாராணி`

**TAMIL SOURCE-COMPLETE** — 22/22 verified, assembly/review PASS, 0 unresolved / 0 blocked. Do not reopen without new source evidence or explicit comparison authorization.

## Active Story 8 — `மானம்`

Workspace: `stories/maanam/`; physical range **scans 73–78**.

Durable state:

- scan 73 opening heading: **`மானம்` — directly confirmed**;
- stale `மனம்`: **rejected**;
- scan 78 ending/boundary: **confirmed — final PDF scan, closing ornament + library stamp**;
- canonical dedup / alternate-title gate: **PASS — new canonical**;
- page records: **6/6**;
- P1 Stage A scans 73–77: **COMPLETE — 5/5**;
- P1 Stage B scans 73–77: **PASS — 5/5**;
- direct transcription total: **5/6**;
- Stage-B verified total: **5/6**;
- verified: **5/6** — scans 73–77;
- `needs-review`: **0/6**;
- not-started: **1/6** — scan 78;
- P1 corrections: **5 total** — scan 74: 2 source corrections; scan 75: 3 historical-glyph corrections;
- blocked / unresolved: **0 / 0**.

### P1 Stage-B corrections

- scan 74: `குப்பைமேட்டில்` → `குப்பை மேட்டில்`;
- scan 74: `வையகத்தை வையத் தீர்த்தாள்` → `வையகத்தை வைத்து தீர்த்தாள்`;
- scan 75: `அரணுவான்` → `அரணாவான்` (`ணா`);
- scan 75: `மகனுவான்` → `மகனாவான்` (`னா`);
- scan 75: `வீரனுவான்` → `வீரனாவான்` (`னா`).

All other P1 source-sensitive queue entries were independently confirmed and retained. P1 unresolved: **0**.

### Source pagination correction

Scan **73** visibly prints folio **`10`** at bottom left. Scans **74–78** visibly print **74–78**. Never normalize scan 73 to printed page 73.

## Exact next activity — P2 Stage A ONLY

Process **scan 78 only** under the two-stage workflow:

1. re-fetch live `main`;
2. use only the attached controlling PDF;
3. directly transcribe the whole final page once, including the story ending and centered closing ornament; record the library stamp as non-story/source artefact rather than fabricating text from it;
4. preserve source punctuation, spacing, paragraphing, source-odd words and clearly readable historical character identity;
5. do **not** run the systematic 13-family Stage B in the same activity;
6. keep scan 78 `needs-review` after Stage A;
7. synchronize Pass-1/current-state controls;
8. commit and stop/report.

P2 Stage B is the following separate activity. Do not assemble Tamil until scan 78 also passes Stage B.
