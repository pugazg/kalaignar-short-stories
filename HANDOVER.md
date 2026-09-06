# HANDOVER — Kalaignar Short Stories Archive

## Repository

- repository: `pugazg/kalaignar-short-stories`
- branch: `main`
- story workflow: `SHORT_STORY_PROCESSING_GUIDE.md`
- collection workflow: `COLLECTION_SOURCE_GUIDE.md`
- historical Tamil glyph workflow: `HISTORICAL_TAMIL_GLYPH_TRANSCRIPTION_GUIDE.md`
- English workflow: `ENGLISH_TRANSLATION_GUIDE.md`
- supplemental English tracker: `NEW_STORY_ENGLISH_TRANSLATION_PROGRESS.md`
- archive-wide closure history: `ARCHIVE_COMPLETION.md`
- historical 1977-only completion record: `PROJECT_COMPLETION.md`

## LIVE MAIN IS AUTHORITATIVE

Always fetch live `main` first and preserve newer durable state.

## Permanent rules

- controlling scan first; no silent normalization;
- shared physical boundaries must remain exact;
- an additional edition witness must not silently overwrite a canonical controlling edition;
- textual differences belong in explicit comparison/audit records;
- if a later witness appears to correct a canonical reading, reopen the exact canonical controlling scan before changing Tamil/English/control layers;
- before creating any new story workspace, prove it is not already canonical under the same or an alternate title;
- historical Tamil typeforms must be decoded by character identity, not modern visual resemblance;
- source PDFs are not committed.

## Closed canonical collection phases

- **1977 — கலைஞர் கருணாநிதியின் சிறுகதைகள்:** Tamil 37/37, visual 37/37, English 37/37, final QA PASS, unresolved 0.
- **2008 — கலைஞர் சொன்ன கதைகள்:** Tamil 40/40, visual 40/40, English 40/40, final QA PASS, unresolved 0.
- **2004 — கலைஞரின் குட்டிக் கதைகள்:** Tamil 34/34, visual 34/34, English 34/34, final QA PASS, unresolved 0.
- **2009 new-story onboarding:** 5/5 COMPLETE / CLOSED.
- **2009 existing-canonical witness comparison:** 11/11 COMPLETE / CLOSED.
- **supplemental English:** 6/6 PASS / CLOSED.

Do not reopen those closed phases merely to create work. A specifically authorized independent-witness comparison is distinct from reopening a canonical source pass.

## ACTIVE AUTHORIZATION — 1987 `கலைஞர் சொன்ன குட்டிக் கதைகள்`

Workspace: `collections/1987-kalaignar-sonna-kuttik-kathaigal/`

Controlling source:

`TVA_BOK_0065566_கலைஞர்_சொன்ன_குட்டிக்_கதைகள்_1987.pdf`

Registered intake facts:

- byte size: **107,757,858 bytes**
- scans: **50**
- printed title: **கலைஞர் சொன்ன குட்டிக் கதைகள்**
- supplied/catalog author: **கலைஞர் மு. கருணாநிதி**
- title-page line: **`தொகுப்பு: முரசொலி குமரப்பன்`**
- publisher: **செல்வகுமார் பதிப்பகம்**, மதுரை
- first edition: **1984**
- represented edition: **இரண்டாம் பதிப்பு — 1987**
- scans **1–4**: front matter
- scans **5–49 / printed 4–48**: story-bearing block
- scan **50**: blank/damaged rear leaf; no visible story continuation
- no printed contents page
- physical story-opening blocks identified: **25 / 25**
- exact/usable direct headings currently: **20 / 25**
- exact title recheck holds: scans **13, 20, 31, 37, 45**
- SHA-256: **PENDING** because mounted-byte hashing failed in the current execution environment; do not invent it.

### Duplicate gate — mandatory

User directive: **do not onboard a story again if it already exists in this repository.**

Durable audit: `collections/1987-kalaignar-sonna-kuttik-kathaigal/DUPLICATE_AUDIT.md`.

Current intake result:

- exact canonical duplicate already established: `குருவி ராமேஸ்வரம்` — 1987 scan **23 / printed 22** — existing `stories/kuruvi-rameswaram/`; this range is **additional witness only**;
- `புகழேந்திப் புலவர் கதை` — identity hold pending full comparison with canonical `புகழேந்தி`;
- `யசோதர காவியம்` — identity hold because canonical `அமிர்தமதி` contains an embedded `யசோதர காவியம்` narrative;
- all other readable headings have no exact canonical-title match at intake, but **must still pass content-level duplicate review before activation**;
- 5 stylized-title rows cannot complete exact-title duplicate review until their headings are source-decoded.

No new 1987 canonical story folder has been created yet.

### Historical Tamil glyph gate — mandatory

The user supplied `HISTORICAL_TAMIL_GLYPH_TRANSCRIPTION_GUIDE.md` for this source, and it has been made a durable repository guide.

For every activated 1987 page:

- inspect the full source page;
- check all 13 known families: `ணா / ணை / ணொ / ணோ / லை / ளை / றா / றொ / றோ / னா / னை / னொ / னோ`;
- decode historical character identity into modern Unicode only;
- preserve source spelling, grammar, vocabulary, punctuation and spacing otherwise;
- compare same-edition forms when uncertain;
- never global-replace;
- unresolved old-glyph clusters remain `needs-review`;
- keep historical-glyph corrections separately auditable from ordinary transcription corrections.

## 1997 source — `திராவிட இயக்க எழுத்தாளர் சிறுகதைகள்`

Workspace: `collections/1997-dravida-iyakka-ezhuthalar-sirukathaigal/`

- source scans: **115**; contents: **10 works**.
- **9** short-story titles are represented canonically.
- `நண்பனா?`: **3/3 verified**, Tamil audit PASS, visual PASS, 0 unresolved, English PASS.
- `நடுத்தெரு நாராயணி`: reserved for separate short-novel handling in the novels archive; scans **62–85 / printed 52–75**.
- new-short-story onboarding from this source: **COMPLETE / CLOSED**.

## 2009 source — `16 கதையினிலே`

Workspace: `collections/2009-16-kathaiyinile/`

- SHA-256: `21daed58600d2e927dec4341fd1e0eab597f12d50f8c444458de9bc4ad18a859`
- size: **384,978,955 bytes**
- scans: **183**
- story block: scans **6–182**
- scan **183**: back cover
- source completeness: **16 / 16**
- new-story onboarding: **5 / 5 COMPLETE / CLOSED**
- existing-canonical additional-witness comparison: **11 / 11 COMPLETE / CLOSED**
- supplemental English for the five new 2009 stories: **5 / 5 PASS**

The supplied conversation upload is the full 183-scan PDF. The earlier 150-page limit was only a rendered-preview/access limit, not PDF truncation.

## Supplemental English translation — COMPLETE / CLOSED — 6 / 6

Tracker: `NEW_STORY_ENGLISH_TRANSLATION_PROGRESS.md`.

1. `நண்பனா?` — PASS.
2. `காந்தி தேசம்` — PASS.
3. `அணில் குஞ்சு` — PASS.
4. `கொள்ளைபுரம்` — PASS.
5. `எழுத்தாளர் ஏகலைவன்` — PASS.
6. `மலரவில்லை` — PASS.

Canonical Tamil remained unchanged during this translation phase.

## Completion-document interpretation

`ARCHIVE_COMPLETION.md` records the archive-wide closure achieved before the newly authorized 1987 intake. It now also carries a post-closure reactivation note. `PROJECT_COMPLETION.md` remains the historical 1977-specific record.

## CURRENT STATE / EXACT NEXT ACTIVITY

The previously authorized archive work remains closed, but the user has now explicitly authorized a **new 1987 collection intake**.

Current 1987 intake is **ACTIVE / NOT YET CLOSED**.

Exact next activity:

1. source-decode the five stylized headings on scans **13, 20, 31, 37 and 45** without guessing;
2. bring the direct-heading inventory to **25 / 25 exact**;
3. rerun duplicate-title/content checks for those five;
4. then process Story 1 (scan **5 / printed 4**) only after a fresh content-identity check;
5. use the historical-glyph guide from the first transcribed line onward.

Do not start `நடுத்தெரு நாராயணி` while the user is waiting for `வெள்ளிக்கிழமை` work in the novels repository to finish.