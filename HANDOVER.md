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

## USER-DIRECTED BATCHING — 15 PHYSICAL SCANS PER ITERATION

The source/structure/canonical-identity review phase is now complete:

- Batch 01: **6–20** — COMPLETE.
- Batch 02: **21–35** — COMPLETE.
- Batch 03: **36–50** — COMPLETE.

Durable records:

- `collections/1987-kalaignar-sonna-kuttik-kathaigal/BATCH_0001_SCANS_0006_0020.md`
- `collections/1987-kalaignar-sonna-kuttik-kathaigal/BATCH_0002_SCANS_0021_0035.md`
- `collections/1987-kalaignar-sonna-kuttik-kathaigal/BATCH_0003_SCANS_0036_0050.md`

The same 15-page rule now applies to lexical/historical-glyph closure.

## Full identity disposition — 25 / 25 COMPLETE

### Existing-canonical witnesses — 2

- Story 2 `அரசாபிமானக் கதை` → canonical `ஜாடி குட்டி போடுமா?`; 1987 witness only; lower 6 → upper 7.
- Story 11 `குருவி ராமேஸ்வரம்` → canonical 2004 story; 1987 witness only; lower 23 → upper 24.

No controlling canonical Tamil/English is changed from these witnesses.

### Positively distinct identities — 23

Story 1; Stories 3–10; Stories 12–25.

Resolved collision checks:

- Story 7 `சொர்க்கத்திற்குச் சென்றுவந்த அழகி!` ≠ 2004 `சொர்க்கத்திற்கு வந்தது எப்படி?`.
- Story 8 `புத்தர் உணர்த்திய உண்மை` ≠ 1977 `சித்தார்த்தன் சிலை`.
- Story 14 `புகழேந்திப் புலவர் கதை` ≠ 1977 `புகழேந்தி`.
- Story 21 `யசோதர காவியம்` ≠ canonical `அமிர்தமதி`; the latter is a separate literary-theft story containing Yashodhara material as embedded source/adaptation.
- Story 19 `தெனாலிராமன் கதை` ≠ Story 24 `தெனாலிராமன் பூனை`.

Unresolved identity holds: **0**.

## Final Batch-03 authoritative boundaries

- Story 18 `ஜெயத்ரதனின் வீழ்ச்சி`: lower **34 → 35 → 36 → upper 37**.
- Story 19 `தெனாலிராமன் கதை`: lower **37 → 38 → upper 39**.
- Story 20 `வல்வில் ஓரி`: lower **39 → 40 → upper 41**.
- Story 21 `யசோதர காவியம்`: lower **41 → 42 → 43 → upper 44**.
- Story 22 `காடு சென்ற குமணன்`: lower **44 → upper 45**.
- Story 23 `அகத்திணை அன்பு!`: lower **45 → upper 46**.
- Story 24 `தெனாலிராமன் பூனை`: lower **46 → 47 → upper 48**.
- Story 25 `குழந்தையும் கிளியும்`: lower **48 → 49**.
- scan **50**: terminal blank/damaged rear leaf; no story continuation.

Do not revert to intake shorthand ranges.

## Historical-glyph status

Mandatory families:

`ணா / ணை / ணொ / ணோ / லை / ளை / றா / றொ / றோ / னா / னை / னொ / னோ`

All three source-review batches used this checklist. The available rendered pages support headings, shared boundaries, illustrations and narrative identity, but do not justify release-level transcription of every small old-type body-text character.

Therefore:

- source/structure review: **COMPLETE for the full 1987 collection**;
- canonical-identity routing: **25 / 25 COMPLETE**;
- exact lexical / character-level historical-glyph closure: **OPEN** where pixels remain insufficient;
- no global replacement;
- no silent modernization;
- no wording imported from another edition to fill uncertain 1987 text.

## CURRENT STATE / EXACT NEXT ACTIVITY

Begin the **Tamil lexical + historical-glyph closure phase** while retaining the user's 15-page rule.

### Next iteration — scans 5–19 inclusive

1. inspect/transcribe the 15 physical scans **5–19** using the authoritative story boundaries;
2. apply `HISTORICAL_TAMIL_GLYPH_TRANSCRIPTION_GUIDE.md` to every page and every candidate in all 13 families;
3. preserve source wording, spelling, punctuation and historical character identity;
4. create/update story-local page records, sections, audits and witness layers only where exact source text is supportable;
5. keep unresolved clusters `needs-review` instead of guessing from grammar or another edition;
6. Story 2 remains an additional witness for canonical `ஜாடி குட்டி போடுமா?`;
7. do not modify closed canonical Tamil/English merely to match this 1987 printing;
8. do not begin English.

After scans 5–19, continue lexical/glyph closure in the same 15-page pattern.

Do not begin `நடுத்தெரு நாராயணி` while waiting for `வெள்ளிக்கிழமை` completion in the novels workflow.
