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

**SOURCE INTAKE COMPLETE / TRANSCRIPTION NOT STARTED — 0 / 22 pages.**

- page records created: **22 / 22**
- `not-started`: **22**
- `needs-review`: **0**
- `verified`: **0**
- `blocked`: **0**
- Tamil assembly: **not started**
- Historical Tamil Glyph Pass 1: **not started**
- Historical Tamil Glyph Pass 2: **not started**

Page map: [`indexes/page-map.md`](indexes/page-map.md).  
Source intake: [`SOURCE_INTAKE.md`](SOURCE_INTAKE.md).  
Pass-1 tracker: [`PASS1_PROGRESS.md`](PASS1_PROGRESS.md).  
Historical-glyph gate: [`HISTORICAL_GLYPH_GATE.md`](HISTORICAL_GLYPH_GATE.md).

## Source-first rule

The controlling scan is authoritative. Do not normalize spelling, punctuation, spacing, grammar, names or historical glyph forms. Do not import wording from the 1977 anthology or any other edition. A page can become `verified` only after direct transcription and a separate historical-glyph second pass against the same physical scan.

## Production batching

For fidelity, process **5 physical scans per iteration**, except the final remainder:

1. scans 25–29
2. scans 30–34
3. scans 35–39
4. scans 40–44
5. scans 45–46

Within each batch, transcribe all pages directly from source pixels, run the mandatory 13-family historical-glyph second pass, synchronize the page map/audits, and commit before beginning the next batch.

## Exact next activity

Process **scans 25–29 / printed pages 25–29** only. Scan 25 includes the display heading and opening prose. Do not begin scan 30 in the same iteration.

Do not begin Story 8 `மானம்` until this story's Tamil/source workflow is fully closed. The separate `நடுத்தெரு நாராயணி` hold also remains in force while `வெள்ளிக்கிழமை` is incomplete.
