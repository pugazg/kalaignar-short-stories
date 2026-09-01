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

The user explicitly authorized English translation and explicitly expanded the latest activity to Stories **16–19**:

- `ஒரிஜினலில் உள்ளபடி`
- `பனங்குலை`
- `செத்தவள் கதை`
- `பிரேத விசாரணை`

Current durable translation state:

- total anthology stories: **37**
- complete: **19 / 37**
- pending: **18 / 37**
- needs review: **0**
- next target: **Story 20 — `கண்டதும் காதல் ஒழிக!`**

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
16. `ஒரிஜினலில் உள்ளபடி` — scans **119–125 / printed 110–116** — **PASS**
17. `பனங்குலை` — scans **126–130 / printed 117–121** — **PASS**
18. `செத்தவள் கதை` — scans **131–139 / printed 122–130** — **PASS**
19. `பிரேத விசாரணை` — scans **140–145 / printed 131–136** — **PASS**

For all nineteen, the English file and story-local `TRANSLATION_REVIEW.md` are committed, source-page markers are complete, review queues were read and respected, and canonical Tamil was **not changed** merely to improve English.

### Latest completed Story 16 — `ஒரிஜினலில் உள்ளபடி`

- workspace: `stories/originalil-ullapadi/`
- English: `translations/en/originalil-ullapadi.md`
- review: `TRANSLATION_REVIEW.md`
- all **7** source-page markers preserved
- physical continuations **120→121**, **121→122**, **122→123** remain traceable
- source-bold notice/program spans and `எல்லாம் என்` represented semantically
- deliberate `யோகானந்த`/`போகானந்த`, `ராமநாதன்`/`காமநாதன்`, `விபசாரம்`/`விபச்சாரம்`, and discourse/begging wordplay retained conservatively
- result: **PASS**
- Tamil source changed during translation: **No**

### Latest completed Story 17 — `பனங்குலை`

- workspace: `stories/panangulai/`
- English: `translations/en/panangulai.md`
- review: `TRANSLATION_REVIEW.md`
- all **5** source-page markers preserved
- physical continuations **128→129** and **129→130** remain traceable
- `பனை நுங்கு`, `பனங் குலைகள்`, `புறம்போக்கு`, source-anomalous `உன் தங்கையைத்:தேடிப்`, and other difficult forms handled conservatively
- false-father deception, Kamalam death, Velan death and final narrator sentence preserved
- result: **PASS**
- Tamil source changed during translation: **No**

### Latest completed Story 18 — `செத்தவள் கதை`

- workspace: `stories/seththaval-kathai/`
- English: `translations/en/seththaval-kathai.md`
- review: `TRANSLATION_REVIEW.md`
- all **9** source-page markers preserved
- physical continuations **134→135**, **135→136**, **138→139** remain traceable
- fire refrains on scans **131, 136, 139** preserve source display lineation
- coercive assault, later contact, Ellappan confrontation, killing, cremation and final `மங்களம்` remain in source order
- result: **PASS**
- Tamil source changed during translation: **No**

### Latest completed Story 19 — `பிரேத விசாரணை`

- workspace: `stories/pretha-visaranai/`
- English: `translations/en/pretha-visaranai.md`
- review: `TRANSLATION_REVIEW.md`
- all **6** source-page markers preserved
- physical continuations **140→141** and **142→143** remain traceable
- source-printed historical caste-language is represented source-close and documented rather than silently modernized
- hospital refusal, landlord-headache contrast, Karuppayi backstory, temple-entry scene, corpse admission/post-mortem irony and final social diagnosis remain complete
- result: **PASS**
- Tamil source changed during translation: **No**

## NEXT ACTIVITY — STORY 20

Story 20 — **`கண்டதும் காதல் ஒழிக!`**:

- canonical workspace: `stories/kandathum-kadhal-ozhiga/`
- printed pages: **137–141**
- anthology scans: **146–150**
- boundary witness: scan **151**, opening Story 21 **`ஆலமரத்துப் புறாக்கள்`**
- Tamil audit: **PASS — 5 / 5 verified**
- English target: `stories/kandathum-kadhal-ozhiga/translations/en/kandathum-kadhal-ozhiga.md`
- translation review target: `stories/kandathum-kadhal-ozhiga/TRANSLATION_REVIEW.md`

Process **one story per activity** unless the user explicitly expands the translation batch.

## Expected closure after Story 20

After `கண்டதும் காதல் ஒழிக!` translation/review is complete:

- English translation complete: **20 / 37**
- pending: **17 / 37**
- next target: Story 21 — **`ஆலமரத்துப் புறாக்கள்`**
- Story 21 printed pages: **142–146**
- Story 21 scans: **151–155**
- Story 21 boundary witness: scan **156**, opening Story 22 **`தொத்துக்கிளி`**

Update the story README, root README, `ENGLISH_TRANSLATION_PROGRESS.md`, this handover and `NEXT_CHAT_PROMPT.md`, then re-fetch live `main` before declaring closure.

## Phase guard

English translation does not authorize modernization, republication, adaptation or replacement of the canonical Tamil source layer.