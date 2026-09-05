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

The controlling PDF only needs to be re-opened during English work if translation exposes a source-fidelity question. The verified canonical Tamil remains the translation authority.

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
9. `stories/valluvar-sonna-poi/README.md`
10. `stories/valluvar-sonna-poi/indexes/page-map.md`
11. both Story-1 page records
12. `stories/valluvar-sonna-poi/sections/valluvar-sonna-poi.md`
13. `stories/valluvar-sonna-poi/audit.md`
14. `stories/valluvar-sonna-poi/POSSIBLE_ERRORS_FOR_REVIEW.md`
15. `stories/valluvar-sonna-poi/visual-fidelity.md`

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
- visual-fidelity prerequisites closed for English: **1 / 34**
- tracker: `collections/2004-kalaignarin-kuttik-kathaigal/ENGLISH_TRANSLATION_PROGRESS.md`
- default batching: **one story per activity unless the user explicitly expands it**

## Story 1 translation gate

Story 1 **`வள்ளுவர் சொன்ன பொய்`** is **translation-ready**.

- verified Tamil source records: **2 / 2**
- Tamil audit: **PASS**
- visual fidelity: **PASS**
- visual-fidelity corrections: **none**
- canonical Tamil changed during visual closure: **No**
- source span: scan **4 / printed 3 → top scan 5 / printed 4**
- Story 2 below on scan 5 is excluded
- English prose: **pending**

## CURRENT EXACT NEXT ACTIVITY

Translate **Story 1 `வள்ளுவர் சொன்ன பொய்`** and create its translation review.

- create `stories/valluvar-sonna-poi/translations/en/valluvar-sonna-poi.md` from the verified Tamil assembly;
- use conservative English for source-sensitive forms and record difficult choices in `TRANSLATION_REVIEW.md` rather than changing Tamil;
- preserve page provenance with `<!-- source scan 4; printed page 3 -->` and `<!-- source scan 5; printed page 4 -->` at the exact physical transition established by the Tamil page records;
- the scan-4 English section must carry the two scan-4 Tamil paragraphs and end with the question asking why Valluvar told a lie;
- the scan-5 English section must begin with Valluvar's answer and contain only the Story-1 closing paragraph;
- exclude Story 2 `நீயும் கைதி - நானும் கைதி` and all later material on scan 5;
- read and respect `POSSIBLE_ERRORS_FOR_REVIEW.md`; do not silently normalize `எங்கேல்லாமோ`, `தன்வீட்டிற்குள்ளே`, `‘வரவில்லை’`, `வாய்மையா, அல்லவா!!` or the closing `வாய்மை` wording;
- create `stories/valluvar-sonna-poi/TRANSLATION_REVIEW.md` with separate checks for marker presence/order and physical content-boundary alignment;
- do not begin Story 2 in this activity.

After Story 1 English is durably PASS and all controls are synchronized, the following activity is the Story-2 translation-gate / visual-fidelity prerequisite, unless the user explicitly expands the batch.