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
- complete: **4 / 37**
- pending: **33 / 37**
- needs recheck: **0**
- current target: **Story 5 — `குப்பைத்தொட்டி`**

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

Canonical workspace: `stories/aattakkavadi/`

- printed pages: **22–29**
- scans: **31–38**
- boundary witness: scan **39**, opening `குப்பைத்தொட்டி`
- result: **PASS — corrected**
- story-local record: `stories/aattakkavadi/visual-fidelity.md`

Direct visual review covered all eight source pages plus scan 39. Paragraph/dialogue separation, source-significant emphasis, page furniture, letter layout and every physical join were checked.

Structural-only corrections made:

1. scan 31 / assembly: recorded the long horizontal rule beneath `ஆட்டக்காவடி`;
2. scan 31 / assembly: recorded the enlarged opening `ஆ`;
3. scan 31 / assembly: preserved the source-bold phrase `காவடி ஆட்டக் கச்சேரி` without changing wording;
4. scan 34 / assembly: recorded the enlarged `க` marking the flashback paragraph `கனிமொழி நெசவாளர்...`;
5. scan 37 / assembly: recorded the enlarged `ம` marking the `மறுநாள்...` paragraph;
6. scan 38: `story-conclusion` → `story-ending`;
7. scan 38: removed the non-source display heading `அச்சு உரை`;
8. scan 38 / assembly: recorded the standalone letter alternatives, the visually separated `இப்படிக்கு / கனிமொழி / பகுத்தறிவுப் பெண்.` sign-off, and the centered closing ornament;
9. page map synchronized with these source-significant roles.

**No story wording changed during Story 4 visual-fidelity review.** Markdown emphasis was added only to represent source-visible bolding. The existing human possible-error queue remains unchanged.

## NEXT EXACT ACTIVITY — STORY 5 VISUAL FIDELITY ONLY

Story 5 — **`குப்பைத்தொட்டி`**:

- canonical workspace: `stories/kuppai-thotti/`
- printed pages: **30–37**
- anthology scans: **39–46**
- boundary witness: scan **47**, opening Story 6 **`சந்தனக்கிண்ணம்`**

When the user says **“Proceed with next activity”**:

1. fetch live `main` first and preserve newer work;
2. inspect scans **39–46** directly from the controlling PDF;
3. compare all eight pages against `stories/kuppai-thotti/pages/` and its Tamil assembly under `VISUAL_FIDELITY_CHECK_GUIDE.md`;
4. inspect scan **47** only as the next-story boundary witness;
5. check opening/ending roles, paragraph/dialogue structure, display/verse/emphasis, non-text marks, page furniture and every physical join;
6. apply only source-supported structural corrections; if wording itself is wrong, verify the complete source span before correction and propagate all affected layers;
7. create `stories/kuppai-thotti/visual-fidelity.md`;
8. update `VISUAL_FIDELITY_PROGRESS.md`, `HANDOVER.md` and `NEXT_CHAT_PROMPT.md`;
9. re-fetch live `main` and changed controls before declaring Story 5 visually complete;
10. **do not begin Story 6 in the same activity**.

Expected result after Story 5 closure: **5 / 37 visual-fidelity complete, 32 pending**.

## Downstream phase guard

Do **not** begin English translation, modernization, republication or another downstream phase unless separately authorized after visual-fidelity work or mandated by newer live repository state.

## Current closure state

- Tamil source pass: **37 / 37 COMPLETE**
- visual fidelity: **4 / 37 COMPLETE**
- next exact activity: **Story 5 `குப்பைத்தொட்டி` visual fidelity**
