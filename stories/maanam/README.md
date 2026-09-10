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

## Activation gates

- source boundary: **PASS**
- canonical dedup / alternate-title check: **PASS — no existing canonical match found**
- stale title `மனம்`: **REJECTED**; scan 73 directly reads `மானம்`
- page records: **6 / 6 initialized**
- direct transcription: **0 / 6**
- historical-glyph/source Stage B: **0 / 6**
- verified: **0 / 6**
- not-started: **6 / 6**
- blocked / unresolved: **0 / 0**
- Tamil assembly: **not started**

The scan-73 folio is a physical source anomaly: the bottom-left printed number is `10`, not `73`. Do not silently normalize it. Scan coordinates remain 73–78.

## Exact next activity

**P1 Stage A only — scans 73–77.** Direct whole-page transcription from the attached source, keep all five pages `needs-review`, synchronize Pass-1 controls, commit, and stop/report. Do not touch scan 78 in that activity.
