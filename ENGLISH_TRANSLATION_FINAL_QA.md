# English Translation Final QA — 1977 Anthology

## Scope

This is a **post-translation structural and control-layer QA pass** for the 1977 anthology `கலைஞர் கருணாநிதியின் சிறுகதைகள்`.

It does **not** reopen or rewrite canonical Tamil, and it does not silently re-edit the English translations for style. Its purpose is to verify that the completed English phase is structurally complete, consistently recorded and safe to hand over.

Controlling source:

`TVA_BOK_0064142_கலைஞர்_கருணாநிதியின்_சிறுகதைகள்.pdf`

## Authority

Authority order remains:

1. live GitHub `main`;
2. verified canonical Tamil assemblies;
3. controlling scan when a source issue must be reopened;
4. repository processing/translation guides;
5. story-local audits, visual-fidelity records and translation reviews.

Canonical Tamil remains authoritative.

## QA baseline and reviewed state

- pre-English visual-fidelity closure baseline: `a537f2a41d7bdf21236176a9730c5f62a80e7175`
- English-phase closure reviewed at: `6fa376e10f35fabec01dcf7c08b6edf34a61f31e`
- compare status: reviewed head is **ahead by 163 commits**, with no divergence from the baseline

## Structural checks

### 1. Story-level English artefacts

The baseline→closure comparison shows that each of the **37 anthology story workspaces** gained:

- exactly one canonical English story file under `translations/en/<slug>.md`; and
- exactly one story-local `TRANSLATION_REVIEW.md`.

All 37 story READMEs were also updated during the English phase.

**Result: PASS**

### 2. Translation tracker agreement

`ENGLISH_TRANSLATION_PROGRESS.md` records:

- total anthology stories: **37**
- English translation complete: **37 / 37**
- pending: **0 / 37**
- needs review: **0**
- phase state: **COMPLETE**

All 37 rows are `PASS`.

**Result: PASS**

### 3. Root/control-file agreement

The root README, `ENGLISH_TRANSLATION_PROGRESS.md`, `HANDOVER.md`, and `NEXT_CHAT_PROMPT.md` agree that:

- Tamil source processing is **37 / 37 complete**;
- visual fidelity is **37 / 37 complete**;
- English translation/review is **37 / 37 complete**;
- there is **0 pending** English work and **0 needs review**;
- unresolved anthology story text is **0**.

**Result: PASS**

### 4. Edition-level title variants

The two known anthology title differences remain explicitly preserved rather than normalized:

- TOC `புரட்சிப்படம்` ↔ story-opening heading `புரட்சிப் படம்`;
- TOC `சித்தார்த்தன்` ↔ story-opening heading `சித்தார்த்தன் சிலை`.

**Result: PASS**

### 5. Final physical boundary

The durable source controls remain synchronized through:

- final story `நுனிக்கரும்பு`: scans **253–259 / printed pages 244–250**;
- scan **259**: story ending and closing ornament;
- scan **260**: verified anthology back cover, excluded from story text.

**Result: PASS**

### 6. Source-layer safety

This QA pass made **no changes to canonical Tamil story text** and did not reopen any source reading. The story-local translation reviews remain the governing record for difficult English choices.

**Result: PASS**

## Final QA result

**PASS — anthology English translation structural/control QA is complete.**

Durable state after this QA:

- Tamil source: **37 / 37 complete**
- visual fidelity: **37 / 37 complete**
- English translation/review: **37 / 37 complete**
- English final structural/control QA: **PASS**
- pending English stories: **0**
- English stories needing review: **0**
- unresolved anthology story text: **0**

This QA closure does not authorize modernization, adaptation, republication, release packaging or replacement of the canonical Tamil layer. Any such next phase requires explicit authorization.

## Post-completion correction / QA strengthening — Story 29, 2026-09-02

A downstream Digital Library Bulk Onboarding Wave-2 source-ingestion check found a provenance defect in Story 29 `திடுக்கிடும் கதை` that the original structural QA above did not detect.

### What the original QA missed

The Story-29 English file had all six markers **199–204** present once and in order, so presence/order checks passed. However, comparison with the six verified Tamil page records showed that marker **200** began one physical page too late, markers **201–203** continued that one-page lag, and marker **204** contained no story prose.

The pre-correction English blob was:

`0547de49e20f8ff96a5be5fb6a683d2b5b661d1e`

The English prose itself was complete and in source order. The defect was **physical source-page anchoring only**.

### Source-backed repair

The markers were re-anchored against the verified Tamil page records so that:

- scan **199 / printed 190** ends at English `Namely:`;
- scan **200 / printed 191** begins `“Dear friends! Today you will have to walk to your room...`;
- scan **201 / printed 192** begins `Whose eyes could be sharper than the eyes of lovers?...`;
- scan **202 / printed 193** begins `A lioness that had killed a spotted deer...`;
- scan **203 / printed 194** begins the physical continuation `—together.`;
- scan **204 / printed 195** begins the physical continuation `—the leader of the uprising immediately cried...` and contains the complete translated ending.

Corrected English blob:

`6e321b1b333d3d1c2bbc598cc73e6f6bd6aeae1d`

No English prose, punctuation, title, source note or heading changed. Canonical Tamil changed: **No**.

### Strengthened regression guard

`ENGLISH_TRANSLATION_GUIDE.md` now explicitly distinguishes marker presence/order from content-boundary alignment. A new generic validator, `scripts/validate-english-page-anchors.py`, checks:

- expected marker scan sequence;
- printed-page agreement;
- a non-empty English marker section whenever the verified Tamil page record contains story text;
- the final source page is not an empty translated section;
- optional human-adjudicated boundary anchors without assuming Tamil/English paragraph-count equality.

Story 29 now carries `translations/en/page-anchors.json`, recording human-reviewed Tamil boundary witnesses and corresponding English start/end anchors for all six scans.

### Negative regression check

Applying the strengthened guard to the page-anchor states gives:

1. corrected Story-29 mapping → **PASS**;
2. pre-correction shifted mapping → **FAIL** on page anchoring, including the scan-200 start-boundary mismatch and empty scan-204 translated section;
3. corrected mapping restored → **PASS**.

The failure is page-provenance specific, not a syntax failure or paragraph-count mismatch.

### QA disposition after correction

The original final QA remains valid for anthology completion counts and English prose completeness, but its former marker-presence criterion was insufficient for scan-level provenance. Story 29 has now been re-reviewed under the strengthened criterion.

**Current final QA result: PASS — 37 / 37 English translations remain complete, with Story 29's physical source-page anchoring corrected and re-verified.**
