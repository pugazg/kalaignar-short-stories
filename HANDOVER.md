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

Durable final-QA record:

`collections/2008-kalaignar-sonna-kathaigal/ENGLISH_TRANSLATION_FINAL_QA.md`

## ACTIVE COLLECTION — கலைஞரின் குட்டிக் கதைகள்

Workspace:

`collections/2004-kalaignarin-kuttik-kathaigal/`

Controlling source:

`TVA_BOK_0065567_கலைஞரின்_குட்டிக்_கதைகள்_2004.pdf`

### Exact source identity

- SHA-256: `33bdfb4f47bc688750fff11f967a0d2b95a93a9aa09044c0467107dae583ab04`;
- size: **98,897,868 bytes**;
- PDF scans: **50**;
- printed title: **கலைஞரின் குட்டிக் கதைகள்**;
- title-page designation: **தொகுப்பு நூல்**;
- publisher: **பாரதி பதிப்பகம்**;
- colophon: **Revised Edition: Aug. 1998; Second Edition: March 2004**;
- represented edition: **Second Edition, March 2004**.

User-supplied bibliographic metadata identifies the author as **கலைஞர் மு. கருணாநிதி** and describes the work as a 34-story `மணி விழா` collection addressing social conditions through religious, economic, political and cultural themes. This remains intake/catalogue context; printed scan wording controls transcription.

### Physical structure

- scans **1–3**: unnumbered front matter;
- scans **4–49**: story block;
- story printed pages represented: **3–48**;
- story-block relation: **scan = printed page + 1**;
- scan **50**: physical back cover, no further story text.

No printed contents page is visible in this source. The book moves from colophon scan 3 directly to story text on scan 4.

### Intake completed

The collection source is now registered on live `main` with:

- `collections/2004-kalaignarin-kuttik-kathaigal/README.md`;
- `metadata/source.md`;
- `indexes/story-inventory.md`;
- `indexes/scan-map.md`.

A direct source-heading survey established **34 / 34** story openings across scans 4–49. No TOC wording was invented.

Canonical story workspaces activated: **0 / 34**.  
Tamil source processing complete: **0 / 34**.  
English translation: **not opened**.

### Final physical boundary

Story 34 `கிழவியின் மனைவி` opens on scan **47 / printed page 46**, continues through scans **48–49**, and ends with `முற்றும்` on scan **49 / printed page 48**. Scan **50** is back-cover matter only.

## Current exact next activity

Process **Story 1 — `வள்ளுவர் சொன்ன பொய்`**.

Routing coordinates:

- opening: scan **4 / printed page 3**;
- required next-story boundary witness: scan **5 / printed page 4**;
- Story 2 heading on scan 5: **`நீயும் கைதி - நானும் கைதி`**.

Before creating Story 1:

1. fetch live `main`;
2. read `SHORT_STORY_PROCESSING_GUIDE.md`, `COLLECTION_SOURCE_GUIDE.md`, this `HANDOVER.md`, `NEXT_CHAT_PROMPT.md`, active collection README, source metadata, story inventory and scan map;
3. perform the required canonical duplicate/content-equivalence search, including plausible alternate-title/content checks;
4. exact-title and key-phrase searches during intake found no existing repository hit for `வள்ளுவர் சொன்ன பொய்`, but this is not a substitute for the final activation check;
5. if no canonical equivalent exists, create the Story-1 workspace and directly transcribe/verify only its true physical span using scan 5 as the ending boundary witness;
6. do not include Story-2 heading/prose in Story 1;
7. follow the default **one story per activity** rule unless the user explicitly expands the batch;
8. synchronize collection controls, handover and next prompt after Story 1 is durably closed.

If the controlling PDF is not available in a fresh chat, reattach/resolve it before source-dependent Story-1 work.
