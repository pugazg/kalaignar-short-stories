# Pass 1 Progress — நாட்டிய கலாராணி

Controlling range: scans **25–46 / printed pages 25–46** — **22 physical pages**.

Workflow: root `BATCH_TRANSCRIPTION_VERIFICATION_WORKFLOW.md` — **Stage A and Stage B are separate durable activities.**

## Current state

- source intake: **PASS**
- page records initialized: **22 / 22**
- direct first-pass transcription: **5 / 22**
- historical-glyph Pass 2: **0 / 22**
- verified pages: **0 / 22**
- `needs-review`: **5 / 22** — scans 25–29, because Stage B is pending
- unresolved source holds: **0** — source-sensitive but legible readings are queued for Stage B

## Batches

| Batch | Scans / printed pages | Stage A — direct transcription | Stage B — independent glyph/source verification | Final page status |
|---|---|---|---|---|
| P1 | 25–29 | **COMPLETE — 5/5** | **NEXT** | `needs-review` |
| P2 | 30–34 | pending | pending | not-started |
| P3 | 35–39 | pending | pending | not-started |
| P4 | 40–44 | pending | pending | not-started |
| P5 | 45–46 | pending | pending | not-started |

## P1 Stage-A notes

- all five pages were transcribed directly from the attached controlling scans;
- no OCR/web/other-edition wording was imported;
- scan 25 → 26 physical split `நட்டுவ` / `னரும்` is preserved;
- scan 27 physically ends `கவிவாணர்-`; scan 28 independently begins `கவிவாணர்-மதிவாணர்`; both are preserved as printed;
- unusual but legible forms are recorded in `POSSIBLE_ERRORS_FOR_REVIEW.md` for independent Stage-B checking;
- no page is promoted to `verified` from Stage A alone.

## Exact next activity

Run **P1 Stage B only** on scans **25–29**:

- independently reopen the same five source pages;
- compare the committed Stage-A text against source pixels; do not fully retranscribe;
- explicitly check `ணா / ணை / ணொ / ணோ / லை / ளை / றா / றொ / றோ / னா / னை / னொ / னோ` and the queued source-sensitive locations;
- use crops/enhancements only for an actual ambiguity;
- record corrections individually; never global-replace;
- synchronize verification controls, commit and stop/report.

Do **not** begin scan 30 before P1 Stage B is committed.
