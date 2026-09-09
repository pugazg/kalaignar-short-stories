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
- Historical Tamil Glyph Gate: **PASS after corrective high-resolution re-audit plus F3 corrective reread — 35/35; 11 total corrections / 0 unresolved**;
- corrective source readings include `பேசினாள்`, `சொல்லியனுப்பினான்`, `துட்ட லக்கணமாம்`, `மலைப்பாம்பு`, `விலக்கினான்`, `கூறினான்`, `பில்கனாவிலே` plus the historical `ளை` fixes including scan-73 `புகுந்துவிட்டவளை`;
- `ஸ்பரிசிக்கப்பட்டு` is retained as printed Tamil; later English sense: **touched / was touched**;
- final source/visual closure: **IN PROGRESS — F1–F3 PASS, 3/7 batches complete**;
- F1 scans **59–63 / pp.57–61**: **PASS — 3 corrections / 0 unresolved**;
- F2 scans **64–68 / pp.62–66**: **PASS — 8 corrections / 0 unresolved**;
- F3 scans **69–73 / pp.67–71**: **PASS — 30 corrections / 0 unresolved**;
- F4 scans **74–78 / pp.72–76**: **NEXT**;
- F3 key source corrections include `ஓடிப் பிடித்து`, `ஓடி விட்டாள்`, `எண்ணெயும்`, `திடீரெனப்`, `அணையிலே`, `தந்தைக்குச் சிரிப்பு`, `நடைபெற்றுத் தான்`, `காதற் கிளிஞ்சல்களைப்`, `தணியாத வேட்கைக்குப்`, `புகுந்துவிட்டவளை`, `அகராதி`, `களங்கத்தை சகித்துக்கொள்ள`, `கூறி விட்டான்`, plus source hyphen restorations;
- F3 joins 69→70 and 71→72 and the 70→71 / 72→73 dialogue boundaries passed; touching 73→74 was checked only as a forward-boundary witness;
- assembled Tamil is synchronized through F3; corrective scans 88–92 still need synchronization when F6/F7 reach that range;
- English: **not started**.

Final-closure ledger: `stories/mudiyatha-thodarkathai/FINAL_SOURCE_VISUAL_PROGRESS.md`.

## Five-scan final-closure rule

Process and commit **exactly 5 physical scans per iteration**:

1. F1 59–63 — **PASS**
2. F2 64–68 — **PASS**
3. F3 69–73 — **PASS**
4. F4 74–78 — **NEXT**
5. F5 79–83
6. F6 84–88
7. F7 89–93

For each batch: native/high-resolution reread → ordinary wording/punctuation/spacing/page-boundary corrections → synchronize affected derivative text → update progress ledger + handover + next-chat prompt → **commit before starting the next batch**.

Keep all pages `needs-review` during partial batches. After all seven batches PASS and zero ordinary source issues remain, perform the story-wide final closure and promote all 35 pages to `verified` together.

## Exact next activity — F4 only

Process **scans 74–78 / printed 72–76 only**. Recheck every word, punctuation/spacing choice and any physical join whose two halves fall in or touch this five-scan range. Apply only source-supported corrections, preserve source-odd forms, synchronize the affected assembled derivative, update F4 progress, keep pages `needs-review`, update handover and next-chat prompt to F5 if F4 passes, and **commit F4 before any F5 work**.

Do not start `நடுத்தெரு நாராயணி`; its `வெள்ளிக்கிழமை` gate remains unsatisfied.
