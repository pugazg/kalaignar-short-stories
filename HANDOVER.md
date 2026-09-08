# HANDOVER — Kalaignar Short Stories Archive

## Repository

- repository: `pugazg/kalaignar-short-stories`
- branch: `main`
- permanent workflows: `SHORT_STORY_PROCESSING_GUIDE.md`, `COLLECTION_SOURCE_GUIDE.md`, `HISTORICAL_TAMIL_GLYPH_TRANSCRIPTION_GUIDE.md`, `ENGLISH_TRANSLATION_GUIDE.md`

## LIVE MAIN IS AUTHORITATIVE

Always fetch live `main` first and preserve newer durable state.

## Permanent phase rules

- controlling scan first; no silent normalization;
- preserve shared physical page boundaries;
- additional witnesses never overwrite controlling canonical editions;
- decode historical Tamil type by character identity, never visual resemblance alone;
- Tamil/source closes before English;
- completed collection phases stay frozen unless stronger source evidence appears or the user explicitly requests maintenance;
- for anthology work, process **one story at a time** unless the user explicitly changes that rule.

## Closed phases — preserve

- 1977 — Tamil/visual/English **37/37 PASS**
- 2008 — Tamil/visual/English **40/40 PASS**
- 2004 — Tamil/visual/English **34/34 PASS**
- 2009 new-story onboarding — **5/5 CLOSED**
- 2009 existing-canonical witness comparison — **11/11 CLOSED**
- supplemental English — **6/6 PASS / CLOSED**
- 1987 `கலைஞர் சொன்ன குட்டிக் கதைகள்` Tamil/source — **PASS / CLOSED**
- 1987 `கலைஞர் சொன்ன குட்டிக் கதைகள்` English — **25/25 PASS / CLOSED**

## Cross-project hold — preserve

`நடுத்தெரு நாராயணி` remains **BLOCKED from starting** while `வெள்ளிக்கிழமை` is incomplete in `pugazg/kalaignar-novels`.

## ACTIVE — 1982 `முடியாத தொடர்கதை`

Collection workspace: `collections/1982-mudiyatha-thodarkathai/`

Controlling source: `TVA_BOK_0065572_முடியாத_தொடர்கதை.pdf`

- **95 scans**
- **194,350,272 bytes**
- SHA-256 **`d69034c5374c6c1604ddeb6d8e034c4410ae0d58201f2dd1608edd0e6d8cfd41`**
- publisher: **தமிழோசை பதிப்பகம்**
- edition: **முதற்பதிப்பு — செப்டம்பர் 1982**
- image-only; do not commit PDF

Collection state:

- source registration: **PASS**
- scan map: **95/95 mapped**
- story inventory: **5/5 COMPLETE**
- Tamil/source stories closed: **3/5**
- English: **not started**

Story ranges:

1. `பெற்ற பிள்ளையை விற்ற தாய்` — scans **7–28**, printed **5–26** — **PASS / CLOSED — 22/22 verified**
2. `காசா லேசா` — scans **29–40**, printed **27–38** — **PASS / CLOSED — 12/12 verified**
3. `சீமான் வீட்டு சீக்காளி` — scans **41–49**, printed **39–47** — **PASS / CLOSED — 9/9 verified**
4. `நந்தியூர் நரியப்பன்` — scans **50–58**, printed **48–56** — **NEXT**
5. `முடியாத தொடர்கதை` — scans **59–93**, printed **57–91** — waiting

## User-directed 1982 phase rule

For every story:

**complete first-pass transcription → dedicated post-transcription Historical Tamil Glyph Gate at native/high resolution → separate final source/visual closure → next story**.

Minimum old-form set on every page:

`ணா / ணை / ணொ / ணோ / லை / ளை / றா / றொ / றோ / னா / னை / னொ / னோ`.

No global replacement, silent modernization or context-only correction.

## Stories 1–3 — CLOSED

- Story 1 `பெற்ற பிள்ளையை விற்ற தாய்`: PASS / CLOSED, 22/22 verified.
- Story 2 `காசா லேசா`: PASS / CLOSED, 12/12 verified.
- Story 3 `சீமான் வீட்டு சீக்காளி`: PASS / CLOSED, 9/9 verified.

Story-3 final audit: `stories/seemaan-veettu-seekkaali/FINAL_SOURCE_VISUAL_AUDIT_2026-09-08.md`.

Story-3 closure details:

- first pass: **9/9 COMPLETE**;
- Historical Tamil Glyph Gate: **PASS 9/9 / 0 unresolved**;
- final source/visual closure: **PASS 9/9**;
- page records: **9/9 verified**;
- final assembled Tamil: **synchronized**;
- physical scan 45→46 split restored at `குடும்பத் / தினர்`;
- unresolved ordinary source-text items: **0**;
- unresolved historical-glyph candidates: **0**.

Do not reopen Stories 1–3 without stronger evidence or explicit maintenance request.

## Exact next activity — Story 4 `நந்தியூர் நரியப்பன்` activation + first pass

Physical range:

- scans **50–58 / printed 48–56**;
- scan 50 opening heading: `நந்தியூர் நரியப்பன்`;
- scan 58: terminal star;
- scan 59: forward boundary opens Story 5 `முடியாத தொடர்கதை`.

Required next activity:

1. fetch live `main` and preserve newer durable work;
2. read permanent guides, this handover, `NEXT_CHAT_PROMPT.md`, active collection controls, and Story-3 closure only as precedent;
3. resolve the controlling PDF before source-pixel work;
4. rerun duplicate/canonical-identity search for exact title `நந்தியூர் நரியப்பன்` plus distinctive opening fragments;
5. visually verify scan 50 opening, scan 58 ending/star, and scan 59 forward boundary;
6. if still new canonical, create Story-4 workspace and exactly 9 page records for scans 50–58 / printed 48–56;
7. complete source-faithful first-pass transcription for all 9 pages;
8. keep every page `needs-review`;
9. synchronize Story-4 first-pass assembly and controls;
10. **stop after durable first pass** — do not run its Historical Tamil Glyph Gate in the same activity;
11. do not pre-create or start Story 5.

Do not start `நடுத்தெரு நாராயணி`; its `வெள்ளிக்கிழமை` gate remains unsatisfied.
