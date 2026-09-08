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
- Tamil/source stories closed: **0/5**
- English: **not started**

Story ranges:

1. `பெற்ற பிள்ளையை விற்ற தாய்` — scans **7–28**, printed **5–26**
2. `காசா லேசா` — scans **29–40**, printed **27–38**
3. `சீமான் வீட்டு சீக்காளி` — scans **41–49**, printed **39–47**
4. `நந்தியூர் நரியப்பன்` — scans **50–58**, printed **48–56**
5. `முடியாத தொடர்கதை` — scans **59–93**, printed **57–91**

## User-directed 1982 historical-glyph phase rule

For every story in this 1982 anthology:

**complete first-pass transcription → dedicated post-transcription historical-glyph gate at native/high resolution → separate final source/visual closure → next story**.

The minimum old-form set checked is:

`ணா / ணை / ணொ / ணோ / லை / ளை / றா / றொ / றோ / னா / னை / னொ / னோ`.

No global replacement, silent modernization or context-only correction is permitted.

## Story 1 — `பெற்ற பிள்ளையை விற்ற தாய்`

Workspace: `stories/petra-pillaiyai-vitra-thaai/`

Physical range:

- scans **7–28 / printed 5–26**
- scan 7: story opening
- scan 28: `ஆனால் அவள் வாழ்வு ????` + terminal star
- scan 29: forward boundary witness opening `காசா லேசா`

Current durable state:

- duplicate/canonical recheck before activation: **PASS — no existing canonical match**
- route: new canonical, controlled by this 1982 range
- first-pass transcription: **22/22 COMPLETE**
- assembled Tamil: **COMPLETE and synchronized with glyph-gate corrections**
- native/high-resolution historical-glyph review: **22/22 COMPLETE**
- historical-glyph gate: **PASS**
- historical-glyph review queue: **CLOSED**
- unresolved historical-glyph clusters: **0**
- page status: **22/22 `needs-review`**
- final verified pages: **0/22**
- final source/visual closure: **PENDING**
- English: **not started / not eligible**

Representative historical-glyph corrections include `நன்றாயில்ல`, `உடலைத்`, `என்றாள்`, `செயல்தானா`, `கண்ணபிரானை`, `சுற்றினாள்`, `எண்ணினாள்`, and `வேண்டுமென்றாள்`. The audit also preserves source-odd forms when high-resolution pixels support them, including `முருங்கை மிலார்`, `தெரியாத்தனம்`, and the source's quoted குறள் wording.

## Exact next activity — Story 1 final source / visual closure

Do **not** start Story 2 yet.

Across scans **7–28 / printed 5–26**:

1. compare every corrected page record against the controlling source;
2. verify phrase/clause/sentence continuity, including every scan-to-scan continuation;
3. verify physical page markers and scan/printed-page mapping;
4. verify the scan 28 ending and scan 29 forward boundary witness;
5. verify page records and assembled Tamil agree after all glyph corrections;
6. resolve any remaining ordinary source-text uncertainty without using modernization or context as authority;
7. only if unresolved source-text items are 0, promote the 22 page records to `verified` and close Story 1 Tamil/source.

After Story 1 is fully source-closed, advance collection controls to Story 2 `காசா லேசா`, scans **29–40 / printed 27–38**, and rerun its duplicate/canonical search before creating a workspace.
