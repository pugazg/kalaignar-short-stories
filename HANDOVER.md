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

The user explicitly authorized English translation and explicitly expanded the latest activity to Stories 9–10.

- total anthology stories: **37**
- complete: **10 / 37**
- pending: **27 / 37**
- needs review: **0**
- next target: **Story 11 — `தப்பவில்லை`**

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
9. `தாய்மை` — scans **73–83 / printed 64–74** — **PASS**
10. `தப்பிவிட்டார்கள்` — scans **84–91 / printed 75–82** — **PASS**

For all ten, the English file and story-local `TRANSLATION_REVIEW.md` are committed, source-page markers are complete, review queues were read and respected, and canonical Tamil was **not changed** merely to improve English.

### Latest completed Story 9 — `தாய்மை`

- workspace: `stories/thaaymai/`
- English: `translations/en/thaaymai.md`
- review: `TRANSLATION_REVIEW.md`
- all **11** source-page markers preserved
- physical continuations **74→75**, **78→79** and **80→81** remain traceable
- source-bold scan-82 `“நிறுத்தாதே! ஊது!! ஊது!” என்று.` is represented semantically in English
- all Tamil spans restored during the earlier visual-fidelity reopen were translated from the current canonical assembly
- unusual forms including `மல்லிகர்த்தவரை`, `திட்டசனயமிக்க`, `கரடித் திருமனியன்`, `மாயமாலத்தில்`, `மொண்டு மொண்டு`, `தணலிவிட்ட புழுவாயிற்று`, and `படந்தாக்கி` were handled conservatively
- result: **PASS**
- Tamil source changed during translation: **No**

### Latest completed Story 10 — `தப்பிவிட்டார்கள்`

- workspace: `stories/thappivittargal/`
- English: `translations/en/thappivittargal.md`
- review: `TRANSLATION_REVIEW.md`
- all **8** source-page markers preserved
- physical continuations **84→85**, **86→87** and **90→91** remain traceable
- public praise of Ramadurai, assault disclosure, Vittal’s retaliation/escape, and the final station sequence remain in source order
- unusual source-close forms such as `பச்சைப் பசங்களியே`, `போக்களத்தில்`, `எச்சிற் பண்டம்`, `கொல்காரன்`, `பலங் கொண்ட மட்டும்`, `கீழ்ஸ்தாயியில்`, and short `-னள்` verb forms were not silently normalized
- result: **PASS**
- Tamil source changed during translation: **No**

## NEXT ACTIVITY — STORY 11

Story 11 — **`தப்பவில்லை`**:

- canonical workspace: `stories/thappavillai/`
- printed pages: **83–92**
- anthology scans: **92–101**
- boundary witness: scan **102**, opening Story 12 **`ஆதரிக்கிறார்`**
- Tamil audit: **PASS — 10 / 10 verified**
- English target: `stories/thappavillai/translations/en/thappavillai.md`
- translation review target: `stories/thappavillai/TRANSLATION_REVIEW.md`

Process **one story per activity** unless the user explicitly expands the translation batch.

## Expected closure after Story 11

After `தப்பவில்லை` translation/review is complete:

- English translation complete: **11 / 37**
- pending: **26 / 37**
- next target: Story 12 — **`ஆதரிக்கிறார்`**
- Story 12 printed pages: **93–98**
- Story 12 scans: **102–107**
- Story 12 boundary witness: scan **108**, opening Story 13 **`இரகசியம்!`**

Update the story README, root README, `ENGLISH_TRANSLATION_PROGRESS.md`, this handover and `NEXT_CHAT_PROMPT.md`, then re-fetch live `main` before declaring closure.

## Phase guard

English translation does not authorize modernization, republication, adaptation or replacement of the canonical Tamil source layer.