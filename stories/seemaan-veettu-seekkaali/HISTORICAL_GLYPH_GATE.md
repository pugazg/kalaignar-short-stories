# Historical Tamil Glyph Gate — சீமான் வீட்டு சீக்காளி

Date: **2026-09-08**

## Scope

- controlling source: `TVA_BOK_0065572_முடியாத_தொடர்கதை.pdf`
- physical range: **PDF scans 41–49 / printed pages 39–47**
- pass: **dedicated post-transcription native/high-resolution reread**
- first-pass state entering gate: **9/9 transcribed; 9/9 `needs-review`**

## Result

**PASS — 9/9 pages; 0 unresolved historical-glyph candidates.**

Every physical page was reopened independently at native/high resolution after the first-pass transcription. The mandatory historical families were explicitly checked:

`ணா / ணை / ணொ / ணோ / லை / ளை / றா / றொ / றோ / னா / னை / னொ / னோ`

No global replacement or contextual modernization was used.

## Source-pixel corrections

| Physical scan | Printed page | Earlier first-pass reading | Source-supported reading | Historical family | Result |
|---:|---:|---|---|---|---|
| 45 | 43 | `திலவிரிகோலமாக!` | `தலைவிரிகோலமாக!` | `லை` | corrected |
| 46 | 44 | `உடலக் குளிப்பாட்டி` | `உடலைக் குளிப்பாட்டி` | `லை` | corrected |

The second correction occurs physically on scan 46. Because the first-pass page boundary currently carries that continuation inside the scan-45 page record, the corrected Unicode reading is synchronized there for now; physical provenance relocation is reserved for the separate final source/visual closure.

## Candidates rechecked and retained

These source forms were independently inspected and are not modernized:

- scan 43 `முடியும்ணு`;
- scan 43 `செதாஸ் கோப்`;
- scan 43 visibly printed source-odd `தங்கியிருக்க வேண்;`;
- scan 46 `பாரத்தைப் போட்டு`;
- scan 47 `எதிர் கொண்டழைத்தாள்`;
- scan 41 opening `சீமான் வீட்டு சீக்காளி` versus later running header `சீமான் வீட்டுச் சீக்காளி!`.

Representative already-correct historical-family readings checked in the first-pass text include scan 41 `இலைகளில்`, scan 42 `கண்ணை`, scan 44 `வேளை`, and scan 47 `கண்ணையும்`.

## Separate non-glyph issues intentionally not closed here

This gate proves historical character identity only. It does not certify ordinary lexical, punctuation, spacing, or physical-page-boundary fidelity. The final source/visual closure must separately resolve the review items recorded in `POSSIBLE_ERRORS_FOR_REVIEW.md`, including the scan 45→46 physical continuation.

## Status after gate

- Historical Tamil Glyph Gate: **PASS 9/9**
- unresolved historical-glyph candidates: **0**
- page status: **9/9 remain `needs-review`**
- final source/visual closure: **NEXT / not started**
- Story 4: **not started**

No page may be promoted to `verified` until the separate final source/visual closure passes.
