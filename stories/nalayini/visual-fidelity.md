# Visual Fidelity Check — நளாயினி

## Scope

- Story: **நளாயினி**
- Collection sequence: **2 / 37**
- Controlling source: `TVA_BOK_0064142_கலைஞர்_கருணாநிதியின்_சிறுகதைகள்.pdf`
- Printed pages: **7–14**
- Source scans: **16–23**
- Boundary witness: scan **24**, opening Story 3 **சபலம்**
- Pages directly inspected: **8 / 8**, plus boundary witness

## Opening / ending findings

### Scan 16 / printed page 7

- The source opens with heading **`நளாயினி`** and a long horizontal rule directly beneath the heading.
- The page was already correctly classified as `story-opening`.
- The opening rule was missing from the archival structural record and is now conservatively recorded in the page record and Tamil assembly.

### Scan 23 / printed page 14

- The narrative concludes with `அந்த ஆசிரமத்தில் இன்பகீதம் ஆரம்பமாயிற்று!`.
- A long horizontal separator then divides the narrative from the separately printed `குறிப்பு :—` note.
- Beneath the note, the page contains a centered short horizontal closing ornament with three small central diamond-like marks.
- The page record used the custom type `story-conclusion-and-note`; visual-fidelity review normalizes the structural role to `story-ending` while preserving the note as a separate source layer.
- Non-source Markdown display headings `அச்சு உரை` and `அச்சு குறிப்பு` were removed from the ending record.
- The separator and closing ornament are now recorded in the page record and Tamil assembly.

Scan **24** independently opens Story 3 **`சபலம்`**; no Story 3 text is included in `நளாயினி`.

## Paragraph / dialogue fidelity

All eight source pages were compared against the committed page records and assembly.

- Paragraph starts and ends on scans **16–23** are preserved.
- Dialogue is correctly separated into source paragraphs throughout scans **17–23**.
- The page-14 printed note remains separate from the narrative conclusion rather than being merged into the final story paragraph.
- No accidental prose paragraph merge or split was found.
- Exact physical line wrapping caused only by page width is intentionally not reproduced.

## Display / emphasis fidelity

### Scan 20 / printed page 11

The paragraph beginning **`சோலையின் பக்கமிருந்து...`** has an enlarged initial **`ச`** in the source. It clearly marks a structural paragraph opening. The effect is now recorded semantically in the page record and assembly without attempting to reproduce the original font size.

No verse, song stanza, illustration caption, or other internal display block requiring special lineation occurs in this story.

## Non-text marks

Source-significant non-text structure recorded during this activity:

1. scan 16 — long horizontal rule beneath `நளாயினி`;
2. scan 23 — long separator between narrative and `குறிப்பு :—`;
3. scan 23 — centered closing ornament below the printed note.

No story illustration or caption occurs on scans 16–23.

## Page furniture

- Printed page numbers **7–14** remain excluded from story body.
- Alternating running furniture — the anthology header `கலைஞர் கருணாநிதியின் சிறுகதைகள்` and the running story title `நளாயினி` — remains excluded from canonical reading text.
- No page-furniture leakage into the Tamil assembly was found.

## Physical joins

All seven internal joins and the next-story boundary were visually checked.

1. scans **16→17**: `கால்` → `பாகத்துக்குமேல் இழந்துவிட்ட மனிதன்...` — continuous.
2. scans **17→18**: ordinary story continuation — no omission or duplication.
3. scans **18→19**: `தனக்குத்` → `தானே ஆச்சரியப்பட்டுக் கொண்டாள்.` — continuous.
4. scans **19→20**: unfinished உலகா quotation continues with `க்ஷமித்துவிடு நளாயினி!...` — continuous.
5. scans **20→21**: split `காணப்படு` → `கிறார்கள்.` — continuous.
6. scans **21→22**: ordinary dialogue continuation — no omission or duplication.
7. scans **22→23**: `“இதயா! இது உண்மையா?”` → `“பொய் இல்லை!...”` — continuous.
8. scan **23→24**: Story 2 ends on scan 23; scan 24 opens `சபலம்`.

## Corrections made

Visual-fidelity review produced **structural-only corrections**:

1. `pages/0016-nalayini-01.md`: recorded the source opening underline rule.
2. `pages/0020-nalayini-05.md`: recorded the enlarged initial `ச` at the `சோலையின்...` paragraph opening.
3. `pages/0023-nalayini-08.md`: `page_type` changed `story-conclusion-and-note` → `story-ending`.
4. `pages/0023-nalayini-08.md`: removed non-source display headings `அச்சு உரை` and `அச்சு குறிப்பு`.
5. `pages/0023-nalayini-08.md`: recorded the narrative/note separator and closing ornament.
6. `sections/nalayini.md`: synchronized all source-significant visual structure above.
7. `indexes/page-map.md`: synchronized opening, enlarged-initial, ending-note and ornament roles.

**No story wording was changed during this visual-fidelity activity.** Existing source-form distinctions, verified readings and the human possible-error queue remain intact.

## Remaining visual-fidelity issues

**None.**

## Result

**PASS — corrected**

`நளாயினி` is visually source-faithful at the semantic archival level defined by `VISUAL_FIDELITY_CHECK_GUIDE.md`, after the structural corrections listed above.
