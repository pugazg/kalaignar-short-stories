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
- Shared physical boundary scans must preserve the exact source span of each story; do not reassign text to make TOC-derived ranges artificially non-overlapping.
- Do not commit controlling PDFs or generated visual-inspection artefacts.

## Closed 1977 anthology

The 1977 anthology `கலைஞர் கருணாநிதியின் சிறுகதைகள்` remains durably closed:

1. Tamil source transcription/audit — **37 / 37 complete**, scans **10–259 / printed 1–250**, **0 blocked / 0 unresolved story text**;
2. visual fidelity — **37 / 37 complete**;
3. English translation/review — **37 / 37 complete**, **0 pending / 0 needs review**;
4. final English structural/control QA — **PASS**;
5. scan **260** — verified back cover.

Story 29 `திடுக்கிடும் கதை` later received the evidence-driven English page-anchor correction. The repair changed marker positions only; canonical Tamil and English prose were unchanged. The corrected Story-29 state remains **PASS**. The old downstream Wave-2 pin `a9b333f12128686785ee981f97313a64af12e29b` is obsolete.

## Active collection — கலைஞர் சொன்ன கதைகள்

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
- story-text scans: **9–81 / printed pages 7–79**;
- scan **82**: verified back cover;
- pagination relation: **scan = printed page + 2** for story pages.

### Collection state

- contents transcribed: **40 / 40**;
- TOC-derived story ranges calculated: **40 / 40**;
- calculated story-opening scans visually checked: **40 / 40**;
- final Story-40/back-cover boundary checked: **Yes**;
- canonical story workspaces activated from this collection: **1 / 40**;
- Tamil source processing complete: **1 / 40**;
- Tamil source processing pending: **39 / 40**;
- English translation from this collection: **0 / 40**.

Five TOC/opening-heading differences remain preserved in the collection inventory:

1. #2 `ஐஸ்கட்டி` ↔ `ஐஸ் கட்டி`;
2. #24 `வெண்ணெய் உருகுது வெயிலில்!` ↔ `வெண்ணெய் உருகுது வெயிலில்`;
3. #28 `அந்த நாள் வந்திலை...` ↔ `அந்த நாள் வந்திலை!`;
4. #35 `தும்... பம்... தீம்... தோம்` ↔ `தும் பம் தீம் தோம்`;
5. #39 `நன்றி சொல்லும் நேரம்...` ↔ `நன்றி சொல்லும் நேரம்`.

## Completed current story — Story 1

**`அப்படித்தான் சிரிப்பேன்` — Tamil source PASS.**

Canonical workspace:

`stories/appadithan-sirippen/`

Durable source state:

- TOC title / opening heading: **`அப்படித்தான் சிரிப்பேன்`**;
- fresh live-main duplicate check before activation: **no canonical match found**;
- primary opening/body: **scan 9 / printed page 7**;
- direct boundary review: Story 1 continues at the top of **scan 10 / printed page 8**;
- scan 9 ends at `“ஆமாம்!` and scan 10 continues `அப்படித்தான் சிரிப்பேன்!” ...`;
- Story 1 closes on scan 10 with a printed asterisk;
- Story 2 starts below that mark on the same scan;
- verified source records: **2 / 2**;
- `needs-review`: **0**;
- `blocked`: **0**;
- unresolved story text: **0**;
- Tamil assembly: complete;
- Tamil audit: **PASS**;
- persistent human recheck queue: present;
- English translation: **not started**;
- Story-2 prose transcribed during Story-1 activity: **No**.

Source-close forms retained without normalization include `ஊடைய`, `சாப்பிட்டலாம்`, joined `மன்னன்கேட்ட`, and the source's later `ராணியையும்` form.

The initial TOC-derived range `printed 7 / scan 9` remains provenance for the opening coordinate, but scan 10 is now explicitly documented as a shared physical ending/boundary witness. Collection inventory and scan map have been synchronized to this source fact.

## Exact next activity

Process **Story 2 — TOC `ஐஸ்கட்டி` / opening `ஐஸ் கட்டி` only**.

- printed page: **8**;
- source scan: **10**;
- shared-page guard: preserve the already-closed Story-1 span at the top of scan 10 and begin Story 2 only below the Story-1 asterisk / Story-2 number-heading boundary;
- next-boundary witness: scan **11**;
- Story 3 TOC/opening title: **`தலையில் மலை`**.

Before Story-2 source-dependent writes:

1. fetch live `main`;
2. read `SHORT_STORY_PROCESSING_GUIDE.md`, `COLLECTION_SOURCE_GUIDE.md`, this `HANDOVER.md`, `NEXT_CHAT_PROMPT.md`, and the active collection README/source/inventory/scan-map;
3. confirm no canonical story already exists under `ஐஸ்கட்டி`, `ஐஸ் கட்டி`, or any documented alternate form;
4. inspect scan 10 directly and activate Story 2 only if no canonical match exists;
5. use scan 11 only as Story-2 ending/boundary witness;
6. do not begin Story 3 in the same activity unless the user explicitly expands the batch.

## Phase guard

The active collection authorizes source-first processing of `கலைஞர் சொன்ன கதைகள்`; it does not authorize modernization, adaptation, republication, Digital Library onboarding, or changes to other repositories.