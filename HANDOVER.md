# HANDOVER — Kalaignar Short Stories Archive

## Repository

- Repository: `pugazg/kalaignar-short-stories`
- Branch: `main`
- Story workflow: `SHORT_STORY_PROCESSING_GUIDE.md`
- Anthology workflow: `COLLECTION_SOURCE_GUIDE.md`
- Visual-fidelity workflow: `VISUAL_FIDELITY_CHECK_GUIDE.md`
- Visual-fidelity tracker: `VISUAL_FIDELITY_PROGRESS.md`
- Cross-chat resume prompt: `NEXT_CHAT_PROMPT.md`
- Source PDFs / generated renders / crops are **not** committed to GitHub.

## Authoritative-state rule

Always fetch live GitHub `main` first. Live `main` is authoritative over chat summaries, prompts and remembered checkpoints. Preserve any newer durable state.

## Permanent source rules

- **Controlling scan first.** Do not silently modernize spelling, grammar, punctuation, names, sandhi or source anomalies.
- Old Tamil glyph shapes must be interpreted from the source typeface and full span, not modern-font expectation.
- Difficult story readings require full-span visual escalation before terminal `blocked` status.
- `POSSIBLE_ERRORS_FOR_REVIEW.md` is a human-review queue, not a list of confirmed errors.
- A source-supported textual correction must be propagated through all affected page, assembly, audit and control layers.
- Running headers, printed page numbers and printer signatures are page furniture, not story body.
- Do not commit the source PDF or generated page renders/crops.

## Mandatory startup

Before visual-fidelity source work:

1. fetch live `main` and preserve newer work;
2. read completely:
   - `SHORT_STORY_PROCESSING_GUIDE.md`
   - `COLLECTION_SOURCE_GUIDE.md`
   - `VISUAL_FIDELITY_CHECK_GUIDE.md`
   - `VISUAL_FIDELITY_PROGRESS.md`
   - `HANDOVER.md`
   - `NEXT_CHAT_PROMPT.md`
   - collection `README.md`
   - collection `indexes/story-inventory.md`
   - collection `indexes/scan-map.md`;
3. inspect the active story's page records, Tamil assembly, audit and page map;
4. use the controlling PDF for all source-dependent decisions.

## Active collection source — 1977 anthology

- title: **கலைஞர் கருணாநிதியின் சிறுகதைகள்**
- filename: `TVA_BOK_0064142_கலைஞர்_கருணாநிதியின்_சிறுகதைகள்.pdf`
- SHA-256: `853032661482eaccb26c083a38d7aa75c081362d33c963c63e37d088bf20acb3`
- file size: **268,486,609 bytes**
- PDF scans: **260**
- edition: **முதல் பதிப்பு: 1977**
- printed story pagination: **1–250**
- story block scans: **10–259**
- scan **260**: back cover
- registered stories: **37 / 37**

## Completed Tamil source-text milestone

**1977 ANTHOLOGY TAMIL SOURCE PASS COMPLETE AND FULLY SYNCHRONIZED.**

- Tamil source processing: **37 / 37 complete**
- remaining source transcription: **0 / 37**
- story-text coverage: scans **10–259 / printed pages 1–250**
- final physical boundary: scan **260**, verified back cover
- all 37 anthology story workspaces have complete Tamil assemblies and source audits
- all 37 have **0 blocked / 0 unresolved story text**
- English translation from this anthology: **0 / 37 started**

Edition-level title variances remain preserved:

- TOC `புரட்சிப்படம்` ↔ opening `புரட்சிப் படம்`
- TOC `சித்தார்த்தன்` ↔ opening `சித்தார்த்தன் சிலை`

## USER-AUTHORIZED CURRENT PHASE — VISUAL FIDELITY CHECK

The user explicitly authorized **visual fidelity check** after Tamil source transcription. This phase is governed by `VISUAL_FIDELITY_CHECK_GUIDE.md` and preserves source-significant structure without facsimile typography.

## Visual-fidelity progress

- total stories: **37**
- complete: **7 / 37**
- pending: **30 / 37**
- needs recheck: **0**
- current target: **Story 8 — `கங்கையின் காதல்`**

### Story 1 — `புகழேந்தி` — VISUAL FIDELITY CLOSED

- scans **10–15 / printed pages 1–6**
- result: **PASS — corrected**
- record: `stories/pugazhendhi/visual-fidelity.md`
- corrections were structural only; story wording changed: **No**

### Story 2 — `நளாயினி` — VISUAL FIDELITY CLOSED

- scans **16–23 / printed pages 7–14**
- result: **PASS — corrected**
- record: `stories/nalayini/visual-fidelity.md`
- corrections were structural only; story wording changed: **No**

### Story 3 — `சபலம்` — VISUAL FIDELITY CLOSED

- scans **24–30 / printed pages 15–21**
- result: **PASS — corrected**
- record: `stories/sabalam/visual-fidelity.md`
- corrections were structural only; story wording changed: **No**

### Story 4 — `ஆட்டக்காவடி` — VISUAL FIDELITY CLOSED

- scans **31–38 / printed pages 22–29**
- result: **PASS — corrected**
- record: `stories/aattakkavadi/visual-fidelity.md`
- corrections were structural only; story wording changed: **No**

### Story 5 — `குப்பைத்தொட்டி` — VISUAL FIDELITY CLOSED

Canonical workspace: `stories/kuppai-thotti/`

- printed pages: **30–37**
- scans: **39–46**
- boundary witness: scan **47**, opening `சந்தனக்கிண்ணம்`
- result: **PASS — corrected**
- story-local record: `stories/kuppai-thotti/visual-fidelity.md`

Direct visual review covered all eight source pages plus scan 47. Paragraph structure, the scan-42 verse display, scan-45 isolated quoted lines, page furniture and every physical join were checked.

Structural-only corrections made:

1. scan 39 / assembly: recorded the long horizontal rule beneath `குப்பைத்தொட்டி`;
2. scan 39 / assembly: recorded the enlarged opening `வீ` in `வீதியோரத்தில்`;
3. scan 42: confirmed the four-line quoted verse is already source-lineated in page record and assembly;
4. scan 42 printer signature `க—3` remains excluded as page furniture;
5. scan 45: confirmed `‘கண்ணு!’ / ‘என் மூக்கு!’ / ‘அய்யோ என் மன்மதராஜா!’` remain isolated as in the source;
6. scan 46: `story-conclusion` → `story-ending`;
7. scan 46 / assembly: recorded the centered closing ornament;
8. page map synchronized with the opening, display, page-furniture and ending roles.

**No story wording changed during Story 5 visual-fidelity review.** The existing human possible-error queue remains unchanged.

### Story 6 — `சந்தனக்கிண்ணம்` — VISUAL FIDELITY CLOSED

Canonical workspace: `stories/santhana-kinnam/`

- printed pages: **38–47**
- scans: **47–56**
- boundary witness: scan **57**, opening `சங்கிலிச்சாமி`
- result: **PASS — corrected**
- story-local record: `stories/santhana-kinnam/visual-fidelity.md`

Direct visual review covered all ten source pages plus scan 57. Paragraph/dialogue boundaries, the long poem across scans 48–50, Vijayā's scan-51 gift display, source emphasis, page furniture and every physical join were checked.

Structural-only corrections made:

1. scan 47 / assembly: recorded the story-opening rule and enlarged opening `த`;
2. scan 48 / assembly: recorded enlarged `கு` beginning the long poem;
3. scan 50 / assembly: preserved source emphasis on `மார்பு காட்டி!` with Markdown bold;
4. scan 51 / assembly: recorded the seven-line gift inscription as a display block and enlarged `கு` at `குடும்பம்...`;
5. scan 52 / assembly: recorded enlarged `தி` at `திடீரென்று...`;
6. scan 53 / assembly: recorded enlarged `க` at `கமலா பலகணி...`;
7. scan 54 / assembly: recorded enlarged `க` at the post-struggle return-home paragraph;
8. scan 55 / assembly: recorded enlarged `கூ` at `கூட்டம் குறிப்பிட்டபடி...`;
9. scan 56: `story-conclusion` → `story-ending`;
10. scan 56 / assembly: recorded enlarged `இ`, isolated `ஆனால்,`, and the centered closing ornament;
11. page map synchronized with these source-significant structures.

**No story wording changed during Story 6 visual-fidelity review.** The existing human possible-error queue remains unchanged.

A prior control-path typo `stories/sandhana-kinnam/` was corrected during Story 6 closure; the canonical repository workspace is **`stories/santhana-kinnam/`**.

### Story 7 — `சங்கிலிச்சாமி` — VISUAL FIDELITY CLOSED

Canonical workspace: `stories/sangilichami/`

- printed pages: **48–59**
- scans: **57–68**
- boundary witness: scan **69**, opening `கங்கையின் காதல்`
- result: **PASS — corrected**
- story-local record: `stories/sangilichami/visual-fidelity.md`

Direct visual review covered all twelve source pages plus scan 69. Paragraph/dialogue boundaries, opening chant display, scan-58 petitions, scan-67 false-letter display/sign-off, page furniture and every physical join were checked.

Structural-only corrections/annotations made:

1. scan 57 / assembly: recorded the long horizontal rule beneath `சங்கிலிச்சாமி` and the two isolated opening chants;
2. scan 58: four devotee petitions remain isolated as printed; printer signature `க—4` remains excluded as page furniture;
3. scan 67 / assembly: explicitly recorded the false-letter display/sign-off and source-bold `சங்கிலிச்சாமி` signature;
4. scan 68: `story-conclusion` → `story-ending`;
5. scan 68 / assembly: recorded the centered floral closing ornament;
6. page map synchronized with source-significant structure and the physical-join check;
7. all 11 internal joins checked; scan **67→68** preserves the lexical sentence split `...அன்றைக்கே` → `ஆயிரம் ரூபாய்!`.

**No story wording changed during Story 7 visual-fidelity review.** The existing human possible-error queue remains unchanged.

## NEXT EXACT ACTIVITY — STORY 8 VISUAL FIDELITY ONLY

Story 8 — **`கங்கையின் காதல்`**:

- canonical workspace: `stories/gangaiyin-kadhal/`
- printed pages: **60–63**
- anthology scans: **69–72**
- boundary witness: scan **73**, opening Story 9 **`தாய்மை`**

When the user says **“Proceed with next activity”**:

1. fetch live `main` first and preserve newer work;
2. inspect scans **69–72** directly from the controlling PDF;
3. compare all four pages against `stories/gangaiyin-kadhal/pages/` and its Tamil assembly under `VISUAL_FIDELITY_CHECK_GUIDE.md`;
4. inspect scan **73** only as the next-story boundary witness;
5. check opening/ending roles, paragraph/dialogue structure, verse/display/emphasis, non-text marks, page furniture and every physical join;
6. apply only source-supported structural corrections; if wording itself is wrong, verify the complete source span before correction and propagate all affected layers;
7. create `stories/gangaiyin-kadhal/visual-fidelity.md`;
8. update `VISUAL_FIDELITY_PROGRESS.md`, `HANDOVER.md` and `NEXT_CHAT_PROMPT.md`;
9. re-fetch live `main` and changed controls before declaring Story 8 visually complete;
10. **do not begin Story 9 in the same activity**.

Expected result after Story 8 closure: **8 / 37 visual-fidelity complete, 29 pending**.

## Downstream phase guard

Do **not** begin English translation, modernization, republication or another downstream phase unless separately authorized after visual-fidelity work or mandated by newer live repository state.

## Current closure state

- Tamil source pass: **37 / 37 COMPLETE**
- visual fidelity: **7 / 37 COMPLETE**
- next exact activity: **Story 8 `கங்கையின் காதல்` visual fidelity**
