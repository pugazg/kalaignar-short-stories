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
- for the 1982 anthology, English translation proceeds in printed story order from verified canonical Tamil;
- complete translation + translation review + durable controls for one story before starting the next.

## Cross-project hold

`நடுத்தெரு நாராயணி` remains **BLOCKED** while `வெள்ளிக்கிழமை` is incomplete in `pugazg/kalaignar-novels`.

## 1982 `முடியாத தொடர்கதை`

Source: `TVA_BOK_0065572_முடியாத_தொடர்கதை.pdf` — **95 scans**, **194,350,272 bytes**, SHA-256 `d69034c5374c6c1604ddeb6d8e034c4410ae0d58201f2dd1608edd0e6d8cfd41`, first edition September 1982, image-only; do not commit PDF.

### Tamil/source state

**COMPLETE / CLOSED — 6 of 6 stories.**

1. `பெற்ற பிள்ளையை விற்ற தாய்` — 22/22 verified
2. `காசா லேசா` — 12/12 verified
3. `சீமான் வீட்டு சீக்காளி` — 9/9 verified
4. `நந்தியூர் நரியப்பன்` — 5/5 verified
5. `நரியூர் நந்தியப்பன்` — 4/4 verified
6. `முடியாத தொடர்கதை` — 35/35 verified; Historical Tamil Glyph Gate PASS 11 corrections / 0 unresolved; final source/visual F1–F7 PASS / 0 unresolved

Do not reopen a closed Tamil/source story absent genuinely stronger source evidence or an explicit maintenance request.

### English translation state

**ACTIVE — 5 / 6 stories PASS / COMPLETE.**

Tracker: `collections/1982-mudiyatha-thodarkathai/ENGLISH_TRANSLATION_PROGRESS.md`.

Story 1 `பெற்ற பிள்ளையை விற்ற தாய்`:

- English title: **The Mother Who Sold the Child She Bore**;
- canonical English: `stories/petra-pillaiyai-vitra-thaai/translations/en/petra-pillaiyai-vitra-thaai.md`;
- page anchors: **22/22 — scans 7–28 / printed 5–26**;
- result: **PASS / COMPLETE / 0 unresolved translation blockers**.

Story 2 `காசா லேசா`:

- English title: **Is Cash Easy?**;
- canonical English: `stories/kaasa-lesa/translations/en/kaasa-lesa.md`;
- page anchors: **12/12 — scans 29–40 / printed 27–38**;
- physical content-boundary alignment: **PASS**;
- result: **PASS / COMPLETE / 0 unresolved translation blockers**;
- Tamil/source issues reopened during translation: **0**.

Story 3 `சீமான் வீட்டு சீக்காளி`:

- English title: **The Invalid in the Rich Man's House**;
- canonical English: `stories/seemaan-veettu-seekkaali/translations/en/seemaan-veettu-seekkaali.md`;
- page anchors: **9/9 — scans 41–49 / printed 39–47**;
- physical content-boundary alignment: **PASS**;
- result: **PASS / COMPLETE / 0 unresolved translation blockers**;
- Tamil/source issues reopened during translation: **0**.

Story 4 `நந்தியூர் நரியப்பன்`:

- English title: **Nariyappan of Nandiyur**;
- canonical English: `stories/nandiyur-nariyappan/translations/en/nandiyur-nariyappan.md`;
- page anchors: **5/5 — scans 50–54 / printed 48–52**;
- physical content-boundary alignment: **PASS**;
- result: **PASS / COMPLETE / 0 unresolved translation blockers**;
- Tamil/source issues reopened during translation: **0**.

Story 5 `நரியூர் நந்தியப்பன்`:

- English title: **Nandiyappan of Nariyur**;
- canonical English: `stories/nariyur-nandiyappan/translations/en/nariyur-nandiyappan.md`;
- translation review: `stories/nariyur-nandiyappan/TRANSLATION_REVIEW.md`;
- page anchors: **4/4 — scans 55–58 / printed 53–56**;
- physical content-boundary alignment: **PASS**, including `ஒரு குடி / மகனாய்`, `பழிப் / பதாயிருக்கும்`, and `கருதா / மல்`;
- `ஒப்பக்காரர்`, paired Story-4/5 reversal, Madhavi/Kannagi analogy, *Parasakthi* passage, `தங்கள் முடங்கள்`, and other source-odd forms documented in the review;
- result: **PASS / COMPLETE / 0 unresolved translation blockers**;
- Tamil/source issues reopened during translation: **0**.

## Exact next activity — Story 6 English only

Translate and review **`முடியாத தொடர்கதை`** from its verified canonical Tamil workspace `stories/mudiyatha-thodarkathai/`.

- physical range: **scans 59–93 / printed pages 57–91**;
- Tamil/source: **PASS / CLOSED — 35/35 verified**;
- Historical Tamil Glyph Gate: **PASS — 11 corrections / 0 unresolved**;
- final source/visual closure: **F1–F7 PASS / 0 unresolved**;
- scan 93 terminal star; scan 94 advertisement excluded;
- preserve all **35** scan / printed-page anchors in source-backed content alignment;
- create `stories/mudiyatha-thodarkathai/translations/en/mudiyatha-thodarkathai.md`;
- create/update Story-6 translation review and README;
- update the 1982 English tracker, collection README, this handover and `NEXT_CHAT_PROMPT.md`;
- **commit Story 6 English before declaring the anthology English phase complete**.

Do not start `நடுத்தெரு நாராயணி` while its external `வெள்ளிக்கிழமை` gate remains unsatisfied.
