# Pass 1 Progress — நாட்டிய கலாராணி

Controlling range: scans **25–46 / printed pages 25–46** — **22 physical pages**.

Workflow: root `BATCH_TRANSCRIPTION_VERIFICATION_WORKFLOW.md` — Stage A and Stage B are separate durable activities.

## Current state

- source intake: **PASS**
- page records initialized: **22 / 22**
- direct first-pass transcription: **20 / 22** — scans 25–44
- historical-glyph/source Stage B: **15 / 22** — scans 25–39
- verified pages: **15 / 22** — scans 25–39
- `needs-review`: **5 / 22** — scans 40–44; P4 Stage B pending
- not-started: **2 / 22** — scans 45–46
- blocked / unresolved source holds: **0**

## Batches

| Batch | Scans / printed pages | Stage A — direct transcription | Stage B — independent glyph/source verification | Final page status |
|---|---|---|---|---|
| P1 | 25–29 | **COMPLETE — 5/5** | **PASS — 5/5** | `verified` |
| P2 | 30–34 | **COMPLETE — 5/5** | **PASS — 5/5** | `verified` |
| P3 | 35–39 | **COMPLETE — 5/5** | **PASS — 5/5** | `verified` |
| P4 | 40–44 | **COMPLETE — 5/5** | **NEXT** | `needs-review` |
| P5 | 45–46 | pending | pending | not-started |

## P4 Stage-A notes

- scans **40–44** were transcribed directly as whole pages from the attached controlling PDF;
- no OCR, web text or another edition was used as transcription authority;
- the systematic 13-family historical-glyph/source verification was **not** run in Stage A;
- printed ornament separators on scans 40 and 42 are preserved in the page records;
- source-sensitive but legible readings were appended to `POSSIBLE_ERRORS_FOR_REVIEW.md` for the separate Stage-B re-read;
- blocking unreadable locations: **0**.

## Exact next activity

Run **P4 Stage B only** on scans **40–44**:

- independently reopen the same five source pages;
- compare committed Stage-A text against source pixels; do not fully retranscribe;
- explicitly audit `ணா / ணை / ணொ / ணோ / லை / ளை / றா / றொ / றோ / னா / னை / னொ / னோ` plus every P4 source-sensitive queue entry;
- use crops/enhancements only for actual ambiguity;
- record corrections individually; never global-replace;
- promote only fully closed pages to `verified`;
- synchronize verification/current-state controls, commit, and stop/report.

Do not begin scan 45 before P4 Stage B is committed.
