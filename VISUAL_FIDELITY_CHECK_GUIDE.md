# Visual Fidelity Check Guide — Kalaignar Short Stories Archive

This guide defines the post-transcription **visual fidelity check** for the 1977 anthology `கலைஞர் கருணாநிதியின் சிறுகதைகள்` after the Tamil source-text pass has been completed.

The purpose is to compare the committed archival Markdown against the controlling page images for **source-significant visual structure**. This is not a modernization, redesign, or facsimile-typesetting phase.

## 1. Authority order

For every visual-fidelity activity:

1. live GitHub `main`;
2. controlling source PDF / rendered source page;
3. `SHORT_STORY_PROCESSING_GUIDE.md`;
4. `COLLECTION_SOURCE_GUIDE.md`;
5. this guide;
6. story-local page records, assembly, audits and review queues.

The controlling scan remains authoritative. A visually expected form must never replace the printed source wording.

## 2. Phase scope

Check all 37 anthology stories in printed order, **one story per activity** unless the user explicitly changes that rule.

For every story, compare every source page in its registered scan range against:

- `stories/<slug>/pages/`;
- the Tamil assembly under `stories/<slug>/sections/`;
- the story page map / source metadata when visual structure affects those records.

Inspect the next physical scan as a boundary witness when needed, but do not import the next story or non-story matter into the active story.

## 3. What must be checked

### A. Opening and ending structure

- exact story-heading wording;
- whether the page is an opening, body, or ending page;
- opening rules / separators when source-significant;
- terminal ornaments, rules, stars, diamonds or other closing marks;
- explicit section breaks within a story.

### B. Paragraph fidelity

- paragraph starts and ends;
- dialogue paragraph separation;
- intentional standalone sentences / display lines;
- no accidental paragraph merge or split introduced during transcription.

Exact prose line wrapping caused only by the printed page width is **not** required to be reproduced.

### C. Verse / display / emphasis fidelity

Preserve source-significant presentation such as:

- verse or song lineation;
- intentionally centered or isolated lines;
- repeated display phrases;
- source emphasis where it changes the visual reading structure;
- drop-cap / enlarged-initial effects when they clearly mark a structural paragraph opening.

Markdown/HTML may use a conservative semantic approximation when exact typography is not portable. Do not invent styling that is not visible in the source.

### D. Non-text marks

Record or represent source-significant:

- story-opening rules;
- story-ending ornaments;
- illustrations that belong to the story opening/body/ending;
- captions or labels attached to illustrations.

Routine scan noise, stains, bleed-through and paper discoloration do not need textual representation unless they obscure or materially interact with the story.

### E. Page furniture

Running headers, printed page numbers and repeated anthology headers must be visually checked so they are not accidentally transcribed as story body.

They normally remain **excluded from the canonical reading text** and should be classified as page furniture rather than reproduced inside the story.

### F. Page boundaries

Check:

- source page start and end;
- split words / split quotations / split sentences across pages;
- no duplicated or omitted text at joins;
- no next-story or back-cover material leaking into the active story.

## 4. What this phase does not attempt

Visual fidelity does **not** require recreating:

- the original font family;
- exact font size;
- kerning;
- exact margins;
- exact prose line lengths;
- paper colour;
- scan skew;
- printing defects that do not affect content.

The archival Markdown should preserve meaningful structure, not imitate the physical page pixel-for-pixel.

## 5. Corrections found during the check

### Structural-only mismatch

If the wording is already correct but the Markdown misses source-significant structure, correct the relevant page record and Tamil assembly. Examples:

- missing closing ornament;
- merged paragraphs;
- lost verse lineation;
- display line incorrectly treated as ordinary prose;
- wrong `page_type` (`story-body` instead of `story-opening` / `story-ending`).

### Textual mismatch discovered visually

If direct visual checking reveals that the committed wording itself is wrong:

1. reopen the reading under `SHORT_STORY_PROCESSING_GUIDE.md`;
2. verify the full source span, not only the isolated glyph;
3. correct all affected page/assembly/audit/review layers;
4. document the correction in the story visual-fidelity record;
5. do not silently modernize or normalize anything else nearby.

## 6. Story-local visual-fidelity record

Each completed story receives:

`stories/<slug>/visual-fidelity.md`

It should record:

- story title and source range;
- pages directly inspected;
- opening/ending findings;
- paragraph / dialogue findings;
- verse / display / emphasis findings;
- non-text marks;
- page-furniture handling;
- physical joins;
- corrections made, if any;
- remaining visual-fidelity issues, if any;
- result: `PASS`, `PASS WITH SOURCE-SUPPORTED CORRECTIONS`, or `NEEDS RECHECK`.

A visual-fidelity `PASS` is separate from the earlier Tamil text `verified` status.

## 7. Phase progress states

`VISUAL_FIDELITY_PROGRESS.md` is the durable phase tracker.

Allowed story states:

- `pending`
- `in progress`
- `PASS`
- `PASS — corrected`
- `needs recheck`

Do not mark a story complete until its story-local `visual-fidelity.md` is committed and any required page/assembly corrections are synchronized.

## 8. Per-activity closure

Before declaring one story's visual fidelity complete:

1. inspect every source page in that story range directly;
2. inspect the boundary witness where relevant;
3. resolve or explicitly record all visual-structure mismatches;
4. synchronize affected page records and assembly;
5. create/update `stories/<slug>/visual-fidelity.md`;
6. update `VISUAL_FIDELITY_PROGRESS.md`;
7. update `HANDOVER.md` and `NEXT_CHAT_PROMPT.md` to the next story;
8. re-fetch live `main` and the changed control files.

Do not begin the following story in the same activity.

## 9. Final phase closure

The visual fidelity phase is complete only when all **37 / 37** anthology stories are `PASS` or `PASS — corrected`, with no `pending`, `in progress`, or `needs recheck` story remaining.

Visual-fidelity completion does **not** automatically authorize English translation, modernization, republication, or another downstream phase.
