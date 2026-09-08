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
- completed collection phases stay frozen unless genuinely stronger source evidence appears or the user explicitly requests maintenance.

## Closed phases — preserve

- 1977 — Tamil/visual/English **37/37 PASS**
- 2008 — Tamil/visual/English **40/40 PASS**
- 2004 — Tamil/visual/English **34/34 PASS**
- 2009 new-story onboarding — **5/5 CLOSED**
- 2009 existing-canonical witness comparison — **11/11 CLOSED**
- supplemental English — **6/6 PASS / CLOSED**
- 1987 `கலைஞர் சொன்ன குட்டிக் கதைகள்` Tamil/source — **PASS / CLOSED**
- 1987 `கலைஞர் சொன்ன குட்டிக் கதைகள்` English — **25/25 PASS / CLOSED**

## 1987 release closure

Collection: `collections/1987-kalaignar-sonna-kuttik-kathaigal/`

Source: `TVA_BOK_0065566_கலைஞர்_சொன்ன_குட்டிக்_கதைகள்_1987.pdf`

- 50 scans; 107,757,858 bytes
- SHA-256 `29c986812f95c43105eec4b38fa9e02c3c4f66cf3c4e8a686b81dd28c1164f0f`
- Tamil/source release: **PASS / CLOSED**
- unresolved Tamil/source/glyph: **0**
- English release: **25 / 25 PASS / CLOSED**
- pending English: **0 / 25**
- needs review: **0**
- unresolved English review items: **0**

Final English release audit:
`collections/1987-kalaignar-sonna-kuttik-kathaigal/FINAL_ENGLISH_RELEASE_AUDIT_2026-09-08.md`

Coverage preserved:

- Story 1: **PASS**
- Batch 01 Stories 2–11: **10/10 PASS**
- Batch 02 Stories 12–21: **10/10 PASS**
- Batch 03 Stories 22–25: **4/4 PASS**

The final gate separately confirmed source-page marker presence/order, physical content-boundary alignment, substantive final source spans, story-local review PASS state, and Tamil/source immutability.

Witness-only routing remains fixed:
- Story 2 `அராபியக் கதை` — 1987 witness-local English; controlling 2008 English unchanged.
- Story 11 `குருவி ராமேஸ்வரம்` — 1987 witness-local English; controlling 2004 English unchanged.

Story 10 remains authoritative as `இரு நிழல்கள்` / **Two Shadows**; its legacy directory slug is retained only for path continuity.

## Current archive boundary

There is no open production task in the 1987 collection. Reopen it only for genuinely stronger source evidence or an explicit maintenance/audit request.

The planned next short-story source `நடுத்தெரு நாராயணி` remains blocked by the user's cross-project gate: **do not begin it while `வெள்ளிக்கிழமை` is incomplete in the novels workflow**.

## Exact next activity — cross-project gate check

Before starting another short-story collection:

1. fetch live `main` of `pugazg/kalaignar-novels`;
2. verify the durable state of `works/vellikkizhamai/`;
3. if `வெள்ளிக்கிழமை` is not COMPLETE/CLOSED, do **not** begin `நடுத்தெரு நாராயணி`; preserve this short-story repository in its closed state and wait for an explicit eligible maintenance/new-source instruction;
4. if `வெள்ளிக்கிழமை` is COMPLETE/CLOSED, return here and onboard `நடுத்தெரு நாராயணி` only under the permanent source-first guides and only after its controlling source is resolved.
