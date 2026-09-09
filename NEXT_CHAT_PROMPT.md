# NEXT CHAT PROMPT — 1976 `நளாயினி` / `நாட்டிய கலாராணி` scans 30–34 — Stage B

Continue in `pugazg/kalaignar-short-stories`, branch `main`. **LIVE MAIN IS AUTHORITATIVE.**

## External hold

`வெள்ளிக்கிழமை` remains incomplete; do **not** start `நடுத்தெரு நாராயணி`.

## Controlling source

`TVA_BOK_0065574_நளாயினி_1976.pdf` — **78 scans**, **164,748,566 bytes**, fourth edition 1976, image-only. Source PDF is not committed. SHA-256 remains pending; do not invent one.

The user supplied this exact downloaded PDF. **The attached PDF itself is the sole controlling authority for this collection. Do not query the Tamil Digital Library website or another external source unless the user explicitly requests comparison.**

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
9. `collections/1976-nalayini/indexes/scan-map.md`
10. `stories/naattiya-kalarani/README.md`
11. `stories/naattiya-kalarani/indexes/page-map.md`
12. `stories/naattiya-kalarani/PASS1_PROGRESS.md`
13. `stories/naattiya-kalarani/HISTORICAL_GLYPH_GATE.md`
14. `stories/naattiya-kalarani/POSSIBLE_ERRORS_FOR_REVIEW.md`

## Collection correction

Attached scan **73** directly shows Story 8 heading **`மானம்`**. Earlier `மனம்` was wrong. Do not begin Story 8 yet.

## Durable state — `நாட்டிய கலாராணி`

Physical range: **scans 25–46 / printed 25–46**.

- source boundary / dedup: **PASS / PASS**;
- page records: **22/22**;
- direct transcription: **10/22 — scans 25–34**;
- Stage B verified: **5/22 — scans 25–29**;
- `needs-review`: **5/22 — scans 30–34**;
- blocked / unresolved blocking locations: **0 / 0**;
- Tamil assembly: not started.

P1 scans 25–29 are fully closed. P2 scans 30–34 have completed Stage A direct transcription only. Their source-sensitive queue is documented in `POSSIBLE_ERRORS_FOR_REVIEW.md`. Scan 33 ends mid-quotation at `‘அன்றொரு நாள்`; scan 34 continues it and ends mid-sentence at `மன்னனும் மற்றவரும்`. Scan 35 remains untouched.

## Two-stage workflow

For every physical batch:

**Stage A** — direct transcription → synchronize → commit → stop/report.  
**Stage B** — later separate independent glyph/source verification → synchronize → commit → stop/report.

P2 Stage A is complete. Do **not** repeat it.

## Exact next activity — P2 Stage B ONLY

Process scans **30–34 / printed pages 30–34** only.

- independently reopen all five attached source pages;
- compare committed Stage-A transcription against source pixels; **do not fully retranscribe**;
- explicitly audit `ணா / ணை / ணொ / ணோ / லை / ளை / றா / றொ / றோ / னா / னை / னொ / னோ`;
- independently check every P2 entry in `POSSIBLE_ERRORS_FOR_REVIEW.md`;
- do not create crops/enhancements routinely; use them only where a real character/spacing/punctuation ambiguity remains;
- record every correction individually; never global-replace;
- any unresolved reading keeps the affected page `needs-review`;
- promote only fully closed pages to `verified`;
- synchronize the five page records, page map, glyph gate, progress, review queue, README/audit/handover/current-state controls;
- commit P2 Stage B;
- **stop and report after the commit**.

Do **not** begin scan 35 or Story 8 `மானம்` in this activity.
