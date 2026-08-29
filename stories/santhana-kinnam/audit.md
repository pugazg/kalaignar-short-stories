# தமிழ் மூலத் தணிக்கை — சந்தனக்கிண்ணம்

## Audit scope

- Controlling source: `TVA_BOK_0064142_கலைஞர்_கருணாநிதியின்_சிறுகதைகள்.pdf`
- Collection: **கலைஞர் கருணாநிதியின் சிறுகதைகள்**, முதல் பதிப்பு 1977
- Story range: scans **47–56** / printed pages **38–47**
- Page records: **10 / 10**
- Source PDF stored in GitHub: **No**

## Source-review method

All ten story scans were directly reviewed from the controlling PDF. Native/high-resolution page views and enlarged full-span inspection were used for difficult typography, poetic lines, old spellings, dialogue punctuation and physical page continuations. Scan **57** was separately inspected and clearly opens Story 7, **`சங்கிலிச்சாமி`**.

No outside edition, modern spelling expectation or contextual reconstruction was allowed to overwrite a visible source reading. Unusual but legible readings are retained in the page records and placed in `POSSIBLE_ERRORS_FOR_REVIEW.md` for later human review.

## Page disposition

| Printed page | Scan | Status | Boundary / key note |
|---:|---:|---|---|
| 38 | 47 | verified | story opening; complete final sentence |
| 39 | 48 | verified | speech + beginning of long poem |
| 40 | 49 | verified | poem continues; no unresolved text |
| 41 | 50 | verified | poem closes; prose ends `அறிஞர்களின்` |
| 42 | 51 | verified | receives `பாராட்டுக்குரிய...`; ends Kandan dialogue setup |
| 43 | 52 | verified | receives Kamala's answer; complete final sentence |
| 44 | 53 | verified | anti-Hindi agitation passage; ends `கந்தன்,` |
| 45 | 54 | verified | receives `கையிலே...`; ends `என்று` |
| 46 | 55 | verified | receives `அழுதான் கந்தன்.`; ends `அசையாமல்` |
| 47 | 56 | verified | receives `அப்படியே...`; story conclusion + ornamental rule |

Totals:

- `verified`: **10 / 10**
- `needs-review`: **0**
- `blocked`: **0**
- explicit missing/unresolved story text: **0**

## Cross-page audit

**PASS**

Verified physical continuations:

1. printed 39→40: the poem continues after `மறவன் மாளிகை!`.
2. printed 40→41: `மானமற்ற வம்சமா நீ? ஏடா?` → `மறத்தமிழக் குடியிலே மாசு தூவி விட்டாய்!`.
3. printed 41→42: `அறிஞர்களின்` → `பாராட்டுக்குரிய ஓர் அன்புத் துணை...`.
4. printed 42→43: Kandan's `கடலிலே மீனை...` setup → Kamala's `வெள்ளைக்காரன் மீனைப் பார்த்து...`.
5. printed 44→45: `கந்தன்,` → `கையிலே கொடியேந்தியவாறு...`.
6. printed 45→46: `என்று` → `அழுதான் கந்தன்.`.
7. printed 46→47: `அசையாமல்` → `அப்படியே நின்று கந்தன்...`.

Printed pages 38 and 43 end complete paragraphs before the following scan.

## Story-boundary audit

- scan 47 / printed 38: `சந்தனக்கிண்ணம்` opening confirmed.
- scan 56 / printed 47: final paragraph ends `...சந்தர்ப்பம் வருமே; அப்போது!`, followed by ornamental rule.
- scan 57: heading **`சங்கிலிச்சாமி`**, confirming Story 7 begins there.
- Story 7 text included in this workspace: **No**.

## Difficult-reading / source-fidelity audit

The following representative spans were checked at full-source-span level rather than accepted from isolated OCR/crops:

- scan 48: `திராவிட உட்கல வங்க`, `திராவிட வித்யாபூஷணம்`, `கீதமிசைத்துத் தந்தார்`, `கிலியும்`;
- scan 49: `கண்டலுக்குப் போர்போன`, `மோழைக்குப் பெயர் போர்வீரனும்!`, old feminine verb forms;
- scan 50: `எண்பதை நெருங்கிய`, `புதுப்புறாவின்`;
- scan 52: `அவள் வலுவில் பேசவந்தாலும்`, `கமலாவைவிட்டுக் கள்ளச் சொல்லிக் கொண்டேயிருந்தாள்`;
- scan 53: `வாட்ட சாட்டமான`, `புலிநிகர்`;
- scan 54: `மோகனத்திலே`, `கழுதை தேய்ந்து கட்டெறும் பாயிற்று!`, `தடந் தோள்களிலே`;
- scan 55: `பாக்கி வெள்ளியிலே!`, `தோழி யளித்தது`;
- scan 56: `திறக்கவே யில்லை`, `பணக்காரனுமில்லா விட்டாலும்`, `தயாரா யிருக்கிறான்`.

These readings remain source-close. Their inclusion in the human review queue is not itself evidence that they are errors.

## Assembly gate

`sections/santhana-kinnam.md` was assembled from all ten page records in source order.

Checks:

- source scans represented: **10 / 10**
- scan order: **47 → 56**
- printed order: **38 → 47**
- duplicated pages: **none**
- omitted pages: **none**
- Story 7 (`சங்கிலிச்சாமி`) included: **No**
- unresolved story markers: **0**

## Translation gate

**Tamil story-source audit complete.**

English translation is not started in this activity. Any later user correction should first be checked against the controlling source span and then propagated through all dependent Tamil/control files.

## Audit result

**PASS — சந்தனக்கிண்ணம் source range fully transcribed and structurally source-complete for the current reading: 10/10 verified, 0 blocked, 0 unresolved story text, with a persistent human possible-error queue.**
