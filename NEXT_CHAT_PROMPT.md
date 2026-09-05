# NEXT CHAT PROMPT — Kalaignar Short Stories / 2004 English Translation

Continue directly in `pugazg/kalaignar-short-stories`, branch `main`.

## LIVE MAIN IS AUTHORITATIVE

Fetch live `main` first. Preserve newer durable work. Do not reset or reopen the closed 1977 / 2008 phases, the closed 2004 Tamil source phase, completed 2004 Story-1 English work, or the closed Story-2 visual gate because a copied checkpoint is older.

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

The verified canonical Tamil is the translation authority. Re-open the controlling PDF only if translation exposes a source-fidelity question.

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
11. `stories/neeyum-kaithi-naanum-kaithi/pages/0005-neeyum-kaithi-naanum-kaithi-01.md`
12. `stories/neeyum-kaithi-naanum-kaithi/sections/neeyum-kaithi-naanum-kaithi.md`
13. `stories/neeyum-kaithi-naanum-kaithi/audit.md`
14. `stories/neeyum-kaithi-naanum-kaithi/POSSIBLE_ERRORS_FOR_REVIEW.md`
15. `stories/neeyum-kaithi-naanum-kaithi/visual-fidelity.md`
16. Story 1 English translation and `TRANSLATION_REVIEW.md` only as the immediate completed implementation precedent.

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
- visual-fidelity prerequisites closed for English: **2 / 34**
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

Do not redo or rewrite Story 1.

## Story 2 translation gate — PASS

Story 2 **`நீயும் கைதி - நானும் கைதி`** is translation-ready.

- collection sequence: **2 / 34**
- Tamil source records: **1 / 1 verified**
- Tamil audit: **PASS**
- visual fidelity: **PASS**
- blocked / unresolved story text: **0**
- verified physical span: **scan 5 / printed page 4 only**
- upper same-scan boundary: Story 1 `வள்ளுவர் சொன்ன பொய்` ends above and is excluded
- lower same-scan boundary: Story 3 `குருவி ராமேஸ்வரம்` begins below and is excluded
- structure: centered framed heading, three prose paragraphs, then separate `நானும் கைதி.` / `நீயும் கைதி.` closing lines
- visual-fidelity correction required: **none**
- Tamil changed during visual closure: **No**
- English prose: **pending**

## CURRENT EXACT NEXT ACTIVITY

Translate **Story 2 `நீயும் கைதி - நானும் கைதி`** and create its translation review.

- create `stories/neeyum-kaithi-naanum-kaithi/translations/en/neeyum-kaithi-naanum-kaithi.md` from the verified Tamil assembly;
- use conservative English for source-sensitive forms and record difficult choices in `TRANSLATION_REVIEW.md` rather than changing Tamil;
- place `<!-- source scan 5; printed page 4 -->` before the translated story content;
- because Story 2 is entirely on a single source page, that marker section must contain the complete Story-2 translation;
- preserve the rhetorical address to the crescent moon and the prison/captivity parallel without importing outside interpretation;
- retain the final two source-significant lines as two separate English display lines corresponding to `நானும் கைதி.` and `நீயும் கைதி.`;
- exclude Story 1 material above and Story 3 `குருவி ராமேஸ்வரம்` below on scan 5;
- read and respect `POSSIBLE_ERRORS_FOR_REVIEW.md`; do not silently normalize `உனக்கென்ன வாழ்கிறதாம்!` or alter the verified Tamil layer;
- create `stories/neeyum-kaithi-naanum-kaithi/TRANSLATION_REVIEW.md` with separate marker presence/order and physical content-boundary checks;
- do not begin Story 3 in this activity.

After Story 2 English is durably PASS and all controls are synchronized, the following activity is the Story-3 translation-gate / visual-fidelity prerequisite, unless the user explicitly expands the batch.