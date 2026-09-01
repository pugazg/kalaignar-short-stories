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

- Controlling scan first; no silent normalization of spelling, punctuation, grammar, sandhi, names or source anomalies.
- Old Tamil glyphs require complete-span visual interpretation.
- Running headers, printed page numbers and printer signatures are page furniture.
- `POSSIBLE_ERRORS_FOR_REVIEW.md` is a human-review queue, not proof of error.
- Source-supported corrections must propagate through affected page, assembly, audit/review and control layers.

## Mandatory startup

Before source-dependent visual work, read completely: `SHORT_STORY_PROCESSING_GUIDE.md`, `COLLECTION_SOURCE_GUIDE.md`, `VISUAL_FIDELITY_CHECK_GUIDE.md`, `VISUAL_FIDELITY_PROGRESS.md`, `HANDOVER.md`, `NEXT_CHAT_PROMPT.md`, collection README, story inventory and scan map; then inspect the active story workspace and controlling PDF.

## Durable Tamil milestone

The 1977 anthology Tamil source pass is complete: **37 / 37 stories**, scans **10–259 / printed pages 1–250**, with **0 blocked / 0 unresolved story text**.

## Visual-fidelity phase state

- complete: **17 / 37**
- pending: **20 / 37**
- needs recheck: **0**
- current target: **Story 18 — `செத்தவள் கதை`**

Stories **1–17** are closed with `PASS — corrected` and story-local `visual-fidelity.md` records.

## Latest completed batch — Stories 13–17

The user explicitly requested Stories 13–17 together for this activity.

### Story 13 — `இரகசியம்!`
- scans **108–111 / printed 99–102**; boundary 112 `முந்நூறு ரூபாய்`
- source-bold leaders/transitions/final reveal represented; opening rule/enlarged `அ`; final `story-ending` and ornament
- wording changed: **No**

### Story 14 — `முந்நூறு ரூபாய்`
- scans **112–114 / printed 103–105**; boundary 115 `ஏழை`
- opening rule/enlarged `அ`; final `story-ending` and ornament; `குதாகலமாய்` rechecked and retained
- wording changed: **No**

### Story 15 — `ஏழை`
- scans **115–118 / printed 106–109**; boundary 119 `ஒரிஜினலில் உள்ளபடி`
- opening rule/enlarged `வ`; final `story-ending` and ornament; unusual `பார்வதிக்கு ... பயந்தான்.` rechecked and retained
- wording changed: **No**

### Story 16 — `ஒரிஜினலில் உள்ளபடி`
- scans **119–125 / printed 110–116**; boundary 126 `பனங்குலை`
- opening rule/enlarged `இ`; source-bold notice spans and `எல்லாம் என்`; printer signature `க—8` excluded; final `story-ending` and ornament
- wording changed: **No**

### Story 17 — `பனங்குலை`
- scans **126–130 / printed 117–121**; boundary 131 `செத்தவள் கதை`
- opening rule/enlarged `உ`; final `story-ending` and ornament; printed anomalies retained
- wording changed: **No**

## NEXT EXACT ACTIVITY — STORY 18 ONLY

Story 18 — **`செத்தவள் கதை`**:

- canonical workspace: `stories/setthaval-kathai/`
- printed pages: **122–130**
- anthology scans: **131–139**
- boundary witness: scan **140**, opening Story 19 **`பிரேத விசாரணை`**

When the user says “Proceed with next activity”:
1. fetch live `main` first;
2. inspect scans 131–139 directly from the controlling PDF;
3. compare every page with page records and Tamil assembly;
4. check opening/ending roles, paragraph/dialogue boundaries, display/emphasis, non-text marks, page furniture and every physical join;
5. inspect scan 140 only as boundary witness;
6. apply only source-supported corrections/annotations;
7. create/update Story 18 visual-fidelity record and controls;
8. re-fetch live main before declaring closure;
9. do **not** begin Story 19 unless the user explicitly expands the batch.

Expected after Story 18: **18 / 37 complete, 19 pending**.

## Phase guard

Do not begin English translation, modernization, republication or another downstream phase unless separately authorized.