# NEXT CHAT PROMPT — 1976 `நளாயினி` / `நாட்டிய கலாராணி` scans 35–39 — Stage B

Continue in `pugazg/kalaignar-short-stories`, branch `main`. **LIVE MAIN IS AUTHORITATIVE.**

## External hold

`வெள்ளிக்கிழமை` remains incomplete; do **not** start `நடுத்தெரு நாராயணி`.

## Controlling source

`TVA_BOK_0065574_நளாயினி_1976.pdf` — **78 scans**, **164,748,566 bytes**, fourth edition 1976, image-only. Source PDF is not committed; SHA-256 remains pending. **The attached PDF itself is the sole controlling authority.** Do not query an external source unless explicitly requested.

## Mandatory startup

Read `SHORT_STORY_PROCESSING_GUIDE.md`, `COLLECTION_SOURCE_GUIDE.md`, `HISTORICAL_TAMIL_GLYPH_TRANSCRIPTION_GUIDE.md`, `BATCH_TRANSCRIPTION_VERIFICATION_WORKFLOW.md`, root `HANDOVER.md`, this prompt, collection README/inventory/scan-map, and the active story README/page-map/PASS1/HISTORICAL_GLYPH_GATE/POSSIBLE_ERRORS controls before source-dependent work.

## Durable state — `நாட்டிய கலாராணி`

Physical range: **scans 25–46 / printed 25–46**.

- source boundary / dedup: **PASS / PASS**;
- page records: **22/22**;
- direct transcription: **15/22 — scans 25–39**;
- Stage B verified: **10/22 — scans 25–34**;
- `needs-review`: **5/22 — scans 35–39**;
- blocked / unresolved blocking locations: **0 / 0**;
- Tamil assembly: not started.

P1 scans 25–29 and P2 scans 30–34 are fully closed. P3 scans 35–39 have completed Stage A direct transcription only. Their source-sensitive queue is documented in `POSSIBLE_ERRORS_FOR_REVIEW.md`. Scan 36 ends `காரணம்; அவன்`; scan 37 continues `கண்ட மற்றத் துறவிகள்...`. Scan 40 remains untouched.

## Two-stage workflow

For every physical batch:

**Stage A** — direct transcription → synchronize → commit → stop/report.  
**Stage B** — later separate independent glyph/source verification → synchronize → commit → stop/report.

P3 Stage A is complete. Do **not** repeat it.

## Exact next activity — P3 Stage B ONLY

Process scans **35–39 / printed pages 35–39** only.

- independently reopen all five attached source pages;
- compare committed Stage-A transcription against source pixels; **do not fully retranscribe**;
- explicitly audit `ணா / ணை / ணொ / ணோ / லை / ளை / றா / றொ / றோ / னா / னை / னொ / னோ`;
- independently check every P3 entry in `POSSIBLE_ERRORS_FOR_REVIEW.md`;
- do not create crops/enhancements routinely; use them only where a real character/spacing/punctuation ambiguity remains;
- record every correction individually; never global-replace;
- any unresolved reading keeps the affected page `needs-review`;
- promote only fully closed pages to `verified`;
- synchronize the five page records, page map, glyph gate, progress, review queue, README/audit/handover/current-state controls;
- commit P3 Stage B;
- **stop and report after the commit**.

Do **not** begin scan 40 or Story 8 `மானம்` in this activity.
