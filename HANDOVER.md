# HANDOVER — Kalaignar Short Stories Archive

## Repository

- Repository: `pugazg/kalaignar-short-stories`
- Branch: `main`
- Story workflow: `SHORT_STORY_PROCESSING_GUIDE.md`
- Anthology workflow: `COLLECTION_SOURCE_GUIDE.md`
- Visual-fidelity workflow: `VISUAL_FIDELITY_CHECK_GUIDE.md`
- Visual-fidelity tracker: `VISUAL_FIDELITY_PROGRESS.md`
- English-translation workflow: `ENGLISH_TRANSLATION_GUIDE.md`
- English-translation tracker: `ENGLISH_TRANSLATION_PROGRESS.md`
- Source PDFs / renders / crops are **not** committed.

## Authoritative-state rule

Always fetch live `main` first and preserve newer durable work.

## Permanent source rules

- Controlling scan first; do not silently modernize spelling, punctuation, grammar, sandhi, names or source anomalies.
- Old Tamil glyphs require complete-span visual interpretation.
- Running headers, printed page numbers and printer signatures are page furniture, not story body.
- `POSSIBLE_ERRORS_FOR_REVIEW.md` is a human-review queue, not proof of error.
- Source-supported textual corrections must propagate through every affected page, assembly, audit/review and dependent English layer.
- Do not commit the controlling PDF or generated visual-inspection artefacts.

## Durable Tamil / visual milestones

The 1977 anthology has:

1. **Tamil source transcription/audit complete — 37 / 37 stories**, scans **10–259 / printed pages 1–250**, with **0 blocked / 0 unresolved story text**; and
2. **visual fidelity complete — 37 / 37 stories**, with **0 pending / 0 needs recheck**.

All 37 stories have story-local `visual-fidelity.md` records with result `PASS` or `PASS — corrected`.

## English translation phase — ACTIVE

The user explicitly authorized the English translation phase.

- total anthology stories: **37**
- complete: **1 / 37**
- pending: **36 / 37**
- needs review: **0**
- next target: **Story 2 — `நளாயினி`**

English is a separate, non-authoritative transformation layer. The verified Tamil assembly remains authoritative and must not be altered merely to improve English.

Before translating each story:

1. fetch live `main`;
2. read `SHORT_STORY_PROCESSING_GUIDE.md`, `COLLECTION_SOURCE_GUIDE.md`, `ENGLISH_TRANSLATION_GUIDE.md`, `ENGLISH_TRANSLATION_PROGRESS.md`, this handover and `NEXT_CHAT_PROMPT.md`;
3. read the story README, Tamil assembly, audit, `POSSIBLE_ERRORS_FOR_REVIEW.md`, visual-fidelity record and page map;
4. follow the current verified Tamil reading exactly; suspicious queue items are not silent corrections;
5. if translation exposes a likely Tamil issue, reopen it against the controlling scan under the Tamil guide before changing any layer.

## COMPLETED ENGLISH ACTIVITY — STORY 1

Story 1 — **`புகழேந்தி`**:

- canonical workspace: `stories/pugazhendhi/`
- printed pages: **1–6**
- anthology scans: **10–15**
- boundary witness: scan **16**, opening Story 2 **`நளாயினி`**
- Tamil audit: **PASS — 6 / 6 verified**
- visual fidelity: **PASS — corrected**
- English file: `stories/pugazhendhi/translations/en/pugazhendhi.md`
- translation review: `stories/pugazhendhi/TRANSLATION_REVIEW.md`
- all six source-page markers represented in English: **Yes**
- possible-error queue read and respected: **Yes**
- Tamil source changed during translation: **No**
- result: **PASS**

Conservative translation choices preserve the current verified Tamil reading. In particular, the unusual source form `பிடேல்டோ` is transliterated rather than externally identified, `மேதை` is rendered as **Genius** while retaining the `மே` + `தை` wordplay, and other queued forms are documented in the translation review instead of silently normalizing the Tamil.

## NEXT ACTIVITY — STORY 2

Story 2 — **`நளாயினி`**:

- canonical workspace: `stories/nalayini/`
- printed pages: **7–14**
- anthology scans: **16–23**
- boundary witness: scan **24**, opening Story 3 **`சபலம்`**
- Tamil audit: **PASS — 8 / 8 verified**
- English target: `stories/nalayini/translations/en/nalayini.md`
- translation review target: `stories/nalayini/TRANSLATION_REVIEW.md`

Process **one story per activity** unless the user explicitly expands the translation batch. Read Story 2's current possible-error queue and visual-fidelity record before translating; do not infer corrections from English expectations.

## Expected closure after Story 2

After `நளாயினி` translation/review is complete:

- English translation complete: **2 / 37**
- pending: **35 / 37**
- next target: Story 3 — **`சபலம்`**
- Story 3 printed pages: **15–21**
- Story 3 scans: **24–30**
- Story 3 boundary witness: scan **31**, opening Story 4 **`ஆட்டக்காவடி`**

Update the story README, root README, `ENGLISH_TRANSLATION_PROGRESS.md`, this handover and `NEXT_CHAT_PROMPT.md`, then re-fetch live `main` before declaring closure.

## Phase guard

English translation does not authorize modernization, republication, adaptation or replacement of the canonical Tamil source layer.
