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
- user directive for this 1987 English phase: **10 stories per iteration**.

## Closed phases — preserve

- 1977 — Tamil/visual/English **37/37 PASS**
- 2008 — Tamil/visual/English **40/40 PASS**
- 2004 — Tamil/visual/English **34/34 PASS**
- 2009 new-story onboarding — **5/5 CLOSED**
- 2009 existing-canonical witness comparison — **11/11 CLOSED**
- supplemental English — **6/6 PASS / CLOSED**
- 1987 `கலைஞர் சொன்ன குட்டிக் கதைகள்` Tamil/source — **CLOSED**

## ACTIVE — 1987 English

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
- English total: **21 / 25 PASS**
- pending: **4 / 25**
- needs review: **0**

Batch 02 record:
`collections/1987-kalaignar-sonna-kuttik-kathaigal/ENGLISH_BATCH_02_STORIES_0012_0021.md`

For every completed English story, physical source-page content-boundary alignment was checked against verified `pages/*.md`, and Tamil was not changed merely for English fluency.

Witness-only routing remains fixed:
- Story 2 `அராபியக் கதை` — 1987 witness-local English; controlling 2008 English unchanged.
- Story 11 `குருவி ராமேஸ்வரம்` — 1987 witness-local English; controlling 2004 English unchanged.

## Exact next activity — final English remainder Stories 22–25

Process all remaining four in source order:

22. `காடு சென்ற குமணன்` — lower 44 / printed 43 → upper 45 / printed 44
23. `அகத்திணை அன்பு!` — lower 45 / printed 44 → upper 46 / printed 45
24. `தெனாலிராமன் பூனை` — lower 46 / printed 45 → 47 / printed 46 → upper 48 / printed 47
25. `குழந்தையும் கிளியும்` — lower 48 / printed 47 → 49 / printed 48

For each: read verified Tamil assembly, every page record, Tamil/historical audits and any review controls; translate complete verified Tamil; preserve physical page boundaries; create `TRANSLATION_REVIEW.md`; update README; do not normalize source-odd forms.

After all four PASS, update English to **25/25 COMPLETE** and make the **collection-wide English final QA / release audit** the automatic next activity.

Do not begin `நடுத்தெரு நாராயணி` while waiting for `வெள்ளிக்கிழமை` completion in the novels workflow.
