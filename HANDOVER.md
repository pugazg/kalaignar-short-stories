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
3. inspect the latest completed story workspace (`stories/sangilichami/`) as the immediate structural reference;
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
- Tamil source processing complete: **7 / 37**
- stories not yet transcribed: **30 / 37**
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
7. `சங்கிலிச்சாமி` — `stories/sangilichami/` — printed **48–59**, scans **57–68**, **12/12 verified**, 0 blocked, audit PASS.

All seven completed anthology stories have **0 unresolved story text**, complete Tamil assemblies and persistent `POSSIBLE_ERRORS_FOR_REVIEW.md` queues. English translation has not been started for them.

## Anthology Story 7 — சங்கிலிச்சாமி — COMPLETE TAMIL SOURCE PASS

Canonical workspace: `stories/sangilichami/`

Files/control layers:

- `README.md`
- `metadata/source.md`
- `indexes/page-map.md`
- pages `0057-sangilichami-01.md` through `0068-sangilichami-12.md`
- `sections/sangilichami.md`
- `audit.md`
- `POSSIBLE_ERRORS_FOR_REVIEW.md`

Final source state:

- page records: **12 / 12**
- verified: **12 / 12**
- needs-review status pages: **0**
- blocked: **0**
- explicit missing/unresolved story text: **0**
- Tamil assembly: complete
- source audit: **PASS**
- English translation: **not started**

### Boundary / continuation checks

- scan 57 / printed 48 opens `சங்கிலிச்சாமி`.
- Most page boundaries occur after complete sentences or dialogue turns.
- printed **58→59** / scans **67→68** is the explicit physical sentence continuation: `சமாதியில் மக்கள் இறைத்த பணம் அன்றைக்கே` → `ஆயிரம் ரூபாய்!`.
- scan 68 / printed 59 contains the conclusion and ornamental closing rule.
- scan 69 opens Story 8 `கங்கையின் காதல்`.
- Story 8 text included in Story 7 workspace: **No**.

### Difficult-reading / review layer

High-value source-close readings retained for human review include:

- `அஷ்டமா சித்துபுரி`
- `துடுக் கடக்கும் தாயனே`
- `‘நமப்பார்வதி படே’`
- `பிள்ளையில்ல....அருள் தேவை`
- `செக்கச் செவேன்னு`
- `நாளைக் காலையில் முழுவதும் வந்துவிடும்`
- `மூடாத்மா ஞானத்மாவாக`
- `அழுத்தமான கயிறு`
- `கருவாடு களவு கொடுத்த பாப்பாத்தி`
- `தவறுக என்னை மதிக்காதீர்`
- `தடியன் தானு?`
- `அவசரந் தாங்காத`
- `கொலைகாரனுக்கிவிட்டாயே`

Resolved by enlarged source inspection:

- scan 61: `ஆகட்டும் ஸ்வாமி`
- scan 68: `மாபெரும் மடம்`

Do not change queued readings merely because they look unusual. A source-supported correction must be checked against the complete source span and propagated through every dependent layer.

## Canonical-story / anthology rule

Before each story:

1. check live `stories/` for TOC title, opening heading and documented alternate title;
2. if a canonical story exists, attach the anthology as an additional edition/witness;
3. otherwise create the story workspace only when that story becomes active;
4. preserve anthology scan + printed-page coordinates;
5. create a persistent possible-error queue;
6. use complete-span verification rather than isolated-crop confidence.

## Next exact activity

Process anthology Story **8 — `கங்கையின் காதல்`** only.

Range:

- printed pages: **60–63**
- anthology scans: **69–72**

Boundary checks:

- scan **69** must open `கங்கையின் காதல்`;
- scan **72** must close Story 8;
- scan **73** must be checked as the opening of Story 9 `தாய்மை` before closing the range.

Actions:

1. fetch live `main` and confirm no canonical `கங்கையின் காதல்` workspace already exists;
2. make the 69 / 72 / 73 boundary checks from the controlling scan;
3. create a stable Story 8 workspace only after the canonical-story check;
4. register the 1977 anthology as controlling source;
5. create **4** page records for scans **69–72** / printed pages **60–63**;
6. transcribe directly from source scans and run full-span visual-fidelity review;
7. exhaust difficult readings before using `blocked`; keep unusual-but-legible source forms in `POSSIBLE_ERRORS_FOR_REVIEW.md`;
8. create assembled Tamil, source audit and story README;
9. synchronize anthology inventory, collection README, root README, scan map, HANDOVER and `NEXT_CHAT_PROMPT.md`;
10. **do not begin Story 9 (`தாய்மை`) in the same activity.**

## New-chat readiness

**READY FOR CONTINUATION.**

The durable resume file is `NEXT_CHAT_PROMPT.md`. The controlling anthology PDF must be available for source-dependent work. If live `main` has moved beyond this state, use the newer repository state rather than reverting to this handover.
