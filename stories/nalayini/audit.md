# தமிழ் மூலத் தணிக்கை — நளாயினி

## Audit scope

- Controlling source: `TVA_BOK_0064142_கலைஞர்_கருணாநிதியின்_சிறுகதைகள்.pdf`
- Collection: **கலைஞர் கருணாநிதியின் சிறுகதைகள்**, முதல் பதிப்பு 1977
- Story range: scans **16–23** / printed pages **7–14**
- Page records: **8 / 8**
- Source PDF stored in GitHub: **No**

## Source-review method

All eight pages were inspected directly from the supplied scan images. Full-page reading was combined with enlarged source spans where a word, proper name, compound or page-boundary continuation could be misread.

No outside edition, modern spelling expectation or contextual reconstruction was allowed to override the visible source. Unusual but legible readings were retained and moved to a separate human review queue rather than silently normalized.

## Page disposition

| Printed page | Scan | Status | Boundary / key note |
|---:|---:|---|---|
| 7 | 16 | verified | story opening; ends `கால்` |
| 8 | 17 | verified | receives `பாகத்துக்குமேல்`; prints `மெளத் கல்யர்` |
| 9 | 18 | verified | prints joined `மெளத்கல்யர்`; ends `தனக்குத்` |
| 10 | 19 | verified | receives `தானே...`; final quotation continues to page 11 |
| 11 | 20 | verified | receives quotation; ends `காணப்படு` |
| 12 | 21 | verified | receives `கிறார்கள்.` |
| 13 | 22 | verified | ends with `“இதயா! இது உண்மையா?”` |
| 14 | 23 | verified | answer + story conclusion + separate printed `குறிப்பு :—` |

Totals:

- `verified`: **8 / 8**
- `needs-review`: **0**
- `blocked`: **0**
- explicit missing story text: **0**

## Cross-page audit

**PASS**

The following physical continuations were checked on both adjoining scans:

1. printed 7→8: `கால்` → `பாகத்துக்குமேல் இழந்துவிட்ட மனிதன்...`
2. printed 9→10: `தனக்குத்` → `தானே ஆச்சரியப்பட்டுக் கொண்டாள்.`
3. printed 10→11: `“நளாயினி! என்னை மன்னித்துவிடு!...` → `க்ஷமித்துவிடு நளாயினி!...`
4. printed 11→12: `காணப்படு` → `கிறார்கள்.`
5. printed 13→14: `“இதயா! இது உண்மையா?”` → `“பொய் இல்லை!...”`

The assembled Tamil layer preserves source-page markers rather than hiding these physical boundaries.

## Name-form audit

The source itself varies the husband's printed name:

- scan 17: `மெளத் கல்யர்`
- scan 18: `மெளத்கல்யர்`

This is preserved as an edition-level source variation. The audit does **not** silently standardize either form.

## Printed-note boundary

The story narrative ends on printed page 14 with:

`அந்த ஆசிரமத்தில் இன்பகீதம் ஆரம்பமாயிற்று!`

Below that, the source separately prints:

`குறிப்பு :—புராணக் கதைப்படி நளாயினிதான் திரெளபதையாகப் பிறந்திருக்கிறாளாம்.`

Audit disposition: **the note is part of the physical source record but not merged into the narrative paragraph.**

## Unusual readings / human-review layer

The story has no unreadable source gap, but several readings remain worth a later human visual recheck because of old usage, uncommon compounds, Sanskrit-derived vocabulary, transliteration, sandhi or semantic oddity.

Representative examples:

- `வரவிழைந்த`
- `சோபிதம்`
- `விசாரத்தைக்`
- `வில மதிக்க வொண்ணா`
- `தவம் புரியவு மல்ல`
- `தாசிநாதீனத்தொழு!`
- `நயனவல்லித்ததை`
- `வண்ணேயாளர்`
- `எடெமுது வோர்`
- `சுருதிவிட்ட`
- `காமக்கிறுக்கு`
- `அண்டெடுத்து`
- `அம்சதூளிகா`
- `கண்ணாடை காட்டினாள்`
- `கற்புக் கரசியின்`
- `புண்ய வதியையும்`
- `எண்ணுதெல்லாம்`
- `விரகதாபத்தை`
- `அந்த வார்த்தின் காரணமாக`
- `குட்டம் பிடித்தவன்`
- `திரெளபதியாகப்`

These are tracked in `POSSIBLE_ERRORS_FOR_REVIEW.md`. An entry there is a **possible-error candidate only**, not proof of an error and not a reason by itself to downgrade a verified page.

## Assembly gate

`sections/nalayini.md` was assembled from all eight page records in source order.

Checks:

- source scans represented: **8 / 8**
- scan order: **16 → 23**
- printed order: **7 → 14**
- duplicated pages: **none**
- omitted pages: **none**
- Story 3 (`சபலம்`) included: **No**
- unresolved story markers: **0**
- printed page-14 note preserved separately: **Yes**

## Translation gate

**Tamil story-source audit complete.**

English translation is not started in this activity. If translation is later requested, first review any user-supplied corrections and the persistent possible-error queue against the controlling scan.

## Audit result

**PASS — நளாயினி source range fully transcribed and structurally source-complete for the current reading: 8/8 verified, 0 blocked, 0 unresolved story text, with a persistent human possible-error queue.**
