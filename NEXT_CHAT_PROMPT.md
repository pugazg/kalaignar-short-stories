# NEXT CHAT PROMPT — 1976 `நளாயினி` / `நாட்டிய கலாராணி` scans 40–44 — Stage B

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
- direct transcription: **20/22 — scans 25–44**;
- Stage B verified: **15/22 — scans 25–39**;
- `needs-review`: **5/22 — scans 40–44**;
- not-started: **2/22 — scans 45–46**;
- blocked / unresolved blocking locations: **0 / 0**;
- Tamil assembly: not started.

P1, P2 and P3 are fully closed. P4 scans 40–44 have completed Stage A direct transcription only. Their source-sensitive queue is documented in `POSSIBLE_ERRORS_FOR_REVIEW.md`. Scan 45 remains untouched. Story 8 heading remains `மானம்`; do not begin it yet.

## Two-stage workflow

For every physical batch:

**Stage A** — direct transcription → synchronize → commit → stop/report.  
**Stage B** — later separate independent glyph/source verification → synchronize → commit → stop/report.

P4 Stage A is complete. Do **not** repeat it.

## Exact next activity — P4 Stage B ONLY

Process scans **40–44 / printed pages 40–44** only.

- independently reopen all five attached source pages;
- compare committed Stage-A transcription against source pixels; **do not fully retranscribe**;
- explicitly audit `ணா / ணை / ணொ / ணோ / லை / ளை / றா / றொ / றோ / னா / னை / னொ / னோ`;
- independently check every P4 entry in `POSSIBLE_ERRORS_FOR_REVIEW.md`;
- do not create crops/enhancements routinely; use them only where a real character/spacing/punctuation ambiguity remains;
- record every correction individually; never global-replace;
- any unresolved reading keeps the affected page `needs-review`;
- promote only fully closed pages to `verified`;
- synchronize the five page records, page map, glyph gate, progress, review queue, README/audit/handover/current-state controls;
- commit P4 Stage B;
- **stop and report after the commit**.

Do **not** begin scan 45 or Story 8 `மானம்` in this activity.
