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
- P1 Stage A scans 73–77: **COMPLETE — 5/5 direct-transcribed**;
- direct transcription total: **5/6**;
- independent historical-glyph/source Stage B: **0/6**;
- verified: **0/6**;
- `needs-review`: **5/6** — scans 73–77;
- not-started: **1/6** — scan 78;
- blocked / unresolved blocking locations: **0 / 0**.

### Source pagination correction

Scan **73** visibly prints folio **`10`** at bottom left. Scans **74–78** visibly print **74–78**. The collection metadata now records this explicitly; never normalize scan 73 to printed page 73.

### P1 Stage-A source-sensitive queue

Stage A deliberately did not run the systematic 13-family glyph gate. `POSSIBLE_ERRORS_FOR_REVIEW.md` carries the independent-re-read queue, including `கொளு வைத்துக்`, `வழியென பதையும் உணர்ந்து`, the 74→75 `அவசரத்தை / யுணர்ந்து` continuation, `அரணுவான் / மகனுவான் / வீரனுவான்`, `கனவேகமாக`, `அவனே`, the 76→77 continuation, and closing source-odd phrases on scan 77.

## Exact next activity — P1 Stage B ONLY

Process **scans 73–77** only:

1. re-fetch live `main`;
2. re-open the same five attached source scans independently;
3. check `ணா / ணை / ணொ / ணோ / லை / ளை / றா / றொ / றோ / னா / னை / னொ / னோ` plus the Stage-A queue;
4. do not full-retranscribe; correct only where direct source evidence requires it;
5. use crops/enhancements only for actual ambiguity;
6. promote clear pages to `verified`; retain any genuine ambiguity as `needs-review`;
7. synchronize controls, commit and stop/report.

**Do not touch scan 78 in P1 Stage B.** P2 scan 78 Stage A begins only after this batch closes.
