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
5. `நரியூர் நந்தியப்பன்` — scans 55–58 / pp.53–56 — **PASS / CLOSED — 4/4 verified**
6. `முடியாத தொடர்கதை` — scans **59–93 / pp.57–91** — **FIRST PASS 35/35 COMPLETE; CORRECTED GLYPH GATE PASS 35/35; FINAL SOURCE/VISUAL CLOSURE IN 5-SCAN BATCHES**

Boundary evidence: scan 58 terminal star; scan 59 Story-6 opening; scan 93 terminal star; scan 94 advertisement.

### Story 6 — current durable checkpoint

Workspace: `stories/mudiyatha-thodarkathai/`

- activation duplicate/canonical search: **PASS — new canonical story entity**;
- scan 59 opening: `முடியாத தொடர்கதை`, scene `சிறைச்சாலை—இரவு நேரம்`;
- scan 93 ending / terminal star: confirmed;
- scan 94 advertisement: excluded forward witness;
- first-pass transcription: **35/35 COMPLETE**;
- page status: **35/35 `needs-review`**;
- Historical Tamil Glyph Gate: **PASS after corrective high-resolution re-audit — 35/35; 10 total corrections / 0 unresolved**;
- corrective source readings committed on live main include scans 88–92: `பேசினாள்`, `சொல்லியனுப்பினான்`, `துட்ட லக்கணமாம்`, `மலைப்பாம்பு`, `விலக்கினான்`, `கூறினான்`, `பில்கனாவிலே`;
- `ஸ்பரிசிக்கப்பட்டு` is retained as printed Tamil; English sense later: **touched / was touched**;
- assembled Tamil part covering scans 88–92 still needs synchronization when the corresponding final-closure batch is processed;
- final source/visual closure: **IN PROGRESS — 0/7 five-scan batches complete**;
- English: **not started**.

Final-closure batch ledger: `stories/mudiyatha-thodarkathai/FINAL_SOURCE_VISUAL_PROGRESS.md`.

## Permanent batch rule from this checkpoint

Process and commit **exactly 5 physical scans per final-closure iteration**. Do not combine batches.

Batch plan:

1. F1 scans **59–63 / printed 57–61**
2. F2 scans **64–68 / printed 62–66**
3. F3 scans **69–73 / printed 67–71**
4. F4 scans **74–78 / printed 72–76**
5. F5 scans **79–83 / printed 77–81**
6. F6 scans **84–88 / printed 82–86**
7. F7 scans **89–93 / printed 87–91**

For each batch: direct native/high-resolution reread → ordinary wording/punctuation/spacing/page-boundary corrections → synchronize affected derivative text → update progress ledger + handover + next-chat prompt → **commit before starting the next batch**.

Keep page records `needs-review` during partial batches. After all seven batches PASS and zero ordinary source issues remain, perform the story-wide final closure and promote all 35 pages to `verified` together.

## Exact next activity — F1 only

Process **scans 59–63 / printed 57–61 only**.

- preserve the corrected historical-glyph gate;
- verify every word, punctuation mark, spacing choice and page boundary directly from native scans;
- verify the 59→60 physical join;
- do not inspect/process scan 64 as part of the batch except if a boundary witness becomes strictly necessary;
- record each source-supported correction individually;
- update `FINAL_SOURCE_VISUAL_PROGRESS.md` to F1 PASS if zero unresolved items remain in scans 59–63;
- keep pages 59–63 `needs-review` until story-wide closure;
- commit the F1 batch before any F2 work.

Do not start `நடுத்தெரு நாராயணி`; its `வெள்ளிக்கிழமை` gate remains unsatisfied.
