# Pass 1 Progress — நாட்டிய கலாராணி

Controlling range: scans **25–46 / printed pages 25–46** — **22 physical pages**.

Workflow: root `BATCH_TRANSCRIPTION_VERIFICATION_WORKFLOW.md` — **Stage A and Stage B are separate durable activities.**

## Current state

- source intake: **PASS**
- page records initialized: **22 / 22**
- direct first-pass transcription: **0 / 22**
- historical-glyph Pass 2: **0 / 22**
- verified pages: **0 / 22**
- unresolved source holds: **0 currently recorded; transcription has not begun**

## Batches

| Batch | Scans / printed pages | Stage A — direct transcription | Stage B — independent glyph/source verification | Final page status |
|---|---|---|---|---|
| P1 | 25–29 | **NEXT** | waits for durable Stage-A commit | not-started |
| P2 | 30–34 | pending | pending | not-started |
| P3 | 35–39 | pending | pending | not-started |
| P4 | 40–44 | pending | pending | not-started |
| P5 | 45–46 | pending | pending | not-started |

## Exact next activity

Run **P1 Stage A only** on scans 25–29:

- direct whole-page visual transcription;
- no systematic 13-family Pass 2 in the same activity;
- no routine crops/enhancements or repeated reopening of already-clear text;
- unresolved readings may remain explicit rather than guessed;
- Stage-A pages remain `needs-review` because independent verification is still pending;
- synchronize Pass-1/current-state controls;
- commit and stop/report.

After that commit, **P1 Stage B on the same scans 25–29 becomes NEXT**. Scan 30 must not begin before P1 Stage B is committed.
