# English Translation Final QA — கலைஞர் சொன்ன கதைகள் (2008)

## Scope

This is the post-translation **structural and control-layer QA** for the 2008 second-edition collection **கலைஞர் சொன்ன கதைகள்**.

It does not reopen canonical Tamil or stylistically re-edit the completed English translations. Its purpose is to verify that the 40-story English layer is structurally complete, page-traceable through its durable review records, internally synchronized, and safe to close.

Controlling source:

`TVA_BOK_0065857_கலைஞர்_சொன்ன_கதைகள்.pdf`

## Authority

1. live GitHub `main`;
2. verified canonical Tamil assemblies and verified `pages/*.md` records;
3. controlling source scan if a source reading must be reopened;
4. repository processing / fidelity / translation guides;
5. story-local audits, page maps, visual-fidelity records and `TRANSLATION_REVIEW.md` records.

Canonical Tamil remains authoritative.

## QA baseline and reviewed closure state

- 2008 visual-fidelity closure baseline: `7e7dcae66948d40cb82182ca8a1bed54000abf64` — `Close 2008 visual fidelity at 40 stories`;
- completed English/control state reviewed at: `570acbbb301d02f37371f21a194bcd36dd58ef82` — `Advance prompt to final 2008 English QA`;
- compare status: reviewed head is **ahead by 172 commits**, **behind by 0**, with the visual-fidelity closure commit as merge base.

The baseline→closure comparison accounts for all forty active 2008 story workspaces and shows that each gained:

- one English story file at `translations/en/<slug>.md`;
- one story-local `TRANSLATION_REVIEW.md`;
- an English-status update in the story README.

Collection/root controls were also advanced during the English phase.

**Result: PASS**

## Structural checks

### 1. Story-level English artefacts — 40 / 40

All **40 / 40** 2008 story workspaces have the expected English translation artefact and story-local translation review. The completed comparison contains no missing story from the registered 40-story collection.

**Result: PASS**

### 2. Translation-review disposition — 40 / 40 PASS

`ENGLISH_TRANSLATION_PROGRESS.md` records:

- total stories: **40**;
- English complete: **40 / 40**;
- `PASS`: **40**;
- pending: **0 / 40**;
- `NEEDS REVIEW`: **0**;
- canonical Tamil changed during English work: **No**.

Every row in the collection tracker is `PASS`.

**Result: PASS**

### 3. Physical source-page provenance

The strengthened requirement in `ENGLISH_TRANSLATION_GUIDE.md` applies: marker presence/order is not by itself proof of page provenance. Each story-local translation review records the physical source span and distinguishes marker order from actual translated content-boundary alignment against the verified Tamil page records.

The collection tracker records all forty verified spans from Story 1 at scan **9 / printed 7** through Story 40 on scan **81 / printed 79**. Shared physical scans and cross-page continuations remain part of those verified spans rather than being forced into non-overlapping TOC ranges.

Direct final-QA re-fetches of the opening, intermediate, and closing control examples confirmed the expected validator-compatible form:

`<!-- source scan N; printed page M -->`

with boundary explanations kept in separate HTML comments. The per-story `TRANSLATION_REVIEW.md` records remain the durable page-boundary adjudication for all forty stories.

Representative rechecked boundary records include:

- Story 1: **9 → 10**, with the quoted reply split at the physical scan boundary;
- Story 10: **25 → 26 → 27**, including the scan-26 → scan-27 squirrel-wound continuation;
- Story 20: **42 → 43**, with the William Tell passage ending and political analogy resuming at the verified transition;
- Story 26: **60 → 61**, with the Prophet's question continuing across the physical boundary;
- Story 27: **61 → 62**, with the Karna/Duryodhana action resuming on scan 62;
- Story 28: **62 → 63 → 64**, including the four-line verse and scan-64 prose continuation;
- Story 30: **65 → 66**, with all three verse/display blocks retained;
- Story 40: **81**, with scan **82** excluded as back-cover matter.

No page-anchor issue is left recorded as pending or `NEEDS REVIEW`.

**Result: PASS**

### 4. Source-significant ending ornament

The visual-fidelity phase established the centered single `*` as the source-significant ending ornament for all forty stories. English translation reviews require and record its preservation. The collection tracker explicitly records the final ornament as retained across the completed English phase.

**Result: PASS**

### 5. TOC / opening-heading variants

All nine known collection title differences remain registered and unnormalized:

1. Story 2 — TOC `ஐஸ்கட்டி` ↔ opening `ஐஸ் கட்டி`;
2. Story 11 — TOC `சாவிதான் இல்லை` ↔ opening `சாவி தான் இல்லை`;
3. Story 24 — TOC `வெண்ணெய் உருகுது வெயிலில்!` ↔ opening `வெண்ணெய் உருகுது வெயிலில்`;
4. Story 27 — TOC `எடுக்கவோ கோக்கவோ!` ↔ opening `எடுக்கவோ கோக்கவோ`;
5. Story 28 — TOC `அந்த நாள் வந்திலை...` ↔ opening `அந்த நாள் வந்திலை!`;
6. Story 29 — TOC `பனித் துளியில் பனைமரம்` ↔ opening `பனித்துளியில் பனை மரம்`;
7. Story 35 — TOC `தும்... பம்... தீம்... தோம்` ↔ opening `தும் பம் தீம் தோம்`;
8. Story 36 — TOC `நல்லவழியும் நல்ல வழியும்` ↔ opening `நல்வழியும் நல்ல வழியும்`;
9. Story 39 — TOC `நன்றி சொல்லும் நேரம்...` ↔ opening `நன்றி சொல்லும் நேரம்`.

**Result: PASS**

### 6. Final physical boundary

The durable source controls agree that:

- Story 39 closes above Story 40 on scan **81 / printed page 79**;
- Story 40 opens and closes on scan **81 / printed page 79**;
- scan **82** is the verified physical back cover and contains no further story text;
- no English Story-40 text is assigned to scan 82.

**Result: PASS**

### 7. Control-file agreement

At the reviewed closure state, the collection English tracker, collection README, collection source metadata, root README, story READMEs, `HANDOVER.md`, and `NEXT_CHAT_PROMPT.md` agree on the material completion state:

- Tamil source: **40 / 40 complete**;
- text fidelity: **40 / 40 complete — 19 PASS / 21 PASS — corrected**;
- visual fidelity: **40 / 40 PASS**;
- English translation/review: **40 / 40 PASS**;
- English pending: **0**;
- English `NEEDS REVIEW`: **0**;
- canonical Tamil changed during English work: **No**.

This QA record becomes the durable statement of the additional final structural/control-QA result.

**Result: PASS**

### 8. Source-layer safety

This QA pass made **no change to canonical Tamil story text**, no translation prose rewrite, and no source-title normalization. Existing human-review queues remain preserved as source-review records and do not represent unresolved English work.

**Result: PASS**

## Final QA result

**PASS — 2008 English translation final structural/control QA is complete.**

Final state:

- Tamil source: **40 / 40 complete**;
- word-by-word text fidelity: **40 / 40 complete**;
- visual fidelity: **40 / 40 PASS**;
- English translation/review: **40 / 40 PASS**;
- English final structural/control QA: **PASS**;
- pending English stories: **0**;
- English stories needing review: **0**;
- unresolved story text: **0**;
- final story boundary: **scan 81 / printed page 79**;
- final physical witness: **scan 82 back cover**;
- canonical Tamil changed by QA: **No**.

## Future-work guard

This closure does **not** authorize modernization, normalization, adaptation, republication, release packaging, Digital Library onboarding, or replacement of the canonical Tamil layer. A new downstream phase requires explicit user authorization.
