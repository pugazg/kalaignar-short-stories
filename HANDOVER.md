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

- complete: **29 / 37**
- pending: **8 / 37**
- needs recheck: **0**
- current target: **Story 30 — `கடைசிக் கட்டம்`**

Stories **1–29** are closed with `PASS — corrected` and story-local `visual-fidelity.md` records.

## Latest completed batch — Stories 28–29

The user explicitly requested these two stories together.

### Story 28 — TOC `புரட்சிப்படம்` / opening `புரட்சிப் படம்`
- workspace: `stories/puratchip-padam/`
- scans **194–198 / printed 185–189**
- boundary witness: scan **199**, opening `திடுக்கிடும் கதை`
- TOC/opening title variance preserved exactly
- scan 194 opening rule and enlarged/heavier `டை` recorded
- scan 196 bold publicity slogans and scan 197 source-bold display text confirmed as already represented
- scan 198 synchronized to `story-ending` and closing ornament recorded
- story wording changed: **No — structure/visual annotation only**

### Story 29 — `திடுக்கிடும் கதை`
- workspace: `stories/thidukkidum-kathai/`
- scans **199–204 / printed 190–195**
- boundary witness: scan **205**, opening `கடைசிக் கட்டம்`
- scan 199 opening rule, enlarged/heavier `நி`, and standalone source-note display treatment recorded
- centered subsection headings `காதல் கதை` and `வீரக்கதை` confirmed
- scan 202 printer signature `க—13` excluded as page furniture
- scan 204 synchronized to `story-ending` and closing ornament recorded
- all internal joins and boundary witness directly checked
- story wording changed: **No — structure/visual annotation only**

## NEXT EXACT ACTIVITY — STORY 30 ONLY

Story 30 — **`கடைசிக் கட்டம்`**:

- canonical workspace: `stories/kadaisi-kattam/`
- printed pages: **196–201**
- anthology scans: **205–210**
- boundary witness: scan **211**, opening Story 31 **`அய்யோ ராஜா!`**

When the user says “Proceed with next activity”:
1. fetch live `main` first;
2. inspect scans **205–210** directly from the controlling PDF;
3. compare all six pages with page records and Tamil assembly;
4. check opening/ending roles, paragraph/dialogue structure, display/emphasis, non-text marks, page furniture and every physical join;
5. inspect scan **211** only as the boundary witness;
6. apply only source-supported corrections/annotations and propagate any actual wording correction through all affected layers;
7. create/update `stories/kadaisi-kattam/visual-fidelity.md` and controls;
8. re-fetch live `main` and changed controls before declaring closure;
9. do **not** begin Story 31 unless the user explicitly expands the batch.

Expected after Story 30: **30 / 37 complete, 7 pending**.

## Phase guard

Do not begin English translation, modernization, republication or another downstream phase unless separately authorized.
