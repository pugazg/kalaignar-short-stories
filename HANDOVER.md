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

The user explicitly confirmed `வெள்ளிக்கிழமை` is still incomplete and supplied a different interim source. Do not use work on the interim source as permission to start `நடுத்தெரு நாராயணி`.

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
- repository duplicate/canonical preflight: **5 / 5 — no existing match found**
- Tamil story processing: **0 / 5**
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

## Exact next activity — Story 1

Process **`பெற்ற பிள்ளையை விற்ற தாய்`**, scans **7–28 / printed pages 5–26**.

Before writing:

1. fetch live `main`;
2. read `SHORT_STORY_PROCESSING_GUIDE.md`, `COLLECTION_SOURCE_GUIDE.md`, `HISTORICAL_TAMIL_GLYPH_TRANSCRIPTION_GUIDE.md`, this handover, `NEXT_CHAT_PROMPT.md`, and the active collection README/inventory/scan map;
3. rerun duplicate/canonical search for `பெற்ற பிள்ளையை விற்ற தாய்` before creating the story folder;
4. visually confirm scan 7 opening and scan 28 ending; scan 29 is the forward boundary witness and opens `காசா லேசா`;
5. if still new, create its canonical workspace and page records for exactly scans 7–28;
6. complete Pass 1 source transcription and the separate high-resolution historical-glyph Pass 2; no global replacement or modernization;
7. do not start Story 2 in the same activity unless the user explicitly changes the one-story rule.

After Story 1 is fully synchronized, advance the collection and root controls to Story 2 `காசா லேசா` scans 29–40 / printed 27–38.
