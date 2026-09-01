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

The user explicitly authorized English translation and explicitly expanded the latest activity to Stories **20–23**:

- `கண்டதும் காதல் ஒழிக!`
- `ஆலமரத்துப் புறாக்கள்`
- `தொத்துக்கிளி`
- `காதல் கடிதம்`

Current durable translation state:

- total anthology stories: **37**
- complete: **23 / 37**
- pending: **14 / 37**
- needs review: **0**
- next target: **Story 24 — `கண்ணடக்கம்`**

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
20. `கண்டதும் காதல் ஒழிக!` — scans **146–150 / printed 137–141** — **PASS**
21. `ஆலமரத்துப் புறாக்கள்` — scans **151–155 / printed 142–146** — **PASS**
22. `தொத்துக்கிளி` — scans **156–160 / printed 147–151** — **PASS**
23. `காதல் கடிதம்` — scans **161–165 / printed 152–156** — **PASS**

For all twenty-three, the English file and story-local `TRANSLATION_REVIEW.md` are committed, source-page markers are complete, review queues were read and respected, and canonical Tamil was **not changed** merely to improve English.

### Latest completed Story 20 — `கண்டதும் காதல் ஒழிக!`

- workspace: `stories/kandathum-kadhal-ozhiga/`
- English: `translations/en/kandathum-kadhal-ozhiga.md`
- review: `TRANSLATION_REVIEW.md`
- all **5** source-page markers preserved
- physical continuations **148→149** and **149→150** remain traceable
- source-bold `“அன்பே! சீதா! அருகில் வா!”` and `“ராமாயணம்”` represented semantically
- `பெண்ணுரல்`, `தருமனுய்`, `சகாதேவனுய்`, `தீங்கனியாக`, `நன்றுக நிதானம்`, and final `‘டோபா’` wording handled conservatively
- theatre confusion, riot/fire sequence and final wig reveal remain complete
- result: **PASS**
- Tamil source changed during translation: **No**

### Latest completed Story 21 — `ஆலமரத்துப் புறாக்கள்`

- workspace: `stories/aalamarathup-puraakkal/`
- English: `translations/en/aalamarathup-puraakkal.md`
- review: `TRANSLATION_REVIEW.md`
- all **5** source-page markers preserved
- physical continuations **151→152** and **152→153** remain traceable
- repeated body form `புறு` / `புறுக்கள்` and compound labels retained conservatively rather than normalized
- source-bold `இது வல்லூறின் மரம்` and final `வல்லூறை விரட்டுவதுதான்!` represented semantically
- no external political decoding of the allegory was imported
- result: **PASS**
- Tamil source changed during translation: **No**

### Latest completed Story 22 — `தொத்துக்கிளி`

- workspace: `stories/thothukkili/`
- English: `translations/en/thothukkili.md`
- review: `TRANSLATION_REVIEW.md`
- all **5** source-page markers preserved
- physical continuations **156→157** and **158→159** remain traceable
- source name `அண்ணுமலை` retained as Annumalai
- difficult forms including `அக்கத்தாகக் குத்திக் கொன்றுவிட்டாள்` and `கருகு தாளிக்கப் பட்டது` handled minimally and documented without Tamil repair
- Vimala’s pregnancy, laboratory retaliation/self-poisoning and final quoted admonition remain complete
- result: **PASS**
- Tamil source changed during translation: **No**

### Latest completed Story 23 — `காதல் கடிதம்`

- workspace: `stories/kadhal-kaditham/`
- English: `translations/en/kadhal-kaditham.md`
- review: `TRANSLATION_REVIEW.md`
- all **5** source-page markers preserved
- physical continuations **161→162**, **163→164**, and **164→165** remain traceable
- long quoted letter across scans **162–163** and centered/source-bold sign-off remain structurally distinct
- source-sensitive `சூழ்நிலே-கூடாரத்தைவிட்டு`, `உழவலன்பு`, repeated `நிலே`, and other queue forms handled conservatively
- wartime frame, returned mail, postman revelation and final ironic sentence remain complete
- result: **PASS**
- Tamil source changed during translation: **No**

## NEXT ACTIVITY — STORY 24

Story 24 — **`கண்ணடக்கம்`**:

- canonical workspace: `stories/kannadakkam/`
- printed pages: **157–163**
- anthology scans: **166–172**
- boundary witness: scan **173**, opening Story 25 **`வாழ முடியாதவர்கள்`**
- Tamil audit: **PASS — 7 / 7 verified**
- English target: `stories/kannadakkam/translations/en/kannadakkam.md`
- translation review target: `stories/kannadakkam/TRANSLATION_REVIEW.md`

Process **one story per activity** unless the user explicitly expands the translation batch.

## Expected closure after Story 24

After `கண்ணடக்கம்` translation/review is complete:

- English translation complete: **24 / 37**
- pending: **13 / 37**
- next target: Story 25 — **`வாழ முடியாதவர்கள்`**
- Story 25 printed pages: **164–171**
- Story 25 scans: **173–180**
- Story 25 boundary witness: scan **181**, opening Story 26 **`அபாக்ய சிந்தாமணி`**

Update the story README, root README, `ENGLISH_TRANSLATION_PROGRESS.md`, this handover and `NEXT_CHAT_PROMPT.md`, then re-fetch live `main` before declaring closure.

## Phase guard

English translation does not authorize modernization, republication, adaptation or replacement of the canonical Tamil source layer.