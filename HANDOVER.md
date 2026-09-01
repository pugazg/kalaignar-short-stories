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

- complete: **21 / 37**
- pending: **16 / 37**
- needs recheck: **0**
- current target: **Story 22 — `தொத்துக்கிளி`**

Stories **1–21** are closed with `PASS — corrected` and story-local `visual-fidelity.md` records.

## Latest completed batch — Stories 18–21

The user explicitly requested Stories 18–21 together for this activity.

### Story 18 — `செத்தவள் கதை`
- workspace: `stories/seththaval-kathai/`
- scans **131–139 / printed 122–130**
- boundary witness: scan **140**, opening `பிரேத விசாரணை`
- opening rule and fire-verse display lineation on scans 131, 136 and 139 synchronized
- final source-emphasized `‘செத்தவள் கதை’`, `story-ending` role and closing ornament synchronized
- story wording changed: **No**

### Story 19 — `பிரேத விசாரணை`
- workspace: `stories/pretha-visaranai/`
- scans **140–145 / printed 131–136**
- boundary witness: scan **146**, opening `கண்டதும் காதல் ஒழிக!`
- opening rule/enlarged `ட`, final `story-ending` role and closing ornament synchronized
- story wording changed: **No**

### Story 20 — `கண்டதும் காதல் ஒழிக!`
- workspace: `stories/kandathum-kadhal-ozhiga/`
- scans **146–150 / printed 137–141**
- boundary witness: scan **151**, opening `ஆலமரத்துப் புறாக்கள்`
- source-bold `“அன்பே! சீதா! அருகில் வா!”` and `“ராமாயணம்”` represented in page records
- opening/closing rules synchronized; small brown lower-margin mark on scan 150 classified as non-story material
- story wording changed: **No — emphasis/structure only**

### Story 21 — `ஆலமரத்துப் புறாக்கள்`
- workspace: `stories/aalamarathup-puraakkal/`
- scans **151–155 / printed 142–146**
- boundary witness: scan **156**, opening `தொத்துக்கிளி`
- opening rule/enlarged `அ`; existing source-bold `“இது வல்லூறின் மரம்”` and `வல்லூறை விரட்டுவதுதான்!` confirmed; ending role and ornament synchronized
- story wording changed: **No**

## NEXT EXACT ACTIVITY — STORY 22 ONLY

Story 22 — **`தொத்துக்கிளி`**:

- canonical workspace: `stories/thothukkili/`
- printed pages: **147–151**
- anthology scans: **156–160**
- boundary witness: scan **161**, opening Story 23 **`காதல் கடிதம்`**

When the user says “Proceed with next activity”:
1. fetch live `main` first;
2. inspect scans **156–160** directly from the controlling PDF;
3. compare all five pages with page records and the Tamil assembly;
4. check opening/ending roles, paragraph/dialogue structure, display/emphasis, non-text marks, page furniture and every physical join;
5. inspect scan **161** only as the boundary witness;
6. apply only source-supported corrections/annotations and propagate any actual wording correction through all affected layers;
7. create/update `stories/thothukkili/visual-fidelity.md` and controls;
8. re-fetch live `main` and changed controls before declaring closure;
9. do **not** begin Story 23 unless the user explicitly expands the batch.

Expected after Story 22: **22 / 37 complete, 15 pending**.

## Phase guard

Do not begin English translation, modernization, republication or another downstream phase unless separately authorized.
