# Collection / Anthology Source Guide

This guide extends `SHORT_STORY_PROCESSING_GUIDE.md` for PDFs that contain **multiple short stories in one physical publication**.

## 1. Collection is a source container, not one canonical story

An anthology PDF must **not** be placed under a single `stories/<slug>/` directory as though the whole book were one story.

Register the physical collection under:

```text
collections/<collection-id>/
  README.md
  metadata/
    source.md
  indexes/
    story-inventory.md
    scan-map.md
```

Individual stories continue to live only under canonical `stories/<slug>/` workspaces.

## 2. Register physical-source identity once

At collection level record at minimum:

- exact source filename;
- SHA-256;
- byte size;
- actual PDF scan-page count;
- printed collection title and author line;
- publisher / edition information visible in the scan;
- front matter, contents, back matter and advertisements;
- printed pagination model;
- source PDF absent-from-repository rule.

Do not duplicate the 200+ MB source PDF into GitHub.

## 3. Inventory before transcription

Before creating story folders:

1. transcribe the complete printed contents list;
2. calculate each story's printed-page range from successive contents entries;
3. calculate its PDF scan range;
4. visually inspect **every calculated story-opening scan** and confirm the actual heading;
5. inspect the final story ending / back-cover boundary so the last range is not guessed.

The inventory must retain both **TOC title** and **story-opening heading** when they differ.

## 4. TOC and opening-heading differences are source facts

Never silently normalize a contents-title discrepancy.

Example source patterns may include:

- joined vs separated words;
- punctuation differences;
- abbreviated TOC title vs longer story-opening title;
- spelling variants.

Record both forms. The later canonical story workspace must document which form is used for folder/display naming and why.

## 5. Canonical-story deduplication

Before creating `stories/<slug>/`, inspect the repository for the same story under:

- the TOC title;
- the opening heading;
- plausible alternate title already documented by another source.

If a canonical story already exists, **do not create a duplicate story folder**. Add the anthology as another edition/source witness under the existing story and compare readings explicitly.

If no canonical story exists, create it only when that story becomes the active processing target.

Do not create dozens of empty placeholder story folders merely because an anthology contents page lists them.

## 6. Controlling source versus additional witness

For a newly created story whose first source is the anthology, that anthology scan range is the controlling source for that edition.

If another independent edition is later added:

- each edition remains source-faithful on its own;
- one edition must not silently overwrite another;
- textual differences belong in explicit comparison/audit notes;
- a secondary witness may help resolve difficult glyphs only under the rules in `SHORT_STORY_PROCESSING_GUIDE.md`.

## 7. Per-story page records

Collection-level `scan-map.md` is structural only. It does not replace story page records.

When a story is activated, create page records for its exact scan range and preserve both anthology coordinates in the marker:

```html
<!-- anthology scan: 10; printed page: 1 -->
```

If the repository's normal marker wording is used, ensure the same scan and printed-page values remain traceable.

## 8. Possible-error queue

Each processed story should maintain `POSSIBLE_ERRORS_FOR_REVIEW.md` when there are suspicious, archaic, unusual, enhancement-sensitive or user-corrected readings.

The queue is **not** a list of confirmed errors and does not automatically downgrade verified pages. Stronger source evidence can reopen a verified reading, after which all Tamil/English/control layers must be resynchronized.

## 9. Translation gate

Do not translate an anthology story merely because the collection inventory is complete.

English may begin only after that individual story has:

- complete page records;
- direct visual/full-span source audit;
- exhaustive resolution of difficult story text;
- synchronized Tamil assembly;
- source/title variants documented.

## 10. Handover requirement

`HANDOVER.md` must record:

- active collection identity;
- collection registration state;
- number of stories inventoried;
- current story number/title and exact scan range;
- whether it is a new canonical story or an additional witness;
- next exact action.
