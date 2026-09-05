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

- activated: **32 / 34**
- Tamil source complete: **32 / 34**
- pending: **2 / 34**
- completed-story blocked / unresolved: **0**
- English: **not opened**

The user-authorized **Stories 19–28** iteration is **10 / 10 PASS**. Stories **29–32** were then completed as successive exact activities.

### Story 32 — உயிருக்கு விலை ஐம்பது லட்சம்

- workspace: `stories/uyirukku-vilai-aimbathu-latcham/`
- verified span: **lower scan 42 / printed 41 → upper scan 44 / printed 43**
- source records: **3 / 3 verified**
- duplicate/content-equivalence search: **no existing canonical match**
- Story 31 `புதிர்` ends above on scan 42 and is excluded
- Story 33 `கைதியின் கதை` begins below on scan 44 and is excluded
- audit: **PASS**
- blocked / unresolved: **0**
- English: **not opened**

The scan-42 → scan-43 and scan-43 → scan-44 transitions were checked as continuous and non-duplicative. Source-sensitive forms including `ரிப்பேரில்`, `நீர்வாகத்திற்கு`, `யூனியன்,முனிசிபாலிடி,`, asymmetric `‘சே, சே... வருவதற்கில்லை.”`, `கிறுகிறுத்தது`, four-dot lead-ins `....`, `‘கன்சஷன்’`, `காசாலேதான்`, `காசாலேசா! நீ காசாலே சா!`, and the final cheque amount `ஐம்பது லட்சம்` are retained exactly as printed.

### Heading corrections locked in the active source controls

- Story 16: **`ஆபாசமே ஆபாசம்!`**
- Story 21: **`விஞ்ஞானிக்குத் தோன்றாது...`**
- Story 26: **`கூற்றுவன் எப்படிப் மறித்தான்?`**
- Story 34: **`கிழவனின் மனைவி`**

## Current exact next activity

Process **Story 33 — `கைதியின் கதை`**.

Routing coordinates:

- opening: scan **44 / printed page 43**, immediately below completed Story 32;
- required ending-boundary witness: Story 34 **`கிழவனின் மனைவி`**, opening scan **47 / printed page 46**.

Before activation:

1. fetch live `main`;
2. read mandatory guides and current active collection controls;
3. perform exact-title / plausible alternate-title / distinctive-content equivalence search;
4. create a new canonical workspace only if no equivalent exists; otherwise register this source as an additional witness;
5. inspect the controlling PDF directly across scans **44–47** and transcribe only the verified Story-33 physical span;
6. preserve the Story-32/33 shared boundary on scan 44 and exclude Story-34 material at/after its heading on scan 47;
7. preserve source spelling, punctuation, paragraph/display structure and non-text marks;
8. do not begin English translation unless explicitly authorized;
9. synchronize all collection controls, root README, `HANDOVER.md` and `NEXT_CHAT_PROMPT.md` after durable closure.

If the controlling PDF is unavailable in a fresh chat, reattach/resolve it before source-dependent work.
