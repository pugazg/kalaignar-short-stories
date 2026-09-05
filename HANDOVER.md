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
- English cannot open before the Tamil/source-fidelity gates are closed.

## Closed prior collections

### 1977 — கலைஞர் கருணாநிதியின் சிறுகதைகள்

Tamil **37 / 37**, visual **37 / 37**, English **37 / 37**, final English QA **PASS**, unresolved **0**, scan **260** verified back cover. Story 29 retains its later marker-only provenance correction. Never reuse obsolete pin `a9b333f12128686785ee981f97313a64af12e29b`.

### 2008 — கலைஞர் சொன்ன கதைகள்

Tamil **40 / 40**, text fidelity **40 / 40**, visual **40 / 40**, English **40 / 40**, final English structural/control QA **PASS**, pending / needs review **0**, scan **82** verified back cover.

## ACTIVE COLLECTION — கலைஞரின் குட்டிக் கதைகள்

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

## Completed Tamil source work

Current collection state:

- activated: **33 / 34**
- Tamil source complete: **33 / 34**
- pending: **1 / 34**
- completed-story blocked / unresolved: **0**
- English: **not opened**

The user-authorized **Stories 19–28** iteration is **10 / 10 PASS**. Stories **29–33** were then completed as successive exact activities.

### Story 33 — கைதியின் கதை

- workspace: `stories/kaithiyin-kathai/`
- verified span: **lower scan 44 / printed 43 → upper scan 47 / printed 46**
- source records: **4 / 4 verified**
- duplicate/content-equivalence search: **no existing canonical match**
- Story 32 `உயிருக்கு விலை ஐம்பது லட்சம்` ends above on scan 44 and is excluded
- Story 34 `கிழவனின் மனைவி` begins below on scan 47 and is excluded
- audit: **PASS**
- blocked / unresolved: **0**
- English: **not opened**

The scan-45 → scan-46 physical split `வைத்திய` / `சாலையில்` was verified and joined as `வைத்தியசாலையில்` in the canonical assembly. Source-sensitive forms including `குபேரன் வீட்டுக் கோதை`, `வளர்த்துவானேன்`, `அழுவானேன்!`, `பர்மாக்காரியை பாரியாளாக`, `பள்ளிக்கூடத்தாம் உணவு விடுதியில்`, `பகன்றேன்`, `கூஷ்டரோகம்`, and `அவன் என்னைக் கொல்லாமல் கொன்று விடுதலை பெற்றான்.` are retained exactly as printed.

### Heading corrections locked in the active source controls

- Story 16: **`ஆபாசமே ஆபாசம்!`**
- Story 21: **`விஞ்ஞானிக்குத் தோன்றாது...`**
- Story 26: **`கூற்றுவன் எப்படிப் மறித்தான்?`**
- Story 34: **`கிழவனின் மனைவி`**

## Current exact next activity

Process **Story 34 — `கிழவனின் மனைவி`**.

Routing coordinates:

- opening: scan **47 / printed page 46**, immediately below completed Story 33;
- story continues through scan **49 / printed page 48**;
- required final physical-boundary witness: scan **50**, the back cover, with no further story text.

Before activation:

1. fetch live `main`;
2. read mandatory guides and current active collection controls;
3. perform exact-title / plausible alternate-title / distinctive-content equivalence search;
4. create a new canonical workspace only if no equivalent exists; otherwise register this source as an additional witness;
5. inspect the controlling PDF directly across scans **47–50** and transcribe only the verified Story-34 physical span;
6. preserve the Story-33/34 shared boundary on scan 47 and verify the final story/back-cover boundary at scans 49–50;
7. preserve source spelling, punctuation, paragraph/display structure and non-text marks;
8. do not begin English translation unless explicitly authorized;
9. synchronize all collection controls, root README, `HANDOVER.md` and `NEXT_CHAT_PROMPT.md` after durable closure.

If the controlling PDF is unavailable in a fresh chat, reattach/resolve it before source-dependent work.
