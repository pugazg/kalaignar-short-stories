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
- Running headers and printed page numbers are normally page furniture, not story body.
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
3. inspect the active story's existing page records, Tamil assembly, audit and page map;
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

Edition-level source-title variances already preserved include:

- TOC `புரட்சிப்படம்` ↔ opening `புரட்சிப் படம்`
- TOC `சித்தார்த்தன்` ↔ opening `சித்தார்த்தன் சிலை`

## USER-AUTHORIZED CURRENT PHASE — VISUAL FIDELITY CHECK

The user explicitly authorized **visual fidelity check** after Tamil source transcription.

This phase is governed by `VISUAL_FIDELITY_CHECK_GUIDE.md` and checks source-significant visual structure rather than facsimile typography.

## Visual-fidelity progress

- total stories: **37**
- visual fidelity complete: **1 / 37**
- pending: **36 / 37**
- needs recheck: **0**
- current target: **Story 2 — `நளாயினி`**

### Story 1 — `புகழேந்தி` — VISUAL FIDELITY CLOSED

Canonical workspace: `stories/pugazhendhi/`

- printed pages: **1–6**
- scans: **10–15**
- boundary witness: scan **16**, opening `நளாயினி`
- result: **PASS — corrected**
- story-local record: `stories/pugazhendhi/visual-fidelity.md`

Direct visual review covered all six pages plus the boundary witness. Paragraph/dialogue structure, the isolated scan-11 `புகழ்! புகழ்!! புகழ்!!!` display line, page furniture, physical joins and story boundary were checked.

Structural-only corrections made:

1. scan 10 page record: `story-body` → `story-opening`;
2. scan 10 page record: removed non-source Markdown heading `அச்சு உரை`;
3. scan 10 / assembly: recorded the source opening ornamented rule above `புகழேந்தி`;
4. scan 15 page record: `story-body` → `story-ending`;
5. scan 15 / assembly: recorded the source closing ornamented rule;
6. Tamil assembly synchronized with the source-significant visual structure.

**No story wording changed during Story 1 visual-fidelity review.**

## NEXT EXACT ACTIVITY — STORY 2 VISUAL FIDELITY ONLY

Story 2 — **`நளாயினி`**:

- canonical workspace: `stories/nalayini/`
- printed pages: **7–14**
- anthology scans: **16–23**
- boundary witness: scan **24**, opening Story 3 **`சபலம்`**

When the user says **“Proceed with next activity”**:

1. fetch live `main` first and preserve newer work;
2. inspect scans **16–23** directly from the controlling PDF;
3. compare all eight pages against `stories/nalayini/pages/` and its Tamil assembly under `VISUAL_FIDELITY_CHECK_GUIDE.md`;
4. inspect scan **24** only as the next-story boundary witness;
5. check opening/ending roles, paragraph/dialogue structure, display/verse/emphasis, non-text marks, page furniture and every physical join;
6. apply only source-supported visual-structure corrections, and textual corrections only if the controlling scan directly proves them;
7. create `stories/nalayini/visual-fidelity.md`;
8. update `VISUAL_FIDELITY_PROGRESS.md`, `HANDOVER.md` and `NEXT_CHAT_PROMPT.md`;
9. re-fetch live `main` and changed controls before declaring Story 2 visually complete;
10. **do not begin Story 3 in the same activity**.

Expected result after Story 2 closure: **2 / 37 visual-fidelity complete, 35 pending**.

## Downstream phase guard

Visual fidelity is the authorized current phase. Do **not** begin English translation, modernization, republication or another downstream phase unless separately authorized after visual-fidelity work or mandated by newer live repository state.

## Current closure state

- Tamil source pass: **37 / 37 COMPLETE**
- visual fidelity: **1 / 37 COMPLETE**
- next exact activity: **Story 2 `நளாயினி` visual fidelity**
