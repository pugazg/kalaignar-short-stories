# Historical Tamil Glyph Gate — நாட்டிய கலாராணி

Status: **NOT STARTED — 0 / 22 pages**.

Mandatory independent second-pass families:

`ணா / ணை / ணொ / ணோ / லை / ளை / றா / றொ / றோ / னா / னை / னொ / னோ`

## Rule

Each page must first receive a direct visual transcription. It must then be reopened in a **separate durable Stage-B activity** and every relevant historical family checked against the physical glyph cluster. Grammar or expected spelling is only a locator, never proof. No global replacements are allowed.

A page remains `needs-review` until both passes close with zero unresolved glyph/source ambiguity. The initial 22 records are `not-started`; none is currently eligible for `verified`.

## Two-stage execution discipline

Follow root `BATCH_TRANSCRIPTION_VERIFICATION_WORKFLOW.md`.

- **Stage A** performs direct transcription and commits it first. The systematic 13-family audit does not run in Stage A.
- **Stage B** begins only after the matching Stage-A batch is durable on live `main`.
- Stage B is an independent re-read of the same pages; it is not a full retranscription.
- Crops/enhancements are created only for an actual ambiguous/suspicious cluster, not merely because a clearly readable word contains a historical family or looks archaic.
- If Stage B leaves an unresolved cluster, the page remains `needs-review` and the documented difficult-reading escalation applies.

## Progress

| Scans | Stage B state | Corrections | Unresolved |
|---|---|---:|---:|
| 25–29 | waiting for durable Stage-A transcription | 0 | 0 |
| 30–34 | pending | 0 | 0 |
| 35–39 | pending | 0 | 0 |
| 40–44 | pending | 0 | 0 |
| 45–46 | pending | 0 | 0 |

The immediate next activity is **not** this gate. First complete and commit Stage A for scans 25–29. Then this Stage-B gate becomes the next exact activity for those same scans.
