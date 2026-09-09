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

### Story 6 durable state

- first-pass transcription: **35/35 COMPLETE**;
- page status: **35/35 `needs-review`**;
- Historical Tamil Glyph Gate: **PASS — 35/35; 11 total corrections / 0 unresolved**;
- `ஸ்பரிசிக்கப்பட்டு` is retained as printed Tamil; later English sense: **touched / was touched**;
- final source/visual closure: **IN PROGRESS — F1–F5 PASS, 5/7 batches complete**;
- F1 scans **59–63 / pp.57–61**: **PASS — 3 corrections / 0 unresolved**;
- F2 scans **64–68 / pp.62–66**: **PASS — 8 corrections / 0 unresolved**;
- F3 scans **69–73 / pp.67–71**: **PASS — 30 corrections / 0 unresolved**;
- F4 scans **74–78 / pp.72–76**: **PASS — 18 corrections / 0 unresolved**;
- F5 scans **79–83 / pp.77–81**: **PASS — 19 corrections / 0 unresolved**;
- F6 scans **84–88 / pp.82–86**: **NEXT**;
- F5 key recoveries include `உன்னிப்பாக`, `பீடிக்கப் பட்டிருந்த`, `நம்மிருவரின் காதலை`, `இந்தப்பாழும்`, `அதைக் கொல்ல`, `உருக்கிக் கொண்டிருந்தது`, `தூங்குவதுபோல்`, plus source punctuation/spacing restorations;
- F5 joins 78→79 and 81→82 passed; touching 83→84 `காணம / லிருந்த` → `காணமலிருந்த` was checked only as a forward-boundary witness;
- assembled Tamil is synchronized through F5; corrective scans 88–92 still need synchronization when F6/F7 reach that range;
- English: **not started**.

Final-closure ledger: `stories/mudiyatha-thodarkathai/FINAL_SOURCE_VISUAL_PROGRESS.md`.
Latest batch record: `stories/mudiyatha-thodarkathai/FINAL_SOURCE_VISUAL_BATCH_F5_079_083.md`.

## Five-scan final-closure rule

Process and commit **exactly 5 physical scans per iteration**:

1. F1 59–63 — **PASS**
2. F2 64–68 — **PASS**
3. F3 69–73 — **PASS**
4. F4 74–78 — **PASS**
5. F5 79–83 — **PASS**
6. F6 84–88 — **NEXT**
7. F7 89–93

For each batch: native/high-resolution reread → ordinary wording/punctuation/spacing/page-boundary corrections → synchronize affected derivative text → update progress ledger + handover + next-chat prompt → **commit before starting the next batch**.

Keep all pages `needs-review` during partial batches. After all seven batches PASS and zero ordinary source issues remain, perform the story-wide final closure and promote all 35 pages to `verified` together.

## Exact next activity — F6 only

Process **scans 84–88 / printed 82–86 only**. Recheck every word, punctuation/spacing choice and any physical join whose two halves fall in or touch this five-scan range. Reconfirm 83→84 from the F6 side and inspect 88→89 only as the touching forward witness. Apply only source-supported corrections, preserve source-odd forms, synchronize the affected assembled derivative including the already-established scan-88 corrective reading when reached, update F6 progress, keep pages `needs-review`, update handover and next-chat prompt to F7 if F6 passes, and **commit F6 before any F7 work**.

Do not start `நடுத்தெரு நாராயணி`; its `வெள்ளிக்கிழமை` gate remains unsatisfied.
