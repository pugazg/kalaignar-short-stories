# Pass 1 Progress — நாட்டிய கலாராணி

Controlling range: scans **25–46 / printed pages 25–46** — **22 physical pages**.

Workflow: root `BATCH_TRANSCRIPTION_VERIFICATION_WORKFLOW.md` — Stage A and Stage B are separate durable activities.

## Current state

- source intake: **PASS**
- page records initialized: **22 / 22**
- direct first-pass transcription: **15 / 22** — scans 25–39
- historical-glyph/source Stage B: **10 / 22** — scans 25–34
- verified pages: **10 / 22** — scans 25–34
- `needs-review`: **5 / 22** — scans 35–39; P3 Stage B pending
- not-started: **7 / 22** — scans 40–46
- blocked / unresolved source holds: **0**

## Batches

| Batch | Scans / printed pages | Stage A — direct transcription | Stage B — independent glyph/source verification | Final page status |
|---|---|---|---|---|
| P1 | 25–29 | **COMPLETE — 5/5** | **PASS — 5/5** | `verified` |
| P2 | 30–34 | **COMPLETE — 5/5** | **PASS — 5/5** | `verified` |
| P3 | 35–39 | **COMPLETE — 5/5** | **NEXT** | `needs-review` |
| P4 | 40–44 | pending | pending | not-started |
| P5 | 45–46 | pending | pending | not-started |

## Closed prior batches

P1 closed with **3 corrections / 0 unresolved**. P2 closed with **8 corrections / 0 unresolved**. Exact correction history remains in `HISTORICAL_GLYPH_GATE.md` and `POSSIBLE_ERRORS_FOR_REVIEW.md`.

## P3 Stage-A notes

- scans **35–39** were transcribed directly as whole pages from the attached controlling PDF;
- no OCR, web text or another edition was used as transcription authority;
- the systematic 13-family historical-glyph/source verification was **not** run in Stage A;
- scan 36 ends mid-sentence at `காரணம்; அவன்`; scan 37 begins `கண்ட மற்றத் துறவிகள்...`;
- a printed two-ornament separator on scan 37 is preserved;
- source-sensitive but legible readings were appended to `POSSIBLE_ERRORS_FOR_REVIEW.md` for the separate Stage-B re-read;
- blocking unreadable locations: **0**.

## Exact next activity

Run **P3 Stage B only** on scans **35–39**:

- independently reopen the same five source pages;
- compare the committed Stage-A text against source pixels; do not fully retranscribe;
- explicitly audit `ணா / ணை / ணொ / ணோ / லை / ளை / றா / றொ / றோ / னா / னை / னொ / னோ` plus every P3 source-sensitive queue entry;
- use crops/enhancements only for actual ambiguity;
- record corrections individually; never global-replace;
- promote only fully closed pages to `verified`;
- synchronize verification/current-state controls, commit, and stop/report.

Do not begin scan 40 before P3 Stage B is committed.
