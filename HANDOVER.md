# HANDOVER — Kalaignar Short Stories Archive

## Repository

- repository: `pugazg/kalaignar-short-stories`
- branch: `main`
- source workflow: `SHORT_STORY_PROCESSING_GUIDE.md`, `COLLECTION_SOURCE_GUIDE.md`, `HISTORICAL_TAMIL_GLYPH_TRANSCRIPTION_GUIDE.md`
- English workflow: `ENGLISH_TRANSLATION_GUIDE.md`

## LIVE MAIN IS AUTHORITATIVE

Always fetch live `main` first and preserve newer durable state.

## Permanent workflow order

For an active story/work/collection processed Tamil-first:

1. complete Tamil source transcription / source audit / visual and historical-glyph fidelity work;
2. close the Tamil/source release gate with zero unresolved source-text issues wherever defensibly recoverable;
3. **English translation is automatically the next activity**.

Do not wait for a separate English authorization after Tamil/source closure unless the user explicitly pauses, redirects, defers or excludes English.

## Permanent source rules

- controlling scan first; no silent normalization;
- prove canonical identity before creating a new story workspace;
- preserve shared physical page boundaries;
- additional witnesses never overwrite controlling canonical editions;
- decode historical Tamil type by character identity, never by modern visual resemblance alone;
- never global-replace historical-looking forms;
- source PDFs / inspection crops are not committed.

## Mandatory two-pass historical-glyph rule

Every historical-Tamil story page requires:

1. Pass 1 direct source-faithful transcription.
2. Pass 2: reopen the same physical page at native/high resolution and independently recheck  
   `ணா / ணை / ணொ / ணோ / லை / ளை / றா / றொ / றோ / னா / னை / னொ / னோ`
   plus suspicious old-type clusters.

Final `verified` requires both passes.

## Closed phases — preserve

- 1977 — Tamil/visual/English **37/37 PASS**
- 2008 — Tamil/visual/English **40/40 PASS**
- 2004 — Tamil/visual/English **34/34 PASS**
- 2009 new-story onboarding — **5/5 CLOSED**
- 2009 existing-canonical witness comparison — **11/11 CLOSED**
- supplemental English — **6/6 PASS / CLOSED**
- 1987 `கலைஞர் சொன்ன குட்டிக் கதைகள்` Tamil/source phase — **CLOSED**

Do not reopen closed phases because of an older prompt.

## ACTIVE — 1987 English translation phase

Collection workspace:
`collections/1987-kalaignar-sonna-kuttik-kathaigal/`

Controlling source:
`TVA_BOK_0065566_கலைஞர்_சொன்ன_குட்டிக்_கதைகள்_1987.pdf`

Source identity:

- 50 scans
- 107,757,858 bytes
- SHA-256 `29c986812f95c43105eec4b38fa9e02c3c4f66cf3c4e8a686b81dd28c1164f0f`
- Second Edition, 1987

Tamil/source release record:
`collections/1987-kalaignar-sonna-kuttik-kathaigal/FINAL_TAMIL_SOURCE_RELEASE_AUDIT_2026-09-07.md`

English tracker:
`collections/1987-kalaignar-sonna-kuttik-kathaigal/ENGLISH_TRANSLATION_PROGRESS.md`

### Closed Tamil/source state

- headings: **25 / 25 PASS**
- canonical identity: **25 / 25 COMPLETE**
- distinct identities: **23**
- witness-only identities: **2**
- story-bearing scans **5–49 = 45 / 45 Pass 1 + independent Pass 2 COMPLETE**
- scan 50: verified blank/damaged terminal non-story leaf
- unresolved 1987 Tamil/source or historical-glyph locations: **0**
- **1987 Tamil/source phase: CLOSED**

### English phase state

- source stories: **25**
- English PASS: **0 / 25**
- pending: **25 / 25**
- needs review: **0**
- phase state: **ACTIVE**

### Authoritative title corrections — do not revert

- Story 2 `அராபியக் கதை`
- Story 4 `நாராயணா ! நாராயணா !`
- Story 6 `மூளி மூக்குக்காரன்`
- Story 10 `இரு நிழல்கள்` — direct banner recheck; earlier `இரு நிகழ்வுகள்` was wrong

Story 10 retains repository directory `stories/iru-nigazhvugal/` only for path continuity. The source-facing title is `இரு நிழல்கள்`.

### Witness-only routing — preserve during English

- Story 2 `அராபியக் கதை` is a completed 1987 witness for canonical `ஜாடி குட்டி போடுமா?`; its 1987 English must be **witness-local** and must not overwrite the controlling 2008 English.
- Story 11 `குருவி ராமேஸ்வரம்` is a completed 1987 witness for the existing 2004 canonical story; its 1987 English must be **witness-local** and must not overwrite the controlling 2004 English.

## Exact next activity

Translate **Story 1 — `மன்னனும் குருவியும்!`** from the verified Tamil workspace:

`stories/mannanum-kuruviyum/`

Before writing English, read completely:

1. `ENGLISH_TRANSLATION_GUIDE.md`;
2. `SHORT_STORY_PROCESSING_GUIDE.md`;
3. `COLLECTION_SOURCE_GUIDE.md`;
4. collection `ENGLISH_TRANSLATION_PROGRESS.md`;
5. root `HANDOVER.md` and `NEXT_CHAT_PROMPT.md`;
6. `stories/mannanum-kuruviyum/README.md`;
7. its Tamil assembly, page map, source audit, historical-glyph audit, visual-fidelity record and `POSSIBLE_ERRORS_FOR_REVIEW.md`.

Create the complete English translation under `stories/mannanum-kuruviyum/translations/en/`, create `TRANSLATION_REVIEW.md`, verify physical source-page anchoring, synchronize the story README, collection English tracker, `HANDOVER.md` and `NEXT_CHAT_PROMPT.md`, then stop after Story 1 unless the user explicitly expands the batch.

If translation exposes a concrete Tamil source issue, reopen only that exact Tamil span against the controlling scan before changing the Tamil or dependent English.

Do not begin `நடுத்தெரு நாராயணி` while waiting for `வெள்ளிக்கிழமை` completion in the novels workflow.
