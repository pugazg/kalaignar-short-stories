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

## Active source — 1977 anthology

Collection workspace:

`collections/1977-kalaignar-karunanidhiyin-sirukathaigal/`

Source:

- filename: `TVA_BOK_0064142_கலைஞர்_கருணாநிதியின்_சிறுகதைகள்.pdf`
- SHA-256: `853032661482eaccb26c083a38d7aa75c081362d33c963c63e37d088bf20acb3`
- file size: **268,486,609 bytes**
- actual PDF scans: **260**
- printed title: **கலைஞர் கருணாநிதியின் சிறுகதைகள்**
- author line: **கலைஞர் மு. கருணாநிதி**
- publisher: **தமிழ்க்கனி பதிப்பகம், சென்னை-28**
- edition: **முதல் பதிப்பு: 1977**
- printed story pagination: **1–250**
- story block scans: **10–259**
- back cover: scan **260**
- source PDF in repository: **No**

## Anthology registration completed

Files created:

- `collections/1977-kalaignar-karunanidhiyin-sirukathaigal/README.md`
- `collections/1977-kalaignar-karunanidhiyin-sirukathaigal/metadata/source.md`
- `collections/1977-kalaignar-karunanidhiyin-sirukathaigal/indexes/story-inventory.md`
- `collections/1977-kalaignar-karunanidhiyin-sirukathaigal/indexes/scan-map.md`
- `COLLECTION_SOURCE_GUIDE.md`

Registration state:

- printed contents transcribed: **37 / 37 stories**
- printed ranges calculated: **37 / 37**
- PDF scan ranges calculated: **37 / 37**
- all 37 calculated start scans visually checked against actual opening headings: **complete**
- per-story transcription: **0 / 37 started**

Story-block pagination relation:

**scan page = printed page + 9**

## Source-title differences already found

Preserve both forms:

1. TOC `புரட்சிப்படம்` — story-opening heading `புரட்சிப் படம்`
2. TOC `சித்தார்த்தன்` — story-opening heading `சித்தார்த்தன் சிலை`

Do not silently normalize these.

## Canonical-story / anthology rule

An anthology is a source container, not one canonical story.

Before creating each story workspace:

1. check `stories/` for the TOC title, opening heading and known alternate title;
2. if a canonical story already exists, register this anthology as an additional edition/witness;
3. if none exists, create `stories/<slug>/` only when that story becomes active;
4. do not create 37 empty placeholder folders;
5. preserve anthology scan + printed-page coordinates in story page records;
6. use `POSSIBLE_ERRORS_FOR_REVIEW.md` for suspicious readings.

At registration time the only existing story folder is `kizhavan-kanavu`; `கிழவன் கனவு` does not occur in the anthology contents, so the 37 inventory entries are currently new processing candidates.

## Next exact activity

Process anthology Story **1 — `புகழேந்தி`**.

Range:

- printed pages: **1–6**
- source scans: **10–15**

Actions:

1. confirm no existing canonical `புகழேந்தி` workspace;
2. create `stories/pugazhendhi/` (or another stable slug only after confirming heading/source identity);
3. register the 1977 anthology as its controlling source with exact scan range;
4. create six page records for scans 10–15 / printed pages 1–6;
5. transcribe from the scan page by page;
6. run direct visual + full-span fidelity verification;
7. create `POSSIBLE_ERRORS_FOR_REVIEW.md`;
8. do not begin Story 2 until Story 1's Tamil source audit is complete.
