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

The user explicitly authorized English translation and explicitly expanded the latest activity to Stories 7–8. The repeated `கங்கையின் காதல்` in the user request was treated as the same Story 8, not as a third distinct story.

- total anthology stories: **37**
- complete: **8 / 37**
- pending: **29 / 37**
- needs review: **0**
- next target: **Story 9 — `தாய்மை`**

English is a separate, non-authoritative transformation layer. The verified Tamil assembly remains authoritative and must not be altered merely to improve English.

Before translating each story:

1. fetch live `main`;
2. read `SHORT_STORY_PROCESSING_GUIDE.md`, `COLLECTION_SOURCE_GUIDE.md`, `ENGLISH_TRANSLATION_GUIDE.md`, `ENGLISH_TRANSLATION_PROGRESS.md`, this handover and `NEXT_CHAT_PROMPT.md`;
3. read the story README, Tamil assembly, audit, `POSSIBLE_ERRORS_FOR_REVIEW.md`, visual-fidelity record and page map;
4. follow the current verified Tamil reading exactly; suspicious queue items are not silent corrections;
5. if translation exposes a likely Tamil issue, reopen it against the controlling scan under the Tamil guide before changing any layer.

## Completed English translations

1. `புகழேந்தி` — scans **10–15 / printed 1–6** — **PASS**
2. `நளாயினி` — scans **16–23 / printed 7–14** — **PASS**
3. `சபலம்` — scans **24–30 / printed 15–21** — **PASS**
4. `ஆட்டக்காவடி` — scans **31–38 / printed 22–29** — **PASS**
5. `குப்பைத்தொட்டி` — scans **39–46 / printed 30–37** — **PASS**
6. `சந்தனக்கிண்ணம்` — scans **47–56 / printed 38–47** — **PASS**
7. `சங்கிலிச்சாமி` — scans **57–68 / printed 48–59** — **PASS**
8. `கங்கையின் காதல்` — scans **69–72 / printed 60–63** — **PASS**

For all eight, the English file and story-local `TRANSLATION_REVIEW.md` are committed, source-page markers are complete, review queues were read and respected, and canonical Tamil was **not changed** merely to improve English.

### Latest completed Story 7 — `சங்கிலிச்சாமி`

- workspace: `stories/sangilichami/`
- English: `translations/en/sangilichami.md`
- review: `TRANSLATION_REVIEW.md`
- opening chants and scan-58 devotee petitions remain display-separated
- scan-67 false letter and sign-off remain distinct; source-bold signature is preserved semantically
- physical 67→68 continuation remains traceable
- unusual verified forms such as `அஷ்டமா சித்துபுரி`, `‘நமப்பார்வதி படே’`, `செக்கச் செவேன்னு`, `மூடாத்மா ஞானத்மாவாக`, `தவறுக என்னை மதிக்காதீர்`, `தடியன் தானு?`, and `கொலைகாரனுக்கிவிட்டாயே` were handled conservatively and documented
- result: **PASS**
- Tamil source changed during translation: **No**

### Latest completed Story 8 — `கங்கையின் காதல்`

- workspace: `stories/gangaiyin-kadhal/`
- English: `translations/en/gangaiyin-kadhal.md`
- review: `TRANSLATION_REVIEW.md`
- scans 69→70 and 71→72 physical continuations remain traceable
- dialogue structure and final narrative paragraph remain distinct
- unusual verified forms including `அல்வித் தண்டில்`, `கிளப்புற்ற வண்டின் கீழ்ஸ்தாயி ரீங்காரம்`, `சல்லாப ரூபா`, `என்..பார்வதியால் தான் முடிந்ததா?`, and `தோன்றுமலிருக்க` were not silently normalized
- result: **PASS**
- Tamil source changed during translation: **No**

## NEXT ACTIVITY — STORY 9

Story 9 — **`தாய்மை`**:

- canonical workspace: `stories/thaaymai/`
- printed pages: **64–74**
- anthology scans: **73–83**
- boundary witness: scan **84**, opening Story 10 **`தப்பிவிட்டார்கள்`**
- Tamil audit: **PASS — 11 / 11 verified**
- English target: `stories/thaaymai/translations/en/thaaymai.md`
- translation review target: `stories/thaaymai/TRANSLATION_REVIEW.md`

Process **one story per activity** unless the user explicitly expands the translation batch.

## Expected closure after Story 9

After `தாய்மை` translation/review is complete:

- English translation complete: **9 / 37**
- pending: **28 / 37**
- next target: Story 10 — **`தப்பிவிட்டார்கள்`**
- Story 10 printed pages: **75–82**
- Story 10 scans: **84–91**
- Story 10 boundary witness: scan **92**, opening Story 11 **`தப்பவில்லை`**

Update the story README, root README, `ENGLISH_TRANSLATION_PROGRESS.md`, this handover and `NEXT_CHAT_PROMPT.md`, then re-fetch live `main` before declaring closure.

## Phase guard

English translation does not authorize modernization, republication, adaptation or replacement of the canonical Tamil source layer.