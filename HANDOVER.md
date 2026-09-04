# HANDOVER — Kalaignar Short Stories Archive

## Repository

- Repository: `pugazg/kalaignar-short-stories`
- Branch: `main`
- Story workflow: `SHORT_STORY_PROCESSING_GUIDE.md`
- Collection workflow: `COLLECTION_SOURCE_GUIDE.md`
- Text-fidelity workflow: `TEXT_FIDELITY_CHECK_GUIDE.md`
- Text-fidelity tracker: `TEXT_FIDELITY_PROGRESS.md`
- 1977 visual-fidelity workflow/tracker: `VISUAL_FIDELITY_CHECK_GUIDE.md` / `VISUAL_FIDELITY_PROGRESS.md`
- 2008 visual-fidelity workflow/tracker: `collections/2008-kalaignar-sonna-kathaigal/VISUAL_FIDELITY_GUIDE.md` / `collections/2008-kalaignar-sonna-kathaigal/VISUAL_FIDELITY_PROGRESS.md`
- English-translation workflow: `ENGLISH_TRANSLATION_GUIDE.md`
- Source PDFs / renders / crops are **not** committed.

## Authoritative-state rule

Always fetch live `main` first and preserve newer durable work.

## Permanent source rules

- controlling scan first; no silent modernization of spelling, punctuation, grammar, sandhi, names or source anomalies;
- running headers / printed page numbers are page furniture, not body text;
- `POSSIBLE_ERRORS_FOR_REVIEW.md` is a human-review queue, not proof of error;
- source-supported textual corrections propagate through page, assembly, audit/review and dependent layers;
- shared physical boundary scans preserve each story's exact source span;
- do not commit controlling PDFs or inspection artefacts.

## Closed 1977 anthology

`கலைஞர் கருணாநிதியின் சிறுகதைகள்` remains durably closed:

- Tamil source: **37 / 37 complete**, 0 blocked / 0 unresolved;
- visual fidelity: **37 / 37 complete**;
- English translation/review: **37 / 37 complete**;
- final English structural/control QA: **PASS**;
- scan **260**: verified back cover.

Story 29 `திடுக்கிடும் கதை` retains its later marker-only provenance correction. Canonical Tamil and English prose were unchanged; obsolete Wave-2 pin `a9b333f12128686785ee981f97313a64af12e29b` must not be reused.

## 2008 collection — closed Tamil source pass

Collection: **கலைஞர் சொன்ன கதைகள்**

Workspace: `collections/2008-kalaignar-sonna-kathaigal/`

Controlling source: `TVA_BOK_0065857_கலைஞர்_சொன்ன_கதைகள்.pdf`

- author: **டாக்டர் கலைஞர் மு. கருணாநிதி**;
- represented edition: **Second Edition, December 2008**;
- source SHA-256: `1b2bf86892717776b1b3dc7fcb18dc146d5bfd0d60986509dc9cbbf5f235444b`;
- PDF scans: **82**;
- contents entries: **40**;
- story text: scans **9–81 / printed pages 7–79**;
- scan **82**: verified back cover, no further story text;
- canonical workspaces / Tamil source complete: **40 / 40**;
- source pending: **0 / 40**;
- blocked / unresolved source story text: **0**;
- English from this collection: **0 / 40**.

Nine TOC/opening-heading differences remain registered and must not be normalized: Stories **2, 11, 24, 27, 28, 29, 35, 36, 39**.

## 2008 collection — closed word-by-word text fidelity

Text fidelity is durably complete:

- complete: **40 / 40**;
- `PASS`: **19**;
- `PASS — corrected`: **21**;
- pending: **0**;
- needs recheck: **0**;
- unresolved fidelity issues: **0**;
- story-local `text-fidelity.md`: **40 / 40**.

All forty stories were directly re-read against the controlling scans for every word, spelling/sandhi form, joined/separated form, punctuation, quotation mark, paragraph structure and physical page join. All confirmed corrections are synchronized through affected page records, Tamil assemblies, audits and review queues.

## Active phase — 2008 visual fidelity

The user's standing collection batch rule is **10 stories per iteration**.

Collection-specific guide:

`collections/2008-kalaignar-sonna-kathaigal/VISUAL_FIDELITY_GUIDE.md`

Tracker:

`collections/2008-kalaignar-sonna-kathaigal/VISUAL_FIDELITY_PROGRESS.md`

### Current visual-fidelity state

- total stories: **40**;
- complete: **10 / 40**;
- `PASS`: **10**;
- `PASS — corrected`: **0**;
- pending: **30 / 40**;
- needs recheck: **0**;
- unresolved visual-fidelity issues among completed stories: **0**.

### Completed visual iteration 1 — Stories 1–10

Stories **1–10** were directly inspected across source scans **9–27**. All ten are **PASS** with no visual-structure or Tamil wording correction required.

Collection-specific visual policy established during this iteration:

- the recurring boxed story sequence number, vertical gutter rule and opening horizontal title rule are source-visible **collection-design furniture**; document them in story-local visual records but do not inject them into canonical prose;
- the centered single `*` before the next story is a source-significant ending ornament and remains represented;
- exact font, margin and ordinary prose line wrapping are not required;
- meaningful paragraph/dialogue/display structure and physical joins are required.

Story 3's two-line Tirukkural display and Story 10's isolated `கடமை`, `கண்ணியம்`, `கட்டுப்பாடு` display lines were checked and are already preserved.

Story-local `visual-fidelity.md` records now exist for Stories **1–10**.

## Exact next activity — visual fidelity Stories 11–20

Process **Stories 11–20 only** in one iteration:

11. TOC `சாவிதான் இல்லை` / opening `சாவி தான் இல்லை` — lower scan **27 → 28**, next boundary **29**;
12. `கண்ணில் கால்` — scan **29 → upper 30**;
13. `மயில் ராவணன்` — lower **30 → 31**, boundary **32**;
14. `ஜாடி குட்டி போடுமா?` — scan **32 → upper 33**;
15. `ஒண்ணு குடுமா?` — lower **33 → 34 → upper 35**;
16. `அத்திரி பாச்சா` — lower **35 → upper 36**;
17. `செருப்போடு இரு` — lower **36 → upper 37**;
18. `இடிக்குப் பின் மழை` — lower **37 → 38 → upper 39**;
19. `நடக்குமா நடக்காதா?` — lower **39 → 40–41 → upper 42**;
20. `கனியும் கணையும்` — lower **42 → upper 43**.

For each story inspect every registered scan directly plus the boundary witness where needed. Check opening/ending structure, paragraph/dialogue fidelity, verse/display blocks, collection-design furniture, page furniture and all physical joins. Create `stories/<slug>/visual-fidelity.md`. Propagate corrections only if the scan directly supports them. Stop after Story 20; do not begin Story 21 in the same iteration.

## Phase guard

Visual fidelity authorizes source-faithful structural correction only. It does **not** authorize English translation, modernization, adaptation, republication or Digital Library onboarding. English may open only after visual fidelity is closed for the relevant story/collection and the user authorizes that downstream phase.
