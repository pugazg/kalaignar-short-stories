# Visual Fidelity Check — குப்பைத்தொட்டி

## Scope

- Story: **குப்பைத்தொட்டி**
- Collection sequence: **5 / 37**
- Controlling source: `TVA_BOK_0064142_கலைஞர்_கருணாநிதியின்_சிறுகதைகள்.pdf`
- Printed pages: **30–37**
- Source scans: **39–46**
- Boundary witness: scan **47**, opening Story 6 **சந்தனக்கிண்ணம்**
- Pages directly inspected: **8 / 8**, plus boundary witness

## Opening / ending findings

### Scan 39 / printed page 30

- The source opens with the heading **`குப்பைத்தொட்டி`** followed by a long horizontal rule.
- The page was already correctly classified as `story-opening`.
- The opening paragraph begins with a visibly enlarged initial **`வீ`** in `வீதியோரத்தில்`.
- The opening rule and enlarged initial were missing from the semantic archival record and are now recorded conservatively.

### Scan 46 / printed page 37

- The page begins by completing scan 45's unfinished `இந்நாட்டு மன்னர்களிலே ஒருவனல்லவா,` sentence.
- The final paragraph ends with `அவள் கழுத்தில் தாலியைக் காணோம்.`
- Beneath the last sentence, the source contains a centered short horizontal floral/diamond-like closing ornament.
- The page record used `story-conclusion`; visual-fidelity review changes the structural role to `story-ending` and records the closing ornament.

Scan **47** independently opens Story 6 **`சந்தனக்கிண்ணம்`** beneath its own heading and horizontal rule. No Story 6 text is included in `குப்பைத்தொட்டி`.

## Paragraph / dialogue fidelity

All eight source pages were compared against the committed page records and Tamil assembly.

- Paragraph starts and ends on scans **39–46** are preserved.
- Scan 45's three short quoted utterances — `‘கண்ணு!’`, `‘என் மூக்கு!’`, and `‘அய்யோ என் மன்மதராஜா!’` — are visibly isolated from the surrounding prose in the source and remain separate in Markdown.
- No accidental prose paragraph merge or split was found.
- Exact line wrapping caused only by the physical page width is intentionally not reproduced.

## Verse / display / emphasis fidelity

### Scan 42 / printed page 33

The source prints the quoted four-line verse as a distinct display block:

`குத்துவிளக்கெரியக் கோட்டுக்கால் கட்டிலின்மேல்`

`மெத்தென்ற பஞ்ச சயனத்தின் மேலேறிக்`

`கொத்தலர் பூங்குழல் நப்பின்னை கொங்கை மேல்`

`வைத்துக்கிடந்த மலர்மார்பா வாய் திறவாய்`

The committed page record and Tamil assembly already preserve this four-line source lineation. No wording or line-order correction was required.

### Scan 45 / printed page 36

The three quoted exclamations noted above are also already represented as isolated lines. Their source-significant separation was retained.

No other verse, illustration caption, or internal display block requires additional semantic encoding in this story.

## Non-text marks

Source-significant non-text structure recorded during this activity:

1. scan **39** — long horizontal rule beneath `குப்பைத்தொட்டி`;
2. scan **46** — centered closing ornament beneath the final story paragraph.

No story illustration or caption occurs on scans **39–46**.

## Page furniture

- Printed page numbers **30–37** remain excluded from story body.
- Alternating running furniture — the story title `குப்பைத்தொட்டி` and anthology header `கலைஞர் கருணாநிதியின் சிறுகதைகள்` — remains excluded from canonical reading text.
- Scan **42** contains the printer's gathering signature **`க—3`** at the bottom; it is page furniture and remains excluded from story text.
- No page-furniture leakage into the Tamil assembly was found.

## Physical joins

All seven internal joins and the next-story boundary were visually checked.

1. scans **39→40**: `மேனகை,` → `ரம்பை, ஊர்வசி, திலோத்தமை ஆகியோர்.` — continuous.
2. scans **40→41**: scan 40 closes its paragraph; scan 41 begins a new paragraph — no omission or duplication.
3. scans **41→42**: `அதிலிருந்து நேரம்` → `இரவாகத்தானிருக்குமென முடிவுகட்டி விடலாம்.` — continuous.
4. scans **42→43**: `சேரக்` → `கூடாதா?` — continuous.
5. scans **43→44**: `கைமாறாக முன்` → `கூட்டியே மூன்றூறு ரூபாய்...` — continuous.
6. scans **44→45**: `நான் தூங்குவதுபோல்` → `நடித்து நடப்பவைகளைக்...` — continuous.
7. scans **45→46**: `இந்நாட்டு மன்னர்களிலே ஒருவனல்லவா,` → `எந்தக் குப்பைத்தொட்டி மறைவுக்குப் போனேனோ; ...` — continuous.
8. scan **46→47**: Story 5 ends on scan 46; scan 47 opens `சந்தனக்கிண்ணம்`.

## Corrections made

Visual-fidelity review produced **structural-only corrections**:

1. `pages/0039-kuppai-thotti-01.md`: recorded the source opening horizontal rule and enlarged initial `வீ`.
2. `pages/0046-kuppai-thotti-08.md`: `page_type` changed `story-conclusion` → `story-ending`.
3. `pages/0046-kuppai-thotti-08.md`: recorded the centered source closing ornament.
4. `sections/kuppai-thotti.md`: synchronized the opening rule/enlarged initial, existing verse/display structure, and closing ornament.
5. `indexes/page-map.md`: synchronized opening, display, page-furniture and ending roles.

The scan-42 verse and scan-45 isolated dialogue lines were already structurally faithful and required no wording change.

**No story wording was changed during this visual-fidelity activity.** Existing verified readings and the human possible-error queue remain intact.

## Remaining visual-fidelity issues

**None.**

## Result

**PASS — corrected**

`குப்பைத்தொட்டி` is visually source-faithful at the semantic archival level defined by `VISUAL_FIDELITY_CHECK_GUIDE.md`, after the structural corrections listed above.
