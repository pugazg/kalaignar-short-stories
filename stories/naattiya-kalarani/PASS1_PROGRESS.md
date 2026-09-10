# Pass 1 Progress — நாட்டிய கலாராணி

Controlling range: scans **25–46 / printed pages 25–46** — **22 physical pages**.

Workflow: root `BATCH_TRANSCRIPTION_VERIFICATION_WORKFLOW.md` — Stage A and Stage B are separate durable activities.

## Current state

- source intake: **PASS**
- page records initialized: **22 / 22**
- direct first-pass transcription: **20 / 22** — scans 25–44
- historical-glyph/source Stage B: **20 / 22** — scans 25–44
- verified pages: **20 / 22** — scans 25–44
- `needs-review`: **0 / 22**
- not-started: **2 / 22** — scans 45–46
- blocked / unresolved source holds: **0**

## Batches

| Batch | Scans / printed pages | Stage A — direct transcription | Stage B — independent glyph/source verification | Final page status |
|---|---|---|---|---|
| P1 | 25–29 | **COMPLETE — 5/5** | **PASS — 5/5** | `verified` |
| P2 | 30–34 | **COMPLETE — 5/5** | **PASS — 5/5** | `verified` |
| P3 | 35–39 | **COMPLETE — 5/5** | **PASS — 5/5** | `verified` |
| P4 | 40–44 | **COMPLETE — 5/5** | **PASS — 5/5** | `verified` |
| P5 | 45–46 | **NEXT** | waits for durable P5 Stage-A commit | not-started |

## P4 Stage-B result

**PASS — 5/5; 4 source/line-break corrections; 0 unresolved.**

1. scan 40 `நடைபெற்றுத் தொடங்கின` → `நடைபெறத் தொடங்கின`;
2. scan 40 `கலிதான்` → `கலைதான்` — historical `லை`;
3. scan 41 physical `ஆத்` / `மாக்களில்` → lexical `ஆத்மாக்களில்`;
4. scan 41 physical `களி` / `மண்` → lexical `களிமண்`, corroborated by same-paragraph `களிமண்ணிலே`.

All 13 mandatory historical families were independently checked on scans 40–44. Representative positive candidates included scan 40 `கலைதான்` / `வேலையை` (`லை`) and `அவனைப்` (`னை`); scan 41 `இலக்கானாள்` (`னா`) and `கால்களை` (`ளை`); scan 42 `சொல்லுகிறாய்` (`றா`) and `அவனை` (`னை`); scan 43 `காலை` / `கலைந்து` / `கூந்தலைக்` (`லை`) and `என்னை` (`னை`); scan 44 `அரண்மனை` (`னை`). Families without a positive occurrence were closed as no-candidate. P4 unresolved / blocked: **0 / 0**.

## Exact next activity

Run **P5 Stage A only** on scans **45–46**:

- direct whole-page visual transcription from the attached controlling PDF;
- no systematic 13-family Stage B in the same activity;
- no routine crops/enhancements or repeated reopening of clear text;
- keep scans 45–46 `needs-review` after Stage A;
- synchronize Pass-1/current-state controls;
- commit and stop/report.

Do not begin P5 Stage B or Story 8 `மானம்` in the same activity.
