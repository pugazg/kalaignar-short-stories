# HANDOVER — Kalaignar Short Stories Archive

## Repository

- repository: `pugazg/kalaignar-short-stories`
- branch: `main`
- story workflow: `SHORT_STORY_PROCESSING_GUIDE.md`
- collection workflow: `COLLECTION_SOURCE_GUIDE.md`
- historical Tamil glyph workflow: `HISTORICAL_TAMIL_GLYPH_TRANSCRIPTION_GUIDE.md`
- English workflow: `ENGLISH_TRANSLATION_GUIDE.md`
- archive-wide closure history: `ARCHIVE_COMPLETION.md`
- historical 1977-only completion record: `PROJECT_COMPLETION.md`

## LIVE MAIN IS AUTHORITATIVE

Always fetch live `main` first and preserve newer durable state.

## Permanent rules

- controlling scan first; no silent normalization;
- before creating any new story workspace, prove it is not already canonical under the same or an alternate title;
- an additional edition witness must not silently overwrite an existing controlling edition;
- textual differences belong in explicit comparison/audit records;
- historical Tamil typeforms must be decoded by character identity, not modern visual resemblance;
- never global-replace historical-looking forms;
- source PDFs are not committed.

## Closed canonical collection phases — preserve

- 1977 — Tamil/visual/English **37/37 PASS**.
- 2008 — Tamil/visual/English **40/40 PASS**.
- 2004 — Tamil/visual/English **34/34 PASS**.
- 2009 new-story onboarding — **5/5 CLOSED**.
- 2009 existing-canonical witness comparison — **11/11 CLOSED**.
- supplemental English — **6/6 PASS / CLOSED**.

Do not reopen these merely to create work.

## ACTIVE AUTHORIZATION — 1987 `கலைஞர் சொன்ன குட்டிக் கதைகள்`

Workspace: `collections/1987-kalaignar-sonna-kuttik-kathaigal/`

Controlling source: `TVA_BOK_0065566_கலைஞர்_சொன்ன_குட்டிக்_கதைகள்_1987.pdf`

### Source identity

- byte size: **107,757,858 bytes**
- scans: **50**
- printed title: **கலைஞர் சொன்ன குட்டிக் கதைகள்**
- supplied/catalog author: **கலைஞர் மு. கருணாநிதி**
- title-page line: **`தொகுப்பு: முரசொலி குமரப்பன்`**
- publisher: **செல்வகுமார் பதிப்பகம்**, மதுரை
- first edition: **1984**
- represented edition: **இரண்டாம் பதிப்பு — 1987**
- scans **1–4**: front matter
- scans **5–49 / printed 4–48**: story block
- scan **50**: blank/damaged rear leaf
- no printed contents page
- SHA-256: **PENDING** because mounted-byte hashing remains unavailable; do not invent it.

### Direct-heading inventory — COMPLETE

Physical openings: **25 / 25**. Exact source headings: **25 / 25**. Title holds: **0**.

Former stylized holds resolved from enlarged pixels:

1. scan 13 — `சொர்க்கத்திற்குச் சென்றுவந்த அழகி!`
2. scan 20 — `இரு நிகழ்வுகள்`
3. scan 31 — `குறிக்கோள்`
4. scan 37 — `தெனாலிராமன் கதை`
5. scan 45 — `அகத்திணை அன்பு!`

Story 1 intake title was separately corrected from `மன்னனும் குறவியும்.` to **`மன்னனும் குருவியும்!`** by direct enlarged banner review.

### Duplicate gate — mandatory

Durable audit: `collections/1987-kalaignar-sonna-kuttik-kathaigal/DUPLICATE_AUDIT.md`.

Current state:

- `குருவி ராமேஸ்வரம்`, scan **23 / printed 22** — existing canonical `stories/kuruvi-rameswaram/`; 1987 is additional witness only.
- `புகழேந்திப் புலவர் கதை` — identity hold pending comparison with canonical `புகழேந்தி`.
- `யசோதர காவியம்` — identity hold because canonical `அமிர்தமதி` contains an embedded narrative of that name.
- all other rows require their own narrative identity check immediately before activation.

### Story 1 — `மன்னனும் குருவியும்!` — COMPLETE / PASS

Workspace: `stories/mannanum-kuruviyum/`

- 1987 scan **5 / printed 4** only
- scan **6** begins Story 2, `அரசாபிமானக் கதை`
- identity/duplicate audit: **PASS — positively distinct from current canon**
- source records: **1 / 1 verified**
- Tamil audit: **PASS**
- historical-glyph audit: **PASS**
- visual fidelity: **PASS**
- blocked / unresolved: **0**
- English: **not authorized / not started**

Historical-glyph-sensitive examples explicitly checked on scan 5 include `லை` (`வம்பில்லை`, `இல்லை`, `தேவையில்லை`), `னை` (`மன்னனைப்`) and `றா` (`என்றான்`). The full 13-family set was checked; unresolved glyphs: **0**.

Collection physical-source progress: **1 / 25 processed; 24 / 25 remain**.

## 1997 / 2009 durable closed state

- 1997 source: `நண்பனா?` onboarded/English PASS; `நடுத்தெரு நாராயணி` reserved for the novels/short-novel workflow, scans **62–85 / printed 52–75**.
- 2009 `16 கதையினிலே`: full source **183 scans / 384,978,955 bytes**; new-story onboarding **5/5 closed**; existing-canonical witness comparison **11/11 closed**; supplemental English for its five new stories **5/5 PASS**.
- The earlier scan-150 issue was only a rendered-preview limit, not PDF truncation.

## CURRENT STATE / EXACT NEXT ACTIVITY

1987 intake remains **ACTIVE**.

Process **Story 2 / 25 — `அரசாபிமானக் கதை` — scan 6 / printed page 5**.

Before writing Story 2:

1. fetch live `main`;
2. confirm Story 2 identity is not already canonical under another title using exact/variant title plus narrative premise/ending;
3. confirm the physical boundary because Story 3 `தென்னை மரத்தில் புல்` begins scan **7 / printed 6**;
4. if positively distinct, create/complete the Story-2 canonical workspace;
5. apply the attached historical-glyph guide to the whole scan, checking all 13 families before `verified`;
6. update collection inventory, scan map, duplicate audit, collection README and this handover;
7. do not start English unless separately authorized.

Do not begin `நடுத்தெரு நாராயணி` while the user is waiting for `வெள்ளிக்கிழமை` in the novels workflow to finish.