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

Activation state:

- scan 73 opening heading: **`மானம்` — directly confirmed**;
- stale `மனம்`: **rejected**;
- scan 78 ending/boundary: **confirmed — final PDF scan, closing ornament + library stamp**;
- canonical dedup / alternate-title gate: **PASS — no existing canonical match**;
- page records: **6/6 initialized as `not-started`**;
- direct transcription: **0/6**;
- Stage B: **0/6**;
- verified: **0/6**;
- blocked / unresolved: **0 / 0**.

### Source pagination correction

Scan **73** visibly prints folio **`10`** at bottom left. Scans **74–78** visibly print **74–78**. Earlier controls inferred printed page 73 for scan 73; the controlling source disproves that inference. Preserve the anomaly and never normalize it silently.

## Exact next activity — P1 Stage A ONLY

Process **scans 73–77** only under the two-stage workflow:

1. re-fetch live `main`;
2. use only the attached controlling PDF;
3. directly transcribe each whole page once;
4. preserve source punctuation, spacing, paragraphing, source-odd words and clearly readable historical character identity;
5. do **not** run the systematic 13-family Stage B in the same activity;
6. do not routinely crop/reopen clear text;
7. keep scans 73–77 `needs-review` after Stage A;
8. synchronize Pass-1/current-state controls;
9. commit and stop/report.

Do **not** touch scan 78 in P1 Stage A. Its single-page P2 comes only after P1 Stage B closes.
