# கலைஞரின் குட்டிக் கதைகள் — 2004 second-edition collection source

This folder registers **`கலைஞரின் குட்டிக் கதைகள்`** as a collection-level archival source for `pugazg/kalaignar-short-stories`.

The PDF is a physical collection/source container, not one canonical story. Individual story units are activated only under canonical `stories/<slug>/` workspaces after a fresh live-`main` duplicate/content-equivalence check.

## Source snapshot

- source filename: `TVA_BOK_0065567_கலைஞரின்_குட்டிக்_கதைகள்_2004.pdf`
- printed title: **கலைஞரின் குட்டிக் கதைகள்**
- publisher: **பாரதி பதிப்பகம்**
- colophon: **Revised Edition: Aug. 1998; Second Edition: March 2004**
- registered physical edition represented by this PDF: **Second Edition, March 2004**
- PDF scans: **50**
- story-text scans: **4–49**
- printed story pages represented: **3–48**
- story units found by direct heading survey: **34**
- scan **50**: physical back cover; no further story text
- source PDF committed to GitHub: **No**

Full checksum, byte size, imprint and scan-condition notes are in `metadata/source.md`.

## Important intake fact — no printed contents page in this scan

This 50-scan edition has **no printed contents list visible between the front matter and the story block**. Scan 3 is the colophon and scan 4 begins the collection/story text.

Therefore the 34-story inventory was not reconstructed from a guessed TOC. It was established by direct sequential inspection of every story-opening heading across scans **4–49**. `indexes/story-inventory.md` records those opening headings and their routing boundaries.

## Pagination model

Across the story block:

`PDF scan = printed page + 1`

Examples:

- scan **4** → printed page **3**;
- scan **5** → printed page **4**;
- scan **49** → printed page **48**.

Scans 1–3 are unnumbered front matter. Scan 50 is the back cover.

## Processing state

- file identity / checksum / size verified: **Yes**
- cover / title / colophon inspected: **Yes**
- printed contents page present: **No**
- direct story-heading inventory: **34 / 34 complete**
- story-opening headings visually checked: **34 / 34**
- final story ending / back-cover boundary checked: **Yes**
- canonical story workspaces activated from this collection: **1 / 34**
- Tamil source processing complete from this collection: **1 / 34**
- Tamil source processing pending: **33 / 34**
- completed-story blocked / unresolved story text: **0**
- English translation from this collection: **not opened**

## Completed source work

| # | Story | Canonical workspace | Verified physical source span | Tamil |
|---:|---|---|---|---|
| 1 | `வள்ளுவர் சொன்ன பொய்` | `stories/valluvar-sonna-poi/` | scan 4 → top scan 5 | **PASS** |

Story 1 was activated only after a fresh exact-title and content-equivalence check found no existing canonical match. Its two source records are verified; scan 5 is a shared boundary where Story 1 closes above Story 2.

## Source design / boundary notes

- story headings are printed as bold display headings framed by horizontal rules;
- several physical pages contain the ending of one story followed by the heading/opening of the next story;
- running page headers and printed page numbers are publication furniture, not story body text;
- the final story `கிழவியின் மனைவி` begins on scan **47 / printed page 46**, continues through scans **48–49**, and closes with `முற்றும்` on scan **49 / printed page 48**;
- scan **50** is back-cover matter only.

Exact per-story boundaries must still be verified when each story is activated; the collection inventory is a routing/control map and does not replace story-local page records.

## Canonical deduplication gate

Do not create the remaining story workspaces from the inventory alone. Each row still requires a fresh live-`main` duplicate/content-equivalence check before activation.

## Next exact activity

Activate and process **Story 2 — `நீயும் கைதி - நானும் கைதி`**.

Routing coordinates:

- opens on scan **5 / printed page 4**, immediately below the completed Story-1 ending;
- Story 3 `குருவி ராமேஸ்வரம்` begins later on the **same scan 5 / printed page 4** and is the required ending-boundary witness.

Before creating Story 2, fetch live `main`, complete the duplicate/content-equivalence check, and isolate only the Story-2 text between the two headings on scan 5. Do not include Story-1 or Story-3 material.