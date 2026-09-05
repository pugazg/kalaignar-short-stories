# HANDOVER — Kalaignar Short Stories Archive

## Repository

- Repository: `pugazg/kalaignar-short-stories`
- Branch: `main`
- Story workflow: `SHORT_STORY_PROCESSING_GUIDE.md`
- Collection workflow: `COLLECTION_SOURCE_GUIDE.md`
- English workflow: `ENGLISH_TRANSLATION_GUIDE.md`

## LIVE MAIN IS AUTHORITATIVE

Always fetch live `main` first and preserve newer durable work. Repository files reachable from live `main`, not chat memory or copied checkpoints, are the durable state. Source PDFs, renders and crops are not committed.

## Permanent source rules

- controlling scan first; no silent modernization or normalization;
- every story requires a live-main duplicate/content-equivalence check before activation;
- shared physical scans preserve exact story boundaries;
- source-supported corrections propagate through dependent layers;
- `POSSIBLE_ERRORS_FOR_REVIEW.md` is a human-review queue, not proof of error;
- English may only translate a story after its current translation gate is fully documented and closed.

## Closed prior collections

### 1977 — கலைஞர் கருணாநிதியின் சிறுகதைகள்

Tamil **37 / 37**, visual **37 / 37**, English **37 / 37**, final English QA **PASS**, unresolved **0**, scan **260** verified back cover. Story 29 retains its later marker-only provenance correction. Never reuse obsolete pin `a9b333f12128686785ee981f97313a64af12e29b`.

### 2008 — கலைஞர் சொன்ன கதைகள்

Tamil **40 / 40**, text fidelity **40 / 40**, visual **40 / 40**, English **40 / 40**, final English structural/control QA **PASS**, pending / needs review **0**, scan **82** verified back cover.

## 2004 COLLECTION — கலைஞரின் குட்டிக் கதைகள்

Workspace: `collections/2004-kalaignarin-kuttik-kathaigal/`  
Controlling source: `TVA_BOK_0065567_கலைஞரின்_குட்டிக்_கதைகள்_2004.pdf`

### Exact source identity

- SHA-256: `33bdfb4f47bc688750fff11f967a0d2b95a93a9aa09044c0467107dae583ab04`
- size: **98,897,868 bytes**
- PDF scans: **50**
- publisher: **பாரதி பதிப்பகம்**
- colophon: **Revised Edition: Aug. 1998; Second Edition: March 2004**
- represented edition: **Second Edition, March 2004**
- printed contents page: **none visible**
- direct heading inventory: **34 / 34**
- story block: scans **4–49 / printed pages 3–48**
- scan **50**: verified physical back cover

User-supplied bibliographic metadata identifies the author as **கலைஞர் மு. கருணாநிதி** and describes the work as a 34-story `மணி விழா` collection. The scan remains authoritative for printed wording.

## Tamil source closure

- activated: **34 / 34**
- Tamil source complete: **34 / 34**
- pending: **0 / 34**
- completed-story blocked / unresolved: **0**
- Tamil source phase: **COMPLETE / CLOSED**

The user-authorized **Stories 19–28** Tamil iteration is **10 / 10 PASS**. Stories **29–34** were then completed as successive exact activities.

### Final Tamil Story 34 — கிழவனின் மனைவி

- workspace: `stories/kizhavanin-manaivi/`
- verified span: **lower scan 47 / printed 46 → scan 49 / printed 48**
- source records: **3 / 3 verified**
- duplicate/content-equivalence search: **no existing canonical match**
- Story 33 `கைதியின் கதை` ends above on scan 47 and is excluded
- centered `முற்றும்` closes Story 34 on scan 49
- scan 49 lower-page library stamp does not obscure story text
- scan 50 directly verified as physical back cover; no further story text
- audit: **PASS**
- blocked / unresolved: **0**

Source-sensitive forms including `பஞ்சுப் பாதங்களைச்`, `சுற்று முற்றும்`, `தங்கக் கரங்களைக் கிளைகளில்`, `அல்லித் தண்டில்`, `கீழ்ஸ்தாயி`, `வைத்திட்டனாகாது`, `தலை எழுத்து`, `சல்லாப ரூபா`, `தள்ளாத காலத்தில்`, and `வேட்டைதான்` are retained exactly as printed. The physical line split `பய` / `மில்லை` is assembled as `பயமில்லை`.

### Heading corrections locked in the 2004 source controls

- Story 16: **`ஆபாசமே ஆபாசம்!`**
- Story 21: **`விஞ்ஞானிக்குத் தோன்றாது...`**
- Story 26: **`கூற்றுவன் எப்படிப் மறித்தான்?`**
- Story 34: **`கிழவனின் மனைவி`**

## 2004 English translation phase — OPEN

The user has explicitly authorized English translation for the 2004 collection.

Tracker: `collections/2004-kalaignarin-kuttik-kathaigal/ENGLISH_TRANSLATION_PROGRESS.md`

- English phase: **OPEN**
- English `PASS`: **1 / 34**
- pending: **33 / 34**
- `NEEDS REVIEW`: **0**
- visual-fidelity prerequisites closed for English: **1 / 34**
- default batching: **one story per activity unless the user explicitly expands it**
- canonical Tamil changed during English opening / Story-1 visual closure / Story-1 translation: **No**

### Latest completed English work — Story 1

Story 1 **`வள்ளுவர் சொன்ன பொய்`** is **English PASS**.

- workspace: `stories/valluvar-sonna-poi/`
- source records: **2 / 2 verified**
- Tamil audit: **PASS**
- visual fidelity: **PASS**
- English: `stories/valluvar-sonna-poi/translations/en/valluvar-sonna-poi.md`
- translation review: `stories/valluvar-sonna-poi/TRANSLATION_REVIEW.md` — **PASS**
- source span: **scan 4 / printed 3 → top scan 5 / printed 4**
- English marker presence/order: **PASS**
- English physical content-boundary alignment: **PASS**
- Story 2 below on scan 5 excluded correctly
- source-sensitive `உண்மை` / `வாய்மை` distinction preserved conservatively
- source double exclamation represented in English
- Tamil source issue reopened during translation: **No**
- canonical Tamil changed during English work: **No**
- blocked / unresolved: **0**

## Current exact next activity

Close the **Story 2 `நீயும் கைதி - நானும் கைதி` visual-fidelity prerequisite** before English prose begins.

1. Fetch live `main` again.
2. Ensure the controlling 2004 PDF is attached/resolved before direct visual work.
3. Read `ENGLISH_TRANSLATION_GUIDE.md`, current English tracker, Story-2 README, page map, the Story-2 page record, Tamil assembly, audit and `POSSIBLE_ERRORS_FOR_REVIEW.md`.
4. Directly inspect Story 2 on scan **5 / printed page 4**. Story 1 `வள்ளுவர் சொன்ன பொய்` ends above it on the same scan; Story 3 `குருவி ராமேஸ்வரம்` begins below it on the same scan and is the next-story boundary witness.
5. Check exact heading/opening/ending structure, paragraph/dialogue/display structure, separators, page furniture and exclusion of neighbouring stories.
6. Create `stories/neeyum-kaithi-naanum-kaithi/visual-fidelity.md` if closure is source-supported; make only independently source-supported corrections if required.
7. Do **not** create Story-2 English prose until the visual prerequisite is durably `PASS`.
8. Do not begin Story 3 in the same activity.
9. Synchronize Story-2 README, the 2004 English tracker, collection/root controls, `HANDOVER.md` and `NEXT_CHAT_PROMPT.md`, then re-fetch live `main` before declaring the Story-2 gate closed.

After Story 2 visual fidelity is PASS, the following activity is Story 2 English translation and `TRANSLATION_REVIEW.md` under `ENGLISH_TRANSLATION_GUIDE.md`.
