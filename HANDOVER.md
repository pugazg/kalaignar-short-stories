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

The user has explicitly authorized opening English translation for the 2004 collection.

Tracker: `collections/2004-kalaignarin-kuttik-kathaigal/ENGLISH_TRANSLATION_PROGRESS.md`

- English phase: **OPEN**
- English `PASS`: **0 / 34**
- pending: **34 / 34**
- `NEEDS REVIEW`: **0**
- default batching: **one story per activity unless the user explicitly expands it**
- canonical Tamil changed during phase opening: **No**

`ENGLISH_TRANSLATION_GUIDE.md` requires visual-fidelity closure before a story enters English. Story 1 `வள்ளுவர் சொன்ன பொய்` has a direct high-resolution Tamil source audit and no unresolved text, but no separate story-local `visual-fidelity.md` is currently present. Do not silently equate those two controls.

## Current exact next activity

Close the **Story 1 `வள்ளுவர் சொன்ன பொய்` visual-fidelity prerequisite** before English prose begins.

1. Fetch live `main` again.
2. Ensure the controlling 2004 PDF is attached/resolved before visual work.
3. Read `ENGLISH_TRANSLATION_GUIDE.md`, the Story-1 README, page map, page records, Tamil assembly, audit and `POSSIBLE_ERRORS_FOR_REVIEW.md`.
4. Directly inspect scan **4 / printed 3** and the Story-1 ending at the top of scan **5 / printed 4**; use Story 2 below as the boundary witness only.
5. Record the visual-fidelity disposition durably at story level; make only source-supported structural corrections if any are required.
6. Do **not** begin Story-1 English prose until this prerequisite is `PASS`.

After that closure, the next activity is Story 1 English translation to `stories/valluvar-sonna-poi/translations/en/valluvar-sonna-poi.md` plus `TRANSLATION_REVIEW.md`, with source-page markers physically aligned under `ENGLISH_TRANSLATION_GUIDE.md`.
