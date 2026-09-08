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

1987 final English release audit:
`collections/1987-kalaignar-sonna-kuttik-kathaigal/FINAL_ENGLISH_RELEASE_AUDIT_2026-09-08.md`

Do not reopen the 1987 collection without genuinely stronger source evidence or an explicit maintenance/audit request.

## Cross-project hold — preserve

`நடுத்தெரு நாராயணி` remains **BLOCKED from starting** while `வெள்ளிக்கிழமை` is incomplete in `pugazg/kalaignar-novels`.

The user explicitly confirmed `வெள்ளிக்கிழமை` is still incomplete and supplied the 1982 anthology below as an interim source. Work on this anthology is not permission to start `நடுத்தெரு நாராயணி`.

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
- source type: image-only; do not commit PDF

Collection state:

- source registration: **PASS**
- scan map: **95/95 mapped**
- story inventory: **5/5 COMPLETE**
- Tamil/source stories closed: **1/5**
- English: **not started**

Story ranges:

1. `பெற்ற பிள்ளையை விற்ற தாய்` — scans **7–28**, printed **5–26** — **PASS / CLOSED**
2. `காசா லேசா` — scans **29–40**, printed **27–38** — **NEXT**
3. `சீமான் வீட்டு சீக்காளி` — scans **41–49**, printed **39–47**
4. `நந்தியூர் நரியப்பன்` — scans **50–58**, printed **48–56**
5. `முடியாத தொடர்கதை` — scans **59–93**, printed **57–91**

## User-directed 1982 historical-glyph phase rule

For every story in this 1982 anthology:

**complete first-pass transcription → dedicated post-transcription historical-glyph gate at native/high resolution → separate final source/visual closure → next story**.

The minimum old-form set checked is:

`ணா / ணை / ணொ / ணோ / லை / ளை / றா / றொ / றோ / னா / னை / னொ / னோ`.

No global replacement, silent modernization or context-only correction is permitted.

## Story 1 — `பெற்ற பிள்ளையை விற்ற தாய்` — CLOSED

Workspace: `stories/petra-pillaiyai-vitra-thaai/`

Physical range:

- scans **7–28 / printed 5–26**
- scan 7: story opening
- scan 28: `ஆனால் அவள் வாழ்வு ????` + terminal star
- scan 29: forward boundary witness opening `காசா லேசா`

Durable final state:

- duplicate/canonical recheck before activation: **PASS — no existing canonical match**
- route: new canonical, controlled by this 1982 range
- first-pass transcription: **22/22 COMPLETE**
- historical-glyph high-resolution reread: **22/22 COMPLETE**
- historical-glyph gate: **PASS**
- unresolved historical-glyph clusters: **0**
- final source/visual closure: **PASS**
- verified pages: **22/22**
- unresolved ordinary source-text items: **0**
- assembled Tamil: **FINAL / synchronized**
- final audit: `stories/petra-pillaiyai-vitra-thaai/FINAL_SOURCE_VISUAL_AUDIT_2026-09-08.md`
- English: **not started**

Representative historical-glyph corrections include `நன்றாயில்ல`, `உடலைத்`, `என்றாள்`, `செயல்தானா`, `கண்ணபிரானை`, `சுற்றினாள்`, `எண்ணினாள்`, and `வேண்டுமென்றாள்`. Source-odd forms confirmed by high-resolution pixels remain preserved, including `முருங்கை மிலார்`, `தெரியாத்தனம்`, `கர்ப்பக்கிரகத்தில்`, `இலவுக்காத்தக் கிளி`, and the source's quoted குறள் wording.

The final source/visual pass also corrected ordinary scan-supported spacing/text readings on scans 27–28 without reopening or conflating the historical-glyph gate.

Do not reopen Story 1 without genuinely stronger source evidence or an explicit maintenance request.

## Exact next activity — Story 2 `காசா லேசா`

Do not pre-create the Story-2 workspace.

Physical range:

- scans **29–40 / printed 27–38**
- scan 29: stylized opening heading `காசா லேசா`
- later running headers may use `காசா லேசா!`; preserve source-layer distinction
- scan 40: Story-2 ending / terminal star
- scan 41: forward boundary witness opening `சீமான் வீட்டு சீக்காளி`

Before writing:

1. fetch live `main`;
2. read the permanent guides, this handover, `NEXT_CHAT_PROMPT.md`, and the active collection controls;
3. rerun duplicate/canonical-identity search for `காசா லேசா` plus distinctive source fragments;
4. verify scan 29 opening, scan 40 ending and scan 41 forward boundary from the controlling PDF;
5. if still a new canonical route, create the Story-2 workspace and page records for exactly scans 29–40;
6. perform source-faithful first-pass transcription only; keep all pages `needs-review`;
7. after the full story transcription is complete, run the user-directed separate native/high-resolution Historical Tamil Glyph Gate before final source/visual closure.

Do **not** start `நடுத்தெரு நாராயணி`; its external `வெள்ளிக்கிழமை` gate remains unsatisfied.
