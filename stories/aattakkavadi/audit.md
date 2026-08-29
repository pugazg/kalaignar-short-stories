# தமிழ் மூலத் தணிக்கை — ஆட்டக்காவடி

## Audit scope

- Controlling source: `TVA_BOK_0064142_கலைஞர்_கருணாநிதியின்_சிறுகதைகள்.pdf`
- Collection: **கலைஞர் கருணாநிதியின் சிறுகதைகள்**, முதல் பதிப்பு 1977
- Story range: scans **31–38** / printed pages **22–29**
- Page records: **8 / 8**
- Source PDF stored in GitHub: **No**

## Source-review method

All eight story scans were visually reviewed from the supplied PDF, with enlarged/full-span source inspection for unusual words, old typography, dialogue punctuation and physical page continuations. Scan **39** was also inspected and clearly opens the next story, **`குப்பைத்தொட்டி`**.

No outside edition, modern spelling expectation or contextual reconstruction was allowed to overwrite a visible source reading. Unusual but legible readings are retained in the page records and placed in `POSSIBLE_ERRORS_FOR_REVIEW.md` for later human review.

## Page disposition

| Printed page | Scan | Status | Boundary / key note |
|---:|---:|---|---|
| 22 | 31 | verified | story opening; ends `...உழைத்தாலும்` |
| 23 | 32 | verified | receives `முழுசாகக் காண முடியாத பணம்...` |
| 24 | 33 | verified | dialogue-heavy page; no unresolved gap |
| 25 | 34 | verified | ends `தாயற்ற அவள் இப்போது` |
| 26 | 35 | verified | receives `அனாதைப் பட்டத்துக்குரியவளானாள்.` |
| 27 | 36 | verified | ends `கந்தனின் வழியிலே பல` |
| 28 | 37 | verified | receives `காளையர்...`; opens Kanimozhi's letter |
| 29 | 38 | verified | letter conclusion + final narrative sentence |

Totals:

- `verified`: **8 / 8**
- `needs-review`: **0**
- `blocked`: **0**
- explicit missing/unresolved story text: **0**

## Cross-page audit

**PASS**

Verified physical continuations:

1. printed 22→23: `நாலைந்து மாதம் சேர்ந்தாற்போல் உழைத்தாலும்` → `முழுசாகக் காண முடியாத பணம்—நூறு ரூபாய்!...`
2. printed 25→26: `தாயற்ற அவள் இப்போது` → `அனாதைப் பட்டத்துக்குரியவளானாள்.`
3. printed 27→28: `கந்தனின் வழியிலே பல` → `காளையர் நடைபோடத் தொடங்கினர்.`
4. printed 28→29: Kanimozhi's letter continues from the `கரும்பை...` passage to `உங்களுடைய முடிவுக்குப் பிறகு...`.

The assembled Tamil keeps explicit source-scan markers rather than hiding physical boundaries.

## Story-boundary audit

- scan 31 / printed 22: `ஆட்டக்காவடி` opening confirmed.
- scan 38 / printed 29: final sentence ends with Kandan fainting.
- scan 39: heading **`குப்பைத்தொட்டி`**, confirming Story 5 begins there.
- Story 5 text included in this workspace: **No**.

## Unusual readings / human-review layer

No story text is physically unreadable, but several source-close readings deserve later human rechecking. High-value items include:

- `ஏழெட்டுக் குடுக்கை`
- `பக்தியின் பாற்பட்டதல்ல`
- `‘பாவலா’`
- `வாக்கலித்துவிட்டு`
- `கொஞ்சந் தோரணையில்`
- `பகுத்தறிவு புரியிலே`
- `தெரிந்த குற்றத்தைப் பிறகு செய்ய மாட்டவர்கள்`
- `சிங்காரச் சிட்டெழுப்பும்`
- `அதிருப சுந்தரன்`
- `விழலுக்கிரைக்கும்`
- `ஊரதிர ...`
- `கண்ணியவானு நீ?`
- `அபயங்கேட்கும்`
- `கருவிழியானை`
- `மனத் தீர்க்கு`
- `‘சுண்’கள்`

These are tracked in `POSSIBLE_ERRORS_FOR_REVIEW.md`. A queue entry is **not** itself proof of an error and does not automatically downgrade a verified page.

## Assembly gate

`sections/aattakkavadi.md` was assembled from all eight page records in source order.

Checks:

- source scans represented: **8 / 8**
- scan order: **31 → 38**
- printed order: **22 → 29**
- duplicated pages: **none**
- omitted pages: **none**
- Story 5 (`குப்பைத்தொட்டி`) included: **No**
- unresolved story markers: **0**

## Translation gate

**Tamil story-source audit complete.**

English translation is not started in this activity. Any later user correction should first be checked against the controlling source span and then propagated through all dependent Tamil/control files.

## Audit result

**PASS — ஆட்டக்காவடி source range fully transcribed and structurally source-complete for the current reading: 8/8 verified, 0 blocked, 0 unresolved story text, with a persistent human possible-error queue.**
