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
- Tamil/source closes before English; once closed, English is automatically next unless the user redirects;
- completed collection phases stay frozen unless genuinely stronger source evidence appears or the user explicitly requests maintenance;
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

1987 final English release audit: `collections/1987-kalaignar-sonna-kuttik-kathaigal/FINAL_ENGLISH_RELEASE_AUDIT_2026-09-08.md`.

## Cross-project hold — preserve

`நடுத்தெரு நாராயணி` remains **BLOCKED from starting** while `வெள்ளிக்கிழமை` is incomplete in `pugazg/kalaignar-novels`. The user explicitly confirmed that external gate is still unsatisfied.

## ACTIVE — 1982 `முடியாத தொடர்கதை`

Collection workspace: `collections/1982-mudiyatha-thodarkathai/`

Controlling source: `TVA_BOK_0065572_முடியாத_தொடர்கதை.pdf`

- **95 scans**
- **194,350,272 bytes**
- SHA-256 **`d69034c5374c6c1604ddeb6d8e034c4410ae0d58201f2dd1608edd0e6d8cfd41`**
- title: **முடியாத தொடர்கதை**
- author: **கலைஞர் மு. கருணாநிதி**
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
3. `சீமான் வீட்டு சீக்காளி` — scans **41–49**, printed **39–47** — **NEXT**
4. `நந்தியூர் நரியப்பன்` — scans **50–58**, printed **48–56** — waiting
5. `முடியாத தொடர்கதை` — scans **59–93**, printed **57–91** — waiting

## User-directed 1982 phase rule

For every story:

**complete first-pass transcription → dedicated post-transcription Historical Tamil Glyph Gate at native/high resolution → separate final source/visual closure → next story**.

Minimum old-form set on every page:

`ணா / ணை / ணொ / ணோ / லை / ளை / றா / றொ / றோ / னா / னை / னொ / னோ`.

No global replacement, silent modernization or context-only correction.

## Story 1 — `பெற்ற பிள்ளையை விற்ற தாய்` — CLOSED

Workspace: `stories/petra-pillaiyai-vitra-thaai/`. Scans **7–28 / printed 5–26**. First pass 22/22, historical-glyph gate PASS, final source/visual closure PASS, 22/22 verified, 0 unresolved source/glyph items. Final audit: `stories/petra-pillaiyai-vitra-thaai/FINAL_SOURCE_VISUAL_AUDIT_2026-09-08.md`. Do not reopen without stronger evidence or explicit maintenance request.

## Story 2 — `காசா லேசா` — CLOSED

Workspace: `stories/kaasa-lesa/`.

- scans **29–40 / printed 27–38**;
- fresh duplicate/canonical recheck before activation: **PASS — new canonical**;
- first-pass transcription: **12/12 COMPLETE**;
- first-pass durable commit: `cd953e2e2d1ecd28fb242a1abf654ff2a4842c26`;
- native/high-resolution Historical Tamil Glyph Gate: **PASS 12/12**;
- glyph-gate durable commit: `1c6cb74eedb68988c8c287440fad70e78d22d2eb`;
- historical-glyph corrections: `காலணா`, `வாறே`, `ஊழலை`;
- separate final source/visual closure: **PASS**;
- verified page records: **12/12**;
- unresolved ordinary source-text items: **0**;
- unresolved historical-glyph candidates: **0**;
- assembled Tamil: **FINAL / synchronized**;
- final audit: `stories/kaasa-lesa/FINAL_SOURCE_VISUAL_AUDIT_2026-09-08.md`;
- English: **not started**.

Source-layer title/header forms preserved:

- scan 29 opening: `காசா லேசா`;
- even-page headers through scan 38: `காசா லேசா!`;
- scan 40 header: `காசாலேசா!`;
- scan 39 body wordplay: `காசாலேசா! காசாலே; நீ; சா!`.

Do not reopen Story 2 without stronger evidence or explicit maintenance request.

## Exact next activity — Story 3 `சீமான் வீட்டு சீக்காளி`

Physical range:

- scans **41–49 / printed 39–47**;
- scan 41 stylized opening heading: `சீமான் வீட்டு சீக்காளி`;
- later running headers may use `சீமான் வீட்டு சீக்காளி!`; preserve source-layer distinction;
- scan 49: terminal star;
- scan 50: forward-boundary witness opening `நந்தியூர் நரியப்பன்`.

Required next activity:

1. fetch live `main` and preserve newer durable work;
2. read permanent guides, this handover, `NEXT_CHAT_PROMPT.md`, active collection controls, and the closed Story-2 controls only as precedent;
3. resolve the controlling PDF before source-pixel work;
4. rerun duplicate/canonical-identity search for exact title `சீமான் வீட்டு சீக்காளி` plus distinctive source fragments;
5. visually verify scan 41 opening, scan 49 ending/star, and scan 50 forward boundary;
6. if still new canonical, create Story-3 workspace and page records for exactly scans 41–49 / printed 39–47;
7. complete source-faithful first-pass transcription for all 9 pages; keep every page `needs-review`;
8. synchronize Story-3 first-pass assembly and controls;
9. **stop after durable first-pass transcription** — do not run the separate historical-glyph gate in the same activity;
10. do not pre-create or start Story 4.

Do not start `நடுத்தெரு நாராயணி`; its `வெள்ளிக்கிழமை` gate remains unsatisfied.
