# HANDOVER — Kalaignar Short Stories Archive

## Repository

- repository: `pugazg/kalaignar-short-stories`
- branch: `main`
- permanent guides: `SHORT_STORY_PROCESSING_GUIDE.md`, `COLLECTION_SOURCE_GUIDE.md`, `HISTORICAL_TAMIL_GLYPH_TRANSCRIPTION_GUIDE.md`, `BATCH_TRANSCRIPTION_VERIFICATION_WORKFLOW.md`, `ENGLISH_TRANSLATION_GUIDE.md`

## LIVE MAIN IS AUTHORITATIVE

Fetch live `main` first. Controlling scans outrank contextual readings; no silent normalization.

## External hold

`நடுத்தெரு நாராயணி` remains **BLOCKED** while `வெள்ளிக்கிழமை` is incomplete.

## 1976 `நளாயினி` — Tamil/source phase CLOSED

Controlling source: attached `TVA_BOK_0065574_நளாயினி_1976.pdf` — **78 scans**, **164,748,566 bytes**, fourth edition 1976, image-only, not committed; SHA-256 pending. The attached PDF itself is the sole controlling source unless the user explicitly requests external comparison.

The anthology reconciliation identified two new canonical stories requiring full source processing:

- `நாட்டிய கலாராணி` — **TAMIL SOURCE-COMPLETE**: 22/22 verified, assembly/review PASS, 0 unresolved / 0 blocked;
- `மானம்` — **TAMIL SOURCE-COMPLETE**: 6/6 verified, assembly/review PASS, 0 unresolved / 0 blocked.

The remaining six story headings resolve to existing canonical workspaces and were intentionally note-only in this anthology intake.

### `மானம்` closure details

- physical range: scans **73–78**;
- source heading: **`மானம்`**; stale `மனம்` rejected;
- scan 73 visible printed folio: **`10` source anomaly**; scans 74–78 = 74–78;
- page records / direct transcription / Stage B / verified: **6/6 / 6/6 / 6/6 / 6/6**;
- source-proven corrections: **9 total**, including 3 historical-glyph corrections;
- canonical assembly: `stories/maanam/sections/maanam.md` — **COMPLETE**;
- assembly review: `stories/maanam/ASSEMBLY_REVIEW.md` — **PASS — 6/6 coverage / 0 omission / 0 duplication**;
- final paired-swans ornament preserved as source mark; library stamp remains non-story.

## English phase — OPEN automatically

`ENGLISH_TRANSLATION_GUIDE.md` requires English to become the automatic next activity after the collection-wide Tamil/source gate closes. Durable tracker: `collections/1976-nalayini/ENGLISH_TRANSLATION_PROGRESS.md`.

Targets introduced by this anthology reconciliation:

1. `நாட்டிய கலாராணி` — English `pending` — **NEXT**;
2. `மானம்` — English `pending` — after Story 4 English closes.

## Exact next activity — `நாட்டிய கலாராணி` English translation ONLY

1. re-fetch live `main`;
2. read `ENGLISH_TRANSLATION_GUIDE.md`, root `HANDOVER.md`, `NEXT_CHAT_PROMPT.md`, the collection translation tracker, `stories/naattiya-kalarani/README.md`, `sections/naattiya-kalarani.md`, `ASSEMBLY_REVIEW.md`, `POSSIBLE_ERRORS_FOR_REVIEW.md`, page map and relevant source/glyph controls;
3. translate the **complete verified Tamil assembly** into `stories/naattiya-kalarani/translations/en/naattiya-kalarani.md`;
4. preserve physical source-page markers and meaningful display/letter structure;
5. create `stories/naattiya-kalarani/TRANSLATION_REVIEW.md` and prove complete coverage / page-anchor alignment / no omission or duplication;
6. do not silently correct Tamil source oddities from English expectation;
7. synchronize story README, collection translation tracker, root handover and next prompt;
8. commit and stop/report.

Do **not** translate `மானம்` in the same activity.
