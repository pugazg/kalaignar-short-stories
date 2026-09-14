# Stage 3 — Batch 2 historical Tamil glyph audit

Work: **நாடும் நாடகமும் (ஆசிரியர் பேசுகிறார்)**  
Controlling source: `TVA_BOK_0064193_நாடும்_நாடகமும்.pdf`  
Batch: scans **10–14 / printed 6–10**

## Result

- pages audited directly against native source pixels: **5/5**
- Stage 3: **COMPLETE / PASS**
- mandatory historical-glyph families audited: **13/13**
- families visibly represented in this batch: **10/13**
- families not present in the audited batch text: **3/13 — `ணொ / ணோ / னொ`**
- character-identity corrections: **0**
- unresolved glyph clusters: **0**
- page status after Stage 3: **needs-review 5/5**
- ordinary unresolved source-text spans: **2 — both on scan 13**
- guessed readings introduced: **0**
- Stage 4 final independent source check: **NEXT**

No OCR, web copy, Wikisource, catalogue text, or alternate edition was used.

## Mandatory-family audit

All required families were explicitly checked:

`ணா / ணை / ணொ / ணோ / லை / ளை / றா / றொ / றோ / னா / னை / னொ / னோ`.

Visible family evidence in scans 10–14:

- `ணா` — scan 14, e.g. `மண்ணாவது`
- `ணை` — scans 10 and 14, e.g. `துணைகொண்டு`, `துணையையும்`
- `லை` — multiple pages, e.g. `கலையை`, `கலை`, `சிலை`, `நிலைமை`, `வேலையிலுமே`
- `ளை` — multiple pages, e.g. `சான்றுகளைப்`, `ஆட்களையும்`, `கருவிகளையும்`, `கொள்கைகளையே`, `கருத்துக்களையும்`
- `றா` — scans 11 and 14, e.g. `நன்றாக`, `கொண்டிருக்கிறார்கள்`
- `றொ` — scan 10, `மற்றொன்று`
- `றோ` — scan 13, `காண்கிறோம்`
- `னா` — scans 10 and 14, e.g. `ஆனால்`, `அம்பினால்`
- `னை` — scans 10–13, e.g. `கற்பனை`, `நினைவில்`, `சிந்தனையைப்`, `எத்தனை`
- `னோ` — scans 12–13, e.g. `தவறினோமா`, `பெயர்தானோ`

The families `ணொ / ணோ / னொ` do not occur in the audited Batch-2 text and therefore required no character adjudication.

## Page dispositions

### Scan 10 / printed 6

Visible families: `ணை / லை / ளை / றொ / னா / னை`.

Representative forms were checked in full-word context. No character-identity change is supported.

### Scan 11 / printed 7

Visible families: `லை / ளை / றா / னை`.

Representative forms including `நன்றாக` and `நினைவில்` agree with the committed Unicode identities.

### Scan 12 / printed 8

Visible families: `லை / ளை / னை / னோ`.

The source form in `தவறினோமா` confirms `னோ`; no glyph correction is required.

### Scan 13 / printed 9

Visible families: `லை / ளை / றோ / னை / னோ`.

The glyph audit did **not** justify filling either of the two Stage-2 unresolved ordinary source-text spans. They remain explicit source-text holds, not unresolved historical-glyph identities.

### Scan 14 / printed 10

Visible families: `ணா / ணை / லை / ளை / றா / னா`.

Representative forms including `மண்ணாவது`, `துணையையும்`, `கொண்டிருக்கிறார்கள்`, and `அம்பினால்` confirm the committed character identities.

## Boundary result

The scan 13→14 split remains source-confirmed:

- scan 13: `சாதனங்`
- scan 14: `களையும்`
- continuous reading: `சாதனங்களையும்`

No glyph finding changes the boundary.

## Status

- Stage 1: **COMPLETE 5/5**
- Stage 2: **COMPLETE 5/5**
- Stage 3: **COMPLETE / PASS 5/5**
- Stage-3 character-identity corrections: **0**
- Stage-3 unresolved glyph clusters: **0**
- ordinary unresolved source-text spans: **2 — scan 13**
- pages: **needs-review 5/5**
- Stage 4: **NEXT**

## Exact next activity

Run **Batch 2 Stage 4 final independent source check** for scans **10–14 / printed 6–10**.

Reopen the full batch fresh from the Stage-3 committed text; check every page end-to-end against the controlling source; confirm all Stage-2 corrections and Stage-3 glyph dispositions; attempt final disposition of the two scan-13 source-text holds without guessing; confirm the scan 13→14 boundary; promote pages to `verified` only if no unresolved source-text issue remains.

Commit/synchronize Stage 4 and stop before beginning Batch 3.
