# English Re-Audit Guide — 1977 Anthology

This guide defines the post-Tamil-re-audit verification of the already-complete English translations for the 1977 anthology `கலைஞர் கருணாநிதியின் சிறுகதைகள்`.

## 1. Purpose and authority

This is a **verification and repair phase, not a retranslation project**.

Authority order:

1. live GitHub `main`;
2. the final canonical Tamil assembly under `stories/<slug>/sections/`, after the 2026 Tamil dual-gate closure;
3. the verified per-scan Tamil page records under `stories/<slug>/pages/` for physical page anchoring;
4. story-local Tamil audit / `RE_AUDIT_2026.md` / possible-error disposition;
5. the existing English translation;
6. `ENGLISH_TRANSLATION_GUIDE.md`.

The controlling 1977 PDF is **not** routinely reopened during English review. Reopen the source scan only if English review exposes a plausible Tamil-source problem. Tamil must never be changed from English expectation alone.

No outside edition, web source, biography, dictionary-driven normalization or general knowledge may silently override the final canonical Tamil.

## 2. Five re-audit gates

### E1 — completeness and physical-page alignment

For each story:

- compare the complete English file with the final canonical Tamil;
- verify every Tamil story span is represented once and in order;
- verify nothing is omitted, duplicated, moved or added as story content;
- use verified Tamil page records as the physical boundary authority;
- verify English source-page markers sit at the same physical transitions;
- verify split words/sentences across page boundaries remain traceable;
- verify title, verse/display blocks, letters, dialogue structure, ending furniture and exclusion of the next story;
- record any English correction needed only for completeness/alignment.

### E2 — meaning fidelity

Sentence-by-sentence, verify that English preserves the final Tamil meaning, agency, tense/aspect, negation, quantities, relationships, rhetoric, irony and ambiguity.

Priority rechecks:

- every Tamil location changed during the 2026 dual-gate programme;
- source-odd Tamil deliberately retained by the Tamil audit;
- pronoun/subject references;
- figurative language;
- dialogue and reported speech;
- numbers, dates, names and relationships.

No interpretive embellishment or smoothing may replace what the Tamil actually says.

### E3 — terminology and cultural consistency

Across the anthology, verify consistent treatment of:

- personal names and honorifics;
- kinship terms;
- social/political/cultural vocabulary;
- religious references;
- institutions and titles;
- transliteration choices;
- repeated idioms, concepts and quoted terms.

Consistency must not erase story-specific source meaning.

### E4 — English quality without meaning drift

Review grammar, punctuation, readability, tense consistency, pronoun clarity, dialogue flow and accidental literalism.

Changes are allowed only when they preserve the E2-approved meaning. Style improvement is subordinate to fidelity.

### E5 — final bilingual approval

After E1–E4:

- compare final English against final Tamil one last time;
- ensure all earlier repairs are synchronized;
- ensure no unresolved English issue remains;
- confirm page traceability and difficult-term documentation;
- mark the story final `PASS`.

The anthology re-audit closes only at **37/37 E5 PASS**.

## 3. Phase order

Default execution is **gate-wide**:

1. complete E1 for Stories 1–37;
2. then E2 for Stories 1–37;
3. then E3;
4. then E4;
5. then E5.

Process **one story per activity** unless the user explicitly expands the batch.

This order makes E3 anthology-wide consistency review meaningful and prevents late E1/E2 discoveries from invalidating already-finished downstream gates.

## 4. Story-local durable record

Each story receives:

`stories/<slug>/ENGLISH_REAUDIT_2026.md`

The record must state:

- Tamil authority used;
- English file reviewed;
- gate coverage;
- physical-page boundary checks for E1;
- corrections made, if any;
- unresolved issues;
- whether Tamil/source was reopened;
- current next gate / next story.

`TRANSLATION_REVIEW.md` should be synchronized when a gate closes or a repair changes the English.

## 5. Repair rules

- Repair English only when the final Tamil supports the repair.
- Do not modify Tamil merely to improve English.
- If a possible Tamil defect is exposed, stop that span and reopen the exact Tamil source under `SHORT_STORY_PROCESSING_GUIDE.md`.
- If the Tamil changes after source verification, synchronize all dependent English and controls before continuing.
- If the English is already correct, record **0 repairs** rather than rewriting for preference.

## 6. Tracker

Anthology progress is recorded in `ENGLISH_REAUDIT_PROGRESS.md`.

A story gate is one of:

- `PENDING`
- `IN PROGRESS`
- `PASS`
- `NEEDS REVIEW`

Existing `ENGLISH_TRANSLATION_PROGRESS.md` remains the historical translation-completion tracker and is not overwritten by this new QA phase.

## 7. Current scope

This guide currently governs only the 37 stories of the 1977 anthology. It does not automatically reopen English for later collections, additional witnesses, or separately onboarded stories.
