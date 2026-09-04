# HANDOVER — Kalaignar Short Stories Archive

## Repository

- Repository: `pugazg/kalaignar-short-stories`
- Branch: `main`
- Story workflow: `SHORT_STORY_PROCESSING_GUIDE.md`
- Anthology workflow: `COLLECTION_SOURCE_GUIDE.md`
- Text-fidelity workflow: `TEXT_FIDELITY_CHECK_GUIDE.md`
- Text-fidelity tracker: `TEXT_FIDELITY_PROGRESS.md`
- Visual-fidelity workflow: `VISUAL_FIDELITY_CHECK_GUIDE.md`
- English-translation workflow: `ENGLISH_TRANSLATION_GUIDE.md`
- Source PDFs / renders / crops are **not** committed.

## Authoritative-state rule

Always fetch live `main` first and preserve newer durable work.

## Permanent source rules

- controlling scan first; no silent modernization of spelling, punctuation, grammar, sandhi, names or source anomalies;
- running headers/page numbers are furniture, not body text;
- `POSSIBLE_ERRORS_FOR_REVIEW.md` is a human-review queue, not proof of error;
- source-supported corrections propagate through page, assembly, audit/review and dependent layers;
- shared physical boundary scans preserve each story's exact source span;
- do not commit controlling PDFs or inspection artefacts.

## Closed 1977 anthology

`கலைஞர் கருணாநிதியின் சிறுகதைகள்` remains durably closed:

- Tamil source: **37 / 37 complete**, 0 blocked / 0 unresolved;
- visual fidelity: **37 / 37 complete**;
- English translation/review: **37 / 37 complete**;
- final English structural/control QA: **PASS**;
- scan **260**: verified back cover.

Story 29 `திடுக்கிடும் கதை` retains its later marker-only provenance correction. Canonical Tamil and English prose were unchanged; old Wave-2 pin `a9b333f12128686785ee981f97313a64af12e29b` is obsolete.

## Closed Tamil source pass — கலைஞர் சொன்ன கதைகள்

Collection workspace: `collections/2008-kalaignar-sonna-kathaigal/`

Controlling source: `TVA_BOK_0065857_கலைஞர்_சொன்ன_கதைகள்.pdf`

- printed author: **டாக்டர் கலைஞர் மு. கருணாநிதி**;
- scanned edition: **Second Edition, December 2008**;
- source SHA-256: `1b2bf86892717776b1b3dc7fcb18dc146d5bfd0d60986509dc9cbbf5f235444b`;
- file size: **24,840,000 bytes**;
- PDF scans: **82**;
- contents entries: **40**;
- story text: scans **9–81 / printed 7–79**;
- scan **82**: verified back cover, no further story text;
- relation: **scan = printed page + 2**.

Source-pass state remains:

- canonical workspaces: **40 / 40**;
- Tamil source complete: **40 / 40**;
- Tamil source pending: **0 / 40**;
- blocked / unresolved story text: **0**;
- English from this collection: **0 / 40**.

Nine TOC/opening-heading differences remain registered and must not be normalized: Stories **2, 11, 24, 27, 28, 29, 35, 36, 39**.

## Active phase — word-by-word text fidelity

The user explicitly authorized a new **text-fidelity pass for every word** and retained the **10 stories per iteration** rule.

Permanent rules are in `TEXT_FIDELITY_CHECK_GUIDE.md`. Existing `verified` status is not accepted as proof in this second pass: every active story is re-read directly against the controlling scans, word by word.

### Current progress

- total: **40**
- fidelity complete: **10 / 40**
- `PASS`: **6**
- `PASS — corrected`: **4**
- pending: **30 / 40**
- needs recheck: **0**
- unresolved fidelity issues among completed stories: **0**

### Completed first fidelity iteration — Stories 1–10

1. `அப்படித்தான் சிரிப்பேன்` — scan 9 → top 10 — **PASS**;
2. TOC `ஐஸ்கட்டி` / opening `ஐஸ் கட்டி` — lower 10 → upper 11 — **PASS — corrected**;
3. `தலையில் மலை` — lower 11 → upper 16 — **PASS — corrected**;
4. `வெறும் கை முழம் போடும்` — lower 16 → upper 17 — **PASS**;
5. `கூட்டணி` — lower 17 → upper 18 — **PASS**;
6. `சீற வேண்டாமா?` — lower 18 → upper 19 — **PASS — corrected**;
7. `கழுதையின் கதை` — lower 19 → 20 → upper 21 — **PASS**;
8. `உனக்கு வயதென்ன?` — lower 21 → upper 22 — **PASS**;
9. `தமிழன் என்று சொல்லடா!` — lower 22 → 23–24 → upper 25 — **PASS — corrected**;
10. `கடமை கண்ணியம் கட்டுப்பாடு` — lower 25 → 26 → upper 27 — **PASS**.

### First-batch correction summary

- Story 2: restored `என்னப்பா!`, source `மக்களுக்கு`, and `அரசே!` punctuation;
- Story 3: restored source `அமர்ச்சியப்படுத்தாமல்`, `இயலாதது`, `எடுத்துக் கொள்க!`, and the scan-15 sentence beginning `அடே! அப்படியொரு ஆசையிருந்தால்`;
- Story 6: restored source `ஒரு சீறு சீறி காட்டக்கூடாது என்றா சொன்னேன்.`;
- Story 9: corrected nine word/punctuation mismatches including `உள்ளத்தை`, `தொகுப்பு நூலில்`, `குமரகுருபர்` / `குமரகுருபரை`, and `சொல்லுகிறார்`.

All affected page records, Tamil assemblies, audits and review queues are synchronized. Story-local `text-fidelity.md` records exist for Stories 1–10.

## Exact next activity — text fidelity Stories 11–20

Process **all ten** stories in this iteration and stop after Story 20:

11. TOC `சாவிதான் இல்லை` / opening `சாவி தான் இல்லை` — lower scan **27 → 28**;
12. `கண்ணில் கால்` — scan **29 → upper 30**;
13. `மயில் ராவணன்` — lower **30 → 31**;
14. `ஜாடி குட்டி போடுமா?` — scan **32 → upper 33**;
15. `ஒண்ணு குடுமா?` — lower **33 → 34 → upper 35**;
16. `அத்திரி பாச்சா` — lower **35 → upper 36**;
17. `செருப்போடு இரு` — lower **36 → upper 37**;
18. `இடிக்குப் பின் மழை` — lower **37 → 38 → upper 39**;
19. `நடக்குமா நடக்காதா?` — lower **39 → 40–41 → upper 42**;
20. `கனியும் கணையும்` — lower **42 → upper 43**.

For every story:

1. re-fetch live `main` before source-dependent writes;
2. inspect every registered story span directly, including shared boundary material;
3. compare every word, spelling/sandhi form, punctuation, quotation boundary, paragraph and physical join;
4. if a mismatch exists, verify the surrounding full phrase and propagate the source-supported correction through page, assembly, audit/review and `text-fidelity.md`;
5. if no mismatch exists, create `text-fidelity.md` with `PASS`;
6. update `TEXT_FIDELITY_PROGRESS.md` only after the story is durably closed.

Story 10 closes above Story 11 on scan **27**; exclude the already-closed Story-10 material. Story 20 closes above Story 21 on scan **43**; inspect that shared boundary but do not begin Story 21 in this iteration.

## Phase guard

Text fidelity does not authorize modernization, adaptation, republication, Digital Library onboarding, or English translation. Verified Tamil remains authoritative after source-supported corrections.
