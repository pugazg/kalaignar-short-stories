# தமிழ் மூலத் தணிக்கை — குப்பைத்தொட்டி

## Audit scope

- Controlling source: `TVA_BOK_0064142_கலைஞர்_கருணாநிதியின்_சிறுகதைகள்.pdf`
- Collection: **கலைஞர் கருணாநிதியின் சிறுகதைகள்**, முதல் பதிப்பு 1977
- Story range: scans **39–46** / printed pages **30–37**
- Page records: **8 / 8**
- Source PDF stored in GitHub: **No**

## Source-review method

All eight story pages were read against the supplied controlling scan. The PDF's native embedded page images were inspected directly at high resolution. Enlarged crops and full phrase/clause/sentence spans were rechecked for difficult typography and cross-page joins. On the most difficult scan-44 reading, native pixels were compared with enlarged nearest-neighbour, sharpening and contrast views before returning to the complete source sentence.

OCR, context, modern spelling expectations and outside editions were not allowed to replace visible source wording.

Scan **47** was separately inspected and clearly opens the following story `சந்தனக்கிண்ணம்`.

## Page disposition

| Printed page | Scan | Status | Boundary / key note |
|---:|---:|---|---|
| 30 | 39 | verified | `குப்பைத்தொட்டி` opening; ends `...மேனகை,` |
| 31 | 40 | verified | receives `ரம்பை...`; unusual `போதுதானு`, `மனமனவென்று` retained |
| 32 | 41 | verified | ends `அதிலிருந்து நேரம்` |
| 33 | 42 | verified | receives continuation; ends `...சேரக்` |
| 34 | 43 | verified | receives `கூடாதா?`; ends `...கைமாறாக முன்` |
| 35 | 44 | verified | `தூராற்றம்` full-span rechecked; `பல்லைக்காட்டி` resolved; ends `தூங்குவதுபோல்` |
| 36 | 45 | verified | source sentence `...வீதிப்பக்கம் வந்து உண்மைதான்.` retained; ends `...ஒருவனல்லவா,` |
| 37 | 46 | verified | receives `போனேனோ`; story conclusion + ornamental rule |

Totals:

- `verified`: **8 / 8**
- `needs-review`: **0**
- `blocked`: **0**
- explicit missing / unresolved story text: **0**

## Cross-page audit

**PASS**

Verified physical continuations:

1. printed 30→31: `அதில் குறிப்பிடத்தக்க நட்சத்திரங்கள் மேனகை,` → `ரம்பை, ஊர்வசி, திலோத்தமை ஆகியோர்.`
2. printed 32→33: `அதிலிருந்து நேரம்` → `இரவாகத்தானிருக்குமென முடிவுகட்டி விடலாம்.`
3. printed 33→34: `எனக்குப் பக்கத்திலே ஒரு பெண் குப்பைத் தொட்டிவந்து சேரக்` → `கூடாதா?`
4. printed 34→35: `...இதற்குக் கைமாறாக முன்` → `கூட்டியே மூன்றூறு ரூபாய்...`
5. printed 35→36: `நான் தூங்குவதுபோல்` → `நடித்து நடப்பவைகளைக் கவனித்துக்கொண்டிருந்தேன்.`
6. printed 36→37: `இந்நாட்டு மன்னர்களிலே ஒருவனல்லவா,` → `எந்தக் குப்பைத்தொட்டி மறைவுக்குப் போனேனோ; தெரிய வில்லை!...`

No page is omitted or duplicated.

## Difficult-reading resolution

The story has **zero unresolved story-text blocks**. Unusual forms were not normalized merely because they look wrong.

Examples retained after source review:

- scan 40: `போதுதானு`, `மனமனவென்று`;
- scan 41: `எங்கிக் கிடந்த`, `காரணகரமான`, `உணர்ச்சி என்னை வளர்த்துக்கொண்டது`;
- scan 42: `சபரகூட மஞ்சமாகி`;
- scan 43: `குப்பைத்தொட்டி எங்கேயிருந்தால் என்ன வென்று!`;
- scan 44: `மூன்றூறு`, `அவசரியப் புத்தி`, `தூராற்றம்`;
- scan 45: `சிக்கிரம்`, `...வீதிப்பக்கம் வந்து உண்மைதான்.`;
- scan 46: `போனேனோ`, `சந்தித்தாகிவிட்டது`, `வயிறாச் சோறின்றி`.

The scan-44 word originally easy to misread was enlarged and resolved as **`பல்லைக்காட்டி`**. The scan-46 phrase was likewise enlarged to distinguish **`சற்று மறைந்து கொள்கிறாள்`** from a visually similar wrong reading.

These items remain available in `POSSIBLE_ERRORS_FOR_REVIEW.md` as a human recheck layer where appropriate. Queue presence is not proof of error.

## Story-boundary audit

- scan 39: heading **`குப்பைத்தொட்டி`** — Story 5 opening confirmed;
- scan 46: final sentence ends `அவள் கழுத்தில் தாலியைக் காணோம்.` followed by non-text ornament;
- scan 47: heading **`சந்தனக்கிண்ணம்`** — Story 6 opening confirmed;
- Story 6 text included in this workspace: **No**.

## Assembly gate

`sections/kuppai-thotti.md` was assembled in source order with explicit scan markers.

Checks:

- source scans represented: **8 / 8**
- scan order: **39 → 46**
- printed order: **30 → 37**
- duplicated pages: **none**
- omitted pages: **none**
- Story 6 text included: **No**
- unresolved story markers: **0**

## Translation gate

**Tamil story-source audit complete.**

English translation is not started in this activity. Any later user correction must first be checked against the controlling source span and then propagated through all dependent Tamil/control files.

## Audit result

**PASS — குப்பைத்தொட்டி source range fully transcribed and structurally source-complete for the current reading: 8/8 verified, 0 blocked, 0 unresolved story text, with a persistent human possible-error queue.**
