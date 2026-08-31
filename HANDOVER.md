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
- complete: **3 / 37**
- pending: **34 / 37**
- needs recheck: **0**
- current target: **Story 4 — `ஆட்டக்காவடி`**

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

Canonical workspace: `stories/sabalam/`

- printed pages: **15–21**
- scans: **24–30**
- boundary witness: scan **31**, opening `ஆட்டக்காவடி`
- result: **PASS — corrected**
- story-local record: `stories/sabalam/visual-fidelity.md`

Direct visual review covered all seven source pages plus scan 31. Paragraph/dialogue separation, page furniture and every physical join were checked.

Structural-only corrections made:

1. scan 24 / assembly: recorded the long horizontal rule beneath `சபலம்`;
2. scan 28 / assembly: recorded the enlarged initial `வ` marking the new `வண்டி...` paragraph;
3. scan 30: `story-conclusion` → `story-ending`;
4. scan 30: removed the non-source display heading `அச்சு உரை`;
5. scan 30 / assembly: recorded the centered closing ornament;
6. page map synchronized with the source-significant roles.

The visually prominent initial `இ` at the top of scan 27 was **not** encoded as a semantic drop-cap because `இருந்தவர்கள்...` is a direct continuation of scan 26's unfinished `அந்தப் பெட்டியில்`.

Scan 26's printer gathering signature `க—2`, running headers and printed page numbers remain excluded as page furniture.

**No story wording changed during Story 3 visual-fidelity review.** The existing human possible-error queue remains unchanged.

## NEXT EXACT ACTIVITY — STORY 4 VISUAL FIDELITY ONLY

Story 4 — **`ஆட்டக்காவடி`**:

- canonical workspace: `stories/aattakkavadi/`
- printed pages: **22–29**
- anthology scans: **31–38**
- boundary witness: scan **39**, opening Story 5 **`குப்பைத்தொட்டி`**

When the user says **“Proceed with next activity”**:

1. fetch live `main` first and preserve newer work;
2. inspect scans **31–38** directly from the controlling PDF;
3. compare all eight pages against `stories/aattakkavadi/pages/` and its Tamil assembly under `VISUAL_FIDELITY_CHECK_GUIDE.md`;
4. inspect scan **39** only as the next-story boundary witness;
5. check opening/ending roles, paragraph/dialogue structure, display/verse/emphasis, non-text marks, page furniture and every physical join;
6. apply only source-supported structural corrections; if wording itself is wrong, verify the complete source span before correction and propagate all affected layers;
7. create `stories/aattakkavadi/visual-fidelity.md`;
8. update `VISUAL_FIDELITY_PROGRESS.md`, `HANDOVER.md` and `NEXT_CHAT_PROMPT.md`;
9. re-fetch live `main` and changed controls before declaring Story 4 visually complete;
10. **do not begin Story 5 in the same activity**.

Expected result after Story 4 closure: **4 / 37 visual-fidelity complete, 33 pending**.

## Downstream phase guard

Do **not** begin English translation, modernization, republication or another downstream phase unless separately authorized after visual-fidelity work or mandated by newer live repository state.

## Current closure state

- Tamil source pass: **37 / 37 COMPLETE**
- visual fidelity: **3 / 37 COMPLETE**
- next exact activity: **Story 4 `ஆட்டக்காவடி` visual fidelity**
