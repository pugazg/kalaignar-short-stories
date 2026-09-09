# Pass 1 Progress — நாட்டிய கலாராணி

Controlling range: scans **25–46 / printed pages 25–46** — **22 physical pages**.

Workflow: root `BATCH_TRANSCRIPTION_VERIFICATION_WORKFLOW.md` — Stage A and Stage B are separate durable activities.

## Current state

- source intake: **PASS**
- page records initialized: **22 / 22**
- direct first-pass transcription: **10 / 22**
- historical-glyph/source Stage B: **10 / 22**
- verified pages: **10 / 22** — scans 25–34
- `needs-review`: **0 / 22**
- not-started: **12 / 22**
- blocked / unresolved source holds: **0**

## Batches

| Batch | Scans / printed pages | Stage A — direct transcription | Stage B — independent glyph/source verification | Final page status |
|---|---|---|---|---|
| P1 | 25–29 | **COMPLETE — 5/5** | **PASS — 5/5** | `verified` |
| P2 | 30–34 | **COMPLETE — 5/5** | **PASS — 5/5** | `verified` |
| P3 | 35–39 | **NEXT** | waits for durable P3 Stage-A commit | not-started |
| P4 | 40–44 | pending | pending | not-started |
| P5 | 45–46 | pending | pending | not-started |

## P2 Stage-B result

**PASS — 5/5; 8 source corrections; 0 unresolved.**

1. scan 30 `கோரிலா` → `கோநிலா`;
2. scan 31 `நிற்கவில்லை` → `நிற்க வில்லை`;
3. scan 31 `சீமான்கள்` → `சீமான்களே`;
4. scan 32 `அன்னைகள்` → `அநாதைகள்`;
5. scan 32 `தலநகரிலே` → `தல நகரிலே`;
6. scan 32 `கடுந்தண்டனைக்குக்` → `கடுந் தண்டனைக்குக்`;
7. scan 32 `பணித்தும் பும்` → `பனித்தும்பும்`;
8. scan 34 `தனியாமலிருக்கும்` → `தணியாமலிருக்கும்`.

The mandatory 13 historical families were independently checked on all five pages. No mandatory-family identity correction was required; source-text corrections above were made individually. Families without a positive occurrence were closed as no-candidate. P2 unresolved / blocked: **0 / 0**.

## Exact next activity

Run **P3 Stage A only** on scans **35–39**:

- direct whole-page visual transcription from the attached controlling PDF;
- no systematic 13-family Stage B in the same activity;
- no routine crops/enhancements or repeated reopening of clear text;
- keep scans 35–39 `needs-review` after Stage A;
- synchronize Pass-1/current-state controls;
- commit and stop/report.

Do not begin P3 Stage B in the same activity.
