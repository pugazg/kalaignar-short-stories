# தெருக்கூத்து

Repository-retained dramatic work from the 1953 first edition of `நாடும் நாடகமும்`.

Per explicit user instruction, this play remains inside `pugazg/kalaignar-short-stories`.

## Controlling source

- source: `TVA_BOK_0064193_நாடும்_நாடகமும்.pdf`
- edition: **முதல் பதிப்பு — 1953**
- source scans for this work: **25–36**
- printed pages: **17–28**
- direct scan pixels are authoritative
- user-supplied baseline: `therukoothu.md`
- baseline role: **draft / locator only; every accepted reading must be supported by the scan**
- OCR / web copies / Wikisource / catalogue text / alternate editions: **not used**
- source PDF committed: **No**

## Corrected physical boundary

Earlier collection intake had provisionally mapped `தெருக்கூத்து` through scan 51. Direct processing now corrects that provisional boundary:

- scan **25 / printed 17** — opens `தெருக்கூத்து` / `காட்சி 1`
- scan **36 / printed 28** — explicitly closes with `[தெருக்கூத்தும் முடிகிறது]`
- scan **37 / printed 29** — opens the separate next unit `சந்தனக்கிண்ணம்`

Therefore the controlling physical span for this play is **25–36 / printed 17–28**.

## Four-stage workflow

The user explicitly expanded the initial Stage-1 batch to the **entire 12-scan play**.

`Stage 1 first-pass → Stage 2 visual fidelity → Stage 3 historical-glyph audit → Stage 4 final independent check`

Only Stage 4 may promote pages to `verified`.

## Current state

User-expanded Batch 1 = scans **25–36 / printed 17–28**.

- Stage 1 baseline-assisted first-pass transcription: **COMPLETE — 12/12**
- page records: **12/12**
- page status: **needs-review 12/12**
- baseline used: **yes — `therukoothu.md`**
- scan pixels checked for every page: **12/12**
- explicit unresolved first-pass source spans: **0**
- guessed readings: **0**
- scan 36 work ending: **PASS — `[தெருக்கூத்தும் முடிகிறது]`**
- scan 37 boundary witness: **PASS — opens `சந்தனக்கிண்ணம்`**
- Stage 2 visual text-fidelity audit: **COMPLETE / PASS — 12/12**
- Stage-2 source-supported corrections: **11**
- Stage-2 unresolved ordinary source-text issues: **0**
- Stage 3: **NEXT**
- Stage 4: **NOT STARTED**

Durable page map: [`indexes/page-map.md`](indexes/page-map.md)

Durable Stage-1 record: [`STAGE1_BATCH_001.md`](STAGE1_BATCH_001.md)

## Baseline use

The Markdown baseline materially accelerated Stage 1, but it was not treated as authority. Direct scan review corrected multiple baseline artefacts, including omitted text, wrong letters/words, line-break artefacts and stray page/header numerals.

Representative scan-supported repairs include:

- scan 25 — `நெற்றாட்களின்` → `நெற்கதிர்களின்`; `நோக்கி திறந்த` → `நோக்கித் திறந்த`; restored missing song line `இந்த உலகினில் ஈடு........!!!`
- scan 26 — `முடிவதறகுமுன்` → `முடிவதற்குமுன்`; `பிடித்துக்கொண்டாள்` → `பிடித்துக்கொண்டான்`; `சன்னத்திலே` → `கன்னத்திலே`
- scan 27 — `மீள் வடிவ` → `மீன் வடிவ`
- scan 28 — source has `இல்லை இல்லை....`
- scan 30 — `திமிர் ஓடித்த` → `திமிர் ஒடித்த`
- scan 31 — `மூவேந்தரம்` → `மூவேந்தரும்`; `ஆல் நமஸ்காரம்` → `ஆனால் நமஸ்காரம்`
- scan 32 — `பார்வசியுட` → `பார்வதியுட`; source reads `பரலோகத்தின் பாதைகள்`
- scan 33 — `கன்னியற்` → `கன்னியர்`; restored omitted `லக்ஷ்மி`
- scan 35 — Stage-1 `தூதன்தான்` was superseded at Stage 2 by source `தூதன் தான்`
- scan 36 — `ஊர்வலப்` → `ஊர்வலம்`; `புறப்படட்டும்` → `புறப்படட்டுமே`

This is a Stage-1 baseline comparison note, not an exhaustive Stage-2 correction count.

## Stage 2 closure

Stage 2 is **COMPLETE / PASS — 12/12 pages**.

- corrections: **11**
- corrected scans: **27, 31, 32, 34, 35, 36**
- zero-correction scans: **25, 26, 28, 29, 30, 33**
- unresolved ordinary source-text issues: **0**
- guessed readings: **0**
- page status remains: **needs-review 12/12**
- durable record: [`STAGE2_BATCH_001.md`](STAGE2_BATCH_001.md)

## Exact next activity

Run **Stage 3 historical Tamil glyph audit** for scans **25–36 / printed 17–28**.

Audit all 13 mandatory families (`ணா / ணை / ணொ / ணோ / லை / ளை / றா / றொ / றோ / னா / னை / னொ / னோ`) directly against the scans, record family disposition and any source-supported character-identity corrections, keep pages `needs-review`, synchronize controls, commit Stage 3, and stop before Stage 4.

Do not begin `சந்தனக்கிண்ணம்` in the same activity.
