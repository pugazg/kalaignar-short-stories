# Pass 1 Progress — நாட்டிய கலாராணி

Controlling range: scans **25–46 / printed pages 25–46** — **22 physical pages**.

Workflow: root `BATCH_TRANSCRIPTION_VERIFICATION_WORKFLOW.md` — Stage A and Stage B are separate durable activities.

## Current state

- source intake: **PASS**
- page records initialized: **22 / 22**
- direct first-pass transcription: **10 / 22**
- historical-glyph/source Stage B: **5 / 22**
- verified pages: **5 / 22** — scans 25–29
- `needs-review`: **5 / 22** — scans 30–34; P2 Stage B pending
- not-started: **12 / 22**
- blocked / unresolved source holds: **0**

## Batches

| Batch | Scans / printed pages | Stage A — direct transcription | Stage B — independent glyph/source verification | Final page status |
|---|---|---|---|---|
| P1 | 25–29 | **COMPLETE — 5/5** | **PASS — 5/5** | `verified` |
| P2 | 30–34 | **COMPLETE — 5/5** | **NEXT** | `needs-review` |
| P3 | 35–39 | pending | pending | not-started |
| P4 | 40–44 | pending | pending | not-started |
| P5 | 45–46 | pending | pending | not-started |

## P1 Stage-B corrections

1. scan 26: `இன்பபுரிக்கு` → `இன்ப புரிக்கு` — source spacing;
2. scan 28: `துடிக்கிட்ட` → `திடுக்கிட்ட` — direct source re-read;
3. scan 29: `ராஜ்ய விஷயங்களைக்` → `ராஜ்ய விஷயங்களை` — direct source re-read; `ளை`-sensitive cluster.

## P2 Stage-A notes

- scans **30–34** were directly transcribed from the attached controlling PDF as whole pages;
- no OCR, web text or another edition was used as transcription authority;
- systematic 13-family historical-glyph verification was **not** run in Stage A;
- scan 33 ends mid-quotation at `‘அன்றொரு நாள்`; scan 34 continues that quotation and itself ends mid-sentence before scan 35;
- source-sensitive but readable forms are appended to `POSSIBLE_ERRORS_FOR_REVIEW.md` for the separate P2 Stage-B re-read;
- blocking unreadable locations: **0**.

## Exact next activity

Run **P2 Stage B only** on scans **30–34**:

- independently reopen the same five source pages;
- compare committed Stage-A text against the source; do not fully retranscribe;
- explicitly audit `ணா / ணை / ணொ / ணோ / லை / ளை / றா / றொ / றோ / னா / னை / னொ / னோ` plus the P2 source-sensitive queue;
- use crops/enhancements only for actual ambiguity;
- record corrections individually; never global-replace;
- promote only fully closed pages to `verified`;
- synchronize verification/current-state controls, commit, and stop/report.

Do not begin scan 35 before P2 Stage B is committed.
