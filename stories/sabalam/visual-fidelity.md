# Visual Fidelity Check — சபலம்

## Scope

- Story: **சபலம்**
- Collection sequence: **3 / 37**
- Controlling source: `TVA_BOK_0064142_கலைஞர்_கருணாநிதியின்_சிறுகதைகள்.pdf`
- Printed pages: **15–21**
- Source scans: **24–30**
- Boundary witness: scan **31**, opening Story 4 **ஆட்டக்காவடி**
- Pages directly inspected: **7 / 7**, plus boundary witness

## Opening / ending findings

### Scan 24 / printed page 15

- The source opens with the story heading **`சபலம்`** followed immediately by a long horizontal rule.
- The page was already correctly classified as `story-opening`.
- The opening rule was missing from the archival structural record and is now conservatively recorded in the page record and Tamil assembly.
- Exact source positioning of the heading is not facsimile-reproduced; the semantic heading and rule are preserved.

### Scan 30 / printed page 21

- The narrative closes with `‘இந்தோ சிலோன் எக்ஸ்பிரஸ்’ கடலூரிலிருந்து புறப்பட்டது.`
- Beneath the final sentence the source contains a centered short horizontal closing ornament with three small central diamond-like marks.
- The page record used `story-conclusion`; visual-fidelity review normalizes the structural role to `story-ending`.
- The non-source Markdown display heading `அச்சு உரை` was removed from the ending record.
- The closing ornament is now recorded in the page record and Tamil assembly.

Scan **31** independently opens Story 4 **`ஆட்டக்காவடி`**; no Story 4 text is included in `சபலம்`.

## Paragraph / dialogue fidelity

All seven source pages were compared against the committed page records and Tamil assembly.

- Paragraph starts and ends on scans **24–30** are preserved.
- Dialogue separation on scans **25–30** follows the printed source.
- No accidental prose paragraph merge or split was found within a source page.
- Physical continuations across page boundaries remain traceable through source-page markers.
- Exact prose line wrapping caused only by printed page width is intentionally not reproduced.

## Display / emphasis fidelity

### Scan 28 / printed page 19

The new paragraph beginning **`வண்டி நெல்லிக்குப்பத்தைத் தாண்டிவிட்டது.`** has a visibly enlarged / heavier initial **`வ`** in the source. It clearly marks the paragraph opening. The effect is now recorded semantically in the page record and assembly without attempting to reproduce the original font size.

### Scan 27 / printed page 18

The physical page begins with a visually prominent initial **`இ`** in `இருந்தவர்கள்`, but this is the direct continuation of scan 26's unfinished `அந்தப் பெட்டியில்`. It therefore does **not** mark a new semantic paragraph and is not encoded as a structural drop-cap.

No verse, song stanza, illustration caption, or other internal display block requiring special lineation occurs in this story.

## Non-text marks

Source-significant non-text structure recorded during this activity:

1. scan 24 — long horizontal rule beneath `சபலம்`;
2. scan 30 — centered closing ornament beneath the final story sentence.

No story illustration or caption occurs on scans 24–30.

## Page furniture

- Printed page numbers and alternating running headers / running story title are excluded from the canonical story body.
- Scan 26 also contains the printer's gathering signature **`க—2`** at the bottom; it is page furniture and remains excluded from story text.
- No page-furniture leakage into the Tamil assembly was found.

## Physical joins

All six internal joins and the next-story boundary were visually checked.

1. scans **24→25**: `சக்தி` → `யிழந்து...`, yielding the physical split `சக்தியிழந்து` — continuous.
2. scans **25→26**: `உச்சரித்தது` → `குழந்தை.` — continuous.
3. scans **26→27**: `அந்தப் பெட்டியில்` → `இருந்தவர்கள் தூக்க மயக்கத்தில்...` — continuous.
4. scans **27→28**: the preceding paragraph closes on scan 27; scan 28 begins the new `வண்டி...` paragraph — no omission or duplication.
5. scans **28→29**: `ஜன்னல்` → `வழியே வீசியெறிந்தான்.` — continuous.
6. scans **29→30**: dialogue / narrative continues normally from the final scan-29 exchange to `“ஏன்?” என்றாள் அவள்.` — no omission or duplication.
7. scan **30→31**: Story 3 ends on scan 30; scan 31 opens `ஆட்டக்காவடி`.

## Corrections made

Visual-fidelity review produced **structural-only corrections**:

1. `pages/0024-sabalam-01.md`: recorded the source opening horizontal rule.
2. `pages/0028-sabalam-05.md`: recorded the enlarged initial `வ` at the `வண்டி...` paragraph opening.
3. `pages/0030-sabalam-07.md`: `page_type` changed `story-conclusion` → `story-ending`.
4. `pages/0030-sabalam-07.md`: removed the non-source `அச்சு உரை` display heading.
5. `pages/0030-sabalam-07.md`: recorded the source closing ornament.
6. `sections/sabalam.md`: synchronized the opening rule, enlarged initial, closing ornament, and visual-fidelity assembly note.
7. `indexes/page-map.md`: synchronized the opening, enlarged-initial and ending-ornament roles.

**No story wording was changed during this visual-fidelity activity.** Existing verified readings and the human possible-error queue remain intact.

## Remaining visual-fidelity issues

**None.**

## Result

**PASS — corrected**

`சபலம்` is visually source-faithful at the semantic archival level defined by `VISUAL_FIDELITY_CHECK_GUIDE.md`, after the structural corrections listed above.
