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
- English translation: **4 / 37 complete**
- English pending: **33 / 37**
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

## COMPLETED ENGLISH STORIES

The current durable English boundary is **Story 4**.

1. `புகழேந்தி` — scans **10–15 / printed 1–6** — **PASS**
2. `நளாயினி` — scans **16–23 / printed 7–14** — **PASS**
3. `சபலம்` — scans **24–30 / printed 15–21** — **PASS**
4. `ஆட்டக்காவடி` — scans **31–38 / printed 22–29** — **PASS**

For all four:

- English file and `TRANSLATION_REVIEW.md` are committed;
- source-page markers are complete;
- possible-error queues were read and respected;
- canonical Tamil was **not changed** during translation.

Story-specific structural facts remain preserved: Nalayini's printed page-14 note is separate from narrative; the source's `மெளத் கல்யர்` / `மெளத்கல்யர்` distinction remains explicit; Aattakkavadi's source emphasis and Kanimozhi letter/sign-off structure remain represented.

## NEXT ACTIVITY — STORY 5 ONLY

Translate and review Story 5 — **`குப்பைத்தொட்டி`**.

- canonical workspace: `stories/kuppai-thotti/`
- printed pages: **30–37**
- anthology scans: **39–46**
- boundary witness: scan **47**, opening Story 6 **`சந்தனக்கிண்ணம்`**
- Tamil audit: **PASS — 8 / 8 verified**
- English target: `stories/kuppai-thotti/translations/en/kuppai-thotti.md`
- review target: `stories/kuppai-thotti/TRANSLATION_REVIEW.md`

For Story 5:

1. read its complete verified Tamil assembly and review queue first;
2. preserve paragraph/dialogue/display structure and source-page markers;
3. preserve names, cultural references and unusual verified forms conservatively;
4. do not import corrections or explanations from outside editions or general knowledge;
5. if translation exposes a likely Tamil transcription problem, stop at that span and reopen the Tamil reading against the controlling scan before changing any source layer;
6. create the complete English file and `TRANSLATION_REVIEW.md`;
7. update Story 5 README, root README, `ENGLISH_TRANSLATION_PROGRESS.md`, `HANDOVER.md` and this prompt;
8. re-fetch live `main` and changed controls before declaring Story 5 complete.

Do **not** begin Story 6 in the same activity unless the user explicitly expands the translation batch.

## EXPECTED STATE AFTER STORY 5

- English translation complete: **5 / 37**
- pending: **32 / 37**
- needs review: **0**, unless Story 5 genuinely requires review
- next target: Story 6 — **`சந்தனக்கிண்ணம்`**, scans **47–56 / printed pages 38–47**
- Story 6 boundary witness: scan **57**, opening `சங்கிலிச்சாமி`

## SOURCE / PHASE RULES

Do not silently modernize or normalize canonical Tamil spelling, punctuation, grammar, sandhi, names, title forms or source anomalies. Do not guess unclear Tamil from context or OCR. Do not commit the controlling source PDF or generated renders/crops. English translation does not authorize modernization, republication, adaptation or replacement of the canonical Tamil source layer.
