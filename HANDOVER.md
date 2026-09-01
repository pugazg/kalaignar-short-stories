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
- Old Tamil glyph shapes must be interpreted from the source typeface and complete source span, not modern-font expectation.
- Difficult readings require full-span visual escalation before terminal `blocked` status.
- `POSSIBLE_ERRORS_FOR_REVIEW.md` is a human-review queue, not a list of confirmed errors.
- Running headers, printed page numbers and printer signatures are page furniture, not story body.
- A source-supported textual correction must be propagated through all affected page, assembly, audit, review and control layers.
- Do not commit the source PDF or generated page renders/crops.

## Mandatory startup before visual-fidelity source work

Before changing anything, fetch live `main`, then read completely:

1. `SHORT_STORY_PROCESSING_GUIDE.md`
2. `COLLECTION_SOURCE_GUIDE.md`
3. `VISUAL_FIDELITY_CHECK_GUIDE.md`
4. `VISUAL_FIDELITY_PROGRESS.md`
5. `HANDOVER.md`
6. `NEXT_CHAT_PROMPT.md`
7. collection `README.md`
8. collection `indexes/story-inventory.md`
9. collection `indexes/scan-map.md`

Then inspect the active story's page records, Tamil assembly, audit and page map and resolve the controlling PDF before source-dependent decisions.

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

The user explicitly authorized visual-fidelity checking after the Tamil source pass. In the latest activity the user explicitly requested **Stories 10–12 together**, overriding the default one-story-per-activity rule for that activity only.

### Current visual-fidelity progress

- total stories: **37**
- complete: **12 / 37**
- pending: **25 / 37**
- needs recheck: **0**
- current target: **Story 13 — `இரகசியம்!`**

Stories **1–12** are closed with `PASS — corrected` and story-local `visual-fidelity.md` records.

## Latest completed batch — Stories 10–12

### Story 10 — `தப்பிவிட்டார்கள்`

- workspace: `stories/thappivittargal/`
- scans **84–91 / printed pages 75–82**
- boundary witness: scan **92**, opening `தப்பவில்லை`
- result: **PASS — corrected**
- structural-only changes: opening rule/enlarged initials; printer signature `க—6` excluded; final `story-ending`; closing ornament; joins synchronized
- story wording changed: **No**
- record: `stories/thappivittargal/visual-fidelity.md`

### Story 11 — `தப்பவில்லை`

- workspace: `stories/thappavillai/`
- scans **92–101 / printed pages 83–92**
- boundary witness: scan **102**, opening `ஆதரிக்கிறார்`
- result: **PASS — corrected**
- structural changes: opening rule/enlarged initials; source-bold `நாட்கள் ஓடின...`; final `story-ending`; closing ornament
- source-supported correction: scan **95** `இரவு-பகல்` → `இரவு—பகல்`, verified against the complete source sentence
- story wording changed: **Yes — punctuation only**
- record: `stories/thappavillai/visual-fidelity.md`

### Story 12 — `ஆதரிக்கிறார்`

- workspace: `stories/aatharikkirar/`
- scans **102–107 / printed pages 93–98**
- boundary witness: scan **108**, opening `இரகசியம்!`
- result: **PASS — corrected**
- structural changes: opening rule/enlarged initial; source-bold first `ராஜ நிலையத்தார்`; printer signature `க—7` excluded; source-bold final `புண்யகோடி பொதுஜனத் தொண்டர்போல்தான் உலவுகிறார்;`; final `story-ending`; closing ornament
- source-supported correction: scan **106** `பொதுத்தொண்டு சங்கம் புண்யகோடி...` → `பொதுத்தொண்டு சிங்கம் புண்யகோடி...`, verified against the complete source span
- source anomaly `தலைவனுக` remains retained exactly as printed
- story wording changed: **Yes — source-supported correction only**
- record: `stories/aatharikkirar/visual-fidelity.md`

## NEXT EXACT ACTIVITY — STORY 13 VISUAL FIDELITY ONLY

Story 13 — **`இரகசியம்!`**:

- canonical workspace: `stories/iragasiyam/`
- printed pages: **99–102**
- anthology scans: **108–111**
- boundary witness: scan **112**, opening Story 14 **`முந்நூறு ரூபாய்`**

When the user says **“Proceed with next activity”**:

1. fetch live `main` first and preserve newer work;
2. inspect scans **108–111** directly from the controlling PDF;
3. compare all four pages against `stories/iragasiyam/pages/` and its Tamil assembly under `VISUAL_FIDELITY_CHECK_GUIDE.md`;
4. inspect scan **112** only as the next-story boundary witness;
5. check opening/ending roles, paragraph/dialogue structure, verse/display/emphasis, non-text marks, page furniture and every physical join;
6. apply only source-supported structural corrections; if wording itself is wrong, verify the complete source span before correction and propagate all affected layers;
7. create `stories/iragasiyam/visual-fidelity.md`;
8. update `VISUAL_FIDELITY_PROGRESS.md`, `HANDOVER.md` and `NEXT_CHAT_PROMPT.md`;
9. re-fetch live `main` and changed controls before declaring Story 13 visually complete;
10. **do not begin Story 14 in the same activity unless the user explicitly changes the batch rule**.

Expected result after Story 13 closure: **13 / 37 visual-fidelity complete, 24 pending**.

## Downstream phase guard

Do **not** begin English translation, modernization, republication or another downstream phase unless separately authorized after visual-fidelity work or mandated by newer live repository state.

## Current closure state

- Tamil source pass: **37 / 37 COMPLETE**
- visual fidelity: **12 / 37 COMPLETE**
- next exact activity: **Story 13 `இரகசியம்!` visual fidelity**
