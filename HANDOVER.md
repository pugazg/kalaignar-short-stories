# HANDOVER — Kalaignar Short Stories Archive

## Repository

- Repository: `pugazg/kalaignar-short-stories`
- Branch: `main`
- Story workflow: `SHORT_STORY_PROCESSING_GUIDE.md`
- Anthology workflow: `COLLECTION_SOURCE_GUIDE.md`
- Source PDFs are **not** committed to GitHub.

## Completed canonical story — கிழவன் கனவு

`stories/kizhavan-kanavu/` remains source-complete.

- story scans: **16 / 16 verified**
- story blocks: **0**
- English: **complete / source-complete / release-ready**
- manual human recheck queue: `stories/kizhavan-kanavu/POSSIBLE_ERRORS_FOR_REVIEW.md`

Important retained rules/results:

- scan 15 full-span correction includes `புத்தமுதம் தின்று கொண்டிருந்த` and the complete temple-history sentence;
- scan 17: `பார்வதியை அணைத்தபடி பரமன்`;
- scan 21: `இந்த நினைவு அந்த துணைவர்கள் உள்ளத்தை உருக்கிவார்த்தது.`;
- scan 22 conclusion ends `வரப்போகும் திராவிடத்தின் அழியாத சித்திரம் ; அந்தக் கிழவன் கனவு.`;
- English uses **Periyar EV Ramasamy** for `ராமசாமிப்பெரியார்`;
- scan 13 archival `வைத்திருந்தான்` remains distinct from publisher errata `வைத்திருந்தாள்`.

Do not reopen these readings without stronger source evidence. Human review items are possible errors, not automatic corrections.

## Active collection source — 1977 anthology

Collection workspace:

`collections/1977-kalaignar-karunanidhiyin-sirukathaigal/`

Source:

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
- source PDF in repository: **No**

Anthology registration:

- contents inventory: **37 / 37**
- start-scan visual checks: **37 / 37**
- story-block relation: **scan = printed page + 9**
- Tamil source processing complete: **1 / 37**
- stories not yet transcribed: **36 / 37**

Source-title differences to preserve:

1. TOC `புரட்சிப்படம்` — opening `புரட்சிப் படம்`
2. TOC `சித்தார்த்தன்` — opening `சித்தார்த்தன் சிலை`

## Anthology Story 1 — புகழேந்தி — COMPLETE TAMIL SOURCE PASS

Canonical workspace:

`stories/pugazhendhi/`

Range:

- printed pages: **1–6**
- anthology scans: **10–15**

Files created:

- `stories/pugazhendhi/README.md`
- `stories/pugazhendhi/metadata/source.md`
- `stories/pugazhendhi/indexes/page-map.md`
- `stories/pugazhendhi/pages/0001.md`
- `stories/pugazhendhi/pages/0002.md`
- `stories/pugazhendhi/pages/0003.md`
- `stories/pugazhendhi/pages/0004.md`
- `stories/pugazhendhi/pages/0005.md`
- `stories/pugazhendhi/pages/0006.md`
- `stories/pugazhendhi/sections/pugazhendhi.md`
- `stories/pugazhendhi/audit.md`
- `stories/pugazhendhi/POSSIBLE_ERRORS_FOR_REVIEW.md`

Final current source state:

- page records: **6 / 6**
- `verified`: **6 / 6**
- `needs-review`: **0**
- `blocked`: **0**
- explicit missing source text: **0**
- Tamil assembly: complete
- Tamil source audit: **PASS**
- English translation: **not started**

The native embedded scan images are **3146 × 4826**. All six pages were visually inspected from native images and difficult spans were enlarged where needed.

### Verified physical joins

1. printed 1→2: `அவனது பெயர் கூறவே` → `மக்கள் தயங்குவர்—...`
2. printed 3→4: `“உங்கள் இலட்சியம்` → `கைகூடும் வரையில்...`
3. printed 5→6: `திருமணமும்` → `வேண்டார்!”`

### Human possible-error queue

`stories/pugazhendhi/POSSIBLE_ERRORS_FOR_REVIEW.md` persists unusual/easily misread readings for later review. An entry there is **not a confirmed error** and does not itself downgrade the verified page.

High-value rechecks include:

- `பாராட்டுப் படித்தது`
- `அவனோர் பிடேல்டோ!`
- `மணக்கும் அவன் நெஞ்சம்.`
- `புகழ்தரும் தீவலி`
- `தத்தரூபமாகச்`
- `மாட்டானும்!`
- `வயித்துக்கிடக்கிறது`
- `காதற் கண்கள்`
- `கால்ப் பணிவிடைகள்`
- `ஏறெடுத்தும் பாராமல்`

Do not change these merely because they look unusual. A correction must be checked against the full native source span and then propagated to page record, assembly, audit, inventory, README and this handover.

## Canonical-story / anthology rule

An anthology is a source container, not one canonical story.

Before each story:

1. check live `stories/` for TOC title, opening heading and alternate title;
2. if canonical story exists, attach anthology as additional edition/witness;
3. otherwise create the story workspace only when active;
4. do not create empty placeholders for all 37 stories;
5. preserve anthology scan + printed-page coordinates;
6. create `POSSIBLE_ERRORS_FOR_REVIEW.md` for unusual readings;
7. use complete-span verification rather than isolated-crop confidence.

## Next exact activity

Process anthology Story **2 — `நளாயினி`** only.

Range:

- printed pages: **7–14**
- anthology scans: **16–23**

Actions:

1. fetch live `main` and confirm no canonical `நளாயினி` workspace already exists;
2. visually confirm scan 16 opening and scan 23 story ending / scan 24 next-story boundary;
3. create `stories/nalayini/` using this 1977 anthology as controlling source;
4. create 8 page records for scans 16–23 / printed pages 7–14;
5. transcribe directly from native scan images;
6. run full-span visual fidelity review and page-boundary checks;
7. create assembled Tamil, audit and `POSSIBLE_ERRORS_FOR_REVIEW.md`;
8. synchronize anthology inventory, collection README, root README and HANDOVER;
9. **do not begin Story 3 (`சபலம்`) in the same activity.**
