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
- scan 78 ending/boundary: **confirmed — final PDF scan, centered paired-swans closing ornament + library stamp**;
- canonical dedup / alternate-title gate: **PASS — new canonical**;
- page records: **6/6**;
- direct transcription: **6/6 — COMPLETE**;
- independent historical-glyph/source Stage B: **6/6 — COMPLETE / PASS**;
- verified: **6/6 — COMPLETE**;
- `needs-review`: **0/6**;
- not-started: **0/6**;
- corrections: **9 total** — P1: 5; P2: 4; historical-glyph corrections: 3;
- blocked / unresolved: **0 / 0**;
- Tamil assembly: **not started**.

### P1 Stage-B corrections

- scan 74: `குப்பைமேட்டில்` → `குப்பை மேட்டில்`;
- scan 74: `வையகத்தை வையத் தீர்த்தாள்` → `வையகத்தை வைத்து தீர்த்தாள்`;
- scan 75: `அரணுவான்` → `அரணாவான்` (`ணா`);
- scan 75: `மகனுவான்` → `மகனாவான்` (`னா`);
- scan 75: `வீரனுவான்` → `வீரனாவான்` (`னா`).

### P2 Stage-B corrections — scan 78

Independent high-resolution review produced four source punctuation/spacing corrections:

- `பயனென்ன?` → `பயனென்ன ?`;
- `ஏற்படக்கூடாது!` → `ஏற்படக்கூடாது !`;
- `மனித குலமே!` → `மனித குலமே !`;
- `நியாயந்தானா?` → `நியாயந்தானா ?`.

Mandatory-family positives `மனிதனை` (`னை`) and `நியாயந்தானா` (`னா`) were directly confirmed. Historical-glyph corrections on scan 78: **0**. The centered paired-swans ornament remains a source mark; the library stamp remains non-story and its obscured text is not transcribed.

### Source pagination correction

Scan **73** visibly prints folio **`10`** at bottom left. Scans **74–78** visibly print **74–78**. Never normalize scan 73 to printed page 73.

## Exact next activity — Tamil assembly + assembly review

Build the canonical assembled Tamil story from all six verified records, scans **73–78**:

1. re-fetch live `main`;
2. use the verified page records as the assembly authority; return to the PDF only if a record-to-record inconsistency requires it;
3. create the canonical `sections/maanam.md` following repository precedent;
4. preserve the source heading and all source punctuation/spacing already verified;
5. resolve only positively established physical page-boundary joins, including 74→75 `அவசரத்தை` / `யுணர்ந்து` and 76→77 `மானத்தைக் காக்கமுடியாத` / `கோழை மகனே`; review the 73→74 sentence boundary from the verified records without inventing text;
6. preserve printed separators and the final paired-swans source mark in the assembled-layer convention;
7. keep the scan-73 folio anomaly in provenance controls, not as story prose;
8. create/update `ASSEMBLY_REVIEW.md` proving **6/6 page coverage, no omission, no duplication**, and documenting every cross-page join;
9. synchronize README/collection controls/root handover/next prompt;
10. commit and stop/report.

Do **not** begin English translation in the same activity.
