# HANDOVER — Kalaignar Short Stories Archive

## Repository

- Repository: `pugazg/kalaignar-short-stories`
- Branch: `main`
- Story workflow: `SHORT_STORY_PROCESSING_GUIDE.md`
- Anthology workflow: `COLLECTION_SOURCE_GUIDE.md`
- Visual-fidelity workflow: `VISUAL_FIDELITY_CHECK_GUIDE.md`
- Visual-fidelity tracker: `VISUAL_FIDELITY_PROGRESS.md`
- Source PDFs / renders / crops are **not** committed.

## Authoritative-state rule

Always fetch live `main` first and preserve newer durable work.

## Permanent source rules

- Controlling scan first; do not silently modernize spelling, punctuation, grammar, sandhi, names or source anomalies.
- Old Tamil glyphs require complete-span visual interpretation.
- Running headers, printed page numbers and printer signatures are page furniture, not story body.
- `POSSIBLE_ERRORS_FOR_REVIEW.md` is a human-review queue, not proof of error.
- Source-supported textual corrections must propagate through every affected page, assembly, audit/review and control layer.
- Do not commit the controlling PDF or generated visual-inspection artefacts.

## Mandatory startup

Before source-dependent visual work, fetch live `main`, then read completely:

1. `SHORT_STORY_PROCESSING_GUIDE.md`
2. `COLLECTION_SOURCE_GUIDE.md`
3. `VISUAL_FIDELITY_CHECK_GUIDE.md`
4. `VISUAL_FIDELITY_PROGRESS.md`
5. `HANDOVER.md`
6. `NEXT_CHAT_PROMPT.md`
7. collection `README.md`
8. collection `indexes/story-inventory.md`
9. collection `indexes/scan-map.md`

Then inspect the active story page records, Tamil assembly, audit and page map and resolve the controlling PDF.

## Durable Tamil milestone

The 1977 anthology Tamil source pass is complete: **37 / 37 stories**, scans **10–259 / printed pages 1–250**, with **0 blocked / 0 unresolved story text**.

## Visual-fidelity phase state

- complete: **32 / 37**
- pending: **5 / 37**
- needs recheck: **0**
- current target: **Story 33 — `வேணியின் காதலன்`**

Stories **1–32** are closed with `PASS — corrected` and story-local `visual-fidelity.md` records.

## Latest completed batch — Stories 30–32

The user explicitly requested these three stories together.

### Story 30 — `கடைசிக் கட்டம்`
- workspace: `stories/kadaisi-kattam/`
- scans **205–210 / printed 196–201**
- boundary witness: scan **211**, opening `அய்யோ ராஜா!`
- scan 205 opening rule recorded; existing source-bold `டாக்டர் பாபு` retained
- scan 206 existing source-bold `மஞ்சுளாவை` retained
- scan 209 two-line கோகிலா letter sign-off display treatment recorded
- scan 210 synchronized to `story-ending` and closing ornament recorded
- story wording changed: **No — structure/visual annotation only**

### Story 31 — `அய்யோ ராஜா!`
- workspace: `stories/ayyo-raja/`
- scans **211–217 / printed 202–208**
- boundary witness: scan **218**, opening `விஷம் இனிது`
- scan 211 opening rule and enlarged/heavier `செ` in `சென்னை` recorded
- prior old-Tamil-glyph correction `என்றாள் முத்தம்மா` retained exactly
- scan 217 already correctly `story-ending`; closing ornament retained
- story wording changed: **No — structure/visual annotation only**

### Story 32 — `விஷம் இனிது`
- workspace: `stories/visham-inidhu/`
- scans **218–224 / printed 209–215**
- boundary witness: scan **225**, opening `வேணியின் காதலன்`
- scan 218 opening rule and enlarged/heavier `ஜெ` recorded; printer signature `க—14` excluded as page furniture
- scan 221 two-line அமிர்தராணி letter sign-off treatment recorded; existing source-bold `அமிர்த ராணி` retained
- scan 224 existing source-bold `ஆண்டவனை விட ஆலஹாலம் இனிது`, `story-ending`, and closing ornament retained
- story wording changed: **No — structure/visual annotation only**

## NEXT EXACT ACTIVITY — STORY 33 ONLY

Story 33 — **`வேணியின் காதலன்`**:

- canonical workspace: `stories/veniyin-kadhalan/`
- printed pages: **216–221**
- anthology scans: **225–230**
- boundary witness: scan **231**, opening Story 34 **`அமிர்தமதி`**

When the user says “Proceed with next activity”:
1. fetch live `main` first;
2. inspect scans **225–230** directly from the controlling PDF;
3. compare all six pages with page records and Tamil assembly;
4. check opening/ending roles, paragraph/dialogue structure, display/emphasis, non-text marks, page furniture and every physical join;
5. inspect scan **231** only as the boundary witness;
6. apply only source-supported corrections/annotations and propagate any actual wording correction through all affected layers;
7. create/update `stories/veniyin-kadhalan/visual-fidelity.md` and controls;
8. re-fetch live `main` and changed controls before declaring closure;
9. do **not** begin Story 34 unless the user explicitly expands the batch.

Expected after Story 33: **33 / 37 complete, 4 pending**.

## Phase guard

Do not begin English translation, modernization, republication or another downstream phase unless separately authorized.
