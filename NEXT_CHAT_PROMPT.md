# NEXT CHAT PROMPT — Kalaignar Short Stories / 2004 English Translation

Continue directly in `pugazg/kalaignar-short-stories`, branch `main`.

## LIVE MAIN IS AUTHORITATIVE

Fetch live `main` first. Preserve newer durable work. Do not reset or reopen the closed 1977 / 2008 phases, the closed 2004 Tamil source phase, or completed 2004 Story-1 English work because a copied checkpoint is older.

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

The controlling PDF must be attached/resolved again before source-dependent visual-fidelity work. Verified canonical Tamil remains authoritative for translation.

## Mandatory startup

Read completely before changing anything:

1. `SHORT_STORY_PROCESSING_GUIDE.md`
2. `COLLECTION_SOURCE_GUIDE.md`
3. `ENGLISH_TRANSLATION_GUIDE.md`
4. root `HANDOVER.md`
5. this `NEXT_CHAT_PROMPT.md`
6. `collections/2004-kalaignarin-kuttik-kathaigal/README.md`
7. `collections/2004-kalaignarin-kuttik-kathaigal/TAMIL_SOURCE_PROGRESS.md`
8. `collections/2004-kalaignarin-kuttik-kathaigal/ENGLISH_TRANSLATION_PROGRESS.md`
9. `stories/neeyum-kaithi-naanum-kaithi/README.md`
10. `stories/neeyum-kaithi-naanum-kaithi/indexes/page-map.md`
11. the Story-2 page record under `stories/neeyum-kaithi-naanum-kaithi/pages/`
12. `stories/neeyum-kaithi-naanum-kaithi/sections/neeyum-kaithi-naanum-kaithi.md`
13. `stories/neeyum-kaithi-naanum-kaithi/audit.md`
14. `stories/neeyum-kaithi-naanum-kaithi/POSSIBLE_ERRORS_FOR_REVIEW.md`
15. Story 1 `stories/valluvar-sonna-poi/README.md`, `visual-fidelity.md`, English translation and `TRANSLATION_REVIEW.md` only as the immediate completed implementation precedent.

Do not import wording or interpretations from another story/source into Story 2.

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
- English `PASS`: **1 / 34**
- pending: **33 / 34**
- `NEEDS REVIEW`: **0**
- visual-fidelity prerequisites closed for English: **1 / 34**
- tracker: `collections/2004-kalaignarin-kuttik-kathaigal/ENGLISH_TRANSLATION_PROGRESS.md`
- default batching: **one story per activity unless the user explicitly expands it**

## Completed English Story 1 — வள்ளுவர் சொன்ன பொய்

Story 1 is **PASS**:

- Tamil source records: **2 / 2 verified**
- Tamil audit: **PASS**
- visual fidelity: **PASS**
- English translation: `stories/valluvar-sonna-poi/translations/en/valluvar-sonna-poi.md`
- translation review: `stories/valluvar-sonna-poi/TRANSLATION_REVIEW.md` — **PASS**
- English source markers: scan **4 / printed 3**, scan **5 / printed 4**
- marker presence/order: **PASS**
- physical content-boundary alignment: **PASS**
- Story 2 material excluded: **Yes**
- Tamil changed during English work: **No**
- unresolved translation issue: **0**

Do not redo or rewrite Story 1 in the next activity.

## Story 2 translation gate

Story 2 **`நீயும் கைதி - நானும் கைதி`**:

- collection sequence: **2 / 34**
- Tamil source records: **1 / 1 verified**
- Tamil audit: **PASS**
- blocked / unresolved story text: **0**
- verified physical span: **scan 5 / printed page 4 only**
- upper same-scan boundary: Story 1 `வள்ளுவர் சொன்ன பொய்` ends above
- lower same-scan boundary / next-story witness: Story 3 `குருவி ராமேஸ்வரம்` begins below
- story-local `visual-fidelity.md`: **not yet present**
- English prose: **pending / must not begin before visual PASS**

## CURRENT EXACT NEXT ACTIVITY

Close the **Story 2 `நீயும் கைதி - நானும் கைதி` visual-fidelity prerequisite**.

- directly inspect the complete Story-2 span on scan **5 / printed page 4**;
- use Story 1 above and Story 3 below only as physical boundary witnesses;
- compare the Story-2 page record and canonical Tamil assembly against the source for exact heading/opening/ending structure, paragraph/dialogue/display fidelity, horizontal separators and page furniture;
- ensure no Story-1 or Story-3 material leaks into Story 2;
- create `stories/neeyum-kaithi-naanum-kaithi/visual-fidelity.md` if closure is source-supported;
- if a textual mismatch is found, reopen only that exact Tamil source span under `SHORT_STORY_PROCESSING_GUIDE.md` before correcting it;
- do **not** create Story-2 English prose in the same activity until the visual prerequisite is durably `PASS`;
- do not begin Story 3.

After Story 2 visual fidelity is durably PASS and controls are synchronized, the following activity is Story 2 English translation and `TRANSLATION_REVIEW.md`.
