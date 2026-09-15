# Stage 1 — Batch 1 first-pass transcription

Work: **தெருக்கூத்து**  
Controlling source: `TVA_BOK_0064193_நாடும்_நாடகமும்.pdf`  
User baseline: `therukoothu.md`  
Batch: scans **25–36 / printed 17–28**

## User override

The repository default is five physical scans per batch. The user explicitly requested processing **pages/scans 25 through 36** in this iteration and instructed that the supplied Markdown be used as the baseline.

Therefore Stage 1 covers the full **12-scan play** in one durable batch.

## Method

- live `main` fetched first;
- direct scan pixels remain controlling authority;
- `therukoothu.md` used as a baseline/draft locator;
- every accepted Stage-1 reading checked against the corresponding scan;
- no OCR, web copy, Wikisource, catalogue text, alternate edition or contextual reconstruction used as source authority;
- running headers, printed folios and stray handwritten/scan marks excluded from body transcription;
- clearly readable historical character identities encoded, but the systematic 13-family glyph audit is deferred to Stage 3;
- no guessed reading inserted.

## Result

- physical scans processed: **12/12**
- printed pages represented: **17–28**
- page records created: **12/12**
- work opening: **PASS — scan 25 / `தெருக்கூத்து` / `காட்சி 1`**
- work ending: **PASS — scan 36 / `[தெருக்கூத்தும் முடிகிறது]`**
- next-unit witness: **PASS — scan 37 opens `சந்தனக்கிண்ணம்`**
- first-pass unresolved source spans: **0**
- guessed readings: **0**
- page status after Stage 1: **needs-review 12/12**
- Stage 2: **NEXT**

## Important structural correction

The earlier intake map had provisionally assigned scans **25–51 / printed 17–43** to `தெருக்கூத்து`.

Direct processing proves that boundary wrong:

- `தெருக்கூத்து` ends on **scan 36 / printed 28**;
- scan **37 / printed 29** opens `சந்தனக்கிண்ணம்`;
- scan **52 / printed 44** opens `ஆலமரத்துப் புறாக்கள்`.

The durable collection/source maps are synchronized to the corrected boundary in this Stage-1 commit.

## Baseline-supported workflow and source deviations

The Markdown baseline was useful for fast alignment, but several baseline artefacts were rejected after scan review. Representative source-supported changes:

### Scan 25

- baseline `நெற்றாட்களின்` → source **`நெற்கதிர்களின்`**
- baseline `நோக்கி திறந்த` → source **`நோக்கித் திறந்த`**
- baseline omitted the fourth song line → restored **`இந்த உலகினில் ஈடு........!!!`**
- baseline `அனுப்பி தொடர்ந்து` → source **`அனுப்பித் தொடர்ந்து`**
- stray baseline numerals/header fragments excluded

### Scan 26

- `முடிவதறகுமுன்` → **`முடிவதற்குமுன்`**
- `பிடித்துக்கொண்டாள்` → **`பிடித்துக்கொண்டான்`**
- `சன்னத்திலே` → **`கன்னத்திலே`**
- stray `18 தெருக்கூத்து` baseline/header contamination excluded

### Scan 27

- `மீள் வடிவ` → **`மீன் வடிவ`**
- split `குதிக்கின் றனர்` captured as source word **`குதிக்கின்றனர்`**

### Scan 28

- source visibly has **`இல்லை இல்லை....`**

### Scan 30

- `திமிர் ஓடித்த` → **`திமிர் ஒடித்த`**

### Scan 31

- `மூவேந்தரம்` → **`மூவேந்தரும்`**
- `ஆல் நமஸ்காரம்` → **`ஆனால் நமஸ்காரம்`**

### Scan 32

- `பார்வசியுட` → **`பார்வதியுட`**
- baseline `பரலோகத்தின் பாதைகளை` → source **`பரலோகத்தின் பாதைகள்`**

### Scan 33

- `கன்னியற்` → **`கன்னியர்`**
- restored source word omitted by baseline: **`லக்ஷ்மி`**

### Scan 35

- Stage-1 captured **`தூதன்தான்`**; Stage-2 later superseded this to source **`தூதன் தான்`**

### Scan 36

- `ஊர்வலப்` → **`ஊர்வலம்`**
- `புறப்படட்டும்` → **`புறப்படட்டுமே`**

These are Stage-1 baseline reconciliation notes, not an exhaustive Stage-2 fidelity-correction count.

## Page records

- `pages/0025-printed-017.md`
- `pages/0026-printed-018.md`
- `pages/0027-printed-019.md`
- `pages/0028-printed-020.md`
- `pages/0029-printed-021.md`
- `pages/0030-printed-022.md`
- `pages/0031-printed-023.md`
- `pages/0032-printed-024.md`
- `pages/0033-printed-025.md`
- `pages/0034-printed-026.md`
- `pages/0035-printed-027.md`
- `pages/0036-printed-028.md`

## Status

- Stage 1: **COMPLETE 12/12**
- Stage 2: **NEXT**
- Stage 3: **NOT STARTED**
- Stage 4: **NOT STARTED**
- verified: **0/12**
- needs-review: **12/12**
- blocked: **0**
- unresolved first-pass spans: **0**
- guessed readings: **0**

## Exact next activity

Run **Stage 2 visual text-fidelity audit** across scans **25–36 / printed 17–28**.

Compare the committed Stage-1 text against the controlling scan line by line / phrase by phrase, including dialogue labels, songs, scene headings, punctuation, spacing and every physical join. Correct only source-supported mismatches, keep all pages `needs-review`, synchronize controls, commit Stage 2, and stop before Stage 3.

Do not begin `சந்தனக்கிண்ணம்` in the same activity.


> Stage-2 supersession note: the direct line-by-line audit is authoritative for post-Stage-1 corrections. See `STAGE2_BATCH_001.md`.
