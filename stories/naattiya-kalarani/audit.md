# Audit — நாட்டிய கலாராணி

## Source intake gate

**PASS.**

- source identity inherited from registered 1976 `நளாயினி` collection;
- story opening directly verified on scan 25;
- ending boundary directly verified on scan 46;
- scan 47 independently opens `விஷம் இனிது`;
- physical range fixed at **22 scans, 25–46**;
- scan and printed page numbers are identical in this range.

## Canonical dedup gate

**PASS.** Live repository search immediately before activation found no canonical `நாட்டிய கலாராணி` / `கலாராணி` match and no documented alternate title.

## Transcription / verification gate

**IN PROGRESS — P1 STAGE A COMPLETE.**

- page records: 22/22 initialized;
- direct source transcription: **5/22** — scans 25–29;
- independent historical-glyph Pass 2: **0/22**;
- `needs-review`: **5/22**;
- verified: **0/22**;
- blocked: **0/22**.

Stage A for scans 25–29 was transcribed directly from the attached controlling source. No OCR, web text or another edition was used as transcription authority. The systematic 13-family second pass was intentionally **not** run in Stage A.

Physical-source boundary facts retained in the page records:

- scan 25 ends mid-word `நட்டுவ`; scan 26 begins `னரும்`;
- scan 27 ends `கவிவாணர்-`; scan 28 independently begins `கவிவாணர்-மதிவாணர்`.

Visually legible but source-sensitive forms are queued in `POSSIBLE_ERRORS_FOR_REVIEW.md`. They remain source readings, not confirmed errors and not permission to normalize.

## Batch execution workflow

Root `BATCH_TRANSCRIPTION_VERIFICATION_WORKFLOW.md` splits each physical batch into two durable activities:

1. Stage A — direct transcription, Pass-1 synchronization, commit, stop/report;
2. Stage B — separate independent historical-glyph/source verification, verification synchronization, commit, stop/report.

## Exact next gate

**P1 Stage B only:** reopen scans **25–29** independently, compare the committed text against the source, check all 13 mandatory historical-glyph families and the source-sensitive queue, use crops/enhancements only where a real ambiguity exists, record any correction individually, synchronize verification controls, commit, and stop/report.

Scan 30 must not begin before P1 Stage B is committed.
