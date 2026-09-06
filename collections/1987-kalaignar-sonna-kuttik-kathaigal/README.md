# கலைஞர் சொன்ன குட்டிக் கதைகள் — 1987 collection source

Collection workspace for the newly authorized source **`கலைஞர் சொன்ன குட்டிக் கதைகள்`**.

## Source snapshot

- source PDF: `TVA_BOK_0065566_கலைஞர்_சொன்ன_குட்டிக்_கதைகள்_1987.pdf`
- file size: **107,757,858 bytes**
- PDF scans: **50**
- printed title: **கலைஞர் சொன்ன குட்டிக் கதைகள்**
- catalog / supplied author: **கலைஞர் மு. கருணாநிதி**
- title-page compilation line: **`தொகுப்பு: முரசொலி குமரப்பன்`**
- publisher: **செல்வகுமார் பதிப்பகம்**, மதுரை
- first edition: **1984**
- represented edition: **இரண்டாம் பதிப்பு — 1987**
- price line: **ரூ. 2-00**
- source PDF committed to GitHub: **No**
- SHA-256: **PENDING** — the current file-execution environment could not hash the mounted 107,757,858-byte upload; do not invent or substitute a weaker checksum. Fill this before declaring source registration fully closed.

The source itself, not OCR or another edition, is controlling.

## Physical structure

- scan **1**: front cover
- scan **2**: title / compilation / publisher page
- scan **3**: edition / rights / price page
- scan **4**: `பதிப்புரை`
- scans **5–49**: story-bearing pages, printed pages **4–48**
- scan **50**: blank / damaged rear leaf; no story text visible
- story-block pagination relation: **scan = printed page + 1**
- printed contents page: **none visible**

Because there is no contents page, this collection uses a **direct visual story-heading inventory**, following the precedent used for the 2004 collection.

## Intake state

- physical story-opening coordinates identified: **25 / 25**
- exact/usable heading readings currently recorded: **20 / 25**
- stylized headings requiring a stricter source-pixel title recheck: **5 / 25** — scans **13, 20, 31, 37, 45**
- known exact canonical-title duplicate at intake: **1** — `குருவி ராமேஸ்வரம்`, scan **23 / printed 22**, already canonical as `stories/kuruvi-rameswaram/`
- other exact-title matches found in the existing canonical inventory: **0 among the 20 currently readable headings**
- content-level duplicate audit: **mandatory story-by-story before any new canonical folder is created**
- Tamil story transcription: **not started**
- English translation: **not authorized / not started**

Exact-title absence is not enough to prove a story is new. Every candidate must be compared against existing canonical story identity, alternate titles and narrative content before activation.

Two especially important collision checks are already flagged:

- `புகழேந்திப் புலவர் கதை` must not be conflated with existing canonical `புகழேந்தி` merely because they share a name token; compare narrative identity first.
- `யசோதர காவியம்` requires content comparison because existing canonical `அமிர்தமதி` explicitly contains a `யசோதர காவியம்` embedded narrative.

See [`DUPLICATE_AUDIT.md`](DUPLICATE_AUDIT.md).

## Historical Tamil glyph rule — mandatory for this source

The user supplied [`../../HISTORICAL_TAMIL_GLYPH_TRANSCRIPTION_GUIDE.md`](../../HISTORICAL_TAMIL_GLYPH_TRANSCRIPTION_GUIDE.md) specifically for this 1987 source.

For **every story-bearing page**:

1. inspect the whole source page before deciding difficult glyphs;
2. check the complete known historical set: `ணா / ணை / ணொ / ணோ / லை / ளை / றா / றொ / றோ / னா / னை / னொ / னோ`;
3. decode historical character identity into modern Unicode **without modernizing the wording**;
4. compare same-edition examples when the form is unclear;
5. never global-replace a historical-looking form;
6. keep an unresolved page `needs-review` rather than guessing;
7. maintain a story-level historical-glyph audit separate from ordinary transcription corrections.

The 1987 printing visibly uses older Tamil typeforms, so this is a required verification layer, not an optional later cleanup.

## Workflow boundary

Do **one story at a time** unless the user explicitly changes the rule.

Before activating any row in the inventory:

1. confirm its exact source heading and physical ending boundary;
2. search the live canonical repository by exact heading, plausible alternate title, and story content;
3. if the story already exists, add this 1987 range only as an **additional witness** under the existing canonical workspace;
4. if it is genuinely new, create a new canonical story workspace;
5. transcribe source-faithfully and run the historical-glyph audit on every page before visual closure;
6. do not start English until Tamil/source/visual work is explicitly closed and translation is separately authorized.

## Current exact next activity

Finish the five **stylized-heading title rechecks** at scans **13, 20, 31, 37 and 45** from source pixels. Do not guess the typography from contextual expectation.

After the direct-heading inventory reaches **25 / 25 exact**, begin Story 1 at scan **5 / printed page 4** only after a fresh duplicate/content check. No story text has been marked verified by this intake commit.