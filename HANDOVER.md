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
- `POSSIBLE_ERRORS_FOR_REVIEW.md` is a human-review queue. Its entries are possible errors, not automatic corrections.
- If a later user correction is source-supported, reopen the affected verified page and resynchronize page record, Tamil assembly, audit, story README, anthology inventory, collection README, root README, scan map, this handover, and `NEXT_CHAT_PROMPT.md` when the next activity changes.

## Cross-chat restart rules

When continuing in a new chat window:

1. **fetch live GitHub `main` first and treat it as authoritative**; never assume the checkpoint in a pasted prompt is still HEAD;
2. read completely before source-dependent writes:
   - `SHORT_STORY_PROCESSING_GUIDE.md`
   - `COLLECTION_SOURCE_GUIDE.md`
   - `HANDOVER.md`
   - `NEXT_CHAT_PROMPT.md`
   - `collections/1977-kalaignar-karunanidhiyin-sirukathaigal/README.md`
   - `collections/1977-kalaignar-karunanidhiyin-sirukathaigal/indexes/story-inventory.md`
   - `collections/1977-kalaignar-karunanidhiyin-sirukathaigal/indexes/scan-map.md`;
3. inspect the latest completed story workspace (`stories/kuppai-thotti/`) as the immediate structural reference;
4. do not redo completed stories/pages unless a user correction, stronger scan evidence, or live-repository inconsistency requires reopening them;
5. the controlling anthology PDF must be available to the new chat/tool context before transcription or visual verification. Do not reconstruct source text from prior-chat memory;
6. when the user says **“Proceed with next activity”**, execute the exact activity in the `Next exact activity` section without routine clarification;
7. process **one anthology story at a time** and do not begin the following story in the same activity;
8. after completing the active story, synchronize story workspace + anthology inventory + collection README + root README + scan map + this handover + `NEXT_CHAT_PROMPT.md`.

## Completed independent story — கிழவன் கனவு

`stories/kizhavan-kanavu/` remains source-complete.

- story scans: **16 / 16 verified**
- story blocks: **0**
- English: **complete / source-complete / release-ready**
- manual recheck queue: `stories/kizhavan-kanavu/POSSIBLE_ERRORS_FOR_REVIEW.md`

Important retained source corrections include:

- scan 15: `புத்தமுதம் தின்று கொண்டிருந்த` and complete temple-history sentence;
- scan 17: `பார்வதியை அணைத்தபடி பரமன்`;
- scan 21: `இந்த நினைவு அந்த துணைவர்கள் உள்ளத்தை உருக்கிவார்த்தது.`;
- scan 22 ending: `வரப்போகும் திராவிடத்தின் அழியாத சித்திரம் ; அந்தக் கிழவன் கனவு.`;
- English display name: **Periyar EV Ramasamy**;
- scan 13 archival `வைத்திருந்தான்` remains distinct from publisher errata `வைத்திருந்தாள்`.

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

Anthology registration / processing:

- contents inventory: **37 / 37**
- story-start visual checks: **37 / 37**
- Tamil source processing complete: **5 / 37**
- stories not yet transcribed: **32 / 37**
- English translation started from anthology: **0 / 37**

Edition-level title differences to preserve:

1. TOC `புரட்சிப்படம்` — opening `புரட்சிப் படம்`
2. TOC `சித்தார்த்தன்` — opening `சித்தார்த்தன் சிலை`

## Anthology Stories 1–4 — COMPLETE TAMIL SOURCE PASSES

1. `புகழேந்தி` — `stories/pugazhendhi/` — printed **1–6**, scans **10–15**, **6/6 verified**, 0 blocked, audit PASS.
2. `நளாயினி` — `stories/nalayini/` — printed **7–14**, scans **16–23**, **8/8 verified**, 0 blocked, audit PASS.
3. `சபலம்` — `stories/sabalam/` — printed **15–21**, scans **24–30**, **7/7 verified**, 0 blocked, audit PASS.
4. `ஆட்டக்காவடி` — `stories/aattakkavadi/` — printed **22–29**, scans **31–38**, **8/8 verified**, 0 blocked, 0 unresolved story text, audit PASS.

All four have persistent `POSSIBLE_ERRORS_FOR_REVIEW.md` queues. English translation has not been started for these anthology stories.

## Anthology Story 5 — குப்பைத்தொட்டி — COMPLETE TAMIL SOURCE PASS

Canonical workspace:

`stories/kuppai-thotti/`

Range:

- printed pages: **30–37**
- anthology scans: **39–46**

Files/control layers:

- `stories/kuppai-thotti/README.md`
- `stories/kuppai-thotti/metadata/source.md`
- `stories/kuppai-thotti/indexes/page-map.md`
- `stories/kuppai-thotti/pages/0039-kuppai-thotti-01.md` through `0046-kuppai-thotti-08.md`
- `stories/kuppai-thotti/sections/kuppai-thotti.md`
- `stories/kuppai-thotti/audit.md`
- `stories/kuppai-thotti/POSSIBLE_ERRORS_FOR_REVIEW.md`

Final current source state:

- page records: **8 / 8**
- `verified`: **8 / 8**
- `needs-review`: **0**
- `blocked`: **0**
- explicit missing/unresolved story text: **0**
- Tamil assembly: complete
- source audit: **PASS**
- English translation: **not started**

### Verified physical joins

1. printed 30→31: `...நட்சத்திரங்கள் மேனகை,` → `ரம்பை, ஊர்வசி, திலோத்தமை ஆகியோர்.`
2. printed 32→33: `அதிலிருந்து நேரம்` → `இரவாகத்தானிருக்குமென முடிவுகட்டி விடலாம்.`
3. printed 33→34: `...குப்பைத் தொட்டிவந்து சேரக்` → `கூடாதா?`
4. printed 34→35: `...இதற்குக் கைமாறாக முன்` → `கூட்டியே மூன்றூறு ரூபாய்...`
5. printed 35→36: `நான் தூங்குவதுபோல்` → `நடித்து நடப்பவைகளைக்...`
6. printed 36→37: `இந்நாட்டு மன்னர்களிலே ஒருவனல்லவா,` → `எந்தக் குப்பைத்தொட்டி மறைவுக்குப் போனேனோ;...`

Scan **47 / printed page 38** was visually checked and begins the next story **`சந்தனக்கிண்ணம்`**. No Story 6 text is included in `குப்பைத்தொட்டி`.

### Human possible-error queue

`stories/kuppai-thotti/POSSIBLE_ERRORS_FOR_REVIEW.md`

High-value rechecks include:

- `போதுதானு`
- `மனமனவென்று`
- `காரணகரமான`
- `உணர்ச்சி என்னை வளர்த்துக்கொண்டது`
- `சபரகூட மஞ்சமாகி`
- `குப்பைத்தொட்டி எங்கேயிருந்தால் என்ன வென்று!`
- `மூன்றூறு`
- `அவசரியப் புத்தி`
- `தூராற்றம்`
- `வீதிப்பக்கம் வந்து உண்மைதான்`
- `போனேனோ`
- `சந்தித்தாகிவிட்டது`
- `வயிறாச் சோறின்றி`

`பல்லைக்காட்டி`, `சற்று மறைந்து கொள்கிறாள்`, and final `ஏன் ஓடுகிறாள்?` were resolved by enlarged source review and are recorded as resolved/rechecked items where appropriate.

Do not change queued readings merely because they look unusual. A source-supported correction must be checked against the complete source span and propagated through every dependent layer.

## Canonical-story / anthology rule

An anthology is a source container, not one canonical story.

Before each story:

1. check live `stories/` for TOC title, opening heading and known alternate title;
2. if a canonical story exists, attach the anthology as an additional edition/witness;
3. otherwise create the story workspace only when that story becomes active;
4. do not create 37 empty placeholders;
5. preserve anthology scan + printed-page coordinates;
6. create a persistent possible-error queue;
7. use complete-span verification rather than isolated-crop confidence.

## Next exact activity

Process anthology Story **6 — `சந்தனக்கிண்ணம்`** only.

Range:

- printed pages: **38–47**
- anthology scans: **47–56**

Boundary checks:

- scan **47** must open `சந்தனக்கிண்ணம்`;
- scan **56** must close Story 6;
- scan **57** must be checked as the opening of Story 7 `சங்கிலிச்சாமி` before closing the range.

Actions:

1. fetch live `main` and confirm no canonical `சந்தனக்கிண்ணம்` workspace already exists;
2. make the boundary checks above from the controlling scan;
3. create `stories/santhana-kinnam/` or another stable slug only after source identity check;
4. register the 1977 anthology as controlling source;
5. create **10** page records for scans **47–56** / printed pages **38–47**;
6. transcribe directly from source scans and run full-span visual fidelity review;
7. resolve difficult readings as far as defensibly possible; keep unusual-but-legible forms in `POSSIBLE_ERRORS_FOR_REVIEW.md`;
8. create assembled Tamil, source audit and story README;
9. synchronize anthology inventory, collection README, root README, scan map, HANDOVER, and `NEXT_CHAT_PROMPT.md`;
10. **do not begin Story 7 (`சங்கிலிச்சாமி`) in the same activity.**

## New-chat readiness

**READY FOR CONTINUATION.**

The durable resume file is `NEXT_CHAT_PROMPT.md`. The controlling anthology PDF must be available for source-dependent work. If live `main` has moved beyond this state, use the newer repository state rather than reverting to this handover.
