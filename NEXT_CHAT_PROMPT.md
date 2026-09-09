# NEXT CHAT PROMPT — 1976 `நளாயினி` / `நாட்டிய கலாராணி` scans 25–29 — Stage B

Continue in `pugazg/kalaignar-short-stories`, branch `main`. **LIVE MAIN IS AUTHORITATIVE.**

## External hold

`வெள்ளிக்கிழமை` remains incomplete; do **not** start `நடுத்தெரு நாராயணி`.

## Controlling source

`TVA_BOK_0065574_நளாயினி_1976.pdf` — **78 scans**, **164,748,566 bytes**, fourth edition 1976, image-only. Source PDF is not committed. SHA-256 remains pending because direct raw-byte checksum access was unavailable; do not invent one.

The user downloaded this exact PDF from the Tamil Digital Library and supplied the downloaded file. **The attached PDF itself is the sole controlling authority for this collection. Do not query the Tamil Digital Library website or another external source unless the user explicitly requests an external comparison.**

## Mandatory startup

Read before source-dependent work:

1. `SHORT_STORY_PROCESSING_GUIDE.md`
2. `COLLECTION_SOURCE_GUIDE.md`
3. `HISTORICAL_TAMIL_GLYPH_TRANSCRIPTION_GUIDE.md`
4. `BATCH_TRANSCRIPTION_VERIFICATION_WORKFLOW.md`
5. root `HANDOVER.md`
6. this prompt
7. `collections/1976-nalayini/README.md`
8. `collections/1976-nalayini/indexes/story-inventory.md`
9. `stories/naattiya-kalarani/README.md`
10. `stories/naattiya-kalarani/SOURCE_INTAKE.md`
11. `stories/naattiya-kalarani/indexes/page-map.md`
12. `stories/naattiya-kalarani/PASS1_PROGRESS.md`
13. `stories/naattiya-kalarani/HISTORICAL_GLYPH_GATE.md`
14. `stories/naattiya-kalarani/POSSIBLE_ERRORS_FOR_REVIEW.md`

## Collection correction

Attached scan **73** directly shows Story 8 heading **`மானம்`**. Earlier controls incorrectly recorded `மனம்`; use `மானம்` from now on. Do not begin it yet.

## Durable state

`நாட்டிய கலாராணி` is a new canonical story, physical range **scans 25–46 / printed 25–46**.

- source boundary: PASS;
- canonical dedup: PASS;
- page records initialized: **22/22**;
- direct transcription: **5/22 — scans 25–29 Stage A COMPLETE**;
- `needs-review`: **5/22**;
- glyph Pass 2: **0/22**;
- verified: **0/22**;
- blocked: **0/22**;
- Tamil assembly: not started.

Stage-A physical facts preserved in the page records:

- scan 25 ends `நட்டுவ`; scan 26 begins `னரும்`;
- scan 27 ends `கவிவாணர்-`; scan 28 independently begins `கவிவாணர்-மதிவாணர்`.

Source-sensitive but legible forms are listed in `stories/naattiya-kalarani/POSSIBLE_ERRORS_FOR_REVIEW.md`. They are review targets, not confirmed errors.

## Two-stage workflow

For each physical batch:

**Stage A** — direct transcription → synchronize → commit → stop/report.  
**Stage B** — separate independent glyph/source verification → synchronize → commit → stop/report.

P1 Stage A is now complete. Do **not** repeat it.

## Exact next activity — Stage B ONLY

Process scans **25–29 / printed pages 25–29** only.

- independently reopen all five attached source pages;
- compare the committed Stage-A transcription against source pixels; **do not fully retranscribe the pages**;
- explicitly audit `ணா / ணை / ணொ / ணோ / லை / ளை / றா / றொ / றோ / னா / னை / னொ / னோ`;
- independently check every entry in `POSSIBLE_ERRORS_FOR_REVIEW.md`;
- **do not create crops/enhancements routinely**; use them only where a real character/spacing/punctuation ambiguity remains after normal/native page inspection;
- record every correction individually; never global-replace;
- any unresolved reading keeps the affected page `needs-review`;
- promote only fully closed pages to `verified`;
- synchronize the five page records, page map, glyph gate, progress, review queue, README/audit/handover/current-state controls;
- commit Stage B;
- **stop and report after the commit**.

Do **not** begin scan 30 in this activity. Do **not** begin Story 8 `மானம்`.
