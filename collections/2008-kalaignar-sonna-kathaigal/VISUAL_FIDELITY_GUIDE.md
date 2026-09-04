# Visual Fidelity Guide — கலைஞர் சொன்ன கதைகள் (2008)

This guide defines the post-text-fidelity **visual-structure review** for the 2008 second-edition collection `கலைஞர் சொன்ன கதைகள்`.

Controlling source: `TVA_BOK_0065857_கலைஞர்_சொன்ன_கதைகள்.pdf`

## Authority order

1. live GitHub `main`;
2. controlling source PDF / rendered scan;
3. `SHORT_STORY_PROCESSING_GUIDE.md`;
4. `COLLECTION_SOURCE_GUIDE.md`;
5. `TEXT_FIDELITY_CHECK_GUIDE.md` and the closed text-fidelity records;
6. this guide;
7. story-local page records, Tamil assembly, audits and review queues.

The source scan remains controlling. Visual review must not normalize or rewrite source wording.

## Batch rule

The standing user directive for this collection is **10 stories per iteration**. Process stories in printed order and close the full ten-story batch before advancing the tracker. The final batch may contain fewer than ten stories if fewer remain.

## What must be checked

For every story inspect every registered physical source page plus the next boundary witness where needed and compare against the committed `pages/` records and Tamil assembly.

Check:

- exact opening-heading wording and title variant provenance;
- source-significant opening / ending structure;
- paragraph and dialogue separation;
- verse, quotation, list or isolated display-line structure;
- source-significant ornaments and separators;
- physical page joins, including shared-page story boundaries;
- exclusion of running headers, printed page numbers and adjacent-story text;
- absence of duplicated or omitted text at page joins.

Exact font family, font size, margins, kerning and ordinary prose line wrapping are not archival invariants.

## Collection-specific page design

This edition uses a recurring graphic system: a large boxed **story sequence number**, a vertical gutter rule, and on opening spans a horizontal title rule. Continuation pages can repeat the boxed sequence number and gutter rule.

These elements are **collection-design furniture**, not story-body text. They must be visually acknowledged in each story's `visual-fidelity.md`, but they must not be injected into the canonical Tamil prose. The Markdown heading is the semantic representation of the printed story heading; facsimile recreation of the rule geometry is not required.

The centered single `*` used before the following story is a source-significant **story-ending ornament** and must remain represented in the Tamil assembly.

## Corrections

If the wording is correct but meaningful structure is missing, correct the page/assembly structure conservatively and record the change. If visual checking exposes a textual mismatch, reopen the exact source span, verify the full phrase, and synchronize every affected Tamil layer before closing visual fidelity.

## Story-local record

Each completed story receives:

`stories/<slug>/visual-fidelity.md`

Record at minimum:

- source span and pages directly inspected;
- opening / ending findings;
- paragraph / dialogue findings;
- display / verse findings;
- collection-design furniture handling;
- page-furniture handling;
- physical joins and shared boundaries;
- corrections, if any;
- remaining issues;
- result: `PASS`, `PASS — corrected`, or `needs recheck`.

## Durable tracker

Collection progress is maintained at:

`collections/2008-kalaignar-sonna-kathaigal/VISUAL_FIDELITY_PROGRESS.md`

Do not count a story complete until its story-local visual record is committed and any required source-supported corrections are synchronized.

## Phase gate

Visual-fidelity completion is required before English translation can open under `ENGLISH_TRANSLATION_GUIDE.md`. Completing visual fidelity does not itself authorize English translation, modernization, adaptation, republication or Digital Library onboarding.
