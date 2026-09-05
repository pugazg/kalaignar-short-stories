# NEXT CHAT PROMPT — Kalaignar Short Stories / 2004 English Translation

Continue directly in `pugazg/kalaignar-short-stories`, branch `main`.

## LIVE MAIN IS AUTHORITATIVE

Fetch live `main` first. Preserve newer durable work. Do not reset or reopen the closed 1977 / 2008 phases or the closed 2004 Tamil source phase because a copied checkpoint is older.

## 2004 controlling source

`TVA_BOK_0065567_கலைஞரின்_குட்டிக்_கதைகள்_2004.pdf`

- title: **கலைஞரின் குட்டிக் கதைகள்**
- publisher: **பாரதி பதிப்பகம்**
- represented edition: **Second Edition, March 2004**
- SHA-256: `33bdfb4f47bc688750fff11f967a0d2b95a93a9aa09044c0467107dae583ab04`
- size: **98,897,868 bytes**
- scans: **50**
- story block: scans **4–49 / printed pages 3–48**
- scan **50**: verified back cover
- no printed contents page; direct heading inventory **34 / 34**

Attach or otherwise resolve the controlling PDF again before any source-dependent visual-fidelity work.

## Mandatory startup

Read completely before changing anything:

1. `SHORT_STORY_PROCESSING_GUIDE.md`
2. `COLLECTION_SOURCE_GUIDE.md`
3. `ENGLISH_TRANSLATION_GUIDE.md`
4. root `HANDOVER.md`
5. this `NEXT_CHAT_PROMPT.md`
6. `collections/2004-kalaignarin-kuttik-kathaigal/README.md`
7. `collections/2004-kalaignarin-kuttik-kathaigal/metadata/source.md`
8. `collections/2004-kalaignarin-kuttik-kathaigal/indexes/story-inventory.md`
9. `collections/2004-kalaignarin-kuttik-kathaigal/indexes/scan-map.md`
10. `collections/2004-kalaignarin-kuttik-kathaigal/TAMIL_SOURCE_PROGRESS.md`
11. `collections/2004-kalaignarin-kuttik-kathaigal/ENGLISH_TRANSLATION_PROGRESS.md`
12. `stories/valluvar-sonna-poi/README.md`
13. `stories/valluvar-sonna-poi/indexes/page-map.md`
14. both Story-1 page records
15. `stories/valluvar-sonna-poi/sections/valluvar-sonna-poi.md`
16. `stories/valluvar-sonna-poi/audit.md`
17. `stories/valluvar-sonna-poi/POSSIBLE_ERRORS_FOR_REVIEW.md`

Use the closed 1977 / 2008 English work only as implementation precedent. Do not import wording or interpretations from those sources into the 2004 Tamil layer.

## Durable phase state

### Tamil

- Tamil source: **34 / 34 PASS**
- pending: **0**
- unresolved story text: **0**
- final story boundary: scan **49 / printed page 48**, centered `முற்றும்`
- final physical boundary: scan **50**, verified back cover
- Tamil phase: **COMPLETE / CLOSED**

### English

The user explicitly authorized the 2004 English phase.

- English phase: **OPEN**
- English `PASS`: **0 / 34**
- pending: **34 / 34**
- `NEEDS REVIEW`: **0**
- tracker: `collections/2004-kalaignarin-kuttik-kathaigal/ENGLISH_TRANSLATION_PROGRESS.md`
- default batching: **one story per activity unless the user explicitly expands it**

## Translation-gate finding

`ENGLISH_TRANSLATION_GUIDE.md` requires story-local visual-fidelity closure before translation. Story 1 `வள்ளுவர் சொன்ன பொய்` already has a direct high-resolution Tamil source audit, but its current workspace has no separate `visual-fidelity.md` record. Do not silently treat the source audit as that separate prerequisite.

## CURRENT EXACT NEXT ACTIVITY

Close the **Story 1 `வள்ளுவர் சொன்ன பொய்` visual-fidelity prerequisite**.

- source span: scan **4 / printed 3 → top scan 5 / printed 4**;
- Story 2 `நீயும் கைதி - நானும் கைதி` begins below on scan 5 and is the boundary witness only;
- inspect source-significant heading/opening/ending structure, paragraph/dialogue structure, page furniture and the scan-4→5 join;
- compare against Story-1 page records and canonical Tamil assembly;
- create a durable Story-1 visual-fidelity record if closure is supportable;
- if a textual problem is discovered, reopen only that exact Tamil span against the controlling source before any correction;
- do **not** create Story-1 English prose in the same activity until the visual prerequisite is durably `PASS`.

Once Story 1 visual fidelity is closed, the following activity is its English translation and `TRANSLATION_REVIEW.md`, using physical source-page markers aligned to the verified Tamil page boundaries.
