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

The user explicitly authorized English translation and explicitly expanded the latest activity to Stories 5–6.

- total anthology stories: **37**
- complete: **6 / 37**
- pending: **31 / 37**
- needs review: **0**
- next target: **Story 7 — `சங்கிலிச்சாமி`**

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

For all six, the English file and story-local `TRANSLATION_REVIEW.md` are committed, source-page markers are complete, review queues were read and respected, and canonical Tamil was **not changed** merely to improve English.

### Latest completed Story 5 — `குப்பைத்தொட்டி`

- workspace: `stories/kuppai-thotti/`
- English: `translations/en/kuppai-thotti.md`
- review: `TRANSLATION_REVIEW.md`
- scan-42 four-line prayer/verse remains a display block
- scan-45 three isolated quoted lines remain isolated
- unusual verified readings such as `போதுதானு`, `மனமனவென்று`, `சபரகூட மஞ்சமாகி`, `தூராற்றம்`, `வந்து உண்மைதான்`, `போனேனோ`, and `வயிறாச் சோறின்றி` were handled conservatively and documented
- result: **PASS**
- Tamil source changed during translation: **No**

### Latest completed Story 6 — `சந்தனக்கிண்ணம்`

- workspace: `stories/santhana-kinnam/`
- English: `translations/en/santhana-kinnam.md`
- review: `TRANSLATION_REVIEW.md`
- scans 48–50 long martial poem preserved as a continuous display
- scan-51 Vijayā seven-line gift inscription preserved
- source emphasis on `மார்பு காட்டி!` preserved semantically
- standalone closing transition `ஆனால்,` remains structurally separate
- unusual verified forms including `திராவிட உட்கல வங்க`, `கிலியும்`, `மோழைக்குப் பெயர் போர்வீரனும்!`, `மோகனத்திலே`, `கழுதை தேய்ந்து கட்டெறும் பாயிற்று!`, `தோழி யளித்தது`, and `தயாரா யிருக்கிறான்` were not silently normalized
- result: **PASS**
- Tamil source changed during translation: **No**

## NEXT ACTIVITY — STORY 7

Story 7 — **`சங்கிலிச்சாமி`**:

- canonical workspace: `stories/sangilichami/`
- printed pages: **48–59**
- anthology scans: **57–68**
- boundary witness: scan **69**, opening Story 8 **`கங்கையின் காதல்`**
- Tamil audit: **PASS — 12 / 12 verified**
- English target: `stories/sangilichami/translations/en/sangilichami.md`
- translation review target: `stories/sangilichami/TRANSLATION_REVIEW.md`

The Story 7 human-review queue includes unusual verified forms such as `அஷ்டமா சித்துபுரி`, `துடுக் கடக்கும் தாயனே`, `‘நமப்பார்வதி படே’`, `பிள்ளையில்ல....அருள் தேவை`, `செக்கச் செவேன்னு`, `மூடாத்மா ஞானத்மாவாக`, `கருவாடு களவு கொடுத்த பாப்பாத்தி`, `தவறுக என்னை மதிக்காதீர்`, `தடியன் தானு?`, and `கொலைகாரனுக்கிவிட்டாயே`. Read the complete queue before translating and preserve the current verified Tamil conservatively.

Process **one story per activity** unless the user explicitly expands the translation batch.

## Expected closure after Story 7

After `சங்கிலிச்சாமி` translation/review is complete:

- English translation complete: **7 / 37**
- pending: **30 / 37**
- next target: Story 8 — **`கங்கையின் காதல்`**
- Story 8 printed pages: **60–63**
- Story 8 scans: **69–72**
- Story 8 boundary witness: scan **73**, opening Story 9 **`தாய்மை`**

Update the story README, root README, `ENGLISH_TRANSLATION_PROGRESS.md`, this handover and `NEXT_CHAT_PROMPT.md`, then re-fetch live `main` before declaring closure.

## Phase guard

English translation does not authorize modernization, republication, adaptation or replacement of the canonical Tamil source layer.