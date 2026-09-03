# HANDOVER — Kalaignar Short Stories Archive

## Repository

- Repository: `pugazg/kalaignar-short-stories`
- Branch: `main`
- Story workflow: `SHORT_STORY_PROCESSING_GUIDE.md`
- Anthology workflow: `COLLECTION_SOURCE_GUIDE.md`
- Visual-fidelity workflow: `VISUAL_FIDELITY_CHECK_GUIDE.md`
- English-translation workflow: `ENGLISH_TRANSLATION_GUIDE.md`
- Source PDFs / renders / crops are **not** committed.

## Authoritative-state rule

Always fetch live `main` first and preserve newer durable work.

## Permanent source rules

- Controlling scan first; do not silently modernize spelling, punctuation, grammar, sandhi, names or source anomalies.
- Running headers, printed page numbers and printer signatures are page furniture, not story body.
- `POSSIBLE_ERRORS_FOR_REVIEW.md` is a human-review queue, not proof of error.
- Source-supported textual corrections must propagate through every affected page, assembly, audit/review and dependent English layer.
- Do not commit controlling PDFs or generated visual-inspection artefacts.

## Closed 1977 anthology

The 1977 anthology `கலைஞர் கருணாநிதியின் சிறுகதைகள்` remains durably closed:

1. Tamil source transcription/audit — **37 / 37 complete**, scans **10–259 / printed 1–250**, **0 blocked / 0 unresolved story text**;
2. visual fidelity — **37 / 37 complete**;
3. English translation/review — **37 / 37 complete**, **0 pending / 0 needs review**;
4. final English structural/control QA — **PASS**;
5. scan **260** — verified back cover.

Story 29 `திடுக்கிடும் கதை` later received the evidence-driven English page-anchor correction. The repair changed marker positions only; canonical Tamil and English prose were unchanged. The corrected Story-29 state remains **PASS**. The old downstream Wave-2 pin `a9b333f12128686785ee981f97313a64af12e29b` is obsolete.

## New active collection — கலைஞர் சொன்ன கதைகள்

The user supplied the next physical source and explicitly authorized repository continuation.

Collection workspace:

`collections/2008-kalaignar-sonna-kathaigal/`

Controlling source:

`TVA_BOK_0065857_கலைஞர்_சொன்ன_கதைகள்.pdf`

Registered identity:

- printed title: **கலைஞர் சொன்ன கதைகள்**;
- printed author: **டாக்டர் கலைஞர் மு. கருணாநிதி**;
- publisher: **பாரதி பதிப்பகம்**;
- first edition: **August 2004**;
- scanned edition: **Second Edition, December 2008**;
- source SHA-256: `1b2bf86892717776b1b3dc7fcb18dc146d5bfd0d60986509dc9cbbf5f235444b`;
- file size: **24,840,000 bytes**;
- PDF scans: **82**;
- printed contents entries: **40**;
- story-text range: scans **9–81 / printed pages 7–79**;
- scan **82**: verified back cover;
- pagination relation: **scan = printed page + 2** for story pages.

### Intake completion

The source-intake activity is complete:

- contents transcribed: **40 / 40**;
- story printed-page ranges calculated: **40 / 40**;
- scan ranges calculated: **40 / 40**;
- calculated story-opening scans visually checked: **40 / 40**;
- final Story-40/back-cover boundary checked: **Yes**;
- canonical story workspaces created from this collection: **0 / 40**;
- Tamil story processing started from this collection: **No**.

Five TOC/opening-heading differences are preserved in the collection inventory:

1. #2 `ஐஸ்கட்டி` ↔ `ஐஸ் கட்டி`;
2. #24 `வெண்ணெய் உருகுது வெயிலில்!` ↔ `வெண்ணெய் உருகுது வெயிலில்`;
3. #28 `அந்த நாள் வந்திலை...` ↔ `அந்த நாள் வந்திலை!`;
4. #35 `தும்... பம்... தீம்... தோம்` ↔ `தும் பம் தீம் தோம்`;
5. #39 `நன்றி சொல்லும் நேரம்...` ↔ `நன்றி சொல்லும் நேரம்`.

## Exact next activity

Process **Story 1 — `அப்படித்தான் சிரிப்பேன்` only**.

- printed page: **7**;
- source scan: **9**;
- next-boundary witness: scan **10**;
- Story 2 TOC title: **`ஐஸ்கட்டி`**;
- Story 2 opening heading: **`ஐஸ் கட்டி`**;
- current canonical-match check for Story 1: **no direct existing title match found at intake**, but re-check live `main` before workspace creation.

Before the Story-1 write, read completely:

1. `SHORT_STORY_PROCESSING_GUIDE.md`;
2. `COLLECTION_SOURCE_GUIDE.md`;
3. this `HANDOVER.md`;
4. `NEXT_CHAT_PROMPT.md`;
5. `collections/2008-kalaignar-sonna-kathaigal/README.md`;
6. `collections/2008-kalaignar-sonna-kathaigal/metadata/source.md`;
7. `collections/2008-kalaignar-sonna-kathaigal/indexes/story-inventory.md`;
8. `collections/2008-kalaignar-sonna-kathaigal/indexes/scan-map.md`.

Then re-check canonical deduplication, create Story 1 only if no canonical match exists, transcribe directly from scan 9, and use scan 10 only as the ending/boundary witness. Do not begin Story 2 in the same activity unless the user explicitly expands the batch.

## Phase guard

The new collection intake authorizes source-first processing of `கலைஞர் சொன்ன கதைகள்`; it does not authorize modernization, adaptation, republication, Digital Library onboarding, or changes to other repositories.