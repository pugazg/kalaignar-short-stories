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
- for the 1982 anthology, English translation now proceeds in printed story order from the already-verified canonical Tamil;
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

**ACTIVE — 1 / 6 stories PASS / COMPLETE.**

Tracker: `collections/1982-mudiyatha-thodarkathai/ENGLISH_TRANSLATION_PROGRESS.md`.

Story 1 `பெற்ற பிள்ளையை விற்ற தாய்`:

- English title: **The Mother Who Sold the Child She Bore**;
- canonical English: `stories/petra-pillaiyai-vitra-thaai/translations/en/petra-pillaiyai-vitra-thaai.md`;
- translation review: `stories/petra-pillaiyai-vitra-thaai/TRANSLATION_REVIEW.md`;
- page anchors: **22/22 — scans 7–28 / printed 5–26**;
- result: **PASS / COMPLETE / 0 unresolved translation blockers**;
- Tamil/source issues reopened during translation: **0**.

## Exact next activity — Story 2 English only

Translate and review **`காசா லேசா`** from its verified canonical Tamil workspace `stories/kaasa-lesa/`.

- physical range: **scans 29–40 / printed pages 27–38**;
- Tamil/source: **PASS / CLOSED — 12/12 verified**;
- source-title variants (`காசா லேசா`, running-header `காசா லேசா!`, scan-40 `காசாலேசா!`) remain source-layer evidence and must not be silently rewritten in Tamil;
- preserve all 12 scan / printed-page anchors in English;
- create `stories/kaasa-lesa/translations/en/kaasa-lesa.md`;
- create/update Story-2 translation review and README;
- update the 1982 English tracker, collection README, this handover and `NEXT_CHAT_PROMPT.md`;
- **commit Story 2 English before beginning Story 3**.

Do not start Story 3 in the same activity. Do not start `நடுத்தெரு நாராயணி` while its external `வெள்ளிக்கிழமை` gate remains unsatisfied.
