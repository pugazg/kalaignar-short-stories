# Stage 2 — Batch 1 visual text-fidelity audit

Work: **தெருக்கூத்து**  
Controlling source: `TVA_BOK_0064193_நாடும்_நாடகமும்.pdf`  
Batch: scans **25–36 / printed 17–28**  
Stage-1 baseline: `therukoothu.md` was a non-authoritative draft only.

## Method

- live `main` re-fetched before audit;
- all 12 committed Stage-1 page records were reopened;
- every page was compared directly against the controlling scan, line by line / phrase by phrase;
- dialogue labels, songs, scene headings, stage directions, punctuation, joined-vs-separated forms, paragraph boundaries and physical continuations were checked;
- no OCR, web copy, Wikisource, catalogue text or alternate edition was used;
- only scan-supported corrections were applied;
- systematic historical Tamil glyph-family adjudication is **not** part of Stage 2 and remains for Stage 3.

## Result

- scans audited: **12/12**
- Stage-2 source-supported corrections: **11**
- pages with corrections: **6/12 — scans 27, 31, 32, 34, 35, 36**
- pages with 0 Stage-2 corrections: **6/12 — scans 25, 26, 28, 29, 30, 33**
- unresolved ordinary source-text issues: **0**
- guessed readings: **0**
- page status after Stage 2: **needs-review 12/12**
- Stage 3 historical-glyph audit: **NEXT**

## Corrections

### Scan 27 / printed 19 — 2
1. `நான் செய்த பேறு பெரும் பேறு!` → **`நான் செய்த பெரும் பேறு!`**
2. `வலிவுமிக்க வீரர் வாழ்கவே` → **`வலிவுமிக்க வீரர் வாழ்கவே!`**

### Scan 31 / printed 23 — 1
3. `நமஸ்காரமென்று நல்ல மொழி இருக்க ஏனப்பா` → **`நமஸ்காரமென்று நல்ல மொழி இருக்க. ஏனப்பா`**

### Scan 32 / printed 24 — 4
4. `தேய்ந்து விட்டீர்கள்.` → **`தேய்ந்து விட்டார்கள்.`**
5. `மிதக்கிறீர்கள்,` → **`மிதக்கிறார்கள்,`**
6. `மறந்துவிட்டீர்கள்.` → **`மறந்துவிட்டார்கள்.`**
7. `போர்க் கருவிகள் கூடாது. புனிதமான` → **`போர்க் கருவிகள் கூடாது, புனிதமான`**

### Scan 34 / printed 26 — 2
8. `கலகல வெனச்` → **`கல கல வெனச்`**
9. removed the non-source terminal period after **`சிரிக்கிறார்`**

### Scan 35 / printed 27 — 1
10. `தூதன்தான்` → **`தூதன் தான்`**

This supersedes the Stage-1 note that had described the form as joined.

### Scan 36 / printed 28 — 1
11. `நான்தான்` → **`நான் தான்`**

## Boundary recheck

- scan 24→25 — prior work / `தெருக்கூத்து` opening: **PASS**
- scan 25→26 — `அழகு` / `சேர் ஆரணங்கு...`: **PASS**
- scan 26→27 — `வில்லும்,` / `அம்புப் பெட்டியும் இருந்தது.`: **PASS**
- scan 27→28 — `என` / `வியக்கும் வண்ணம்...`: **PASS**
- scan 28→29 — Pandiyan song continuation: **PASS**
- scan 29→30 — Cheran song continuation: **PASS**
- scan 30→31 — three-kings song continuation: **PASS**
- scan 31→32 — dialogue continuation: **PASS**
- scan 32→33 — song continuation: **PASS**
- scan 33→34 — paragraph/scene boundary: **PASS**
- scan 34→35 — Scene 4 continuation: **PASS**
- scan 35→36 — dialogue continuation: **PASS**
- scan 36 — explicit work ending `[தெருக்கூத்தும் முடிகிறது]`: **PASS**
- scan 37 — separate `சந்தனக்கிண்ணம்` opening; excluded: **PASS**

## Stage-2 disposition

**COMPLETE / PASS — 12/12 pages, 11 corrections, 0 unresolved ordinary text issues.**

All pages remain `needs-review` because Stage 3 historical-glyph audit and Stage 4 final independent source check are still pending.

## Exact next activity

Run **Stage 3 historical Tamil glyph audit** for scans **25–36 / printed 17–28**.

Explicitly audit the 13 mandatory families:

`ணா / ணை / ணொ / ணோ / லை / ளை / றா / றொ / றோ / னா / னை / னொ / னோ`

Use direct scan pixels, compare complete words/phrases, apply character-identity corrections only when source evidence supports them, record present/absent family disposition and unresolved glyph clusters, keep all pages `needs-review`, synchronize controls, commit Stage 3, and stop before Stage 4.
