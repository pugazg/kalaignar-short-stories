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

Do not reopen those layers without stronger source evidence or explicit maintenance/audit authorization.

## Active source — 1969 `கண்ணடக்கம்`

Attached controlling source:

`TVA_BOK_0064095_கண்ணடக்கம்.pdf`

- title: **கண்ணடக்கம்**
- author: **மு. கருணாநிதி**
- publisher/imprint: **திராவிடப்பண்ணை**
- represented edition: **இரண்டாம் பதிப்பு — 1969**
- scans: **43**
- bytes: **50,321,052**
- SHA-256: **PENDING — do not invent**
- source PDF committed: **No**
- parser text layer: **none usable; rendered scan pixels control**

## Source intake

**PASS for visible physical structure / completeness OPEN.**

Visible story blocks:

1. `கண்ணடக்கம்` — scans **4–10 / printed 3–9** — existing canonical witness;
2. `நெருப்பு` — scans **11–24 / printed 10–23** — **NEW canonical candidate**;
3. `வேணியின் காதலன்` — scans **25–31 / printed 24–30** — existing canonical witness;
4. `அமிர்தமதி` — scans **32–41 / printed 53–62** — existing canonical witness.

Back matter:

- scan 42 — `அண்ணாவின் அரிய நூல்கள்` advertisement;
- scan 43 — terminal rear leaf.

## Critical completeness gap

The source jumps from printed **30** to the `அமிர்தமதி` opening structurally at printed **53**. Printed pages **31–52 (22 pages)** are absent from the supplied PDF.

Do not guess missing story identities or text. Process only what is physically present unless the user supplies stronger same-source evidence.

## Deduplication

Existing canonical workspaces confirmed:

- `stories/kannadakkam/`
- `stories/veniyin-kadhalan/`
- `stories/amirthamathi/`

No canonical match found for `நெருப்பு`.

Existing stories are comparison-only witnesses: no duplicate Tamil transcription and no duplicate English translation.

## Exact next activity

Activate **`நெருப்பு`** as a new canonical story.

- source scans: **11–24**
- printed pages: **10–23**
- next-story boundary witness: scan **25** opens `வேணியின் காதலன்`
- create `stories/neruppu/` only now, when processing begins
- direct Tamil source transcription / page records / historical-glyph verification
- do not start `வேணியின் காதலன்` in the same activity

After `நெருப்பு` Tamil/source closure, English is automatically next unless the user redirects. Then process the three existing stories as comparison-only witnesses.
