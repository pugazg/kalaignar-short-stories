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

Story 1 `வள்ளுவர் சொன்ன பொய்` was completed first. The user then explicitly authorized an **11-story iteration**, Stories **2–12**; that batch is **11 / 11 PASS**. Story 13 `வீரவாடி` was subsequently processed as the next source activity and is also PASS.

Collection state:

- activated: **13 / 34**
- Tamil source complete: **13 / 34**
- pending: **21 / 34**
- completed-story blocked / unresolved: **0**
- English: **not opened**

Completed Stories 2–13:

2. `நீயும் கைதி - நானும் கைதி` — scan 5 only — PASS
3. `குருவி ராமேஸ்வரம்` — scans 5–6 — PASS
4. `பெண்களுக்கு ஏன் - மீசை தாடியில்லை?` — scans 6–11 — PASS
5. `கடலைத் தூர்ப்பது மிக எளிது` — scans 11–13 — PASS
6. `மனைவி சொன்ன விளக்கம்` — scans 13–14 — PASS
7. `நாதம் எழாது - நரம்புதான் அறும்` — scans 14–15 — PASS
8. `அவள் சொன்னாள்` — scan 15 only — PASS
9. `இருவரும் கூடியிருப்பது ஆத்தி மாலைதான்` — scans 15–16 — PASS
10. `கொல்லப்பட வேண்டியது புலி, ஆனால்...` — scans 16–17 — PASS
11. `அந்தக் காலத்திலே!` — scan 17 only — PASS
12. `ஆண்டவன் தரிசனம் கொடுத்த ஊர்` — scan 18 only — PASS
13. `வீரவாடி` — scan 18 → top scan 19 — PASS

All have canonical workspaces, page records, Tamil assemblies, source metadata, page maps, audits and persistent possible-error queues. No English translation was opened.

### Latest completed Story 13 — வீரவாடி

Workspace: `stories/veeravadi/`

- fresh exact-title/content-equivalence searches found **no existing canonical match**;
- verified source span: **scan 18 / printed 17 → top scan 19 / printed 18**;
- source records: **2 / 2 verified**;
- page join: `அந்த ஊரையே அவர்களுக்கு` → `மானியமாக வழங்கி...`;
- Story 14 material below the ending on scan 19 is excluded;
- audit: **PASS**;
- blocked / unresolved: **0**;
- English: **not opened**.

Source-sensitive `சிற்றாருக்கு` is preserved exactly from direct visual review and retained in the human-review queue rather than silently changed. Other source forms retained include `பெயர் தான்`, `இனத்தவர்க்கு`, and `இறங்குகிறீர்களோ. அந்த ஊரையே...`.

## Current exact next activity

Process **Story 14 — `சொர்க்கத்திற்கு வந்தது எப்படி?`**.

Routing coordinates:

- opening: scan **19 / printed page 18**, immediately below completed Story 13;
- next opening / boundary witness: Story 15 **`கள்ளியும் ரோஜாவும்`**, scan **22 / printed page 21**.

Before activation:

1. fetch live `main`;
2. read mandatory guides and current active collection controls, including `TAMIL_SOURCE_PROGRESS.md` and the completed `stories/veeravadi/` workspace;
3. perform exact-title / alternate-title / distinctive-content equivalence search;
4. create a new canonical workspace only if no equivalent exists; otherwise register this source as an additional witness;
5. inspect scans **19–22** directly and adjudicate Story 14's exact ending before the Story-15 heading;
6. preserve source spelling, punctuation, paragraph/display structure and shared-page boundary;
7. do not begin English translation unless explicitly authorized;
8. synchronize collection controls, root handover and next prompt after durable closure.

If the controlling PDF is unavailable in a fresh chat, reattach or otherwise resolve it before page-level source work.
