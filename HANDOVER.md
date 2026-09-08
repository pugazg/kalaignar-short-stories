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

The planned source `நடுத்தெரு நாராயணி` remains **BLOCKED from starting** while `வெள்ளிக்கிழமை` is incomplete in `pugazg/kalaignar-novels`.

The user explicitly confirmed `வெள்ளிக்கிழமை` is still incomplete and supplied the 1982 anthology below as an interim source. Work on the interim source is not permission to start `நடுத்தெரு நாராயணி`.

## ACTIVE — 1982 `முடியாத தொடர்கதை`

Collection workspace:
`collections/1982-mudiyatha-thodarkathai/`

Controlling source:
`TVA_BOK_0065572_முடியாத_தொடர்கதை.pdf`

Source identity:

- **95 scans**
- **194,350,272 bytes**
- SHA-256 **`d69034c5374c6c1604ddeb6d8e034c4410ae0d58201f2dd1608edd0e6d8cfd41`**
- printed title: **முடியாத தொடர்கதை**
- printed author: **கலைஞர் மு. கருணாநிதி**
- publisher: **தமிழோசை பதிப்பகம்**
- edition: **முதற்பதிப்பு — செப்டம்பர் 1982**
- source type: image-only
- source PDF committed: **No**

## Collection intake state

- source registration: **PASS**
- structural scan map: **95 / 95 mapped**
- separate printed contents page: **not present**
- story-opening inventory: **5 / 5 COMPLETE**
- collection-level duplicate/canonical preflight: **5 / 5 — no existing match found**
- Tamil/source stories closed: **0 / 5**
- English: **not started**

Story ranges:

1. `பெற்ற பிள்ளையை விற்ற தாய்` — scans **7–28**, printed **5–26**
2. `காசா லேசா` — scans **29–40**, printed **27–38**
3. `சீமான் வீட்டு சீக்காளி` — scans **41–49**, printed **39–47**
4. `நந்தியூர் நரியப்பன்` — scans **50–58**, printed **48–56**
5. `முடியாத தொடர்கதை` — scans **59–93**, printed **57–91**

Back matter:

- scan 94 — advertisement / next-publication page
- scan 95 — back cover

Important source-title notes:

- opening `காசா லேசா`; later running header `காசா லேசா!`;
- opening `சீமான் வீட்டு சீக்காளி`; later running header `சீமான் வீட்டு சீக்காளி!`;
- collection title and Story 5 share the wording `முடியாத தொடர்கதை`; keep collection and story identities separate.

## User-directed 1982 historical-glyph phase rule

This book contains many historical Tamil glyphs. For every story in this 1982 anthology, use an explicit **post-transcription historical-glyph gate**:

1. complete the whole story's first-pass transcription from the controlling scan;
2. keep all page records `needs-review` and do **not** call them finally verified;
3. after transcription is complete, run one dedicated independent old-glyph gate over **every page** in the story;
4. explicitly check the minimum families `ணா / ணை / ணொ / ணோ / லை / ளை / றா / றொ / றோ / னா / னை / னொ / னோ`, plus any other suspicious historical forms;
5. compare native/high-resolution pixels and same-edition forms where needed; record each correction individually;
6. never global-replace, silently modernize, or use expected modern wording as proof;
7. do not advance to the next anthology story until the active story's historical-glyph gate and source closure have PASSed.

This gate is deliberately a separate phase **after transcription**. Old-glyph observations made during the first pass do not count as gate closure.

## Story 1 — `பெற்ற பிள்ளையை விற்ற தாய்`

Workspace:
`stories/petra-pillaiyai-vitra-thaai/`

Physical range:

- scans **7–28**
- printed pages **5–26**
- scan 7 opening: `பெற்ற பிள்ளையை விற்ற தாய்`
- scan 28 ending: `ஆனால் அவள் வாழ்வு ????` + terminal star
- forward boundary witness: scan 29 opens `காசா லேசா`

Activation / current state:

- live-main duplicate recheck before creation: **PASS — no existing canonical match**
- canonical route: **new canonical**, controlled by this 1982 source
- first-pass transcription: **22 / 22 COMPLETE**
- assembled first-pass Tamil: **COMPLETE**
- page status: **22 / 22 `needs-review`**
- final verified pages: **0 / 22**
- historical-glyph gate: **PENDING**
- possible-error / old-glyph candidate queue: **OPEN**
- English: **not started / not eligible**

Important: current first-pass forms such as `நன்றுயில்ல`, `சுற்றினுள்`, `எண்ணினுள்`, `வேண்டுமென்றுள்` are **not claims of final source readings**. They remain explicit old-glyph candidates until the dedicated gate proves character identity from the scan.

## Exact next activity — Story 1 Historical Tamil Glyph Gate

Do **not** start Story 2 yet.

Run `stories/petra-pillaiyai-vitra-thaai/HISTORICAL_GLYPH_GATE.md` across **all scans 7–28 / printed 5–26**:

1. reopen every physical page at native/high resolution;
2. check all 13 mandatory historical families on every page, plus all suspicious forms;
3. revisit every item in `POSSIBLE_ERRORS_FOR_REVIEW.md`;
4. record each source-supported correction in the gate log;
5. synchronize corrections into the relevant `pages/*.md` file and `sections/petra-pillaiyai-vitra-thaai.md`;
6. leave genuinely unresolved clusters `needs-review` and use the difficult-reading escalation protocol rather than guessing;
7. only after this gate PASSes proceed to Story-1 final source/visual closure.

After Story 1 is fully source-closed, advance the collection controls to Story 2 `காசா லேசா`, scans **29–40 / printed 27–38**, and rerun its duplicate/canonical search before creating a workspace.
