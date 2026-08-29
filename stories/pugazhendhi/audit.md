# தமிழ் மூலத் தணிக்கை — புகழேந்தி

## Audit scope

- Controlling source: `TVA_BOK_0064142_கலைஞர்_கருணாநிதியின்_சிறுகதைகள்.pdf`
- Collection: **கலைஞர் கருணாநிதியின் சிறுகதைகள்**, முதல் பதிப்பு 1977
- Story range: scans **10–15** / printed pages **1–6**
- Page records: **6 / 6**
- Source PDF stored in GitHub: **No**

## Source-review method

Each of the six pages was inspected from the PDF's native embedded **3146 × 4826** scan image. The review used full-page and enlarged crops where necessary. Page-boundary continuations were checked on both adjoining source pages.

No OCR text, outside edition, modern grammar expectation or contextual reconstruction was used as controlling authority.

## Page disposition

| Printed page | Scan | Status | Boundary / key note |
|---:|---:|---|---|
| 1 | 10 | verified | story opening; continues `அவனது பெயர் கூறவே` |
| 2 | 11 | verified | receives page-1 continuation |
| 3 | 12 | verified | ends inside `“உங்கள் இலட்சியம்` quotation |
| 4 | 13 | verified | receives page-3 quotation continuation |
| 5 | 14 | verified | `காதற் கண்கள்` rechecked in enlarged native crop; ends `திருமணமும்` |
| 6 | 15 | verified | receives `வேண்டார்!”`; story concludes `“மேதை வாழ்க!”` |

Totals:

- `verified`: **6 / 6**
- `needs-review`: **0**
- `blocked`: **0**
- explicit missing story text: **0**

## Cross-page audit

**PASS**

1. printed 1→2: `அவனது பெயர் கூறவே` → `மக்கள் தயங்குவர்—...`
2. printed 3→4: `“உங்கள் இலட்சியம்` → `கைகூடும் வரையில்...`
3. printed 5→6: `திருமணமும்` → `வேண்டார்!”`

The assembled Tamil layer preserves a source-scan marker at each of these physical boundaries.

## Unusual readings / manual review layer

The story currently has no unreadable source gap, but several visually legible readings are semantically, grammatically or transliterationally unusual. They are intentionally **not silently corrected**.

Representative examples:

- `பாராட்டுப் படித்தது`
- `அவனோர் பிடேல்டோ!`
- `மணக்கும் அவன் நெஞ்சம்.`
- `புகழ்தரும் தீவலி`
- `தத்தரூபமாகச்`
- `மாட்டானும்!`
- `வயித்துக்கிடக்கிறது`
- `காதற் கண்கள்`
- `கால்ப் பணிவிடைகள்`
- `ஏறெடுத்தும் பாராமல்`

These and other review-worthy readings are tracked in:

`POSSIBLE_ERRORS_FOR_REVIEW.md`

An item in that file is a **human recheck candidate, not a confirmed error** and does not by itself downgrade the page from `verified`.

## Assembly gate

`sections/pugazhendhi.md` was assembled from all six page records in source order.

Checks:

- source pages represented: **6 / 6**
- source order: **10 → 15**
- printed order: **1 → 6**
- duplicated pages: **none**
- omitted pages: **none**
- Story 2 text included: **No**
- explicit unresolved markers: **0**

## Translation gate

**Tamil story-source audit complete.**

However, English translation should not begin automatically in the same activity. The next repository activity is Story 2 in source order unless the user chooses to review/correct `POSSIBLE_ERRORS_FOR_REVIEW.md` first. If translation of `புகழேந்தி` is later requested, re-read the manual recheck queue before opening the translation gate.

## Audit result

**PASS — புகழேந்தி source range fully transcribed and structurally source-complete for the current reading, with a persistent human possible-error queue.**
