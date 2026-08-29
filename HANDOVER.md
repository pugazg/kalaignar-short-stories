# HANDOVER — Kalaignar Short Stories Archive

## Repository

- Repository: `pugazg/kalaignar-short-stories`
- Branch: `main`
- Story workflow: `SHORT_STORY_PROCESSING_GUIDE.md`
- Anthology workflow: `COLLECTION_SOURCE_GUIDE.md`
- Cross-chat resume prompt: `NEXT_CHAT_PROMPT.md`
- Source PDFs are **not** committed to GitHub.

## Permanent source rules

- **Controlling scan first.** Do not silently modernize spelling, grammar, punctuation, names, sandhi or source anomalies.
- **No stones should be left unturned.** Difficult story readings must receive full-span visual escalation before terminal `blocked` status.
- **Processed-crop confidence is not source confidence.** Verify the complete phrase/clause/sentence against the source span.
- `POSSIBLE_ERRORS_FOR_REVIEW.md` is a human-review queue, not a list of confirmed errors.
- A later source-supported correction must be propagated through the page record, Tamil assembly, audit, story README and all affected collection/root control files.

## Cross-chat restart rules

When continuing in a new chat window:

1. fetch live GitHub `main` first and treat it as authoritative;
2. read completely before source-dependent writes:
   - `SHORT_STORY_PROCESSING_GUIDE.md`
   - `COLLECTION_SOURCE_GUIDE.md`
   - `HANDOVER.md`
   - `NEXT_CHAT_PROMPT.md`
   - collection `README.md`
   - collection `indexes/story-inventory.md`
   - collection `indexes/scan-map.md`;
3. inspect the latest completed story workspace (`stories/santhana-kinnam/`) as the immediate structural reference;
4. do not redo completed stories/pages without user correction, stronger scan evidence or a live-repository inconsistency;
5. controlling PDF availability is mandatory for transcription/visual verification;
6. when the user says **“Proceed with next activity”**, execute the exact activity below without routine clarification;
7. process one anthology story at a time and do not begin the following story in the same activity;
8. synchronize story workspace + anthology inventory + collection README + root README + scan map + this handover + `NEXT_CHAT_PROMPT.md` before closure.

## Completed independent story — கிழவன் கனவு

`stories/kizhavan-kanavu/` remains source-complete: **16/16 verified, 0 story blocks, English complete/source-complete/release-ready**.

## Active collection source — 1977 anthology

Collection workspace:

`collections/1977-kalaignar-karunanidhiyin-sirukathaigal/`

Source identity:

- filename: `TVA_BOK_0064142_கலைஞர்_கருணாநிதியின்_சிறுகதைகள்.pdf`
- SHA-256: `853032661482eaccb26c083a38d7aa75c081362d33c963c63e37d088bf20acb3`
- file size: **268,486,609 bytes**
- PDF scans: **260**
- printed title: **கலைஞர் கருணாநிதியின் சிறுகதைகள்**
- author line: **கலைஞர் மு. கருணாநிதி**
- publisher: **தமிழ்க்கனி பதிப்பகம், சென்னை-28**
- edition: **முதல் பதிப்பு: 1977**
- printed story pagination: **1–250**
- story block scans: **10–259**
- back cover: scan **260**
- story-block relation: **scan = printed page + 9**
- source PDF in repository: **No**

Anthology processing state:

- contents inventory: **37 / 37**
- story-start visual checks: **37 / 37**
- Tamil source processing complete: **6 / 37**
- stories not yet transcribed: **31 / 37**
- English translation started from anthology: **0 / 37**

Edition-level title differences to preserve:

1. TOC `புரட்சிப்படம்` — opening `புரட்சிப் படம்`
2. TOC `சித்தார்த்தன்` — opening `சித்தார்த்தன் சிலை`

## Completed anthology stories

1. `புகழேந்தி` — `stories/pugazhendhi/` — printed **1–6**, scans **10–15**, **6/6 verified**, 0 blocked, audit PASS.
2. `நளாயினி` — `stories/nalayini/` — printed **7–14**, scans **16–23**, **8/8 verified**, 0 blocked, audit PASS.
3. `சபலம்` — `stories/sabalam/` — printed **15–21**, scans **24–30**, **7/7 verified**, 0 blocked, audit PASS.
4. `ஆட்டக்காவடி` — `stories/aattakkavadi/` — printed **22–29**, scans **31–38**, **8/8 verified**, 0 blocked, audit PASS.
5. `குப்பைத்தொட்டி` — `stories/kuppai-thotti/` — printed **30–37**, scans **39–46**, **8/8 verified**, 0 blocked, audit PASS.
6. `சந்தனக்கிண்ணம்` — `stories/santhana-kinnam/` — printed **38–47**, scans **47–56**, **10/10 verified**, 0 blocked, audit PASS.

All six completed anthology stories have **0 unresolved story text**, complete Tamil assemblies and persistent `POSSIBLE_ERRORS_FOR_REVIEW.md` queues. English translation has not been started for them.

## Anthology Story 6 — சந்தனக்கிண்ணம் — COMPLETE TAMIL SOURCE PASS

Canonical workspace: `stories/santhana-kinnam/`

Files/control layers:

- `README.md`
- `metadata/source.md`
- `indexes/page-map.md`
- pages `0047-santhana-kinnam-01.md` through `0056-santhana-kinnam-10.md`
- `sections/santhana-kinnam.md`
- `audit.md`
- `POSSIBLE_ERRORS_FOR_REVIEW.md`

Final source state:

- page records: **10 / 10**
- verified: **10 / 10**
- needs-review status pages: **0**
- blocked: **0**
- explicit missing/unresolved story text: **0**
- Tamil assembly: complete
- source audit: **PASS**
- English translation: **not started**

Verified physical continuations:

1. printed 39→40: poem continues after `மறவன் மாளிகை!`.
2. printed 40→41: `மானமற்ற வம்சமா நீ? ஏடா?` → `மறத்தமிழக் குடியிலே மாசு தூவி விட்டாய்!`.
3. printed 41→42: `அறிஞர்களின்` → `பாராட்டுக்குரிய...`.
4. printed 42→43: Kandan's `கடலிலே மீனை...` setup → Kamala's response.
5. printed 44→45: `கந்தன்,` → `கையிலே கொடியேந்தியவாறு...`.
6. printed 45→46: `என்று` → `அழுதான் கந்தன்.`.
7. printed 46→47: `அசையாமல்` → `அப்படியே நின்று...`.

Boundary:

- scan 47 opens `சந்தனக்கிண்ணம்`;
- scan 56 contains the conclusion and ornamental closing rule;
- scan 57 opens Story 7 `சங்கிலிச்சாமி`;
- Story 7 text included in Story 6 workspace: **No**.

High-value human rechecks include `பூரிப்பு வழிய`, `திராவிட உட்கல வங்க`, `கிலியும்`, `மோழைக்குப் பெயர் போர்வீரனும்!`, `பழமைப்பித்துப் பிடித்தவள்`, `அவள் வலுவில் பேசவந்தாலும்`, `கழுதை தேய்ந்து கட்டெறும் பாயிற்று!`, `தோழி யளித்தது`, `பணக்காரனுமில்லா விட்டாலும்`, and `தயாரா யிருக்கிறான்`.

Do not change these merely because they look unusual. A source-supported correction must be checked against the complete source span and propagated through every dependent layer.

## Canonical-story / anthology rule

Before each story:

1. check live `stories/` for TOC title, opening heading and documented alternate title;
2. if a canonical story exists, attach the anthology as an additional edition/witness;
3. otherwise create the story workspace only when that story becomes active;
4. preserve anthology scan + printed-page coordinates;
5. create a persistent possible-error queue;
6. use complete-span verification rather than isolated-crop confidence.

## Next exact activity

Process anthology Story **7 — `சங்கிலிச்சாமி`** only.

Range:

- printed pages: **48–59**
- anthology scans: **57–68**

Boundary checks:

- scan **57** must open `சங்கிலிச்சாமி`;
- scan **68** must close Story 7;
- scan **69** must be checked as the opening of Story 8 `கங்கையின் காதல்` before closing the range.

Actions:

1. fetch live `main` and confirm no canonical `சங்கிலிச்சாமி` workspace already exists;
2. make the 57 / 68 / 69 boundary checks from the controlling scan;
3. create a stable Story 7 workspace only after the canonical-story check;
4. register the 1977 anthology as controlling source;
5. create **12** page records for scans **57–68** / printed pages **48–59**;
6. transcribe directly from source scans and run full-span visual-fidelity review;
7. exhaust difficult readings before using `blocked`; keep unusual-but-legible source forms in `POSSIBLE_ERRORS_FOR_REVIEW.md`;
8. create assembled Tamil, source audit and story README;
9. synchronize anthology inventory, collection README, root README, scan map, HANDOVER and `NEXT_CHAT_PROMPT.md`;
10. **do not begin Story 8 (`கங்கையின் காதல்`) in the same activity.**

## New-chat readiness

**READY FOR CONTINUATION.**

The durable resume file is `NEXT_CHAT_PROMPT.md`. The controlling anthology PDF must be available for source-dependent work. If live `main` has moved beyond this state, use the newer repository state rather than reverting to this handover.
