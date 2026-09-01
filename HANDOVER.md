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

The user explicitly expanded the latest activity to Stories **31–34**:

- `அய்யோ ராஜா!`
- `விஷம் இனிது`
- `வேணியின் காதலன்`
- `அமிர்தமதி`

Current durable translation state:

- total anthology stories: **37**
- complete: **34 / 37**
- pending: **3 / 37**
- needs review: **0**
- next target: **Story 35 — `சுமந்தவள்`**

English is a separate, non-authoritative transformation layer. The verified Tamil assembly remains authoritative and must not be altered merely to improve English.

Before translating each story:

1. fetch live `main`;
2. read `SHORT_STORY_PROCESSING_GUIDE.md`, `COLLECTION_SOURCE_GUIDE.md`, `ENGLISH_TRANSLATION_GUIDE.md`, `ENGLISH_TRANSLATION_PROGRESS.md`, this handover and `NEXT_CHAT_PROMPT.md`;
3. read the story README, Tamil assembly, audit, `POSSIBLE_ERRORS_FOR_REVIEW.md`, visual-fidelity record and page map;
4. follow the current verified Tamil reading exactly; suspicious queue items are not silent corrections;
5. if translation exposes a likely Tamil issue, reopen it against the controlling scan under the Tamil guide before changing any layer.

## Completed English translations

Stories **1–34** are now **PASS**. For all thirty-four, the English file and story-local `TRANSLATION_REVIEW.md` are committed, source-page markers are complete, review queues were read and respected, and canonical Tamil was **not changed** merely to improve English.

Latest completed batch:

31. `அய்யோ ராஜா!` — scans **211–217 / printed 202–208** — **PASS**
32. `விஷம் இனிது` — scans **218–224 / printed 209–215** — **PASS**
33. `வேணியின் காதலன்` — scans **225–230 / printed 216–221** — **PASS**
34. `அமிர்தமதி` — scans **231–238 / printed 222–229** — **PASS**

### Latest completed Story 31 — `அய்யோ ராஜா!`

- workspace: `stories/ayyo-raja/`
- English: `translations/en/ayyo-raja.md`
- review: `TRANSLATION_REVIEW.md`
- all **7** source-page markers preserved
- physical continuations **212→213**, **214→215**, and **215→216** remain traceable
- Kodambakkam railway-gate opening, Muthamma’s survival context, Raja’s illness, rickshaw journey, Nepal-king roadblock and final doctor scene remain complete
- old-glyph correction **`என்றாள் முத்தம்மா`** respected; provisional `என்றுள்` not reintroduced
- result: **PASS**
- Tamil source changed during translation: **No**

### Latest completed Story 32 — `விஷம் இனிது`

- workspace: `stories/visham-inidhu/`
- English: `translations/en/visham-inidhu.md`
- review: `TRANSLATION_REVIEW.md`
- all **7** source-page markers preserved and all six joins traceable
- Amirtharani’s letter/two-line sign-off and source emphasis preserved
- Rama-temple/diamond plan, suspicion, poison test, Arthol’s death and final `ஆண்டவனை விட ஆலஹாலம் இனிது` contrast remain complete
- `பாஷாணம்` / `ஆலஹாலம்` handled conservatively rather than replaced with unsupported identifications
- result: **PASS**
- Tamil source changed during translation: **No**

### Latest completed Story 33 — `வேணியின் காதலன்`

- workspace: `stories/veniyin-kadhalan/`
- English: `translations/en/veniyin-kadhalan.md`
- review: `TRANSLATION_REVIEW.md`
- all **6** source-page markers preserved
- open speech **226→227**, exact split **227→228**, and **229→230** join remain traceable
- source-corrected **`கூண்டுக் கிளி ஆக்குவேனென்றான்`** respected
- Veni/Kandan/Gundappan history, Surya’s past, her rejected poisoning thought, nursing-ethics decision and final trolley scene remain complete
- result: **PASS**
- Tamil source changed during translation: **No**

### Latest completed Story 34 — `அமிர்தமதி`

- workspace: `stories/amirthamathi/`
- English: `translations/en/amirthamathi.md`
- review: `TRANSLATION_REVIEW.md`
- all **8** source-page markers preserved
- exact joins **234→235** and **236→237** remain traceable
- literary-theft frame, `சுகம் எங்கே?` / `யசோதர காவியம்` embedded narrative and scan-236 quoted description remain complete
- unusual `குதர்களால்`, royal-luxury list, quoted verse and other source-sensitive forms handled conservatively
- alleged literary thieves remain unnamed at the ending exactly as the source does
- result: **PASS**
- Tamil source changed during translation: **No**

## NEXT ACTIVITY — STORY 35

Story 35 — **`சுமந்தவள்`**:

- canonical workspace: `stories/sumanthaval/`
- printed pages: **230–240**
- anthology scans: **239–249**
- boundary witness: scan **250**, opening Story 36
- Story 36 TOC title: **`சித்தார்த்தன்`**
- Story 36 opening heading: **`சித்தார்த்தன் சிலை`**
- Tamil audit: **PASS — 11 / 11 verified**
- English target: `stories/sumanthaval/translations/en/sumanthaval.md`
- translation review target: `stories/sumanthaval/TRANSLATION_REVIEW.md`

Process **one story per activity** unless the user explicitly expands the translation batch.

## Expected closure after Story 35

After `சுமந்தவள்` translation/review is complete:

- English translation complete: **35 / 37**
- pending: **2 / 37**
- next target: Story 36 — TOC **`சித்தார்த்தன்`** / opening **`சித்தார்த்தன் சிலை`**
- Story 36 printed pages: **241–243**
- Story 36 scans: **250–252**
- Story 36 boundary witness: scan **253**, opening Story 37 **`நுனிக்கரும்பு`**

Update the story README, root README, `ENGLISH_TRANSLATION_PROGRESS.md`, this handover and `NEXT_CHAT_PROMPT.md`, then re-fetch live `main` before declaring closure.

## Phase guard

English translation does not authorize modernization, republication, adaptation or replacement of the canonical Tamil source layer.