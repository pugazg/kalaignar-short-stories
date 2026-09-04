# HANDOVER — Kalaignar Short Stories Archive

## Repository

- Repository: `pugazg/kalaignar-short-stories`
- Branch: `main`
- Story workflow: `SHORT_STORY_PROCESSING_GUIDE.md`
- Collection workflow: `COLLECTION_SOURCE_GUIDE.md`
- Text fidelity: `TEXT_FIDELITY_CHECK_GUIDE.md` / `TEXT_FIDELITY_PROGRESS.md`
- 2008 visual fidelity: `collections/2008-kalaignar-sonna-kathaigal/VISUAL_FIDELITY_GUIDE.md` / `VISUAL_FIDELITY_PROGRESS.md`
- English workflow: `ENGLISH_TRANSLATION_GUIDE.md`
- 1977 English tracker: `ENGLISH_TRANSLATION_PROGRESS.md`
- 1977 final QA: `ENGLISH_TRANSLATION_FINAL_QA.md`
- 2008 English tracker: `collections/2008-kalaignar-sonna-kathaigal/ENGLISH_TRANSLATION_PROGRESS.md`
- 2008 final QA: `collections/2008-kalaignar-sonna-kathaigal/ENGLISH_TRANSLATION_FINAL_QA.md`

## LIVE MAIN IS AUTHORITATIVE

Always fetch live `main` first and preserve newer durable work. Repository files reachable from live `main`, not chat memory or copied checkpoints, are the durable state. Source PDFs, renders and crops are not committed.

## Permanent source / translation rules

- controlling scan first; no silent modernization or normalization;
- verified canonical Tamil is authoritative for English;
- running headers and printed page numbers are page furniture, not body text;
- shared physical scans preserve exact story boundaries;
- source-supported corrections propagate through page, assembly, audit/review and dependent layers;
- `POSSIBLE_ERRORS_FOR_REVIEW.md` is a human-review queue, not proof of error;
- English source markers use exactly `<!-- source scan N; printed page M -->`;
- boundary notes belong in separate HTML comments;
- marker presence/order alone is insufficient: actual translated content boundaries must align to verified Tamil page records.

## Closed 1977 anthology

`கலைஞர் கருணாநிதியின் சிறுகதைகள்` remains fully closed:

- Tamil source **37 / 37**;
- visual fidelity **37 / 37**;
- English translation/review **37 / 37**;
- final English structural/control QA **PASS**;
- unresolved story text **0**;
- scan **260** verified back cover.

Story 29 `திடுக்கிடும் கதை` retains the later marker-only provenance correction and strengthened page-anchor regression record. Obsolete Wave-2 pin `a9b333f12128686785ee981f97313a64af12e29b` must not be reused.

## 2008 collection — ALL AUTHORIZED ARCHIVAL / ENGLISH PHASES CLOSED

Collection: **கலைஞர் சொன்ன கதைகள்**  
Workspace: `collections/2008-kalaignar-sonna-kathaigal/`  
Controlling source: `TVA_BOK_0065857_கலைஞர்_சொன்ன_கதைகள்.pdf`

- represented edition: **Second Edition, December 2008**;
- PDF scans: **82**;
- story text: scans **9–81 / printed pages 7–79**;
- scan **82**: verified back cover, no further story text;
- Tamil source: **40 / 40 complete**, 0 blocked / 0 unresolved;
- word-by-word text fidelity: **40 / 40 complete — 19 PASS / 21 PASS — corrected**;
- visual fidelity: **40 / 40 PASS**;
- English translation/review: **40 / 40 PASS**;
- English pending: **0**;
- English `NEEDS REVIEW`: **0**;
- English final structural/control QA: **PASS**;
- canonical Tamil changed during English work or final QA: **No**.

Durable 2008 final-QA record:

`collections/2008-kalaignar-sonna-kathaigal/ENGLISH_TRANSLATION_FINAL_QA.md`

## 2008 English batching history

- Stories **1–4**: completed individually;
- Stories **5–14**: **10 / 10 PASS**;
- Story **15**: completed individually;
- Stories **16–25**: **10 / 10 PASS**;
- user-expanded final iteration Stories **26–40**: **15 / 15 PASS**.

Every 2008 story has:

- complete English under `translations/en/`;
- story-local `TRANSLATION_REVIEW.md` with result **PASS**;
- synchronized story README;
- source-marker sequence recorded;
- actual physical content-boundary alignment independently checked against verified Tamil page records during story review;
- source-significant final `*` preserved;
- no Tamil change caused merely by translation.

## Preserved 2008 title variances

Nine TOC/opening-heading differences remain source facts and must not be normalized:

1. Story 2 — `ஐஸ்கட்டி` ↔ `ஐஸ் கட்டி`;
2. Story 11 — `சாவிதான் இல்லை` ↔ `சாவி தான் இல்லை`;
3. Story 24 — `வெண்ணெய் உருகுது வெயிலில்!` ↔ `வெண்ணெய் உருகுது வெயிலில்`;
4. Story 27 — `எடுக்கவோ கோக்கவோ!` ↔ `எடுக்கவோ கோக்கவோ`;
5. Story 28 — `அந்த நாள் வந்திலை...` ↔ `அந்த நாள் வந்திலை!`;
6. Story 29 — `பனித் துளியில் பனைமரம்` ↔ `பனித்துளியில் பனை மரம்`;
7. Story 35 — `தும்... பம்... தீம்... தோம்` ↔ `தும் பம் தீம் தோம்`;
8. Story 36 — `நல்லவழியும் நல்ல வழியும்` ↔ `நல்வழியும் நல்ல வழியும்`;
9. Story 39 — `நன்றி சொல்லும் நேரம்...` ↔ `நன்றி சொல்லும் நேரம்`.

## Final 2008 English QA closure

The final structural/control QA used the closed visual-fidelity checkpoint as baseline and reviewed the completed English/control state. The baseline→English-closure comparison is ahead by **172 commits**, behind by **0**, and accounts for the expected English translation, translation-review and README updates across all forty 2008 story workspaces.

The QA confirms:

- English artefacts: **40 / 40**;
- story-local translation reviews: **40 / 40**;
- tracker disposition: **40 PASS / 0 pending / 0 NEEDS REVIEW**;
- physical page-provenance control retained through story-local reviews;
- final source-significant `*` policy retained;
- nine title variances retained;
- Story 40 opens and closes on scan **81 / printed page 79**;
- scan **82** remains back-cover matter only;
- collection/root controls agree on the **40 / 40** material completion state;
- canonical Tamil changed by final QA: **No**.

**Final result: PASS — 2008 English final structural/control QA complete.**

## Current exact next activity

**No routine archival or English-translation activity remains in the currently authorized 2008 scope.**

Do not automatically begin modernization, normalization, adaptation, republication, release packaging, Digital Library onboarding, or another downstream phase. Wait for explicit user authorization of a new scope.

If future work exposes a possible source or page-provenance defect, reopen only the exact affected span against the controlling source and propagate any source-supported correction through all dependent layers.
