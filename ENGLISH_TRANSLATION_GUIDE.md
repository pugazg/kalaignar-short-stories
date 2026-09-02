# English Translation Guide — Kalaignar Short Stories Archive

This guide defines the English-translation phase for verified Kalaignar short-story archival texts in this repository.

## 1. Authority and purpose

The English layer is a **faithful translation layer**, not a replacement edition of the Tamil source.

Authority order for translation work:

1. live GitHub `main`;
2. the verified canonical Tamil assembly under `stories/<slug>/sections/`;
3. the controlling source scan when a fidelity question must be reopened;
4. `SHORT_STORY_PROCESSING_GUIDE.md`;
5. `COLLECTION_SOURCE_GUIDE.md`;
6. this guide;
7. story-local audit, visual-fidelity and review records.

The canonical Tamil remains authoritative. Translation must never silently edit, normalize or overwrite it.

## 2. Translation gate

English translation may begin for a story only after the repository shows:

- complete page records for the story;
- direct visual/full-span Tamil source audit;
- no unresolved or blocked story text requiring immediate resolution;
- synchronized Tamil assembly;
- source/title variants documented;
- visual-fidelity closure for the story.

A persistent `POSSIBLE_ERRORS_FOR_REVIEW.md` queue does not itself block translation when the Tamil reading is already verified, but every queued item must be read before translation. The English must follow the current verified Tamil reading and must not silently “fix” a suspicious form.

## 3. Translation principles

- Translate the **verified Tamil actually preserved in the repository**.
- Do not import corrections from memory, outside editions, websites, historical assumptions or expected grammar.
- Preserve meaning, tone, rhetorical repetition, irony, dialogue, paragraph structure, quoted passages, letters, verse/display lineation and source-significant emphasis as closely as natural English allows.
- Do not reproduce running headers, page numbers, printer signatures or other excluded page furniture.
- Preserve names and uncertain transliterated source forms conservatively when an interpretive identification would require outside knowledge.
- Do not silently modernize cultural, historical or political references.
- Where a literal source form is awkward but intelligible, prefer a faithful natural-English rendering and document the difficult choice in `TRANSLATION_REVIEW.md`.
- Where the source itself remains unusual or ambiguous, choose the least speculative English supported by the verified Tamil and record the issue for review.
- Page-boundary markers should be retained in the English file so the translation remains traceable to the anthology scan and printed page.

## 4. Story-local translation structure

For each translated story:

```text
stories/<slug>/
  translations/
    en/
      <slug>.md
  TRANSLATION_REVIEW.md
```

The English file should contain the complete story in source order. It may include brief non-reading comments for page/source traceability, but translator explanations do not belong inside the story body.

`TRANSLATION_REVIEW.md` should record at minimum:

- Tamil title and English title treatment;
- source scan / printed-page range;
- canonical Tamil assembly used;
- translation completeness;
- structural/page-marker completeness;
- difficult terms, names, source anomalies and choices;
- confirmation that possible-error queue items were not silently corrected;
- any Tamil source issue reopened during translation;
- result: `PASS` or `NEEDS REVIEW`.

## 5. Source issue discovered during translation

If translation exposes a likely Tamil transcription problem:

1. stop translating that affected span;
2. reopen the reading under `SHORT_STORY_PROCESSING_GUIDE.md` against the controlling scan at full phrase/clause/sentence span;
3. do not correct Tamil from English expectation;
4. if the source supports a Tamil correction, synchronize the page record, Tamil assembly, audit/review controls and every dependent English layer;
5. record what changed and why in the relevant review/audit files.

## 6. Translation progress states

`ENGLISH_TRANSLATION_PROGRESS.md` is the durable anthology translation tracker.

Allowed story states:

- `pending`
- `in progress`
- `PASS`
- `NEEDS REVIEW`

A story counts as complete only when both the English translation and `TRANSLATION_REVIEW.md` are committed and the tracker/control files are synchronized.

## 7. Per-activity workflow

Process **one anthology story per activity** unless the user explicitly expands the batch.

For each story:

1. fetch live `main` first;
2. read this guide, `SHORT_STORY_PROCESSING_GUIDE.md`, `COLLECTION_SOURCE_GUIDE.md`, `ENGLISH_TRANSLATION_PROGRESS.md`, `HANDOVER.md` and `NEXT_CHAT_PROMPT.md`;
3. read the story README, Tamil assembly, audit, `POSSIBLE_ERRORS_FOR_REVIEW.md`, visual-fidelity record and page map;
4. translate the complete verified Tamil story into `translations/en/<slug>.md`;
5. preserve source/page boundaries and meaningful display structure;
6. create/update `TRANSLATION_REVIEW.md`;
7. update the story README, `ENGLISH_TRANSLATION_PROGRESS.md`, root README, `HANDOVER.md` and `NEXT_CHAT_PROMPT.md`;
8. re-fetch live `main` and the changed controls before declaring closure;
9. do not begin the next story in the same activity unless the user explicitly requested a batch.

## 8. Review standard

A translation `PASS` means:

- the full verified Tamil assembly is represented in English;
- no Tamil paragraph or source page has been omitted or duplicated;
- source-significant dialogue, display, letter or verse structure is retained;
- difficult source forms are handled conservatively and documented;
- canonical Tamil was not modified merely to improve English;
- no known translation issue remains unresolved.

### 8.1 Physical source-page anchoring — mandatory provenance check

Marker **presence and numeric order are not sufficient** to prove page traceability. A translation may contain every source-page marker in order while the markers delimit the wrong translated content.

Before a story is declared page-traceable:

1. use the verified Tamil `pages/*.md` records as the controlling per-scan boundary evidence;
2. identify the actual Tamil opening and closing span of each physical source page, including split sentences/words that continue across a page boundary;
3. confirm that the corresponding English source-page marker is placed at that same physical transition in the translated content;
4. do **not** require Tamil and English paragraph counts to match — paragraph count is not a provenance invariant;
5. every source page whose verified Tamil record contains story text must have substantive translated story content in its English marker section;
6. the final story source page must not have an empty English section merely because its marker exists;
7. cross-page sentences may continue naturally across the marker, but the marker must sit at the source-established transition;
8. `TRANSLATION_REVIEW.md` must distinguish **marker presence/order** from **content-boundary alignment**.

For a story where scan-level provenance is consumed downstream, or where a page-anchor defect has been corrected, a human-adjudicated boundary manifest may be maintained at:

`stories/<slug>/translations/en/page-anchors.json`

The manifest records source-backed Tamil boundary witnesses together with the corresponding English start/end anchors. The repository validator:

`python3 scripts/validate-english-page-anchors.py stories/<slug>`

checks marker sequence, printed-page agreement, non-empty translated sections and any recorded human-reviewed boundary anchors without using paragraph-count arithmetic.

After fixing a page-anchor defect, regression verification must include:

1. corrected state → **PASS**;
2. the prior defective marker pattern, or an equivalent shifted-marker fixture → **FAIL because of page anchoring**;
3. corrected/restored state → **PASS**.

This regression check must not be satisfied by an unrelated syntax failure.

## 9. Phase closure

The anthology English-translation phase is complete only when all **37 / 37** anthology stories are `PASS`, with no `pending`, `in progress` or `NEEDS REVIEW` story remaining.

Translation completion does **not** authorize modernization, republication, adaptation or replacement of the canonical Tamil source layer.
