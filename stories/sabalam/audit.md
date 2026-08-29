# தமிழ் மூலத் தணிக்கை — சபலம்

## Audit scope

- Controlling source: `TVA_BOK_0064142_கலைஞர்_கருணாநிதியின்_சிறுகதைகள்.pdf`
- Collection: **கலைஞர் கருணாநிதியின் சிறுகதைகள்**, முதல் பதிப்பு 1977
- Story range: scans **24–30** / printed pages **15–21**
- Page records: **7 / 7**
- Source PDF stored in GitHub: **No**

## Source-review method

All seven pages were reviewed from the supplied scan, including high-resolution/native page images and enlarged spans where old typography, sandhi, page-boundary splitting or unusual words could be misread.

The next source page, scan **31 / printed page 22**, was also checked and begins **`ஆட்டக்காவடி`**, confirming the end boundary of `சபலம்` at scan 30.

No outside edition, modern grammar expectation or contextual reconstruction was allowed to overwrite the visible source. Unusual but legible readings were retained and placed in `POSSIBLE_ERRORS_FOR_REVIEW.md` for later human review.

## Page disposition

| Printed page | Scan | Status | Boundary / key note |
|---:|---:|---|---|
| 15 | 24 | verified | story opening; ends `கழுத்தில் நிற்கச் சக்தி` |
| 16 | 25 | verified | begins `யிழந்து...`; ends `உச்சரித்தது` |
| 17 | 26 | verified | begins `குழந்தை.`; ends `அந்தப் பெட்டியில்` |
| 18 | 27 | verified | begins `இருந்தவர்கள்...`; no unresolved gap |
| 19 | 28 | verified | ends `ஜன்னல்` |
| 20 | 29 | verified | begins `வழியே வீசியெறிந்தான்.`; final exchange continues to p.21 |
| 21 | 30 | verified | story conclusion; next scan starts Story 4 |

Totals:

- `verified`: **7 / 7**
- `needs-review`: **0**
- `blocked`: **0**
- explicit missing/unresolved story text: **0**

## Cross-page audit

**PASS**

Verified physical continuations:

1. printed 15→16: `கழுத்தில் நிற்கச் சக்தி` → `யிழந்து தொங்கும் தலையை...`
2. printed 16→17: `“மூர்த்தி” என்று கணீரென்று உச்சரித்தது` → `குழந்தை.`
3. printed 17→18: `அந்தப் பெட்டியில்` → `இருந்தவர்கள் தூக்க மயக்கத்தில்...`
4. printed 19→20: `ஜன்னல்` → `வழியே வீசியெறிந்தான்.`
5. printed 20→21: the station/child exchange continues directly to the page-21 question and confession.

The assembled Tamil layer keeps source-page markers at every physical boundary.

## Unusual readings / human-review layer

No source text remains unreadable, but several readings merit later human checking because they are old, colloquial, semantically unusual or typographically easy to misread.

Representative items:

- `பிரத்யட்சமாவது போல`
- `இமைகளேப் பிடித்திழுத்து`
- `ஒருவரோ டொருவர்`
- `கும்பகர்ண லோக`
- `முக்கால் பாகந்தான்`
- `கணீரென்று`
- `ஜாடையாகப்`
- `நடசத்திரத்துக்குக்`
- `கையுங்களவுமாகப்`
- `ஊற்றுவதாகயிருந்தது`
- `அந்தப் பசலை`
- `கன்னக் கதுப்பை`
- `சபலம் பிடித்த மைனர்`
- `நாலா புறமிருந்தும்`

These are tracked in `POSSIBLE_ERRORS_FOR_REVIEW.md`. A queue entry is **not** itself proof of an error and does not automatically downgrade a verified page.

## Assembly gate

`sections/sabalam.md` was assembled from all seven page records in source order.

Checks:

- source scans represented: **7 / 7**
- scan order: **24 → 30**
- printed order: **15 → 21**
- duplicated pages: **none**
- omitted pages: **none**
- Story 4 (`ஆட்டக்காவடி`) included: **No**
- unresolved story markers: **0**

## Translation gate

**Tamil story-source audit complete.**

English translation was not started in this activity. Any later user correction should first be checked against the controlling source span and then propagated through all dependent Tamil/control files.

## Audit result

**PASS — சபலம் source range fully transcribed and structurally source-complete for the current reading: 7/7 verified, 0 blocked, 0 unresolved story text, with a persistent human possible-error queue.**
