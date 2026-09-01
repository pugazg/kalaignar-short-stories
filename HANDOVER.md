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

The user explicitly authorized English translation and explicitly expanded the latest activity to Stories 2–4.

- total anthology stories: **37**
- complete: **4 / 37**
- pending: **33 / 37**
- needs review: **0**
- next target: **Story 5 — `குப்பைத்தொட்டி`**

English is a separate, non-authoritative transformation layer. The verified Tamil assembly remains authoritative and must not be altered merely to improve English.

Before translating each story:

1. fetch live `main`;
2. read `SHORT_STORY_PROCESSING_GUIDE.md`, `COLLECTION_SOURCE_GUIDE.md`, `ENGLISH_TRANSLATION_GUIDE.md`, `ENGLISH_TRANSLATION_PROGRESS.md`, this handover and `NEXT_CHAT_PROMPT.md`;
3. read the story README, Tamil assembly, audit, `POSSIBLE_ERRORS_FOR_REVIEW.md`, visual-fidelity record and page map;
4. follow the current verified Tamil reading exactly; suspicious queue items are not silent corrections;
5. if translation exposes a likely Tamil issue, reopen it against the controlling scan under the Tamil guide before changing any layer.

## Completed English translations

### Story 1 — `புகழேந்தி`

- workspace: `stories/pugazhendhi/`
- scans **10–15 / printed 1–6**
- English: `translations/en/pugazhendhi.md`
- review: `TRANSLATION_REVIEW.md`
- result: **PASS**
- Tamil source changed during translation: **No**

### Story 2 — `நளாயினி`

- workspace: `stories/nalayini/`
- scans **16–23 / printed 7–14**
- boundary witness: scan **24**, opening `சபலம்`
- English: `translations/en/nalayini.md`
- review: `TRANSLATION_REVIEW.md`
- page-14 printed note kept separate from narrative: **Yes**
- source forms `மெளத் கல்யர்` / `மெளத்கல்யர்` kept distinct rather than normalized
- result: **PASS**
- Tamil source changed during translation: **No**

### Story 3 — `சபலம்`

- workspace: `stories/sabalam/`
- scans **24–30 / printed 15–21**
- boundary witness: scan **31**, opening `ஆட்டக்காவடி`
- English: `translations/en/sabalam.md`
- review: `TRANSLATION_REVIEW.md`
- unusual source forms handled conservatively and documented
- result: **PASS**
- Tamil source changed during translation: **No**

### Story 4 — `ஆட்டக்காவடி`

- workspace: `stories/aattakkavadi/`
- scans **31–38 / printed 22–29**
- boundary witness: scan **39**, opening `குப்பைத்தொட்டி`
- English: `translations/en/aattakkavadi.md`
- review: `TRANSLATION_REVIEW.md`
- source-bold opening phrase and Kanimozhi letter/display/sign-off structure preserved semantically
- unusual forms including `‘பாவலா’`, `அதிருப சுந்தரன்`, `கருவிழியானை`, `‘சுண்’கள்` were not silently normalized
- result: **PASS**
- Tamil source changed during translation: **No**

## NEXT ACTIVITY — STORY 5

Story 5 — **`குப்பைத்தொட்டி`**:

- canonical workspace: `stories/kuppai-thotti/`
- printed pages: **30–37**
- anthology scans: **39–46**
- boundary witness: scan **47**, opening Story 6 **`சந்தனக்கிண்ணம்`**
- Tamil audit: **PASS — 8 / 8 verified**
- English target: `stories/kuppai-thotti/translations/en/kuppai-thotti.md`
- translation review target: `stories/kuppai-thotti/TRANSLATION_REVIEW.md`

Process **one story per activity** unless the user explicitly expands the translation batch.

## Expected closure after Story 5

After `குப்பைத்தொட்டி` translation/review is complete:

- English translation complete: **5 / 37**
- pending: **32 / 37**
- next target: Story 6 — **`சந்தனக்கிண்ணம்`**
- Story 6 printed pages: **38–47**
- Story 6 scans: **47–56**
- Story 6 boundary witness: scan **57**, opening Story 7 **`சங்கிலிச்சாமி`**

Update the story README, root README, `ENGLISH_TRANSLATION_PROGRESS.md`, this handover and `NEXT_CHAT_PROMPT.md`, then re-fetch live `main` before declaring closure.

## Phase guard

English translation does not authorize modernization, republication, adaptation or replacement of the canonical Tamil source layer.
