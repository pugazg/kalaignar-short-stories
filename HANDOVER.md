# HANDOVER — Kalaignar Short Stories Archive

## Repository

- Repository: `pugazg/kalaignar-short-stories`
- Branch: `main`
- Story workflow: `SHORT_STORY_PROCESSING_GUIDE.md`
- Anthology workflow: `COLLECTION_SOURCE_GUIDE.md`
- Source PDFs are **not** committed to GitHub.

## Permanent source rules

- **Controlling scan first.** Do not silently modernize spelling, grammar, punctuation, names, sandhi or source anomalies.
- **No stones should be left unturned.** Difficult story readings must receive full-span visual escalation before terminal `blocked` status.
- **Processed-crop confidence is not source confidence.** Verify the complete phrase/clause/sentence against the source span.
- `POSSIBLE_ERRORS_FOR_REVIEW.md` is a human-review queue. Its entries are possible errors, not automatic corrections.
- If a later user correction is source-supported, reopen the affected verified page and resynchronize page record, Tamil assembly, audit, story README, anthology inventory, collection README, root README and this handover.

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
- Tamil source processing complete: **3 / 37**
- stories not yet transcribed: **34 / 37**
- English translation started from anthology: **0 / 37**

Edition-level title differences to preserve:

1. TOC `புரட்சிப்படம்` — opening `புரட்சிப் படம்`
2. TOC `சித்தார்த்தன்` — opening `சித்தார்த்தன் சிலை`

## Anthology Story 1 — புகழேந்தி — COMPLETE TAMIL SOURCE PASS

Canonical workspace: `stories/pugazhendhi/`

- printed pages: **1–6**
- anthology scans: **10–15**
- page records: **6 / 6 verified**
- `needs-review`: **0**
- `blocked`: **0**
- unresolved story text: **0**
- assembled Tamil: complete
- audit: **PASS**
- human review queue: `stories/pugazhendhi/POSSIBLE_ERRORS_FOR_REVIEW.md`
- English: not started

Verified physical joins:

1. printed 1→2: `அவனது பெயர் கூறவே` → `மக்கள் தயங்குவர்—...`
2. printed 3→4: `“உங்கள் இலட்சியம்` → `கைகூடும் வரையில்...`
3. printed 5→6: `திருமணமும்` → `வேண்டார்!”`

## Anthology Story 2 — நளாயினி — COMPLETE TAMIL SOURCE PASS

Canonical workspace: `stories/nalayini/`

- printed pages: **7–14**
- anthology scans: **16–23**
- page records: **8 / 8 verified**
- `needs-review`: **0**
- `blocked`: **0**
- unresolved story text: **0**
- assembled Tamil: complete
- source audit: **PASS**
- human review queue: `stories/nalayini/POSSIBLE_ERRORS_FOR_REVIEW.md`
- English: not started

Preserve the source's two visible husband-name forms:

- scan 17: `மெளத் கல்யர்`
- scan 18: `மெளத்கல்யர்`

Printed page 14 ends the narrative with `அந்த ஆசிரமத்தில் இன்பகீதம் ஆரம்பமாயிற்று!`; the subsequent `குறிப்பு :—புராணக் கதைப்படி நளாயினிதான் திரெளபதையாகப் பிறந்திருக்கிறாளாம்.` remains a separate source layer.

## Anthology Story 3 — சபலம் — COMPLETE TAMIL SOURCE PASS

Canonical workspace:

`stories/sabalam/`

Range:

- printed pages: **15–21**
- anthology scans: **24–30**

Files/control layers:

- `stories/sabalam/README.md`
- `stories/sabalam/metadata/source.md`
- `stories/sabalam/indexes/page-map.md`
- `stories/sabalam/pages/0024-sabalam-01.md` through `0030-sabalam-07.md`
- `stories/sabalam/sections/sabalam.md`
- `stories/sabalam/audit.md`
- `stories/sabalam/POSSIBLE_ERRORS_FOR_REVIEW.md`

Final current source state:

- page records: **7 / 7**
- `verified`: **7 / 7**
- `needs-review`: **0**
- `blocked`: **0**
- explicit missing/unresolved story text: **0**
- Tamil assembly: complete
- source audit: **PASS**
- English translation: **not started**

### Verified physical joins

1. printed 15→16: `கழுத்தில் நிற்கச் சக்தி` → `யிழந்து தொங்கும் தலையை...`
2. printed 16→17: `“மூர்த்தி” என்று கணீரென்று உச்சரித்தது` → `குழந்தை.`
3. printed 17→18: `அந்தப் பெட்டியில்` → `இருந்தவர்கள் தூக்க மயக்கத்தில்...`
4. printed 19→20: `ஜன்னல்` → `வழியே வீசியெறிந்தான்.`
5. printed 20→21: the station/child exchange continues into the concluding page.

Scan **31 / printed page 22** was visually checked and begins the next story **`ஆட்டக்காவடி`**. No Story 4 text is included in `சபலம்`.

### Human possible-error queue

`stories/sabalam/POSSIBLE_ERRORS_FOR_REVIEW.md`

High-value rechecks include:

- `பிரத்யட்சமாவது போல`
- `இமைகளேப் பிடித்திழுத்து`
- `ஒருவரோ டொருவர்`
- `முக்கால் பாகந்தான்`
- `கணீரென்று`
- `ஜாடையாகப்`
- `நடசத்திரத்துக்குக்`
- `கையுங்களவுமாகப்`
- `ஊற்றுவதாகயிருந்தது`
- `அந்தப் பசலை`
- `கன்னக் கதுப்பை`
- `சபலம் பிடித்த மைனர்`
- `நாலா புறமிருந்தும்`

Do not change these merely because they look unusual. A source-supported correction must be checked against the complete source span and then propagated through every dependent layer.

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

Process anthology Story **4 — `ஆட்டக்காவடி`** only.

Range:

- printed pages: **22–29**
- anthology scans: **31–38**

Actions:

1. fetch live `main` and confirm no canonical `ஆட்டக்காவடி` workspace already exists;
2. visually confirm scan **31** opening and scan **38** ending / scan **39** next-story (`குப்பைத்தொட்டி`) boundary;
3. create `stories/aattakkavadi/` or another stable slug only after source identity check;
4. register the 1977 anthology as controlling source;
5. create **8** page records for scans **31–38** / printed pages **22–29**;
6. transcribe directly from source scans and run full-span visual fidelity review;
7. resolve difficult readings as far as defensibly possible; keep unusual-but-legible forms in `POSSIBLE_ERRORS_FOR_REVIEW.md`;
8. create assembled Tamil, source audit and story README;
9. synchronize anthology inventory, collection README, root README and HANDOVER;
10. **do not begin Story 5 (`குப்பைத்தொட்டி`) in the same activity.**
