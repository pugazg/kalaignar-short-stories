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
5. `நரியூர் நந்தியப்பன்` — scans **55–58 / pp.53–56** — **GLYPH GATE PASS 4/4; FINAL SOURCE/VISUAL CLOSURE NEXT**
6. `முடியாத தொடர்கதை` — scans **59–93 / pp.57–91** — waiting

Boundary evidence: scan 58 terminal star; scan 59 `முடியாத தொடர்கதை` opening.

### Story 5 — current durable checkpoint

Workspace: `stories/nariyur-nandiyappan/`

- activation duplicate/canonical search: **PASS — new canonical** at live main `7b0f4e37bcf16737032d961162acc058a67f91b8`;
- scan 55 opening display: `நரியூர் நந்தியப்பன்`;
- scan 58 terminal star;
- scan 59 distinct Story-6 opening `முடியாத தொடர்கதை`, excluded;
- first-pass transcription: **4/4 COMPLETE**;
- dedicated native/high-resolution Historical Tamil Glyph Gate: **PASS 4/4**;
- historical-glyph corrections required: **0**;
- unresolved historical-glyph candidates: **0**;
- gate record: `stories/nariyur-nandiyappan/HISTORICAL_GLYPH_GATE.md`;
- page status: **4/4 `needs-review`**;
- assembled Tamil: **synchronized / post-glyph gate**;
- final source/visual closure: **NOT STARTED / NEXT**;
- English: **not started**.

Source-odd forms deliberately retained at the glyph gate include `காணத்தவங்கிடப்பர்`, `மறைவ துண்டோ?`, `தெய்வானு கூலம்`, `சிறப்புக் களையும்`, `என்பாடு`, `தங்கள் முடங்கள்`, `கெளரவத்திற்கும்`, `பந்து மித்திரர்களுடன்`, `ஷேத்திரங்களை`, and `மட்டுந்தானு?`.

## Exact next activity — Story 5 final source/visual closure

1. fetch live `main` and preserve newer durable work;
2. read permanent guides, this handover, `NEXT_CHAT_PROMPT.md`, Story-5 README/metadata/page-map/glyph-gate/review queue, all four page records and assembled Tamil;
3. resolve the controlling PDF;
4. directly reread scans **55–58** at native/high resolution for full lexical, punctuation, spacing and source-odd fidelity;
5. keep the Historical Tamil Glyph Gate closed; ordinary final-pass corrections must remain a separate layer;
6. verify cross-page continuations `ஒரு குடி / மகனாய்`, `பழிப் / பதாயிருக்கும்`, and `கருதா / மல்`;
7. recheck scan 58 terminal star and scan 59 next-story exclusion;
8. only if zero ordinary source-text items remain unresolved, promote 4/4 pages to `verified`, create `FINAL_SOURCE_VISUAL_AUDIT_2026-09-08.md`, and close Story 5;
9. **hard stop: do not start Story 6 in the same activity.**

Do not start `நடுத்தெரு நாராயணி`; its `வெள்ளிக்கிழமை` gate remains unsatisfied.
