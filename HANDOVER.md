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
- do not create anthology story folders from an inventory alone;
- every story requires a live-main duplicate/content-equivalence check before activation;
- shared physical scans preserve exact story boundaries;
- source-supported corrections propagate through every dependent layer;
- `POSSIBLE_ERRORS_FOR_REVIEW.md` is a human-review queue, not proof of error;
- English cannot open before the Tamil/source-fidelity gates are closed for the story.

## Closed 1977 anthology

`கலைஞர் கருணாநிதியின் சிறுகதைகள்` remains fully closed:

- Tamil source **37 / 37**;
- visual fidelity **37 / 37**;
- English translation/review **37 / 37**;
- final English structural/control QA **PASS**;
- unresolved story text **0**;
- scan **260** verified back cover.

Story 29 `திடுக்கிடும் கதை` retains its later marker-only provenance correction and strengthened page-anchor regression record. Obsolete Wave-2 pin `a9b333f12128686785ee981f97313a64af12e29b` must not be reused.

## Closed 2008 collection

`கலைஞர் சொன்ன கதைகள்`, Second Edition, December 2008 remains fully closed:

- Tamil source **40 / 40**;
- word-by-word text fidelity **40 / 40 — 19 PASS / 21 PASS — corrected**;
- visual fidelity **40 / 40 PASS**;
- English translation/review **40 / 40 PASS**;
- final 2008 English structural/control QA **PASS**;
- pending / `NEEDS REVIEW`: **0**;
- final story boundary: scan **81 / printed page 79**;
- scan **82** verified back cover;
- canonical Tamil changed during English/final QA: **No**.

## ACTIVE COLLECTION — கலைஞரின் குட்டிக் கதைகள்

Workspace: `collections/2004-kalaignarin-kuttik-kathaigal/`  
Controlling source: `TVA_BOK_0065567_கலைஞரின்_குட்டிக்_கதைகள்_2004.pdf`

### Exact source identity

- SHA-256: `33bdfb4f47bc688750fff11f967a0d2b95a93a9aa09044c0467107dae583ab04`;
- size: **98,897,868 bytes**;
- PDF scans: **50**;
- printed title: **கலைஞரின் குட்டிக் கதைகள்**;
- title-page designation: **தொகுப்பு நூல்**;
- publisher: **பாரதி பதிப்பகம்**;
- colophon: **Revised Edition: Aug. 1998; Second Edition: March 2004**;
- represented edition: **Second Edition, March 2004**.

User-supplied bibliographic metadata identifies the author as **கலைஞர் மு. கருணாநிதி** and describes the work as a 34-story `மணி விழா` collection. This remains intake/catalogue context; the scan controls transcription.

### Physical structure

- scans **1–3**: unnumbered front matter;
- scans **4–49**: story block / printed pages **3–48**;
- story-block relation: **scan = printed page + 1**;
- scan **50**: physical back cover, no further story text;
- printed contents page: **none visible**;
- direct heading inventory: **34 / 34**.

## Story 1 completed — வள்ளுவர் சொன்ன பொய்

Canonical workspace:

`stories/valluvar-sonna-poi/`

Fresh live-main exact-title and distinctive-content searches found no existing canonical equivalent, so Story 1 was activated as a new canonical story.

Source result:

- opening: scan **4 / printed page 3**;
- ending: top of scan **5 / printed page 4**;
- source records: **2 / 2 verified**;
- Tamil assembly: complete;
- audit: **PASS**;
- `needs-review`: **0**;
- `blocked`: **0**;
- unresolved story text: **0**;
- English: **not opened**.

Physical boundary: scan 4 contains the heading and main two paragraphs. Scan 5 begins with the final Valluvar answer and then opens Story 2 `நீயும் கைதி - நானும் கைதி`; Story-2 material was excluded. Source-close `எங்கேல்லாமோ`, joined `தன்வீட்டிற்குள்ளே`, quoted `‘வரவில்லை’`, and `வாய்மையா, அல்லவா!!` were retained without normalization.

Collection state after Story 1:

- canonical story workspaces activated: **1 / 34**;
- Tamil source processing complete: **1 / 34**;
- pending: **33 / 34**;
- completed-story blocked / unresolved: **0**.

## Current exact next activity

Process **Story 2 — `நீயும் கைதி - நானும் கைதி`**.

Routing coordinates:

- Story 2 opens on scan **5 / printed page 4**, immediately below the completed Story-1 ending;
- Story 3 **`குருவி ராமேஸ்வரம்`** begins later on the **same scan 5 / printed page 4** and is the required Story-2 ending-boundary witness.

Before Story-2 activation:

1. fetch live `main`;
2. read the mandatory startup guides and active collection controls;
3. perform a fresh exact-title / alternate-title / content-equivalence search;
4. if an equivalent canonical story exists, add this 2004 witness rather than creating a duplicate;
5. otherwise create the canonical Story-2 workspace;
6. transcribe only the Story-2 text between its heading and the Story-3 heading on scan 5;
7. do not include the Story-1 ending above or Story-3 text below;
8. default to **one story per activity** unless the user explicitly expands the batch;
9. synchronize collection/root controls, `HANDOVER.md` and `NEXT_CHAT_PROMPT.md` after durable closure.

If the controlling PDF is unavailable in a fresh chat, reattach/resolve it before source-dependent Story-2 work.