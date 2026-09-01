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

The user explicitly authorized English translation and explicitly expanded the latest activity to Stories **24–26**:

- `கண்ணடக்கம்`
- `வாழ முடியாதவர்கள்`
- `அபாக்ய சிந்தாமணி`

Current durable translation state:

- total anthology stories: **37**
- complete: **26 / 37**
- pending: **11 / 37**
- needs review: **0**
- next target: **Story 27 — `பாலைவன ரோஜா`**

English is a separate, non-authoritative transformation layer. The verified Tamil assembly remains authoritative and must not be altered merely to improve English.

Before translating each story:

1. fetch live `main`;
2. read `SHORT_STORY_PROCESSING_GUIDE.md`, `COLLECTION_SOURCE_GUIDE.md`, `ENGLISH_TRANSLATION_GUIDE.md`, `ENGLISH_TRANSLATION_PROGRESS.md`, this handover and `NEXT_CHAT_PROMPT.md`;
3. read the story README, Tamil assembly, audit, `POSSIBLE_ERRORS_FOR_REVIEW.md`, visual-fidelity record and page map;
4. follow the current verified Tamil reading exactly; suspicious queue items are not silent corrections;
5. if translation exposes a likely Tamil issue, reopen it against the controlling scan under the Tamil guide before changing any layer.

## Completed English translations

Stories **1–26** are now **PASS**. For all twenty-six, the English file and story-local `TRANSLATION_REVIEW.md` are committed, source-page markers are complete, review queues were read and respected, and canonical Tamil was **not changed** merely to improve English.

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
24. `கண்ணடக்கம்` — scans **166–172 / printed 157–163** — **PASS**
25. `வாழ முடியாதவர்கள்` — scans **173–180 / printed 164–171** — **PASS**
26. `அபாக்ய சிந்தாமணி` — scans **181–188 / printed 172–179** — **PASS**

### Latest completed Story 24 — `கண்ணடக்கம்`

- workspace: `stories/kannadakkam/`
- English: `translations/en/kannadakkam.md`
- review: `TRANSLATION_REVIEW.md`
- all **7** source-page markers preserved
- physical continuation **169→170** remains traceable
- epidemic/cremation opening, Kali dialogue, `கண்ணடக்கம்` explanation, removal of the silver eye-covering, doctors/public-health response and final eye-hospital frame remain complete
- difficult `துணி ஏண்`, `பிணக்கொலு`, and `நம்முலகு செல்லும்` handled conservatively
- result: **PASS**
- Tamil source changed during translation: **No**

### Latest completed Story 25 — `வாழ முடியாதவர்கள்`

- workspace: `stories/vazha-mudiyathavargal/`
- English: `translations/en/vazha-mudiyathavargal.md`
- review: `TRANSLATION_REVIEW.md`
- all **8** source-page markers preserved
- physical continuations **175→176**, **176→177**, **177→178**, and **178→179** remain traceable
- source-emphasized central sentence and `“ஆண்டவன் படைப்பு”` represented semantically
- queue forms including `கவாட்டா`, `‘காலேஜ் வேடர்’`, `‘கிம்பள சான்ஸ்’`, `அழுக்கியது`, and `தீவிதி` handled conservatively
- father–daughter night sequence kept to the source’s degree of explicitness without added mechanics or euphemistic omission
- result: **PASS**
- Tamil source changed during translation: **No**

### Latest completed Story 26 — `அபாக்ய சிந்தாமணி`

- workspace: `stories/abagya-chinthamani/`
- English: `translations/en/abagya-chinthamani.md`
- review: `TRANSLATION_REVIEW.md`
- all **8** source-page markers preserved
- physical continuations **182→183**, **183→184**, **184→185**, and **187→188** remain traceable
- scan-182 display/song blocks and source emphasis are preserved
- final Tamil closure corrections were respected and not reverted
- mother’s history, gurukulam/love sequence, staged-infidelity device, pregnancy and stillbirth remain complete
- result: **PASS**
- Tamil source changed during translation: **No**

## NEXT ACTIVITY — STORY 27

Story 27 — **`பாலைவன ரோஜா`**:

- canonical workspace: `stories/palaivana-roja/`
- printed pages: **180–184**
- anthology scans: **189–193**
- boundary witness: scan **194**, opening Story 28; TOC title **`புரட்சிப்படம்`**, story-opening heading **`புரட்சிப் படம்`**
- Tamil audit: **PASS — 5 / 5 verified**
- English target: `stories/palaivana-roja/translations/en/palaivana-roja.md`
- translation review target: `stories/palaivana-roja/TRANSLATION_REVIEW.md`

Process **one story per activity** unless the user explicitly expands the translation batch.

## Expected closure after Story 27

After `பாலைவன ரோஜா` translation/review is complete:

- English translation complete: **27 / 37**
- pending: **10 / 37**
- next target: Story 28 — TOC **`புரட்சிப்படம்`** / opening **`புரட்சிப் படம்`**
- Story 28 printed pages: **185–189**
- Story 28 scans: **194–198**
- Story 28 boundary witness: scan **199**, opening Story 29 **`திடுக்கிடும் கதை`**

Update the story README, root README, `ENGLISH_TRANSLATION_PROGRESS.md`, this handover and `NEXT_CHAT_PROMPT.md`, then re-fetch live `main` before declaring closure.

## Phase guard

English translation does not authorize modernization, republication, adaptation or replacement of the canonical Tamil source layer.