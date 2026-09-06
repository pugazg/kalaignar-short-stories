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

## USER-DIRECTED BATCHING — 15 NEW SCANS PER ITERATION

The user explicitly changed the active 1987 workflow to **15 physical source pages per iteration**.

- Batch 01: scans **6–20** — source/structure/identity review COMPLETE.
- Batch 02: scans **21–35** — NEXT.
- Boundary-context pages may be reopened without counting them among the 15 new scans.
- This batching rule overrides the earlier one-story-at-a-time stopping point for this active source, but does **not** override duplicate, source, glyph, or shared-boundary gates.

Batch-01 durable record:

`collections/1987-kalaignar-sonna-kuttik-kathaigal/BATCH_0001_SCANS_0006_0020.md`

## Batch 01 — authoritative physical routing

- Story 1 `மன்னனும் குருவியும்!`: scan **5 → upper 6**.
- Story 2 `அரசாபிமானக் கதை`: **lower 6 → upper 7**.
- Story 3 `தென்னை மரத்தில் புல்`: **lower 7 only**.
- Story 4 `நாராயணு! நாராயணு!`: **8 → 9 → upper 10**.
- Story 5 `துறவியும் சீடர்களும்`: **lower 10 → 11 → upper 12**.
- Story 6 `முல்லை முத்துக்குமரன்`: **lower 12 → upper 13**.
- Story 7 `சொர்க்கத்திற்குச் சென்றுவந்த அழகி!`: **lower 13 → 14 → upper 15**.
- Story 8 `புத்தர் உணர்த்திய உண்மை`: **lower 15 → 16 → 17 → upper 18**.
- Story 9 `கஜினி முகமதுவும் கவிஞர் பார்டோசியும்`: **lower 18 → 19 → upper 20**.
- Story 10 `இரு நிகழ்வுகள்`: begins **lower 20**, continues through scans 21–22.

Do not revert to the earlier simple one-heading-per-scan ranges.

## Canonical-identity state through Batch 01

### Story 1 — `மன்னனும் குருவியும்!`

- identity: **PASS — new canonical identity**
- workspace: `stories/mannanum-kuruviyum/`
- scan 5: verified
- upper scan 6: physical ending confirmed; exact old-type text `needs-review`
- story-wide Tamil/visual/historical-glyph closure: **OPEN**
- English: not authorized

### Story 2 — `அரசாபிமானக் கதை`

- identity: **PASS — existing canonical `ஜாடி குட்டி போடுமா?`**
- 1987 witness path: `stories/jaadi-kutti-poduma/witnesses/1987-kalaignar-sonna-kuttik-kathaigal/`
- physical span: lower 6 → upper 7
- exact 1987 lexical/historical-glyph closure: `needs-review`
- canonical 2008 Tamil changed: **No**
- canonical English changed: **No**

### Stories 3–9

Canonical-identity audit: **PASS — seven positively distinct identities**.

- `தென்னை மரத்தில் புல்`
- `நாராயணு! நாராயணு!`
- `துறவியும் சீடர்களும்`
- `முல்லை முத்துக்குமரன்`
- `சொர்க்கத்திற்குச் சென்றுவந்த அழகி!`
- `புத்தர் உணர்த்திய உண்மை`
- `கஜினி முகமதுவும் கவிஞர் பார்டோசியும்`

Special collision checks completed:

- 1987 `சொர்க்கத்திற்குச் சென்றுவந்த அழகி!` is **not** 2004 canonical `சொர்க்கத்திற்கு வந்தது எப்படி?`;
- 1987 `புத்தர் உணர்த்திய உண்மை` is **not** 1977 canonical `சித்தார்த்தன் சிலை`.

Their identities are cleared, but low-confidence canonical story folders were **not** created merely from rendered-page text. Exact lexical/historical-glyph closure remains open where character-level source certainty is insufficient.

### Story 10 — `இரு நிகழ்வுகள்`

- lower scan 20 reviewed;
- story continues 21–22;
- identity: **OPEN / partial**;
- complete in Batch 02 before any workspace decision.

## Other known duplicate controls ahead

- Story 11 `குருவி ராமேஸ்வரம்` — existing canonical; 1987 additional witness only.
- Story 14 `புகழேந்திப் புலவர் கதை` — identity hold vs canonical `புகழேந்தி`.
- Story 21 `யசோதர காவியம்` — identity hold vs embedded material in canonical `அமிர்தமதி`.
- `தெனாலிராமன் கதை` and `தெனாலிராமன் பூனை` require independent cross-comparison when reached.

## Historical-glyph status

Mandatory set:

`ணா / ணை / ணொ / ணோ / லை / ளை / றா / றொ / றோ / னா / னை / னொ / னோ`

Batch 01 completed 15/15 page-level physical/source-zone review with the historical-glyph checklist active. The available rendered source view is not sufficient to certify every small old-type character, so textual `verified` status was **not** fabricated.

- source/structure review: **Batch 01 COMPLETE**
- identity review: Stories 3–9 PASS; Story 10 open
- exact lexical / character-level historical-glyph closure: **OPEN where source pixels remain insufficient**
- no global replacement
- no silent modernization
- no later-edition wording imported into the 1987 source layer

## CURRENT STATE / EXACT NEXT ACTIVITY

1987 intake remains **ACTIVE**.

Process **Batch 02 — 15 new scans 21–35 inclusive**.

1. reopen scan 20 only as boundary context for Story 10;
2. review scans 21–22 and close Story 10's full physical span and duplicate/content identity;
3. scan 23 `குருவி ராமேஸ்வரம்` must remain an additional witness under its existing canonical workspace;
4. process scans 24–35, preserving every intra-page story boundary;
5. run duplicate/alternate-title narrative checks before any new story workspace creation;
6. apply the full historical-glyph gate to every reviewed page;
7. do not silently promote uncertain old-type text to `verified`;
8. update batch ledger, collection controls, `HANDOVER.md` and `NEXT_CHAT_PROMPT.md`;
9. next iteration after that should be 15 new scans **36–50** (with scan 35 available as boundary context if needed).

English is not authorized.

Do not begin `நடுத்தெரு நாராயணி` while waiting for `வெள்ளிக்கிழமை` completion in the novels workflow.
