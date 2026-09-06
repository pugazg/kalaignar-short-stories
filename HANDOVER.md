# HANDOVER — Kalaignar Short Stories Archive

## Repository

- repository: `pugazg/kalaignar-short-stories`
- branch: `main`
- story workflow: `SHORT_STORY_PROCESSING_GUIDE.md`
- collection workflow: `COLLECTION_SOURCE_GUIDE.md`
- historical Tamil glyph workflow: `HISTORICAL_TAMIL_GLYPH_TRANSCRIPTION_GUIDE.md`
- English workflow: `ENGLISH_TRANSLATION_GUIDE.md`
- archive-wide closure history: `ARCHIVE_COMPLETION.md`

## LIVE MAIN IS AUTHORITATIVE

Always fetch live `main` first and preserve newer durable state.

## Permanent rules

- controlling scan first; no silent normalization;
- before creating any new story workspace, prove it is not already canonical under the same or an alternate title;
- preserve shared physical page boundaries exactly;
- additional witnesses never silently overwrite canonical controlling editions;
- textual differences belong in explicit comparison/audit records;
- historical Tamil typeforms are decoded by character identity, not modern visual resemblance;
- never global-replace historical-looking forms;
- source PDFs are not committed.

## Closed phases — preserve

- 1977 — Tamil/visual/English **37/37 PASS**.
- 2008 — Tamil/visual/English **40/40 PASS**.
- 2004 — Tamil/visual/English **34/34 PASS**.
- 2009 new-story onboarding — **5/5 CLOSED**.
- 2009 existing-canonical witness comparison — **11/11 CLOSED**.
- supplemental English — **6/6 PASS / CLOSED**.

## ACTIVE — 1987 `கலைஞர் சொன்ன குட்டிக் கதைகள்`

Workspace: `collections/1987-kalaignar-sonna-kuttik-kathaigal/`

Controlling source: `TVA_BOK_0065566_கலைஞர்_சொன்ன_குட்டிக்_கதைகள்_1987.pdf`

Source identity:

- scans: **50**
- size: **107,757,858 bytes**
- publisher: **செல்வகுமார் பதிப்பகம்**, மதுரை
- first edition: **1984**
- represented edition: **இரண்டாம் பதிப்பு — 1987**
- headings: **25 / 25 exact**
- SHA-256: **PENDING**; do not invent it.

## Shared-boundary correction — authoritative

Direct whole-page review of scans 6–7 supersedes the earlier simple scan ranges:

- Story 1 `மன்னனும் குருவியும்!`: scan **5 → upper scan 6**;
- Story 2 `அரசாபிமானக் கதை`: **lower scan 6 → upper scan 7**;
- Story 3 `தென்னை மரத்தில் புல்`: begins **lower scan 7**.

The previous Story-1 statement “scan 5 only / no continuation on scan 6” is withdrawn.

## Story 1 — `மன்னனும் குருவியும்!` — REOPENED

Workspace: `stories/mannanum-kuruviyum/`.

- identity: **PASS — new canonical identity**
- scan 5: verified
- upper scan 6: physical continuation confirmed, exact text **needs-review**
- source records: **1 verified + 1 needs-review**
- scan-5 historical glyph audit: PASS
- upper-scan-6 historical glyph audit: pending
- story-wide Tamil/visual PASS: withdrawn until full span closes
- English: not authorized

Do not reconstruct the missing upper scan-6 wording from context.

## Story 2 — `அரசாபிமானக் கதை` — EXISTING CANONICAL IDENTITY

Duplicate gate result: **PASS — same narrative as canonical `ஜாடி குட்டி போடுமா?`**.

Existing canonical workspace: `stories/jaadi-kutti-poduma/`.

1987 witness path:

`stories/jaadi-kutti-poduma/witnesses/1987-kalaignar-sonna-kuttik-kathaigal/`

State:

- physical span: lower scan 6 → upper scan 7
- narrative identity: PASS
- new `அரசாபிமானக் கதை` canonical folder: **No**
- exact 1987 lexical transcription: **needs-review**
- 1987 historical-glyph audit: **needs-review**
- canonical 2008 Tamil changed: **No**
- canonical English changed: **No**

The alternate 1987 heading is edition evidence and does not rename the canonical 2008 story.

## Other duplicate controls

- `குருவி ராமேஸ்வரம்` — existing canonical, additional witness only.
- `புகழேந்திப் புலவர் கதை` — identity hold vs `புகழேந்தி`.
- `யசோதர காவியம்` — identity hold vs embedded material in `அமிர்தமதி`.

## CURRENT STATE / EXACT NEXT ACTIVITY

1987 intake is **ACTIVE**. Do **not** start Story 3 yet.

Finish shared scans **6–7**:

1. direct source transcription of Story-1 upper scan 6;
2. full 13-family historical-glyph audit for that span;
3. direct source transcription of the Story-2 1987 witness lower scan 6 → upper scan 7;
4. full witness historical-glyph audit;
5. line-level reversible comparison with canonical `ஜாடி குட்டி போடுமா?`, without changing the 2008 canonical layer;
6. re-run Story-1 Tamil/visual closure;
7. synchronize collection controls;
8. only then advance to Story 3 `தென்னை மரத்தில் புல்` at lower scan 7.

Do not begin `நடுத்தெரு நாராயணி` while waiting for `வெள்ளிக்கிழமை` completion in the novels workflow.