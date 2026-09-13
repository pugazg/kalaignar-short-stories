# HANDOVER — Kalaignar Short Stories Archive

## Repository

- repository: `pugazg/kalaignar-short-stories`
- branch: `main`
- **LIVE MAIN IS AUTHORITATIVE**

## Closed durable layers

- 1977 Tamil dual-gate: **37/37 CURRENT PASS / CLOSED**
- 1977 English E1–E5 re-audit: **37/37 PASS / CLOSED**
- 1987 `கலைஞர் சொன்ன குட்டிக் கதைகள்`: **Tamil/source + English CLOSED**
- 1976 `நளாயினி` reconciliation: **CLOSED / PASS**

## Active source — 1969 `கண்ணடக்கம்`

Controlling attached source:

`TVA_BOK_0064095_கண்ணடக்கம்.pdf`

- title: **கண்ணடக்கம்**
- author: **மு. கருணாநிதி**
- publisher/imprint: **திராவிடப்பண்ணை**
- edition: **இரண்டாம் பதிப்பு — 1969**
- scans: **43**
- bytes: **50,321,052**
- SHA-256: **PENDING**
- no usable parsed text layer; source pixels control

Collection physical completeness remains **OPEN** because printed pages **31–52 (22 pages)** are absent. Do not guess those missing story identities/text.

## Visible story routing

1. `கண்ணடக்கம்` 4–10 — existing canonical witness
2. `நெருப்பு` 11–24 — **NEW canonical ACTIVE**
3. `வேணியின் காதலன்` 25–31 — existing canonical witness
4. `அமிர்தமதி` 32–41 — existing canonical witness

## `நெருப்பு` activation state

Workspace: `stories/neruppu/`

- source intake: **PASS**
- story range: scans **11–24 / printed 10–23**
- physical pages: **14**
- boundary: scan 24 ending; scan 25 opens `வேணியின் காதலன்`
- page records initialized: **14/14**
- Stage A: **0/14**
- Stage B: **0/14**
- verified: **0/14**
- not-started: **14/14**
- unresolved / blocked: **0/0**
- no prose committed during activation

## Exact next activity

**`நெருப்பு` P1 Stage A — scans 11–15 / printed 10–14.**

Follow `BATCH_TRANSCRIPTION_VERIFICATION_WORKFLOW.md`:

- direct whole-page transcription only;
- pages become `needs-review`;
- do not perform systematic Stage B in the same activity;
- commit Stage A and stop.

After that, exact next will be P1 Stage B scans 11–15.
