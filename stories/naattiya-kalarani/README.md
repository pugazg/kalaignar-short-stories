# நாட்டிய கலாராணி

Canonical story workspace for **நாட்டிய கலாராணி**, opened from the attached 1976 fourth edition of **நளாயினி**.

## Controlling source

- source filename: `TVA_BOK_0065574_நளாயினி_1976.pdf`
- collection: `collections/1976-nalayini/`
- edition: **நான்காம் பதிப்பு 1976**
- author line: **மு. கருணாநிதி**
- physical range: **PDF scans 25–46 / printed pages 25–46**
- story opening: scan **25**, heading `நாட்டிய கலாராணி`
- story ending: scan **46**, ending prose followed by the printed closing ornaments
- forward boundary: scan **47** independently opens `விஷம் இனிது`
- source PDF committed: **No**
- source SHA-256: **pending at collection level**; do not invent or borrow a digest

Full source note: [`metadata/source.md`](metadata/source.md).

## Canonical deduplication

Before this workspace was created, live `main` was re-fetched and the repository was searched again for `கலாராணி` / the exact source heading. No existing canonical story or documented alternate-title match was found.

This workspace is therefore the canonical target for the 1976 source range above.

## Current Tamil/source state

**TRANSCRIPTION IN PROGRESS — P1 STAGE A COMPLETE — 5 / 22 direct-transcribed.**

- page records created: **22 / 22**
- direct first-pass transcription: **5 / 22** — scans 25–29
- `not-started`: **17**
- `needs-review`: **5** — Stage B pending
- `verified`: **0**
- `blocked`: **0**
- Tamil assembly: **not started**
- Historical Tamil Glyph Pass 2: **0 / 22**

Page map: [`indexes/page-map.md`](indexes/page-map.md).  
Source intake: [`SOURCE_INTAKE.md`](SOURCE_INTAKE.md).  
Pass-1 tracker: [`PASS1_PROGRESS.md`](PASS1_PROGRESS.md).  
Historical-glyph gate: [`HISTORICAL_GLYPH_GATE.md`](HISTORICAL_GLYPH_GATE.md).  
Source-sensitive queue: [`POSSIBLE_ERRORS_FOR_REVIEW.md`](POSSIBLE_ERRORS_FOR_REVIEW.md).

## Source-first rule

The controlling scan is authoritative. Do not normalize spelling, punctuation, spacing, grammar, names or historical glyph forms. Do not import wording from the 1977 anthology or any other edition. A page can become `verified` only after direct transcription and a separate historical-glyph second pass against the same physical scan.

## Production batching — two separate durable activities per batch

Use root [`BATCH_TRANSCRIPTION_VERIFICATION_WORKFLOW.md`](../../BATCH_TRANSCRIPTION_VERIFICATION_WORKFLOW.md).

Physical batches remain:

1. scans 25–29
2. scans 30–34
3. scans 35–39
4. scans 40–44
5. scans 45–46

Each physical batch is executed as:

1. **Stage A — direct transcription only**: read each whole page once, transcribe source-faithfully, keep pages `needs-review`, synchronize Pass-1/current-state controls, commit, stop/report;
2. **Stage B — independent historical-glyph/source verification**: in a later activity reopen the same pages, check all 13 historical families plus recorded uncertainties, create crops/enhancements only for genuine ambiguity, synchronize verification controls, commit, stop/report.

Do not begin the next physical batch until Stage B of the current batch is committed unless the user explicitly overrides the workflow.

## P1 durable state

Scans **25–29** have completed **Stage A**. The page text is committed as direct source transcription and deliberately remains `needs-review`. Notable physical boundaries are preserved: scan 25 ends `நட்டுவ` and scan 26 begins `னரும்`; scan 27 ends `கவிவாணர்-` and scan 28 independently begins `கவிவாணர்-மதிவாணர்`.

## Exact next activity

**Stage B only:** independently reopen scans **25–29 / printed pages 25–29**, compare the committed transcription with the attached source, check the mandatory 13 historical-glyph families plus `POSSIBLE_ERRORS_FOR_REVIEW.md`, correct only source-proven mismatches, synchronize verification controls, commit, and stop/report.

Do **not** begin scan 30 before this Stage-B commit. Do not begin Story 8 `மானம்` until this story's Tamil/source workflow is fully closed. The separate `நடுத்தெரு நாராயணி` hold also remains in force while `வெள்ளிக்கிழமை` is incomplete.
