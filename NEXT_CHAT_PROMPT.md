# NEXT CHAT PROMPT — Kalaignar Short Stories Archive — Post-1987 Closure / Next-Source Gate

Continue directly in `pugazg/kalaignar-short-stories`, branch `main`.

## LIVE MAIN IS AUTHORITATIVE

Fetch live `main` first and preserve newer durable state.

## Closed collection — preserve

`collections/1987-kalaignar-sonna-kuttik-kathaigal/`

Controlling PDF: `TVA_BOK_0065566_கலைஞர்_சொன்ன_குட்டிக்_கதைகள்_1987.pdf`

- 50 scans
- Second Edition 1987
- SHA-256 `29c986812f95c43105eec4b38fa9e02c3c4f66cf3c4e8a686b81dd28c1164f0f`
- Tamil/source phase: **PASS / CLOSED**
- English phase: **25 / 25 PASS / CLOSED**
- pending English: **0 / 25**
- needs review: **0**
- unresolved English review items: **0**

Final English release audit:
`collections/1987-kalaignar-sonna-kuttik-kathaigal/FINAL_ENGLISH_RELEASE_AUDIT_2026-09-08.md`

The final English gate confirmed all 25 source headings against exactly 25 English routes, story-local PASS controls, marker order, physical content-boundary alignment, substantive final source spans, witness-local routing for Stories 2 and 11, authoritative Story 10 title **Two Shadows**, and no Tamil changes made merely for English fluency.

Do not reopen this 1987 collection without genuinely stronger source evidence or an explicit maintenance/audit request.

## Mandatory startup

Read before any new short-story production:

1. `SHORT_STORY_PROCESSING_GUIDE.md`
2. `COLLECTION_SOURCE_GUIDE.md`
3. `HISTORICAL_TAMIL_GLYPH_TRANSCRIPTION_GUIDE.md`
4. `ENGLISH_TRANSLATION_GUIDE.md`
5. root `HANDOVER.md`
6. this prompt
7. the 1987 final English release audit only as a closed-state reference

## Exact next activity — cross-project gate check

The planned next short-story source is `நடுத்தெரு நாராயணி`, but the user has explicitly blocked its start while `வெள்ளிக்கிழமை` remains incomplete.

Therefore:

1. fetch live `main` from `pugazg/kalaignar-novels`;
2. inspect the durable `works/vellikkizhamai/` state and its authoritative handover/progress controls;
3. if `வெள்ளிக்கிழமை` is **not COMPLETE/CLOSED**, do **not** start `நடுத்தெரு நாராயணி`; make no speculative short-story production changes and wait for an explicitly eligible maintenance/new-source task;
4. if `வெள்ளிக்கிழமை` is **COMPLETE/CLOSED**, return to `pugazg/kalaignar-short-stories` and begin `நடுத்தெரு நாராயணி` only after resolving its controlling source and running normal source intake / duplicate-identity checks.

Do not infer `வெள்ளிக்கிழமை` completion from an old copied prompt; live durable state in `pugazg/kalaignar-novels` controls.
