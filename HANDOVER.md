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
- complete: **0 / 37**
- in progress: **Story 1 — `புகழேந்தி`**
- pending after Story 1: **36**
- needs review: **0**

English is a separate, non-authoritative transformation layer. The verified Tamil assembly remains authoritative and must not be altered merely to improve English.

Before translating each story:

1. fetch live `main`;
2. read `SHORT_STORY_PROCESSING_GUIDE.md`, `COLLECTION_SOURCE_GUIDE.md`, `ENGLISH_TRANSLATION_GUIDE.md`, `ENGLISH_TRANSLATION_PROGRESS.md`, this handover and `NEXT_CHAT_PROMPT.md`;
3. read the story README, Tamil assembly, audit, `POSSIBLE_ERRORS_FOR_REVIEW.md`, visual-fidelity record and page map;
4. follow the current verified Tamil reading exactly; suspicious queue items are not silent corrections;
5. if translation exposes a likely Tamil issue, reopen it against the controlling scan under the Tamil guide before changing any layer.

## CURRENT ACTIVITY — STORY 1

Story 1 — **`புகழேந்தி`**:

- canonical workspace: `stories/pugazhendhi/`
- printed pages: **1–6**
- anthology scans: **10–15**
- boundary witness: scan **16**, opening Story 2 **`நளாயினி`**
- Tamil audit: **PASS — 6 / 6 verified**
- visual fidelity: **PASS — corrected**
- English target: `stories/pugazhendhi/translations/en/pugazhendhi.md`
- translation review: `stories/pugazhendhi/TRANSLATION_REVIEW.md`

The story's possible-error queue contains unusual source forms such as `பாராட்டுப் படித்தது`, `அவனோர் பிடேல்டோ!`, `புகழ்தரும் தீவலி`, `தத்தரூபமாகச்`, `வயித்துக்கிடக்கிறது`, `காதற் கண்கள்`, `கால்ப் பணிவிடைகள்` and others. Translate the **current verified Tamil** conservatively; do not infer an outside identity or silently normalize those source readings.

Process **one story per activity** unless the user explicitly expands the translation batch.

## Expected closure after Story 1

After `புகழேந்தி` translation/review is complete:

- English translation complete: **1 / 37**
- pending: **36 / 37**
- next target: Story 2 — **`நளாயினி`**
- Story 2 printed pages: **7–14**
- Story 2 scans: **16–23**
- Story 2 boundary witness: scan **24**, opening Story 3 **`சபலம்`**

Update the story README, root README, `ENGLISH_TRANSLATION_PROGRESS.md`, this handover and `NEXT_CHAT_PROMPT.md`, then re-fetch live `main` before declaring closure.

## Phase guard

English translation does not authorize modernization, republication, adaptation or replacement of the canonical Tamil source layer.