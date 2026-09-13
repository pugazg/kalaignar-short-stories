# நெருப்பு

Canonical story workspace for **நெருப்பு**, controlled by the attached 1969 second edition of **கண்ணடக்கம்**.

## Controlling source

- source filename: `TVA_BOK_0064095_கண்ணடக்கம்.pdf`
- collection: `collections/1969-kannadakkam/`
- printed collection title: **கண்ணடக்கம்**
- printed author: **மு. கருணாநிதி**
- publisher/imprint: **திராவிடப்பண்ணை**
- edition: **இரண்டாம் பதிப்பு — 1969**
- physical range: **scans 11–24**
- printed pages: **10–23**
- source PDF scans: **43**
- source file size: **50,321,052 bytes**
- SHA-256: **PENDING at collection level**
- source PDF committed: **No**

## Canonical activation

**SOURCE INTAKE PASS / TAMIL TRANSCRIPTION NOT STARTED.**

- live `main` was re-fetched before activation;
- no canonical `நெருப்பு` workspace or documented alternate-title match was found;
- scan 11 visibly opens with the heading **நெருப்பு**;
- scan 24 contains the story ending and closing ornament;
- scan 25 independently opens **வேணியின் காதலன்**, proving the forward boundary;
- 14 / 14 page records are initialized as `not-started`;
- no story prose has been committed from OCR, memory, another edition or lexical inference.

## Four-stage workflow

This story follows `BATCH_TRANSCRIPTION_VERIFICATION_WORKFLOW.md`.

For every batch:

1. **Stage 1 — first-pass transcription** → commit + sync;
2. **Stage 2 — visual text-fidelity audit** → commit + sync;
3. **Stage 3 — historical Tamil glyph audit** → commit + sync;
4. **Stage 4 — final independent source check** → commit + sync; only then `verified`.

Mandatory Stage-3 families:

`ணா / ணை / ணொ / ணோ / லை / ளை / றா / றொ / றோ / னா / னை / னொ / னோ`

Default batch size: **5 physical scans**.

A high-resolution verification problem in Stage 2/3/4 must not block a responsible Stage-1 first-pass transcription. Uncertain readings may remain explicitly queued as `needs-review`.

## Current state

- page records: **14 / 14 initialized**
- Stage 1 first-pass: **0 / 14**
- Stage 2 visual fidelity: **0 / 14**
- Stage 3 historical glyph: **0 / 14**
- Stage 4 final check: **0 / 14**
- verified: **0 / 14**
- needs-review: **0 / 14**
- not-started: **14 / 14**
- blocked / unresolved: **0 / 0**
- Tamil assembly: **NOT STARTED**
- English: **BLOCKED until Tamil/source closure**

## Exact next activity

**P1 Stage 1 — scans 11–15 / printed pages 10–14.**

Perform the first-pass transcription of those five whole pages from the attached source. Do **not** wait for Stage-2 visual adjudication, Stage-3 historical-glyph audit or Stage-4 final verification.

- record uncertain readings explicitly rather than guessing;
- set the five pages to `needs-review`;
- synchronize controls;
- commit and stop.

Next after that durable commit: **P1 Stage 2 — visual text-fidelity audit, scans 11–15**.