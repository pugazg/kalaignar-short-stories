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

The user explicitly expanded the latest activity to Stories **27–30**:

- `பாலைவன ரோஜா`
- TOC `புரட்சிப்படம்` / opening `புரட்சிப் படம்`
- `திடுக்கிடும் கதை`
- `கடைசிக் கட்டம்`

Current durable translation state:

- total anthology stories: **37**
- complete: **30 / 37**
- pending: **7 / 37**
- needs review: **0**
- next target: **Story 31 — `அய்யோ ராஜா!`**

English is a separate, non-authoritative transformation layer. The verified Tamil assembly remains authoritative and must not be altered merely to improve English.

Before translating each story:

1. fetch live `main`;
2. read `SHORT_STORY_PROCESSING_GUIDE.md`, `COLLECTION_SOURCE_GUIDE.md`, `ENGLISH_TRANSLATION_GUIDE.md`, `ENGLISH_TRANSLATION_PROGRESS.md`, this handover and `NEXT_CHAT_PROMPT.md`;
3. read the story README, Tamil assembly, audit, `POSSIBLE_ERRORS_FOR_REVIEW.md`, visual-fidelity record and page map;
4. follow the current verified Tamil reading exactly; suspicious queue items are not silent corrections;
5. if translation exposes a likely Tamil issue, reopen it against the controlling scan under the Tamil guide before changing any layer.

## Completed English translations

Stories **1–30** are now **PASS**. For all thirty, the English file and story-local `TRANSLATION_REVIEW.md` are committed, source-page markers are complete, review queues were read and respected, and canonical Tamil was **not changed** merely to improve English.

Latest completed batch:

27. `பாலைவன ரோஜா` — scans **189–193 / printed 180–184** — **PASS**
28. TOC `புரட்சிப்படம்` / opening `புரட்சிப் படம்` — scans **194–198 / printed 185–189** — **PASS**
29. `திடுக்கிடும் கதை` — scans **199–204 / printed 190–195** — **PASS**
30. `கடைசிக் கட்டம்` — scans **205–210 / printed 196–201** — **PASS**

### Latest completed Story 27 — `பாலைவன ரோஜா`

- workspace: `stories/palaivana-roja/`
- English: `translations/en/palaivana-roja.md`
- review: `TRANSLATION_REVIEW.md`
- all **5** source-page markers preserved
- physical continuations **191→192** and **192→193** remain traceable
- source-bold opening `நாம்` / `கந்தையா`, college ambitions, clerk reversal, constitutional quotation and desert-rose conclusion remain complete
- queue forms including `ஜாக்கையை`, `மேடனிக் காட்சி`, `மாறுத புகழ்`, `அத்திம்பேர்`, and `வெள்ளெருக்கை` handled conservatively
- result: **PASS**
- Tamil source changed during translation: **No**

### Latest completed Story 28 — TOC `புரட்சிப்படம்` / opening `புரட்சிப் படம்`

- workspace: `stories/puratchip-padam/`
- English: `translations/en/puratchip-padam.md`
- review: `TRANSLATION_REVIEW.md`
- all **5** source-page markers preserved
- physical continuations **194→195**, **195→196**, **196→197**, and **197→198** remain traceable
- TOC/opening-heading variance remains explicitly preserved
- two publicity slogans and source-bold `செவ்வானம்`, `தயாரிப்பு பரமசிவானந்தம்`, `படம் முற்றிற்று—வணக்கம்` remain represented
- final two-censor-cut punchline remains complete
- result: **PASS**
- Tamil source changed during translation: **No**

### Latest completed Story 29 — `திடுக்கிடும் கதை`

- workspace: `stories/thidukkidum-kathai/`
- English: `translations/en/thidukkidum-kathai.md`
- review: `TRANSLATION_REVIEW.md`
- all **6** source-page markers preserved
- standalone source note and `காதல் கதை` / `வீரக்கதை` subsection structure preserved
- Pyramus–Thisbe sequence, unnamed heroic/political parable and final staircase-key reveal remain complete
- source `மல்பெரி` / `மல்பரி` variation documented rather than used to rewrite Tamil
- result: **PASS**
- Tamil source changed during translation: **No**

### Latest completed Story 30 — `கடைசிக் கட்டம்`

- workspace: `stories/kadaisi-kattam/`
- English: `translations/en/kadaisi-kattam.md`
- review: `TRANSLATION_REVIEW.md`
- all **6** source-page markers preserved
- physical continuations **205→206**, **207→208**, **208→209**, and **209→210** remain traceable
- source-bold `டாக்டர் பாபு` / `மஞ்சுளாவை`, Kokila letter and two-line sign-off remain structurally represented
- courtroom confession, shooting and stage-company reveal remain complete
- result: **PASS**
- Tamil source changed during translation: **No**

## NEXT ACTIVITY — STORY 31

Story 31 — **`அய்யோ ராஜா!`**:

- canonical workspace: `stories/ayyo-raja/`
- printed pages: **202–208**
- anthology scans: **211–217**
- boundary witness: scan **218**, opening Story 32 **`விஷம் இனிது`**
- Tamil audit: **PASS — 7 / 7 verified**
- English target: `stories/ayyo-raja/translations/en/ayyo-raja.md`
- translation review target: `stories/ayyo-raja/TRANSLATION_REVIEW.md`

Process **one story per activity** unless the user explicitly expands the translation batch.

## Expected closure after Story 31

After `அய்யோ ராஜா!` translation/review is complete:

- English translation complete: **31 / 37**
- pending: **6 / 37**
- next target: Story 32 — **`விஷம் இனிது`**
- Story 32 printed pages: **209–215**
- Story 32 scans: **218–224**
- Story 32 boundary witness: scan **225**, opening Story 33 **`வேணியின் காதலன்`**

Update the story README, root README, `ENGLISH_TRANSLATION_PROGRESS.md`, this handover and `NEXT_CHAT_PROMPT.md`, then re-fetch live `main` before declaring closure.

## Phase guard

English translation does not authorize modernization, republication, adaptation or replacement of the canonical Tamil source layer.