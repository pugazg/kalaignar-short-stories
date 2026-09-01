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

The user explicitly authorized English translation and explicitly expanded the latest activity to Stories **11–15**:

- `தப்பவில்லை`
- `ஆதரிக்கிறார்`
- `இரகசியம்!`
- `முந்நூறு ரூபாய்`
- `ஏழை`

Current durable translation state:

- total anthology stories: **37**
- complete: **15 / 37**
- pending: **22 / 37**
- needs review: **0**
- next target: **Story 16 — `ஒரிஜினலில் உள்ளபடி`**

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
11. `தப்பவில்லை` — scans **92–101 / printed 83–92** — **PASS**
12. `ஆதரிக்கிறார்` — scans **102–107 / printed 93–98** — **PASS**
13. `இரகசியம்!` — scans **108–111 / printed 99–102** — **PASS**
14. `முந்நூறு ரூபாய்` — scans **112–114 / printed 103–105** — **PASS**
15. `ஏழை` — scans **115–118 / printed 106–109** — **PASS**

For all fifteen, the English file and story-local `TRANSLATION_REVIEW.md` are committed, source-page markers are complete, review queues were read and respected, and canonical Tamil was **not changed** merely to improve English.

### Latest completed Story 11 — `தப்பவில்லை`

- workspace: `stories/thappavillai/`
- English: `translations/en/thappavillai.md`
- review: `TRANSLATION_REVIEW.md`
- all **10** source-page markers preserved
- physical continuations **92→93**, **93→94**, **95→96** remain traceable
- source-bold `நாட்கள் ஓடின...` represented semantically
- final appeal/death-row reversal preserved
- result: **PASS**
- Tamil source changed during translation: **No**

### Latest completed Story 12 — `ஆதரிக்கிறார்`

- workspace: `stories/aatharikkirar/`
- English: `translations/en/aatharikkirar.md`
- review: `TRANSLATION_REVIEW.md`
- all **6** source-page markers preserved
- source-bold `ராஜ நிலையத்தார்` and final disclosure span represented
- physical continuations **104→105**, **105→106**, **106→107** remain traceable
- source-supported `பொதுத்தொண்டு சிங்கம்` translated from current canonical Tamil
- result: **PASS**
- Tamil source changed during translation: **No**

### Latest completed Story 13 — `இரகசியம்!`

- workspace: `stories/iragasiyam/`
- English: `translations/en/iragasiyam.md`
- review: `TRANSLATION_REVIEW.md`
- all **4** source-page markers preserved
- source-bold correspondence labels, death note, `சிபாரிசுக் கடிதங்கள்`, and final two-line explanation preserved
- physical continuation **109→110** remains within the same letter
- result: **PASS**
- Tamil source changed during translation: **No**

### Latest completed Story 14 — `முந்நூறு ரூபாய்`

- workspace: `stories/munnuru-rupai/`
- English: `translations/en/munnuru-rupai.md`
- review: `TRANSLATION_REVIEW.md`
- all **3** source-page markers preserved
- both physical continuations remain traceable
- unusual `எழுபட்டு`, `குதாகலமாய்`, `ஓடும்பிள்ளையாய்` handled conservatively
- train-dream reversal preserved as the ending
- result: **PASS**
- Tamil source changed during translation: **No**

### Latest completed Story 15 — `ஏழை`

- workspace: `stories/ezhai/`
- English: `translations/en/ezhai.md`
- review: `TRANSLATION_REVIEW.md`
- all **4** source-page markers preserved
- physical continuations **115→116**, **116→117**, **117→118** remain traceable
- anomalous verified `...பயந்தான்.` handled by narrative sense without modifying Tamil
- final `யார் அது? “ஏழை”!` reveal preserved
- result: **PASS**
- Tamil source changed during translation: **No**

## NEXT ACTIVITY — STORY 16

Story 16 — **`ஒரிஜினலில் உள்ளபடி`**:

- canonical workspace: `stories/originalil-ullapadi/`
- printed pages: **110–116**
- anthology scans: **119–125**
- boundary witness: scan **126**, opening Story 17 **`பனங்குலை`**
- Tamil audit: **PASS — 7 / 7 verified**
- English target: `stories/originalil-ullapadi/translations/en/originalil-ullapadi.md`
- translation review target: `stories/originalil-ullapadi/TRANSLATION_REVIEW.md`

Process **one story per activity** unless the user explicitly expands the translation batch.

## Expected closure after Story 16

After `ஒரிஜினலில் உள்ளபடி` translation/review is complete:

- English translation complete: **16 / 37**
- pending: **21 / 37**
- next target: Story 17 — **`பனங்குலை`**
- Story 17 printed pages: **117–121**
- Story 17 scans: **126–130**
- Story 17 boundary witness: scan **131**, opening Story 18 **`செத்தவள் கதை`**

Update the story README, root README, `ENGLISH_TRANSLATION_PROGRESS.md`, this handover and `NEXT_CHAT_PROMPT.md`, then re-fetch live `main` before declaring closure.

## Phase guard

English translation does not authorize modernization, republication, adaptation or replacement of the canonical Tamil source layer.