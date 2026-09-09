# Audit — நாட்டிய கலாராணி

## Source intake gate

**PASS.** Source identity is inherited from the registered 1976 `நளாயினி` collection; physical story range is scans **25–46**, with scan 47 independently opening `விஷம் இனிது`.

## Canonical dedup gate

**PASS.** No existing canonical `நாட்டிய கலாராணி` / documented alternate-title match was found at activation.

## P1 transcription / verification gate — scans 25–29

**PASS / CLOSED.** Stage A direct source transcription **5/5**; independent Stage B **5/5**; verified **5/5**; unresolved / blocked **0/0**.

P1 Stage-B corrections: scan 26 `இன்பபுரிக்கு` → `இன்ப புரிக்கு`; scan 28 `துடிக்கிட்ட` → `திடுக்கிட்ட`; scan 29 `ராஜ்ய விஷயங்களைக்` → `ராஜ்ய விஷயங்களை`. All 13 mandatory families were checked and P1 has zero unresolved candidates.

## P2 transcription gate — scans 30–34

**STAGE A COMPLETE / STAGE B PENDING.**

- direct whole-page source transcription: **5/5**;
- status after Stage A: **5/5 `needs-review`**;
- systematic historical-glyph/source Stage B: **not run**;
- blocking unreadable locations: **0**;
- no OCR, web text or another edition was used as transcription authority.

Physical-source facts retained:

- scan 33 ends mid-quotation at `‘அன்றொரு நாள்`; scan 34 continues it;
- scan 34 ends mid-sentence at `மன்னனும் மற்றவரும்`; scan 35 was not touched;
- source-sensitive readings including `கோரிலா`, `திருப்பினேன்`, `எண்ண வில்லை`, `ஐஸ்வர்ய முள்ளவர்கள்`, `விலைபோகும்`, `பணித்தும்` / `பும்`, and `சீரங் படைத்தவர்கள்` are queued for independent Stage B rather than silently normalized.

## Current work-level state

- page records: **22/22 initialized**;
- direct transcription: **10/22**;
- Stage B verified: **5/22**;
- `needs-review`: **5/22**;
- not-started: **12/22**;
- blocked: **0**;
- Tamil assembly: not started.

## Exact next gate

**P2 Stage B only — scans 30–34.** Independently compare the committed Stage-A text to the controlling source, run the 13-family/source-sensitive audit, synchronize, commit, and stop/report. Scan 35 must remain untouched until that commit.
