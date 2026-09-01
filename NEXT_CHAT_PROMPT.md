# NEXT CHAT PROMPT — Kalaignar Short Stories English Translation

Continue the Kalaignar Short Stories archival project directly in:

`https://github.com/pugazg/kalaignar-short-stories`

Branch: `main`

Use the GitHub connector and work directly on `main`.

Controlling anthology source:
`TVA_BOK_0064142_கலைஞர்_கருணாநிதியின்_சிறுகதைகள்.pdf`

## LIVE MAIN IS AUTHORITATIVE

Fetch live `main` first and preserve any newer durable state. Do not reset or repeat work if the branch has advanced beyond a checkpoint copied into this prompt.

## DURABLE MILESTONES

- Tamil source processing: **37 / 37 complete**
- visual fidelity: **37 / 37 complete**
- English translation: **1 / 37 complete**
- English pending: **36 / 37**
- English needs review: **0**

English is a separate translation layer. The verified canonical Tamil remains authoritative.

## MANDATORY STARTUP FOR EACH ENGLISH STORY

Before translating, read completely:

1. `SHORT_STORY_PROCESSING_GUIDE.md`
2. `COLLECTION_SOURCE_GUIDE.md`
3. `ENGLISH_TRANSLATION_GUIDE.md`
4. `ENGLISH_TRANSLATION_PROGRESS.md`
5. `HANDOVER.md`
6. this `NEXT_CHAT_PROMPT.md`
7. the active story `README.md`
8. the active story Tamil assembly under `sections/`
9. the active story `audit.md`
10. the active story `POSSIBLE_ERRORS_FOR_REVIEW.md`
11. the active story `visual-fidelity.md`
12. the active story `indexes/page-map.md`

Translate the **current verified Tamil actually preserved in the repository**. Do not silently correct a suspicious Tamil reading merely because smoother English suggests another wording.

## COMPLETED ENGLISH STORY

Story 1 — **`புகழேந்தி`** is closed:

- workspace: `stories/pugazhendhi/`
- scans **10–15 / printed pages 1–6**
- English: `stories/pugazhendhi/translations/en/pugazhendhi.md`
- review: `stories/pugazhendhi/TRANSLATION_REVIEW.md`
- result: **PASS**
- Tamil source changed during translation: **No**

The English retains all six source-page markers. Queued unusual Tamil readings were not silently normalized; conservative choices are documented in `TRANSLATION_REVIEW.md`.

## NEXT ACTIVITY — STORY 2 ONLY

Translate and review Story 2 — **`நளாயினி`**.

- canonical workspace: `stories/nalayini/`
- printed pages: **7–14**
- anthology scans: **16–23**
- boundary witness: scan **24**, opening Story 3 **`சபலம்`**
- Tamil audit: **PASS — 8 / 8 verified**
- English target: `stories/nalayini/translations/en/nalayini.md`
- review target: `stories/nalayini/TRANSLATION_REVIEW.md`

For Story 2:

1. read its complete verified Tamil assembly and review queue first;
2. preserve paragraph/dialogue/display structure and source-page markers;
3. preserve names, cultural references and unusual verified forms conservatively;
4. do not import corrections or explanations from outside editions or general knowledge;
5. if translation exposes a likely Tamil transcription problem, stop at that span and reopen the Tamil reading against the controlling scan before changing any source layer;
6. create the complete English file and `TRANSLATION_REVIEW.md`;
7. update Story 2 README, root README, `ENGLISH_TRANSLATION_PROGRESS.md`, `HANDOVER.md` and this prompt;
8. re-fetch live `main` and changed controls before declaring Story 2 complete.

Do **not** begin Story 3 in the same activity unless the user explicitly expands the translation batch.

## EXPECTED STATE AFTER STORY 2

- English translation complete: **2 / 37**
- pending: **35 / 37**
- needs review: **0**, unless Story 2 genuinely requires review
- next target: Story 3 — **`சபலம்`**, scans **24–30 / printed pages 15–21**
- Story 3 boundary witness: scan **31**, opening `ஆட்டக்காவடி`

## SOURCE / PHASE RULES

Do not silently modernize or normalize canonical Tamil spelling, punctuation, grammar, sandhi, names, title forms or source anomalies. Do not guess unclear Tamil from context or OCR. Do not commit the controlling source PDF or generated renders/crops. English translation does not authorize modernization, republication, adaptation or replacement of the canonical Tamil source layer.
