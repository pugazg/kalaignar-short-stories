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

## USER-DIRECTED BATCHING — 15 NEW SCANS PER ITERATION

The active source is processed in batches of **15 new physical source scans**.

- Batch 01: **6–20** — COMPLETE at source/structure/identity-review layer.
- Batch 02: **21–35** — COMPLETE at source/structure/identity-review layer.
- Batch 03: **36–50** — NEXT.
- boundary-context overlap does not count toward the 15 new scans.
- batching does not weaken duplicate, source, shared-boundary, or historical-glyph gates.

Durable records:

- `collections/1987-kalaignar-sonna-kuttik-kathaigal/BATCH_0001_SCANS_0006_0020.md`
- `collections/1987-kalaignar-sonna-kuttik-kathaigal/BATCH_0002_SCANS_0021_0035.md`

## Identity / routing state through Batch 02

### Existing-canonical witnesses

- Story 2 `அரசாபிமானக் கதை` → canonical `ஜாடி குட்டி போடுமா?`; 1987 witness only; lower scan 6 → upper scan 7.
- Story 11 `குருவி ராமேஸ்வரம்` → existing canonical 2004 story; 1987 witness only; **corrected 1987 span lower scan 23 → upper scan 24**.

No canonical 2004/2008 Tamil or English is changed from these witnesses.

### Positively distinct identities established

**15 distinct 1987 identities:** Story 1; Stories 3–10; Stories 12–17.

Special resolved collisions:

- Story 7 `சொர்க்கத்திற்குச் சென்றுவந்த அழகி!` ≠ 2004 `சொர்க்கத்திற்கு வந்தது எப்படி?`.
- Story 8 `புத்தர் உணர்த்திய உண்மை` ≠ 1977 `சித்தார்த்தன் சிலை`.
- Story 14 `புகழேந்திப் புலவர் கதை` ≠ canonical 1977 `புகழேந்தி`; the earlier identity hold is **CLOSED**.

### Story 18 — partial

`ஜெயத்ரதனின் வீழ்ச்சி` begins lower scan **34**, continues scan **35**, and continues into scan **36**.

- Batch 02 source-zone review: done through scan 35.
- identity: **OPEN until complete span is reviewed in Batch 03**.

### Remaining explicit collision control

Story 21 `யசோதர காவியம்` — compare complete scans 41–43 against embedded material in canonical `stories/amirthamathi/` before any new-folder decision.

Stories 19 `தெனாலிராமன் கதை` and 24 `தெனாலிராமன் பூனை` must also be compared independently against current canon and against each other.

## Batch 02 authoritative boundaries

- Story 10 `இரு நிகழ்வுகள்`: lower **20 → 21 → 22 → upper 23**.
- Story 11 `குருவி ராமேஸ்வரம்`: lower **23 → upper 24**.
- Story 12 `சாமியாரும் பூக்காரியும்`: lower **24 → upper 25**.
- Story 13 `ஹஜ்ரத் அலியும் யூதனும்`: lower **25 → 26 → upper 27**.
- Story 14 `புகழேந்திப் புலவர் கதை`: lower **27 → 28**.
- Story 15 `மன மாற்றம்`: **29 → 30**.
- Story 16 `குறிக்கோள்`: **31 → upper 32**.
- Story 17 `பாலும் தண்ணீரும்`: lower **32 → 33 → upper 34**.
- Story 18 `ஜெயத்ரதனின் வீழ்ச்சி`: lower **34 → 35 → continues 36**.

Do not revert to intake shorthand ranges.

## Historical-glyph status

Mandatory families:

`ணா / ணை / ணொ / ணோ / லை / ளை / றா / றொ / றோ / னா / னை / னொ / னோ`

Both completed batches used this checklist during page review. The current rendered pages support physical boundaries, headings and narrative identity, but do not justify release-level transcription of every small old-type body-text character.

Therefore:

- source/structure review: Batches 01 and 02 COMPLETE;
- identity review: through Story 17 COMPLETE except existing-canonical witnesses; Story 18 partial;
- exact lexical / character-level historical-glyph closure: OPEN where pixels remain insufficient;
- no global replacement;
- no silent modernization;
- no wording imported from another edition to fill uncertain 1987 text.

## CURRENT STATE / EXACT NEXT ACTIVITY

Process **Batch 03 — 15 new scans 36–50 inclusive**.

1. reopen scan 35 only as context and finish Story 18 on scan 36;
2. close Story 18's duplicate/content identity gate;
3. process Stories 19–25 through scans 37–49, preserving all shared-page boundaries;
4. independently compare `தெனாலிராமன் கதை` and `தெனாலிராமன் பூனை`;
5. resolve Story 21 `யசோதர காவியம்` against canonical `அமிர்தமதி` before any workspace decision;
6. verify scan 50 as the final blank/damaged rear leaf;
7. apply the historical-glyph guide throughout;
8. create no low-confidence canonical text merely because identity is cleared;
9. synchronize collection controls, `HANDOVER.md`, and `NEXT_CHAT_PROMPT.md`;
10. English remains unauthorized.

Do not begin `நடுத்தெரு நாராயணி` while waiting for `வெள்ளிக்கிழமை` completion in the novels workflow.
