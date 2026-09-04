# Text Fidelity Check Guide — Kalaignar Short Stories Archive

This guide defines the post-transcription **word-by-word Tamil text-fidelity phase**.

## 1. Authority order

For every text-fidelity activity:

1. live GitHub `main`;
2. controlling source scan / PDF;
3. `SHORT_STORY_PROCESSING_GUIDE.md`;
4. `COLLECTION_SOURCE_GUIDE.md`;
5. this guide;
6. story-local page records, Tamil assembly, audit and review queue.

The scan is controlling. Existing `verified` status is **not** proof that a word is correct in this second-pass phase.

## 2. Purpose

Re-read every story against the controlling scan **word by word** and verify:

- every lexical word and inflected form;
- source spelling and sandhi / joined-vs-separated forms;
- punctuation attached to the reading;
- quotation marks and dialogue boundaries;
- numerals and source-significant symbols;
- paragraph starts / ends;
- physical page joins, including split words and shared story-boundary scans;
- exclusion of running headers, printed page numbers and adjacent-story matter.

Do not silently modernize, regularize grammar, repair an unusual printed form, or replace source wording with contextual expectation.

## 3. Direct-source rule

The fidelity result must come from direct visual comparison with the controlling scan. OCR memory, prior-chat prose, earlier Markdown, web copies and inferred wording are not substitutes for the source.

If a glyph remains genuinely ambiguous, use the escalation protocol in `SHORT_STORY_PROCESSING_GUIDE.md`. A secondary witness may corroborate but may not silently overwrite the controlling edition.

## 4. Correction propagation

When a mismatch is found:

1. verify the complete phrase / clause around it in the scan;
2. correct the affected `pages/*.md` record;
3. correct the Tamil assembly under `sections/`;
4. update `audit.md` with the old committed form and the source-supported replacement;
5. update `POSSIBLE_ERRORS_FOR_REVIEW.md` when the recovered source form is unusual or merits future human recheck;
6. record the correction in `text-fidelity.md`;
7. do not alter unrelated nearby wording.

Source-supported fidelity corrections do not reopen unrelated closed text.

## 5. Story-local record

Each completed story receives:

`stories/<slug>/text-fidelity.md`

It records:

- source span inspected;
- direct word-by-word method;
- corrections, if any;
- page-join / boundary result;
- remaining unresolved fidelity issues;
- result: `PASS`, `PASS — corrected`, or `needs recheck`.

## 6. Progress tracker

`TEXT_FIDELITY_PROGRESS.md` is the durable phase tracker.

Allowed states:

- `pending`
- `in progress`
- `PASS`
- `PASS — corrected`
- `needs recheck`

A story is complete only after its story-local record and every source-supported correction are durable on `main`.

## 7. Iteration policy

For `கலைஞர் சொன்ன கதைகள்`, process **10 stories per iteration** in collection order:

- Stories 1–10;
- Stories 11–20;
- Stories 21–30;
- Stories 31–40.

Do not advance the tracker to the next batch until all corrections and controls for the current batch are synchronized and live `main` is re-fetched.

## 8. Phase closure

The 2008 collection text-fidelity phase closes only at **40 / 40**, with no `pending`, `in progress`, `needs recheck`, or unresolved word-level issue remaining.

Text-fidelity completion does not automatically authorize English translation, modernization, adaptation, republication, or Digital Library onboarding.
