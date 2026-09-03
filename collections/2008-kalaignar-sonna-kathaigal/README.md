# கலைஞர் சொன்ன கதைகள் — 2008 second-edition anthology source

This folder registers **`கலைஞர் சொன்ன கதைகள்`** as a collection-level archival source for `pugazg/kalaignar-short-stories`.

The book is a physical collection/source container, not one canonical story. Its forty numbered stories/anecdotes are activated under canonical `stories/<slug>/` workspaces one at a time, following `COLLECTION_SOURCE_GUIDE.md` and `SHORT_STORY_PROCESSING_GUIDE.md`.

## Source snapshot

- source filename: `TVA_BOK_0065857_கலைஞர்_சொன்ன_கதைகள்.pdf`
- printed title: **கலைஞர் சொன்ன கதைகள்**
- printed author line: **டாக்டர் கலைஞர் மு. கருணாநிதி**
- English colophon title: **KALAIGNAR SONNA KATHAIGAL**
- English colophon description: **Collection of Short stories**
- publisher: **பாரதி பதிப்பகம்**, 126/108, உஸ்மான் சாலை, தி.நகர், சென்னை-600017
- copyright line: **© TamizhkkaniPathippagam**
- first edition: **August 2004**
- registered scanned edition: **Second Edition: December 2008**
- printed price: **Rs. 30.00**
- PDF scans: **82**
- printed story pages: **7–79**
- stories in printed contents: **40**
- story-text scans: **9–81**
- scan **82**: back cover
- source PDF committed to GitHub: **No**

Full checksum, byte size, imprint and scan-condition notes are in `metadata/source.md`.

## Intake / processing state

- printed contents transcribed: **40 / 40**
- calculated printed-page ranges: **40 / 40**
- calculated scan ranges: **40 / 40**
- calculated story-opening scans visually checked: **40 / 40**
- final story ending / back-cover boundary checked: **Yes**
- canonical story workspaces activated from this collection: **1 / 40**
- Tamil source processing complete from this collection: **1 / 40**
- Tamil source processing pending: **39 / 40**
- English translation from this collection: **0 / 40**

The story block follows a stable pagination offset:

- scan **9** = printed page **7**;
- scan **81** = printed page **79**;
- therefore story pages use **scan = printed page + 2**;
- scan **82** is the physical back cover and is outside story text.

### Story 1 completion — அப்படித்தான் சிரிப்பேன்

Canonical workspace: [`../../stories/appadithan-sirippen/`](../../stories/appadithan-sirippen/README.md)

- TOC title / opening heading: **`அப்படித்தான் சிரிப்பேன்`**;
- primary opening: scan **9 / printed page 7**;
- direct boundary review found a Story-1 tail at the top of **scan 10 / printed page 8**;
- scan 10 is therefore a **shared physical boundary**: Story 1 ends above its printed asterisk, then Story 2 begins below;
- Story-1 source records verified: **2 / 2**;
- blocked / unresolved Story-1 text: **0 / 0**;
- Tamil audit: **PASS**;
- Story-2 prose transcribed during Story-1 activity: **No**.

The initial range table was TOC-start-derived. The shared scan-10 boundary is now explicitly documented in the inventory/scan map rather than silently assigning Story-1 text to the wrong scan.

## Front matter / physical structure

- scan 1: front cover;
- scan 2: donation/bookplate label;
- scan 3: title page, with library stamp;
- scan 4: colophon/imprint, with handwritten accession/call-number marks;
- scan 5: `கலைஞர் உரை` page with photograph and handwritten message/signature; library stamp present;
- scan 6: `பதிப்புரை`;
- scans 7–8: printed contents;
- scans 9–81: forty numbered story units, printed pages 7–79;
- scan 82: back cover.

## Source-title differences found during intake

The contents title and story-opening heading are both source facts. Five differences were found and must remain explicit:

1. Story 2 — TOC **`ஐஸ்கட்டி`** ↔ opening **`ஐஸ் கட்டி`**;
2. Story 24 — TOC **`வெண்ணெய் உருகுது வெயிலில்!`** ↔ opening **`வெண்ணெய் உருகுது வெயிலில்`**;
3. Story 28 — TOC **`அந்த நாள் வந்திலை...`** ↔ opening **`அந்த நாள் வந்திலை!`**;
4. Story 35 — TOC **`தும்... பம்... தீம்... தோம்`** ↔ opening **`தும் பம் தீம் தோம்`**;
5. Story 39 — TOC **`நன்றி சொல்லும் நேரம்...`** ↔ opening **`நன்றி சொல்லும் நேரம்`**.

No title form is silently normalized. `indexes/story-inventory.md` retains both witnesses.

## Canonical-story deduplication

Story 1 was re-checked against live `main` before activation under its TOC/opening title and documented forms. No existing canonical match was found, so `stories/appadithan-sirippen/` was created.

Every later story must repeat the live-main duplicate check immediately before its workspace is created.

## Exact next activity

Process **Story 2 — TOC `ஐஸ்கட்டி` / opening `ஐஸ் கட்டி` only**.

- printed page: **8**
- source scan: **10**
- next-boundary witness: scan **11**, opening Story 3
- Story 3 title: **`தலையில் மலை`**

Before Story-2 writes, fetch live `main`, re-check canonical deduplication under both Story-2 title forms, inspect scan 10 directly from the controlling source, and use scan 11 only as the next ending/boundary witness. Preserve the already-closed Story-1 span at the top of scan 10 and do not duplicate it into Story 2.