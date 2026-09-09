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

## ACTIVE — 1982 `முடியாத தொடர்கதை`

Source: `TVA_BOK_0065572_முடியாத_தொடர்கதை.pdf` — **95 scans**, **194,350,272 bytes**, SHA-256 `d69034c5374c6c1604ddeb6d8e034c4410ae0d58201f2dd1608edd0e6d8cfd41`, first edition September 1982, image-only; do not commit PDF.

Stories 1–5 are **PASS / CLOSED**. Story 6 `முடியாத தொடர்கதை` occupies scans **59–93 / printed 57–91**.

### Story 6 durable state after F7

- first-pass transcription: **35/35 COMPLETE**;
- page status: **35/35 `needs-review`** pending the separate story-wide promotion;
- Historical Tamil Glyph Gate: **PASS — 35/35; 11 total corrections / 0 unresolved**;
- final source/visual closure batches: **F1–F7 ALL PASS / 7 of 7 / 0 unresolved**;
- F1 59–63: **PASS — 3 corrections / 0 unresolved**;
- F2 64–68: **PASS — 8 corrections / 0 unresolved**;
- F3 69–73: **PASS — 30 corrections / 0 unresolved**;
- F4 74–78: **PASS — 18 corrections / 0 unresolved**;
- F5 79–83: **PASS — 19 corrections / 0 unresolved**;
- F6 84–88: **PASS — 12 new corrections / 0 unresolved**;
- F7 89–93: **PASS — 19 new corrections / 0 unresolved**;
- all previously established scan-89–92 glyph/source corrections are now synchronized in the assembled derivative: `சொல்லியனுப்பினான்`, `துட்ட லக்கணமாம்`, `மலைப்பாம்பு`, `விலக்கினான்`, `கூறினான்`, `பில்கனாவிலே`;
- `ஸ்பரிசிக்கப்பட்டு` and scan-90 `தந்தையை அண்ணை-இழந்து` remain retained as source-faithful printed forms;
- all logged physical joins are resolved; scan 93 terminal star confirmed; scan 94 advertisement excluded;
- assembled Tamil is synchronized through the story ending;
- English: **not started**.

Final-closure ledger: `stories/mudiyatha-thodarkathai/FINAL_SOURCE_VISUAL_PROGRESS.md`.
Latest batch record: `stories/mudiyatha-thodarkathai/FINAL_SOURCE_VISUAL_BATCH_F7_089_093.md`.

## Exact next activity — story-wide promotion only

F7 must already be durably committed. Then perform a separate Story-6 final-closure commit:

1. promote all **35/35** Story-6 page records together from `needs-review` to `verified`;
2. update each page's transcription method/footer to record final source/visual closure;
3. update Story README, review queue, glyph gate phase boundary, assembled index, progress ledger, root handover and next-chat prompt to **Tamil/source CLOSED**;
4. keep the source-faithful assembled Tamil unchanged except for status metadata;
5. do **not** start English unless separately authorized;
6. do **not** start `நடுத்தெரு நாராயணி` while `வெள்ளிக்கிழமை` remains incomplete.

The five-scan batch rule has been fully satisfied: every batch F1–F7 was committed before the next batch began.
