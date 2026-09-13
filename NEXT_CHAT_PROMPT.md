# NEXT CHAT PROMPT — 1969 `கண்ணடக்கம்` / `நெருப்பு` P1 Stage 1

Continue in `pugazg/kalaignar-short-stories`, branch `main`. **LIVE MAIN IS AUTHORITATIVE.**

## Controlling source

Use only the attached:

`TVA_BOK_0064095_கண்ணடக்கம்.pdf`

- edition: **இரண்டாம் பதிப்பு — 1969**
- active story: **நெருப்பு**
- story scans: **11–24**
- printed pages: **10–23**
- scan 25 opens `வேணியின் காதலன்`
- image-only source; source pixels control

## Durable state

`stories/neruppu/` source intake: **PASS**.

- page records: **14/14 initialized**
- Stage 1 first-pass: **0/14**
- Stage 2 visual fidelity: **0/14**
- Stage 3 historical glyph: **0/14**
- Stage 4 final check: **0/14**
- verified: **0/14**
- not-started: **14/14**

## Mandatory four-stage workflow

For each batch:

`Stage 1 first-pass transcription → COMMIT/SYNC → Stage 2 visual text fidelity → COMMIT/SYNC → Stage 3 historical glyph → COMMIT/SYNC → Stage 4 final independent check → COMMIT/SYNC`

Only Stage 4 promotes pages to `verified`.

A later high-resolution/visual-verification problem must not delay Stage 1. First-pass uncertainty should be explicitly recorded and carried forward as `needs-review`.

## Exact next activity

Perform **P1 Stage 1 — scans 11–15 / printed pages 10–14** only.

1. re-fetch live `main`;
2. transcribe each whole page once from the attached source;
3. preserve source wording, punctuation, spacing, paragraph/dialogue structure and page boundaries;
4. do not do the detailed Stage-2 fidelity audit yet;
5. do not run the systematic historical-glyph audit yet;
6. record uncertain readings explicitly instead of guessing;
7. set completed pages to `needs-review`;
8. synchronize page map, progress tracker, README, HANDOVER and NEXT prompt;
9. commit and stop.

Next after that commit: **P1 Stage 2 — visual text-fidelity audit scans 11–15**.
