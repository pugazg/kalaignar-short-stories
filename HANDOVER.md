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
- Tamil/source stories closed: **2/5**
- English: **not started**

Story ranges:

1. `பெற்ற பிள்ளையை விற்ற தாய்` — scans **7–28**, printed **5–26** — **PASS / CLOSED — 22/22 verified**
2. `காசா லேசா` — scans **29–40**, printed **27–38** — **PASS / CLOSED — 12/12 verified**
3. `சீமான் வீட்டு சீக்காளி` — scans **41–49**, printed **39–47** — **FIRST PASS 9/9 COMPLETE; GLYPH GATE NEXT**
4. `நந்தியூர் நரியப்பன்` — scans **50–58**, printed **48–56** — waiting
5. `முடியாத தொடர்கதை` — scans **59–93**, printed **57–91** — waiting

## User-directed 1982 phase rule

For every story:

**complete first-pass transcription → dedicated post-transcription Historical Tamil Glyph Gate at native/high resolution → separate final source/visual closure → next story**.

Minimum old-form set on every page:

`ணா / ணை / ணொ / ணோ / லை / ளை / றா / றொ / றோ / னா / னை / னொ / னோ`.

No global replacement, silent modernization or context-only correction.

## Stories 1–2 — CLOSED

- Story 1 `பெற்ற பிள்ளையை விற்ற தாய்`: PASS / CLOSED, 22/22 verified.
- Story 2 `காசா லேசா`: PASS / CLOSED, 12/12 verified, final audit `stories/kaasa-lesa/FINAL_SOURCE_VISUAL_AUDIT_2026-09-08.md`.

Do not reopen without stronger evidence or explicit maintenance request.

## Story 3 — `சீமான் வீட்டு சீக்காளி` — CURRENT DURABLE CHECKPOINT

Workspace: `stories/seemaan-veettu-seekkaali/`

Physical range:

- scans **41–49 / printed 39–47**;
- scan 41 opening display: `சீமான் வீட்டு சீக்காளி`;
- later running header: `சீமான் வீட்டுச் சீக்காளி!`;
- scan 49: terminal star;
- scan 50: forward boundary opens `நந்தியூர் நரியப்பன்` and is excluded.

Activation / first-pass state:

- fresh duplicate/canonical recheck against live `main` `e12339ebcc9cdfdc2f24197747874ddf9d2ca43d`: **PASS — no existing canonical match**;
- route: **new canonical** controlled by this 1982 source range;
- first-pass transcription: **9/9 COMPLETE**;
- first-pass assembled Tamil: **COMPLETE / synchronized**;
- page status: **9/9 `needs-review`**;
- Historical Tamil Glyph Gate: **NOT STARTED / NEXT**;
- final source/visual closure: **not started**;
- English: **not started**.

Review queue: `stories/seemaan-veettu-seekkaali/POSSIBLE_ERRORS_FOR_REVIEW.md`.

## Exact next activity — Story 3 Historical Tamil Glyph Gate

1. fetch live `main` and preserve newer durable work;
2. read permanent guides, this handover, `NEXT_CHAT_PROMPT.md`, Story-3 README, metadata, page map, review queue, all nine page records and the assembled Tamil;
3. resolve the controlling PDF before source-pixel work;
4. reopen scans **41–49** at native/high resolution independently of the first pass;
5. explicitly inspect `ணா / ணை / ணொ / ணோ / லை / ளை / றா / றொ / றோ / னா / னை / னொ / னோ` plus every suspicious ligature/touching character;
6. record every correction individually; never global-replace or modernize;
7. synchronize corrections across page records and assembled Tamil;
8. if zero unresolved historical-glyph candidates remain, record gate PASS;
9. keep all nine page records `needs-review` because final source/visual closure remains separate;
10. **hard stop: do not run final source/visual closure in the same activity and do not start Story 4.**

Do not start `நடுத்தெரு நாராயணி`; its `வெள்ளிக்கிழமை` gate remains unsatisfied.
