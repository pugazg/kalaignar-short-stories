# NEXT CHAT PROMPT — 1976 `நளாயினி` / `நாட்டிய கலாராணி` scans 25–29 — Stage A

Continue in `pugazg/kalaignar-short-stories`, branch `main`. **LIVE MAIN IS AUTHORITATIVE.**

## External hold

`வெள்ளிக்கிழமை` remains incomplete; do **not** start `நடுத்தெரு நாராயணி`.

## Controlling source

`TVA_BOK_0065574_நளாயினி_1976.pdf` — **78 scans**, **164,748,566 bytes**, fourth edition 1976, image-only. Source PDF is not committed. SHA-256 remains pending because direct raw-byte checksum access was unavailable; do not invent one.

The user downloaded this exact PDF from the Tamil Digital Library and supplied the downloaded file. **The attached PDF itself is the sole controlling authority for this collection. Do not query the Tamil Digital Library website or another external source unless the user explicitly requests an external comparison.**

## Mandatory startup

Read before source-dependent work:

1. `SHORT_STORY_PROCESSING_GUIDE.md`
2. `COLLECTION_SOURCE_GUIDE.md`
3. `HISTORICAL_TAMIL_GLYPH_TRANSCRIPTION_GUIDE.md`
4. `BATCH_TRANSCRIPTION_VERIFICATION_WORKFLOW.md`
5. root `HANDOVER.md`
6. this prompt
7. `collections/1976-nalayini/README.md`
8. `collections/1976-nalayini/indexes/story-inventory.md`
9. `stories/naattiya-kalarani/README.md`
10. `stories/naattiya-kalarani/SOURCE_INTAKE.md`
11. `stories/naattiya-kalarani/indexes/page-map.md`
12. `stories/naattiya-kalarani/PASS1_PROGRESS.md`
13. `stories/naattiya-kalarani/HISTORICAL_GLYPH_GATE.md`
14. `stories/naattiya-kalarani/POSSIBLE_ERRORS_FOR_REVIEW.md`

## Collection correction

Attached scan **73** directly shows Story 8 heading **`மானம்`**. Earlier controls incorrectly recorded `மனம்`; use `மானம்` from now on. Do not begin it yet.

## Durable state

`நாட்டிய கலாராணி` is a new canonical story, physical range **scans 25–46 / printed 25–46**.

- source boundary: PASS;
- canonical dedup: PASS;
- page records initialized: **22/22**;
- direct transcription: **0/22**;
- glyph Pass 2: **0/22**;
- verified: **0/22**;
- Tamil assembly: not started.

Scan 25 visibly opens with the display heading `நாட்டிய கலாராணி`; scan 46 ends the story; scan 47 opens existing canonical `விஷம் இனிது` and is excluded.

## Revised two-stage workflow

Page batches are no longer processed as one oversized transcription+glyph activity.

For each batch:

**Stage A** — direct transcription → synchronize Pass-1 state → commit → stop/report.  
**Stage B** — later, as a separate activity, independently reopen the same pages for the historical-glyph/source verification → synchronize → commit → stop/report.

Routine crops/enhancements are forbidden. Use them only for an actual reading ambiguity.

## Exact next activity — Stage A ONLY

Process scans **25–29 / printed pages 25–29** only.

- visually read and transcribe each complete page once from the attached source pixels;
- preserve punctuation, spacing, paragraphing, source-odd words, page boundaries and clearly readable historical character identity;
- **do not perform the systematic `ணா / ணை / ணொ / ணோ / லை / ளை / றா / றொ / றோ / னா / னை / னொ / னோ` Pass 2 in this activity**;
- **do not repeatedly reopen already-clear words/pages**;
- **do not create crops/enhancements unless a reading genuinely cannot be transcribed responsibly at normal/native page view**;
- unresolved readings may remain explicitly marked; do not guess;
- after Stage A the affected pages remain `needs-review`, not final `verified`;
- synchronize the five page records, page map, Pass-1 tracker and current-state controls;
- commit Stage A before any independent glyph audit;
- **stop and report after the commit**.

The following activity, only after that durable commit, will be Stage B for the **same scans 25–29**. Do **not** begin scan 30 yet.

Do **not** begin Story 8 `மானம்` in the same activity.
