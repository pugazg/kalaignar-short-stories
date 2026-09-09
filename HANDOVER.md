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
- translation proceeds only from verified canonical Tamil;
- completed Tamil/source and English layers are not reopened without genuinely stronger evidence or explicit maintenance authorization.

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

### English translation state

**COMPLETE / CLOSED — 6 / 6 stories PASS / COMPLETE.**

Tracker: `collections/1982-mudiyatha-thodarkathai/ENGLISH_TRANSLATION_PROGRESS.md`.

1. `பெற்ற பிள்ளையை விற்ற தாய்` — **The Mother Who Sold the Child She Bore** — PASS / COMPLETE — 22/22 anchors
2. `காசா லேசா` — **Is Cash Easy?** — PASS / COMPLETE — 12/12 anchors
3. `சீமான் வீட்டு சீக்காளி` — **The Invalid in the Rich Man's House** — PASS / COMPLETE — 9/9 anchors
4. `நந்தியூர் நரியப்பன்` — **Nariyappan of Nandiyur** — PASS / COMPLETE — 5/5 anchors
5. `நரியூர் நந்தியப்பன்` — **Nandiyappan of Nariyur** — PASS / COMPLETE — 4/4 anchors
6. `முடியாத தொடர்கதை` — **The Never-Ending Story** — PASS / COMPLETE — 35/35 anchors

Story 6 details:

- canonical English: `stories/mudiyatha-thodarkathai/translations/en/mudiyatha-thodarkathai.md`;
- translation review: `stories/mudiyatha-thodarkathai/TRANSLATION_REVIEW.md`;
- physical range: scans **59–93 / printed 57–91**;
- content-boundary alignment: **PASS — 35/35**;
- scan 93 terminal star represented; scan 94 advertisement excluded;
- source-sensitive choices documented, including source scene numbering `1 → 2 → 4 → 5`, `ஆடுதன் ராஜா`, `களிவற்ற கொளியும்`, `அவலட்சணத்துக்கும் அறிவுக் குந்தானடா`, `மீனவி புதல்வன்`, Chicken-Bite/Chick-Bite Swami satire, scan-90 kinship wording, `பில்கனாவிலே`, and final mistaken-sibling reversal;
- Tamil/source issues reopened during translation: **0**;
- unresolved English translation blockers: **0**.

## Current project state / next action

The 1982 `முடியாத தொடர்கதை` anthology is **FULLY CLOSED for Tamil/source and English**. There is no pending routine activity inside this collection.

The next candidate story `நடுத்தெரு நாராயணி` must **NOT** start because its external `வெள்ளிக்கிழமை` gate remains unsatisfied. Until that gate is confirmed complete, remain on **HOLD** unless the user explicitly supplies a new source, requests maintenance/re-audit of a closed item, or redirects to another authorized archive activity.
