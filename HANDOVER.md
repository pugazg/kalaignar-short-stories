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
- Difficult readings require full-span visual escalation before terminal `blocked` status.
- `POSSIBLE_ERRORS_FOR_REVIEW.md` is a human-review queue, not a list of confirmed errors.
- Running headers, printed page numbers and printer signatures are page furniture, not story body.
- A source-supported textual correction must be propagated through all affected page, assembly, audit and control layers.
- Do not commit the source PDF or generated page renders/crops.

## Mandatory startup before visual-fidelity source work

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
- scan **260**: verified back cover
- registered stories: **37 / 37**

## Completed Tamil source-text milestone

**1977 ANTHOLOGY TAMIL SOURCE PASS COMPLETE AND FULLY SYNCHRONIZED.**

- Tamil source processing: **37 / 37 complete**
- remaining source transcription: **0 / 37**
- story-text coverage: scans **10–259 / printed pages 1–250**
- all 37 story workspaces have complete Tamil assemblies and source audits
- all 37 have **0 blocked / 0 unresolved story text**
- English translation from this anthology: **0 / 37 started**

Edition-level title variances remain preserved:
- TOC `புரட்சிப்படம்` ↔ opening `புரட்சிப் படம்`
- TOC `சித்தார்த்தன்` ↔ opening `சித்தார்த்தன் சிலை`

## USER-AUTHORIZED CURRENT PHASE — VISUAL FIDELITY CHECK

The user explicitly authorized **visual fidelity check** after Tamil source transcription. This phase preserves source-significant structure without facsimile typography.

### Current visual-fidelity progress

- total stories: **37**
- complete: **8 / 37**
- pending: **29 / 37**
- needs recheck: **0**
- current target: **Story 9 — `தாய்மை`**

Stories 1–8 are closed with `PASS — corrected` and story-local `visual-fidelity.md` records.

## Story 8 — `கங்கையின் காதல்` — VISUAL FIDELITY CLOSED

Canonical workspace: `stories/gangaiyin-kadhal/`

- printed pages: **60–63**
- scans: **69–72**
- boundary witness: scan **73**, opening `தாய்மை`
- pages directly inspected: **4 / 4**, plus boundary witness
- result: **PASS — corrected**
- story-local record: `stories/gangaiyin-kadhal/visual-fidelity.md`

Direct visual review checked opening/ending roles, paragraph/dialogue structure, page furniture and all three internal joins.

Structural-only corrections/annotations:
1. scan 69 / assembly: recorded the long horizontal rule beneath `கங்கையின் காதல்`;
2. scan 69 / assembly: recorded the enlarged opening `கை` in `கைலாயத்தில்`;
3. scan 69: confirmed `ஆழ்ந்த உறக்கம்—அமைதி—...` remains a separate source paragraph;
4. scan 72: `story-conclusion` → `story-ending`;
5. scan 72 / assembly: recorded the centered floral closing ornament;
6. page map synchronized with the opening/ending roles and physical joins;
7. scan 69→70 preserves `எதிர்பார்த்திருந்` → `தாள்.`;
8. scan 71→72 preserves `...என்பொருட்டுச் சொல்` → `....என் போன்ற பெண்கள்...`;
9. scan 73 independently opens Story 9 `தாய்மை` beneath its own heading and horizontal rule.

**No story wording changed during Story 8 visual-fidelity review.** Existing verified source readings and the persistent human possible-error queue remain intact.

## NEXT EXACT ACTIVITY — STORY 9 VISUAL FIDELITY ONLY

Story 9 — **`தாய்மை`**:

- canonical workspace: `stories/thaaymai/`
- printed pages: **64–74**
- anthology scans: **73–83**
- boundary witness: scan **84**, opening Story 10 **`தப்பிவிட்டார்கள்`**

When the user says **“Proceed with next activity”**:

1. fetch live `main` first and preserve newer work;
2. inspect scans **73–83** directly from the controlling PDF;
3. compare all eleven pages against `stories/thaaymai/pages/` and its Tamil assembly under `VISUAL_FIDELITY_CHECK_GUIDE.md`;
4. inspect scan **84** only as the next-story boundary witness;
5. check opening/ending roles, paragraph/dialogue structure, verse/display/emphasis, non-text marks, page furniture and every physical join;
6. apply only source-supported structural corrections; if wording itself is wrong, verify the complete source span before correction and propagate all affected layers;
7. create `stories/thaaymai/visual-fidelity.md`;
8. update `VISUAL_FIDELITY_PROGRESS.md`, `HANDOVER.md` and `NEXT_CHAT_PROMPT.md`;
9. re-fetch live `main` and changed controls before declaring Story 9 visually complete;
10. **do not begin Story 10 in the same activity**.

Expected result after Story 9 closure: **9 / 37 visual-fidelity complete, 28 pending**.

## Downstream phase guard

Do **not** begin English translation, modernization, republication or another downstream phase unless separately authorized after visual-fidelity work or mandated by newer live repository state.

## Current closure state

- Tamil source pass: **37 / 37 COMPLETE**
- visual fidelity: **8 / 37 COMPLETE**
- next exact activity: **Story 9 `தாய்மை` visual fidelity**
