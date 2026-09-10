# மானம்

Canonical story workspace for **மானம்**, activated from the attached 1976 fourth edition of **நளாயினி**.

## Controlling source

- source filename: `TVA_BOK_0065574_நளாயினி_1976.pdf`
- collection: `collections/1976-nalayini/`
- edition: **நான்காம் பதிப்பு 1976**
- author line: **மு. கருணாநிதி**
- physical range: **PDF scans 73–78**
- visible printed folios: **scan 73 = `10` (source anomaly); scans 74–78 = 74–78**
- story opening: scan **73**, display heading `மானம்`
- story ending: scan **78**, followed by a centered paired-swans closing ornament and library stamp; this is the final PDF scan
- source PDF committed: **No**
- SHA-256: **pending at collection level**; do not invent or borrow a digest

## Gates / current state

- source boundary: **PASS**
- canonical dedup / alternate-title check: **PASS — no existing canonical match found**
- stale title `மனம்`: **REJECTED**; scan 73 directly reads `மானம்`
- page records: **6 / 6 initialized**
- direct transcription: **6 / 6 — COMPLETE**
- P1 Stage A: **COMPLETE — 5/5**
- P1 Stage B: **PASS — 5/5**
- P2 Stage A scan 78: **COMPLETE — 1/1**
- historical-glyph/source Stage B total: **5 / 6**
- verified: **5 / 6** — scans 73–77
- `needs-review`: **1 / 6** — scan 78
- `not-started`: **0 / 6**
- P1 corrections: **5 total** — 3 historical-glyph + 2 source-text/spacing
- blocked / unresolved: **0 / 0**
- Tamil assembly: **not started**

The scan-73 folio is a physical source anomaly: the bottom-left printed number is `10`, not `73`. Do not silently normalize it. Scan coordinates remain 73–78.

Scan 78 Stage A preserves the final prose and records the centered paired-swans closing ornament as a source mark. The library stamp below it is documented as a non-story artefact without promoting unreadable/obscured stamp text.

## Exact next activity

**P2 Stage B only — scan 78.** Independently reopen the final page, run the mandatory 13-family source/glyph audit plus the P2 source-sensitive queue, make only source-proven corrections, promote the page to `verified` if all readings close, synchronize controls, commit, and stop/report. Tamil assembly is a later separate activity.
