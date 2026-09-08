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
- user directive for this 1987 English phase: **10 stories per iteration**, with the final four-story remainder handled together.

## Closed phases — preserve

- 1977 — Tamil/visual/English **37/37 PASS**
- 2008 — Tamil/visual/English **40/40 PASS**
- 2004 — Tamil/visual/English **34/34 PASS**
- 2009 new-story onboarding — **5/5 CLOSED**
- 2009 existing-canonical witness comparison — **11/11 CLOSED**
- supplemental English — **6/6 PASS / CLOSED**
- 1987 `கலைஞர் சொன்ன குட்டிக் கதைகள்` Tamil/source — **CLOSED**

## ACTIVE — 1987 English final QA / release audit

Collection: `collections/1987-kalaignar-sonna-kuttik-kathaigal/`

Source: `TVA_BOK_0065566_கலைஞர்_சொன்ன_குட்டிக்_கதைகள்_1987.pdf`

- 50 scans; 107,757,858 bytes
- SHA-256 `29c986812f95c43105eec4b38fa9e02c3c4f66cf3c4e8a686b81dd28c1164f0f`
- Tamil/source release: **PASS / CLOSED**
- unresolved Tamil/source/glyph: **0**

## English progress

- Story 1: **PASS**
- Batch 01 Stories 2–11: **10/10 PASS**
- Batch 02 Stories 12–21: **10/10 PASS**
- Batch 03 final remainder Stories 22–25: **4/4 PASS**
- English total: **25 / 25 PASS**
- pending: **0 / 25**
- needs review: **0**
- story-level translation: **COMPLETE**
- collection English release closure: **PENDING FINAL QA**

Final-remainder record:
`collections/1987-kalaignar-sonna-kuttik-kathaigal/ENGLISH_BATCH_03_STORIES_0022_0025.md`

For every completed English story, physical source-page marker order and content-boundary alignment were checked separately against verified `pages/*.md`, and Tamil was not changed merely for English fluency.

Witness-only routing remains fixed:
- Story 2 `அராபியக் கதை` — 1987 witness-local English; controlling 2008 English unchanged.
- Story 11 `குருவி ராமேஸ்வரம்` — 1987 witness-local English; controlling 2004 English unchanged.

Story 10 remains authoritative as `இரு நிழல்கள்` / **Two Shadows**; its legacy directory slug is retained only for path continuity.

## Exact next activity — collection-wide English final QA / release audit

Run the final English gate across all 25 source stories. At minimum:

1. reconcile the 25 source-story inventory against all English translation files and story READMEs;
2. confirm every story-local `TRANSLATION_REVIEW.md` is PASS;
3. confirm source-page marker presence/order separately from physical content-boundary alignment and substantive final source spans;
4. recheck witness-local routing for Stories 2 and 11 and the authoritative Story 10 title **Two Shadows**;
5. confirm unresolved English review items remain **0** and no Tamil/source text was changed merely for English fluency;
6. reconcile Batch 01, Batch 02, Batch 03, the English tracker, collection README, root `HANDOVER.md`, and `NEXT_CHAT_PROMPT.md`.

If the gate PASSes, create the final English release-audit record and then mark the 1987 English phase **PASS / CLOSED** across durable controls.

Do not begin `நடுத்தெரு நாராயணி` while waiting for `வெள்ளிக்கிழமை` completion in the novels workflow.
