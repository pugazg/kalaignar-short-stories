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
- story ending: scan **78**, followed by a centered closing ornament and library stamp; this is the final PDF scan
- source PDF committed: **No**
- SHA-256: **pending at collection level**; do not invent or borrow a digest

## Gates / current state

- source boundary: **PASS**
- canonical dedup / alternate-title check: **PASS — no existing canonical match found**
- stale title `மனம்`: **REJECTED**; scan 73 directly reads `மானம்`
- page records: **6 / 6 initialized**
- direct transcription: **5 / 6** — scans 73–77
- P1 Stage A: **COMPLETE — 5/5**
- historical-glyph/source Stage B: **0 / 6**
- verified: **0 / 6**
- `needs-review`: **5 / 6** — scans 73–77
- `not-started`: **1 / 6** — scan 78
- blocked / unresolved blocking locations: **0 / 0**
- Tamil assembly: **not started**

The scan-73 folio is a physical source anomaly: the bottom-left printed number is `10`, not `73`. Do not silently normalize it. Scan coordinates remain 73–78.

## Exact next activity

**P1 Stage B only — scans 73–77.** Re-open those five pages independently, perform the mandatory 13-family source/glyph audit, inspect the Stage-A source-sensitive queue, make only source-proven corrections, synchronize controls, commit, and stop/report. Do not touch scan 78 in that activity.
