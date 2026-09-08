# HANDOVER — Kalaignar Short Stories Archive

## Repository

- repository: `pugazg/kalaignar-short-stories`
- branch: `main`
- permanent workflows: `SHORT_STORY_PROCESSING_GUIDE.md`, `COLLECTION_SOURCE_GUIDE.md`, `HISTORICAL_TAMIL_GLYPH_TRANSCRIPTION_GUIDE.md`, `ENGLISH_TRANSLATION_GUIDE.md`

## LIVE MAIN IS AUTHORITATIVE

Always fetch live `main` first and preserve newer durable state.

## Permanent phase rules

- controlling scan first; no silent normalization;
- preserve physical page boundaries;
- historical Tamil glyphs are decoded by character identity, not visual resemblance;
- Tamil/source closes before English;
- anthology work proceeds one story at a time;
- each 1982 story: **first pass → dedicated historical-glyph gate → separate final source/visual closure → next story**.

## Closed phases — preserve

- 1977 — Tamil/visual/English **37/37 PASS**
- 2008 — Tamil/visual/English **40/40 PASS**
- 2004 — Tamil/visual/English **34/34 PASS**
- 2009 new-story onboarding — **5/5 CLOSED**
- 2009 existing-canonical witness comparison — **11/11 CLOSED**
- supplemental English — **6/6 PASS / CLOSED**
- 1987 `கலைஞர் சொன்ன குட்டிக் கதைகள்` Tamil/source + English — **CLOSED / 25/25 English PASS**

## Cross-project hold

`நடுத்தெரு நாராயணி` remains **BLOCKED** while `வெள்ளிக்கிழமை` is incomplete in `pugazg/kalaignar-novels`.

## ACTIVE — 1982 `முடியாத தொடர்கதை`

Source: `TVA_BOK_0065572_முடியாத_தொடர்கதை.pdf` — **95 scans**, **194,350,272 bytes**, SHA-256 `d69034c5374c6c1604ddeb6d8e034c4410ae0d58201f2dd1608edd0e6d8cfd41`, first edition September 1982, image-only; do not commit PDF.

### Corrected inventory — 6 stories

1. `பெற்ற பிள்ளையை விற்ற தாய்` — scans 7–28 / pp.5–26 — **PASS / CLOSED — 22/22 verified**
2. `காசா லேசா` — scans 29–40 / pp.27–38 — **PASS / CLOSED — 12/12 verified**
3. `சீமான் வீட்டு சீக்காளி` — scans 41–49 / pp.39–47 — **PASS / CLOSED — 9/9 verified**
4. `நந்தியூர் நரியப்பன்` — scans 50–54 / pp.48–52 — **PASS / CLOSED — 5/5 verified**
5. `நரியூர் நந்தியப்பன்` — scans **55–58 / pp.53–56** — **PASS / CLOSED — 4/4 verified**
6. `முடியாத தொடர்கதை` — scans **59–93 / pp.57–91** — **NEXT**

Boundary evidence: scan 58 terminal star; scan 59 `முடியாத தொடர்கதை` opening; scan 93 story ending; scan 94 advertisement.

### Story 5 — durable closure

Workspace: `stories/nariyur-nandiyappan/`

- activation duplicate/canonical search: **PASS — new canonical** at live main `7b0f4e37bcf16737032d961162acc058a67f91b8`;
- first-pass transcription: **4/4 COMPLETE**;
- Historical Tamil Glyph Gate: **PASS 4/4 / 0 corrections / 0 unresolved**;
- final source/visual closure: **PASS 4/4**;
- final ordinary source corrections: **3**;
- page status: **4/4 `verified`**;
- unresolved source/glyph items: **0**;
- assembled Tamil: **FINAL / synchronized**;
- final audit: `stories/nariyur-nandiyappan/FINAL_SOURCE_VISUAL_AUDIT_2026-09-08.md`;
- English: **not started**.

Do not reopen Story 5 without genuinely stronger source evidence or explicit maintenance request.

## Exact next activity — Story 6 activation + first pass only

Story 6: **`முடியாத தொடர்கதை`**, scans **59–93 / printed 57–91**.

1. fetch live `main`;
2. read permanent guides, this handover, `NEXT_CHAT_PROMPT.md`, collection README/source metadata/inventory/scan-map/duplicate audit, and Story-5 closure only as immediate workflow precedent;
3. resolve the controlling PDF;
4. freshly search exact heading `முடியாத தொடர்கதை`, distinguishing the legitimate collection-title match from a canonical story match;
5. search a distinctive opening fragment such as `சிறைச்சாலை—இரவு நேரம்` or `சங்கு, சந்தனம் என்ற இரண்டு கைதிகள்`;
6. verify scan 59 opening directly;
7. verify scan 93 story ending / terminal star and scan 94 advertisement as forward-boundary witness;
8. if no existing canonical story match exists, create the Story-6 canonical workspace;
9. create exactly **35 page records**, scans **59–93 / printed 57–91**;
10. transcribe all 35 pages source-faithfully and keep every record **`needs-review`**;
11. synchronize first-pass assembly, metadata, page map and review queue;
12. record Story-6 Historical Tamil Glyph Gate as **NEXT**;
13. **hard stop: do not run the glyph gate in the same activity.**

Do not start `நடுத்தெரு நாராயணி`; its `வெள்ளிக்கிழமை` gate remains unsatisfied.
