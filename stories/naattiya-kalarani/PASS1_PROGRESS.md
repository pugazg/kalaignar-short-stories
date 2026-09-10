# Pass 1 Progress — நாட்டிய கலாராணி

Controlling range: scans **25–46 / printed pages 25–46** — **22 physical pages**.

Workflow: root `BATCH_TRANSCRIPTION_VERIFICATION_WORKFLOW.md` — Stage A and Stage B are separate durable activities.

## Current state

- source intake: **PASS**
- page records initialized: **22 / 22**
- direct first-pass transcription: **15 / 22** — scans 25–39
- historical-glyph/source Stage B: **15 / 22** — scans 25–39
- verified pages: **15 / 22** — scans 25–39
- `needs-review`: **0 / 22**
- not-started: **7 / 22** — scans 40–46
- blocked / unresolved source holds: **0**

## Batches

| Batch | Scans / printed pages | Stage A — direct transcription | Stage B — independent glyph/source verification | Final page status |
|---|---|---|---|---|
| P1 | 25–29 | **COMPLETE — 5/5** | **PASS — 5/5** | `verified` |
| P2 | 30–34 | **COMPLETE — 5/5** | **PASS — 5/5** | `verified` |
| P3 | 35–39 | **COMPLETE — 5/5** | **PASS — 5/5** | `verified` |
| P4 | 40–44 | **NEXT** | waits for durable P4 Stage-A commit | not-started |
| P5 | 45–46 | pending | pending | not-started |

## P3 Stage-B result

**PASS — 5/5; 4 source corrections; 0 unresolved.**

1. scan 36 `ஆமாம்` → `ஆம்`;
2. scan 36 `வரவேற்றாள் உபசரித்தாள்` → `வரவேற்று உபசரித்தாள்`;
3. scan 37 `ஜோடிப் புறு` → `ஜோடிப் புறா` — historical `றா`, confirmed against same-edition scan 25 `நன்றாக`;
4. scan 37 `ஒன்பது பற்றி அறியதோர்` → `என்பது பற்றி அறியதோர்`.

All 13 mandatory historical families were independently checked on scans 35–39. Representative positive candidates included scan 35 `நிர்வாணக்` (`ணா`) and `தன்னை` / `என்னை` (`னை`); scan 36 `மணிமேகலை` (`லை`); scan 37 `புறா` (`றா`), `அவனை` (`னை`) and `இவரன்றோ` (`றோ`); scan 38 `நிலையாமை` / `புகழ்மாலை` (`லை`), `நாளை` (`ளை`), `மண்ணோடு` (`ணோ`); scan 39 `கலை` / `நிலையில்லா` (`லை`), `அனைவருக்கும்` (`னை`) and `நாளை` (`ளை`). Families without a positive occurrence were closed as no-candidate. P3 unresolved / blocked: **0 / 0**.

## Exact next activity

Run **P4 Stage A only** on scans **40–44**:

- direct whole-page visual transcription from the attached controlling PDF;
- no systematic 13-family Stage B in the same activity;
- no routine crops/enhancements or repeated reopening of clear text;
- keep scans 40–44 `needs-review` after Stage A;
- synchronize Pass-1/current-state controls;
- commit and stop/report.

Do not begin P4 Stage B in the same activity.
