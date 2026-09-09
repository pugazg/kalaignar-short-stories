# HANDOVER — Kalaignar Short Stories Archive

## Repository

- repository: `pugazg/kalaignar-short-stories`
- branch: `main`
- permanent workflows: `SHORT_STORY_PROCESSING_GUIDE.md`, `COLLECTION_SOURCE_GUIDE.md`, `HISTORICAL_TAMIL_GLYPH_TRANSCRIPTION_GUIDE.md`, `ENGLISH_TRANSLATION_GUIDE.md`

## LIVE MAIN IS AUTHORITATIVE

Always fetch live `main` first and preserve newer durable state.

## Permanent phase rules

- controlling scan first; no silent normalization;
- preserve physical page boundaries;
- historical Tamil glyphs are decoded by character identity, not visual resemblance;
- Tamil/source closes before English;
- anthology work proceeds one story at a time;
- each 1982 story: **first pass → dedicated historical-glyph gate → separate final source/visual closure → next story**.

## Cross-project hold

`நடுத்தெரு நாராயணி` remains **BLOCKED** while `வெள்ளிக்கிழமை` is incomplete in `pugazg/kalaignar-novels`.

## 1982 `முடியாத தொடர்கதை` — Story 6

Source: `TVA_BOK_0065572_முடியாத_தொடர்கதை.pdf` — **95 scans**, **194,350,272 bytes**, SHA-256 `d69034c5374c6c1604ddeb6d8e034c4410ae0d58201f2dd1608edd0e6d8cfd41`, first edition September 1982, image-only; do not commit PDF.

Stories 1–5 are **PASS / CLOSED**. Story 6 `முடியாத தொடர்கதை` occupies scans **59–93 / printed 57–91** and is now **TAMIL/SOURCE CLOSED**.

### Story 6 final durable state

- first-pass transcription: **35/35 COMPLETE**;
- page records: **35/35 `verified`**;
- Historical Tamil Glyph Gate: **PASS — 35/35; 11 total corrections / 0 unresolved**;
- final source/visual closure: **PASS — F1–F7 / 7 of 7 / 0 unresolved**;
- assembled Tamil: **synchronized through the story ending**;
- all physical joins: **resolved**;
- scan 93 terminal star: **confirmed**;
- scan 94 advertisement: **excluded**;
- source-faithful `ஸ்பரிசிக்கப்பட்டு` and scan-90 `தந்தையை அண்ணை-இழந்து` retained;
- English: **not started / not authorized**.

Final-closure ledger: `stories/mudiyatha-thodarkathai/FINAL_SOURCE_VISUAL_PROGRESS.md`.
Final batch record: `stories/mudiyatha-thodarkathai/FINAL_SOURCE_VISUAL_BATCH_F7_089_093.md`.

## Current hold / next permitted work

There is no authorized Story-6 Tamil/source work remaining. Do not reopen it absent genuinely new source evidence. Do not start Story-6 English unless separately authorized.

Do not start `நடுத்தெரு நாராயணி` while `வெள்ளிக்கிழமை` remains incomplete.
