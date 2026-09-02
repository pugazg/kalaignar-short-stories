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
- English final QA: `ENGLISH_TRANSLATION_FINAL_QA.md`
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

## Durable anthology milestones

The 1977 anthology now has all archival/translation control layers closed:

1. **Tamil source transcription/audit — COMPLETE: 37 / 37 stories**, scans **10–259 / printed pages 1–250**, with **0 blocked / 0 unresolved story text**;
2. **visual fidelity — COMPLETE: 37 / 37 stories**, with **0 pending / 0 needs recheck**;
3. **English translation/review — COMPLETE: 37 / 37 stories**, with **0 pending / 0 needs review**; and
4. **English final structural/control QA — PASS**, recorded in `ENGLISH_TRANSLATION_FINAL_QA.md`.

All 37 stories have story-local `visual-fidelity.md`, `translations/en/<slug>.md`, and `TRANSLATION_REVIEW.md` records with final result `PASS` or `PASS — corrected` as applicable to the source layer.

English remains a separate, non-authoritative transformation layer. The verified Tamil assembly remains authoritative and must not be altered merely to improve English.

## Final English batch

The user explicitly expanded the final translation activity to all remaining stories:

35. `சுமந்தவள்` — scans **239–249 / printed 230–240** — **PASS**
36. TOC `சித்தார்த்தன்` / opening `சித்தார்த்தன் சிலை` — scans **250–252 / printed 241–243** — **PASS**
37. `நுனிக்கரும்பு` — scans **253–259 / printed 244–250** — **PASS**

### Story 35 — `சுமந்தவள்`

- workspace: `stories/sumanthaval/`
- English: `translations/en/sumanthaval.md`
- review: `TRANSLATION_REVIEW.md`
- all **11** source-page markers preserved
- physical continuations **243→244**, **244→245**, and **247→248** remain traceable
- narrator/mother framing, embedded Maragatham–Soundari story, motherhood/beauty conflict, armed confrontation and diagnosis ending remain complete
- source-sensitive forms including `களித்துப்போய்`, source pronoun `அவள் உள்ளத்தில்`, `முழுங்கால்`, `சன சுரத்தை`, `மூனையளவு`, `மண்ணுக்கி`, `‘பெட்காபி’`, and `எமை விட்டு எச்சில் இலையே!` handled conservatively
- result: **PASS**
- Tamil source changed during translation: **No**

### Story 36 — TOC `சித்தார்த்தன்` / opening `சித்தார்த்தன் சிலை`

- workspace: `stories/siddharthan-silai/`
- English: `translations/en/siddharthan-silai.md`
- review: `TRANSLATION_REVIEW.md`
- all **3** source-page markers preserved
- exact **251→252** physical mid-speech continuation remains traceable
- TOC/opening-heading variance preserved exactly
- idealized opening, shrine lament, apparent Buddha-statue speech, husband reveal and final critique remain complete
- source-sensitive forms including `கெண்டை`, `இரு கிழமை`, `மின்னாட்டி`, `அவனிக்கு`, and `துணவியிடம்` handled conservatively
- no outside doctrinal or biographical explanation inserted
- result: **PASS**
- Tamil source changed during translation: **No**

### Story 37 — `நுனிக்கரும்பு`

- workspace: `stories/nunikkarumbu/`
- English: `translations/en/nunikkarumbu.md`
- review: `TRANSLATION_REVIEW.md`
- all **7** source-page markers preserved
- opening Bharathidasan quotation retained as a three-line verse block
- exact **257→258** `உள்ளங்` → `களைக்` continuation remains traceable
- Arulnambi’s cultural status/age-denial, Amudha fixation, phone and dinner sequence, family return and final `தாத்தா` reversal remain complete
- opaque `நாறுவது` preserved conservatively as transliterated `naaruvathu` rather than silently converted to an assumed ordinal
- scan **260** independently confirmed as anthology back cover and excluded from story text
- result: **PASS**
- Tamil source changed during translation: **No**

## Final structural/control QA

A post-translation QA pass has now been completed and recorded in `ENGLISH_TRANSLATION_FINAL_QA.md`.

The QA independently checked the completed English phase against the pre-English visual-fidelity baseline and verified that:

- all **37** anthology story workspaces have one English file under `translations/en/`;
- all **37** have a story-local `TRANSLATION_REVIEW.md`;
- the tracker and control files agree on **37 / 37 PASS**, **0 pending**, **0 needs review**;
- the title variances `புரட்சிப்படம்` ↔ `புரட்சிப் படம்` and `சித்தார்த்தன்` ↔ `சித்தார்த்தன் சிலை` remain preserved;
- scan **260** remains the verified back-cover boundary;
- no canonical Tamil text was changed by the QA pass.

QA result: **PASS**.

## Post-completion source correction — Story 29 English page anchoring

On **2026-09-02**, downstream Digital Library Wave-2 ingestion exposed a provenance defect in `stories/thidukkidum-kathai/translations/en/thidukkidum-kathai.md`.

The six English markers 199–204 were present and ordered, but the verified Tamil page records proved that content from scan **200** onward was anchored one marker too early and the scan-204 marker section contained no story prose. English prose itself was complete.

Correction scope:

- pre-correction source checkpoint: `a9b333f12128686785ee981f97313a64af12e29b`;
- pre-correction English blob: `0547de49e20f8ff96a5be5fb6a683d2b5b661d1e`;
- corrected English blob: `6e321b1b333d3d1c2bbc598cc73e6f6bd6aeae1d`;
- English prose changed: **No**;
- Tamil changed: **No**;
- title/note/headings changed: **No**;
- marker positions re-anchored: **Yes**;
- Story-29 translation review: **PASS after re-verification**.

A Story-29 boundary manifest and generic `scripts/validate-english-page-anchors.py` guard now verify content-boundary anchoring without assuming paragraph-count equality. The pre-correction shifted pattern fails this guard; the corrected mapping passes.

The earlier downstream Wave-2 source pin `a9b333f12128686785ee981f97313a64af12e29b` is obsolete after this repair. **Wave 2 must recompute the 37-story source freeze from the newer live `main`; no Digital Library implementation is part of this source correction.**

## Final phase state

- anthology stories: **37**
- Tamil source complete: **37 / 37**
- visual fidelity complete: **37 / 37**
- English translation complete: **37 / 37**
- English final structural/control QA: **PASS**
- English pending: **0**
- English needs review: **0**
- story-level unresolved source text: **0**
- final story boundary: scan **259 / printed page 250**
- scan **260**: verified anthology back cover

## Future continuation rule

There is **no pending anthology English story or English final-QA activity**. Do not restart Story 35, 36 or 37 or repeat the final QA from an older prompt.

If future work is explicitly authorized:

1. fetch live `main` first;
2. treat the 37/37 Tamil, visual, English and final-QA closure as authoritative unless newer repository evidence says otherwise;
3. if an English revision suggests a Tamil source problem, reopen that exact Tamil span against the controlling scan under `SHORT_STORY_PROCESSING_GUIDE.md` before changing any source or translation layer;
4. preserve the TOC/opening-title differences `புரட்சிப்படம்` ↔ `புரட்சிப் படம்` and `சித்தார்த்தன்` ↔ `சித்தார்த்தன் சிலை`;
5. do not begin a new phase such as modernization, adaptation, republication or release packaging without explicit authorization.

## Phase guard

English translation and final QA completion do not authorize modernization, republication, adaptation or replacement of the canonical Tamil source layer.
