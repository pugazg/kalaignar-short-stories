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

**NOT STARTED.**

- page records: 22/22 initialized;
- direct source transcription: 0/22;
- independent historical-glyph Pass 2: 0/22;
- verified: 0/22;
- blocked: 0/22.

No story prose has been imported from OCR, another edition or contextual inference.

## Revised batch execution workflow

Root `BATCH_TRANSCRIPTION_VERIFICATION_WORKFLOW.md` splits each physical batch into two durable activities:

1. Stage A — direct transcription, Pass-1 synchronization, commit, stop/report;
2. Stage B — separate independent historical-glyph/source verification, verification synchronization, commit, stop/report.

Routine crops/enhancements are not part of Stage A and are not automatic in Stage B; they are reserved for genuine ambiguity.

## Exact next gate

**Stage A only:** process scans **25–29** by direct whole-page source transcription, keep them `needs-review`, synchronize Pass-1/current-state controls, commit, and stop/report.

Only after that durable commit should Stage B reopen scans 25–29 for the independent 13-family/source check. Scan 30 must not begin before Stage B is committed.
