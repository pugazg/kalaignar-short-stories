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

- complete: **26 / 37**
- pending: **11 / 37**
- needs recheck: **0**
- current target: **Story 27 — `பாலைவன ரோஜா`**

Stories **1–26** are closed with `PASS — corrected` and story-local `visual-fidelity.md` records.

## Recently completed — Stories 22–26

### Story 22 — `தொத்துக்கிளி`
- workspace: `stories/thothukkili/`
- scans **156–160 / printed 147–151**
- boundary witness: scan **161**, opening `காதல் கடிதம்`
- opening rule/enlarged initial and final `story-ending`/ornament synchronized
- story wording changed: **No**

### Story 23 — `காதல் கடிதம்`
- workspace: `stories/kadhal-kaditham/`
- scans **161–165 / printed 152–156**
- boundary witness: scan **166**, opening `கண்ணடக்கம்`
- opening structure, two-line letter sign-off/source-emphasized `சுந்தர் பாபு”`, final `story-ending`/ornament synchronized
- story wording changed: **No**

### Story 24 — `கண்ணடக்கம்`
- workspace: `stories/kannadakkam/`
- scans **166–172 / printed 157–163**
- boundary witness: scan **173**, opening `வாழ முடியாதவர்கள்`
- opening rule/enlarged initial, source emphasis on `‘கண்ணடக்கம்’`, printer signature `க—11` exclusion and final ending/ornament synchronized
- story wording changed: **No**

### Story 25 — `வாழ முடியாதவர்கள்`
- workspace: `stories/vazha-mudiyathavargal/`
- scans **173–180 / printed 164–171**
- boundary witness: scan **181**, opening `அபாக்ய சிந்தாமணி`
- opening rule, source emphasis on `“ஆண்டவன் படைப்பு”`, final ending/ornament synchronized
- existing source-bold sentence on scan 177 retained
- story wording changed: **No**

### Story 26 — `அபாக்ய சிந்தாமணி`
- workspace: `stories/abagya-chinthamani/`
- scans **181–188 / printed 172–179**
- boundary witness: scan **189**, opening `பாலைவன ரோஜா`
- scan 181 opening rule/enlarged `அ` and source-bold quoted characterization represented
- scan 182 two song/verse blocks kept as display lineation; source emphasis on `எங்கள் ஒளவைப் பாட்டிதான்` represented
- scan 185 source emphasis `நாயைக் குளிப்பாட்டி நடுவுள்ளே வைத்தால்...` represented
- scan 186 printer signature `க—12` excluded as page furniture
- scan 188 `story-ending` and closing ornament synchronized
- story wording changed: **No — structure/emphasis only**

## NEXT EXACT ACTIVITY — STORY 27 ONLY

Story 27 — **`பாலைவன ரோஜா`**:

- canonical workspace: `stories/palaivana-roja/`
- printed pages: **180–184**
- anthology scans: **189–193**
- boundary witness: scan **194**, opening Story 28 — TOC `புரட்சிப்படம்`, opening heading `புரட்சிப் படம்`

When the user says “Proceed with next activity”:
1. fetch live `main` first;
2. inspect scans **189–193** directly from the controlling PDF;
3. compare all five pages with page records and Tamil assembly;
4. check opening/ending roles, paragraph/dialogue structure, display/emphasis, non-text marks, page furniture and every physical join;
5. inspect scan **194** only as the boundary witness;
6. apply only source-supported corrections/annotations and propagate any actual wording correction through all affected layers;
7. create/update `stories/palaivana-roja/visual-fidelity.md` and controls;
8. re-fetch live `main` and changed controls before declaring closure;
9. do **not** begin Story 28 unless the user explicitly expands the batch.

Expected after Story 27: **27 / 37 complete, 10 pending**.

## Phase guard

Do not begin English translation, modernization, republication or another downstream phase unless separately authorized.
