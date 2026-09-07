# Final Tamil / Source Release Audit — 1987 `கலைஞர் சொன்ன குட்டிக் கதைகள்`

Audit date: **2026-09-07**  
Controlling source: `TVA_BOK_0065566_கலைஞர்_சொன்ன_குட்டிக்_கதைகள்_1987.pdf`  
SHA-256: `29c986812f95c43105eec4b38fa9e02c3c4f66cf3c4e8a686b81dd28c1164f0f`

## Result — PASS / Tamil-source phase CLOSED

The collection-wide final consistency gate is complete.

Release state:

- source headings: **25 / 25 PASS**;
- canonical-identity routing: **25 / 25 COMPLETE**;
- distinct identities: **23**;
- witness-only identities: **2**;
- L1 scans **5–19**: **15 / 15 COMPLETE**;
- L2 scans **20–34**: **15 / 15 COMPLETE**;
- L3 scans **35–49**: **15 / 15 COMPLETE**;
- story-bearing physical scans **5–49**: **45 / 45 Pass 1 + independent Pass 2 COMPLETE**;
- scan 50: **verified blank/damaged terminal non-story leaf**;
- unresolved 1987 Tamil/source or historical-glyph locations: **0**;
- next workflow phase: **English translation**.

## Layers reconciled

The final gate reconciled the durable collection controls against the closed story/witness layers:

- `TITLE_GLYPH_REAUDIT_2026-09-06.md`;
- `RETROSPECTIVE_GLYPH_REAUDIT_L1_L2_2026-09-07.md`;
- the L1, L2 and L3 lexical/historical-glyph ledgers;
- `indexes/story-inventory.md` and `indexes/scan-map.md`;
- story/witness README status controls;
- story-local page maps, page/section structure, Tamil source audits and historical-glyph audits where the final reconciliation required direct exception checking;
- shared-page routing and terminal scan-50 disposition.

No new source-text reading was introduced by this release audit. Already verified source wording remains controlled by the physical 1987 scan and the completed two-pass records.

## Final-audit consistency corrections

The audit found **three stale status/control statements**, all outside the verified Tamil text itself. They were synchronized to the already-completed witness records:

1. `stories/jaadi-kutti-poduma/README.md` still called the 1987 heading `அரசாபிமானக் கதை` and still described its lexical/glyph work as needing review. The current verified 1987 witness controls prove the heading **`அராபியக் கதை`**, **2 / 2 pages verified**, historical-glyph Pass 2 **2 / 2 PASS**, unresolved **0**.
2. `stories/jaadi-kutti-poduma/witnesses/1987-kalaignar-sonna-kuttik-kathaigal/VARIANT_COMPARISON.md` still carried an old deferred/open lexical-comparison note. It is now synchronized to the completed witness transcription and glyph audit.
3. `stories/kuruvi-rameswaram/README.md` still described the 1987 witness lexical/glyph layer as `OPEN / NEEDS REVIEW`. The witness-local README/audit controls already record **PASS**, unresolved **0**; the canonical 2004 Tamil and English remain unchanged.

These were **control-layer corrections only**. No source pixel reopening was necessary because the mismatch was between stale summary text and newer already-verified witness records, not between competing source readings.

## Title and routing invariants

Authoritative 1987 headings include:

- Story 2 **`அராபியக் கதை`**;
- Story 4 **`நாராயணா ! நாராயணா !`**;
- Story 6 **`மூளி மூக்குக்காரன்`**;
- Story 10 **`இரு நிழல்கள்`** — not the earlier misread `இரு நிகழ்வுகள்`.

The Story-10 repository directory remains `stories/iru-nigazhvugal/` only for path continuity; the source-facing title is `இரு நிழல்கள்`.

Sensitive historical-type title forms in `தென்னை`, `தெனாலிராமன்`, `அகத்திணை`, and `பூனை` remain as verified.

## Witness-only routing — PASS

Two 1987 identities remain additional witnesses rather than duplicate canonicals:

- Story 2 `அராபியக் கதை` → canonical `ஜாடி குட்டி போடுமா?` controlled by the 2008 edition;
- Story 11 `குருவி ராமேஸ்வரம்` → canonical `குருவி ராமேஸ்வரம்` controlled by the 2004 edition.

Their 1987 witness transcriptions and historical-glyph checks are closed, while the controlling canonical Tamil and existing canonical English layers remain unchanged.

During the 1987 English phase, those two source identities must receive **witness-local English translations** if translated; they must not overwrite the controlling canonical English from the other editions.

## Historical batch-state note

The L2 ledger correctly records Story 18 `ஜெயத்ரதனின் வீழ்ச்சி` as partial/open **at the moment L2 closed**, because only lower scan 34 belonged to L2. That historical batch statement is preserved as provenance, not treated as a current stale state. Story 18 was completed and closed in L3 through upper scan 37.

Likewise, older intake/batch records remain historical snapshots and are not rewritten merely because later phases advanced.

## Two-pass historical-glyph gate — PASS

Across the three 15-scan lexical/glyph batches, every story-bearing physical scan was subject to:

1. direct source-faithful Pass 1;
2. independent native/high-resolution Pass 2 checking at minimum  
   `ணா / ணை / ணொ / ணோ / லை / ளை / றா / றொ / றோ / னா / னை / னொ / னோ`
   plus suspicious historical-type clusters.

No global replacement was authorized or used as a substitute for page-level source proof. Source spelling, grammar, compounds, spacing and punctuation remain unnormalized where the scan supports them.

## Release decision

**1987 Tamil/source phase: CLOSED.**

The next phase is **English translation**, tracked at:

`collections/1987-kalaignar-sonna-kuttik-kathaigal/ENGLISH_TRANSLATION_PROGRESS.md`

Repository workflow rule: after a Tamil/source phase is fully closed, English translation becomes the automatic next activity unless the user explicitly pauses, redirects, defers or excludes English.

First English target: **Story 1 — `மன்னனும் குருவியும்!`**.

Do not routinely reopen closed Tamil pages or witness layers. If English translation exposes genuinely new or stronger source evidence, reopen only the affected Tamil coverage and propagate the correction through all dependent controls before resuming that span.
