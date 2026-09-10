# Pass 1 Progress — நாட்டிய கலாராணி

Controlling range: scans **25–46 / printed pages 25–46** — **22 physical pages**.

Workflow: root `BATCH_TRANSCRIPTION_VERIFICATION_WORKFLOW.md` — Stage A and Stage B are separate durable activities.

## Current state

- source intake: **PASS**
- page records initialized: **22 / 22**
- direct first-pass transcription: **22 / 22 — COMPLETE — scans 25–46**
- historical-glyph/source Stage B: **20 / 22 — scans 25–44**
- verified pages: **20 / 22 — scans 25–44**
- `needs-review`: **2 / 22 — scans 45–46; P5 Stage B pending**
- not-started: **0 / 22**
- blocked / unresolved source holds: **0**

## Batches

| Batch | Scans / printed pages | Stage A — direct transcription | Stage B — independent glyph/source verification | Final page status |
|---|---|---|---|---|
| P1 | 25–29 | **COMPLETE — 5/5** | **PASS — 5/5** | `verified` |
| P2 | 30–34 | **COMPLETE — 5/5** | **PASS — 5/5** | `verified` |
| P3 | 35–39 | **COMPLETE — 5/5** | **PASS — 5/5** | `verified` |
| P4 | 40–44 | **COMPLETE — 5/5** | **PASS — 5/5** | `verified` |
| P5 | 45–46 | **COMPLETE — 2/2** | **NEXT** | `needs-review` |

## Closed Stage-B history

- P1: **3 corrections / 0 unresolved**.
- P2: **8 corrections / 0 unresolved**.
- P3: **4 corrections / 0 unresolved**.
- P4: **4 corrections / 0 unresolved**.

## P5 Stage-A notes

- scans **45–46** were transcribed directly as whole pages from the attached controlling PDF;
- this completes direct transcription for the full physical story range **25–46**;
- no OCR, web text or another edition was used as transcription authority;
- systematic 13-family historical-glyph/source verification was **not** run in Stage A;
- scan 46 includes the closing `வணக்கம், / இன்பசாகரன்.` block and two printed closing ornaments;
- source-sensitive but legible readings were appended to `POSSIBLE_ERRORS_FOR_REVIEW.md`;
- blocking unreadable locations: **0**.

## Exact next activity

Run **P5 Stage B only** on scans **45–46**: independently re-open both pages, compare the committed Stage-A text to source pixels, audit all 13 mandatory historical families plus every P5 queue entry, correct only source-proven mismatches, synchronize verification controls, commit, and stop/report.

Do not begin Story 8 `மானம்` in the same activity.
