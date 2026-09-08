# NEXT CHAT PROMPT — Kalaignar Short Stories Archive — 1987 English Final QA / Release Audit

Continue directly in `pugazg/kalaignar-short-stories`, branch `main`.

## LIVE MAIN IS AUTHORITATIVE

Fetch live `main` first and preserve newer durable state.

## Active collection

`collections/1987-kalaignar-sonna-kuttik-kathaigal/`

Controlling PDF: `TVA_BOK_0065566_கலைஞர்_சொன்ன_குட்டிக்_கதைகள்_1987.pdf`

- 50 scans
- Second Edition 1987
- SHA-256 `29c986812f95c43105eec4b38fa9e02c3c4f66cf3c4e8a686b81dd28c1164f0f`
- Tamil/source phase: **PASS / CLOSED**
- unresolved Tamil/source/glyph: **0**

## English state

User directive for production was **10 stories per iteration**; the final remainder contained four stories and is now complete.

- English PASS: **25 / 25**
- pending: **0 / 25**
- needs review: **0**
- Story 1: PASS
- Batch 01 Stories 2–11: PASS 10/10
- Batch 02 Stories 12–21: PASS 10/10
- Batch 03 Stories 22–25: PASS 4/4
- story-level translation: **COMPLETE**
- collection English release: **FINAL QA PENDING**

Final-remainder record:
`collections/1987-kalaignar-sonna-kuttik-kathaigal/ENGLISH_BATCH_03_STORIES_0022_0025.md`

## Mandatory startup

Read before final-QA writes:

1. `ENGLISH_TRANSLATION_GUIDE.md`
2. `SHORT_STORY_PROCESSING_GUIDE.md`
3. `COLLECTION_SOURCE_GUIDE.md`
4. root `HANDOVER.md`
5. this prompt
6. collection `README.md` and `ENGLISH_TRANSLATION_PROGRESS.md`
7. `ENGLISH_BATCH_01_STORIES_0002_0011.md`
8. `ENGLISH_BATCH_02_STORIES_0012_0021.md`
9. `ENGLISH_BATCH_03_STORIES_0022_0025.md`
10. the 25 story READMEs, English translation files, and `TRANSLATION_REVIEW.md` controls; inspect verified `pages/*.md` wherever a final-QA marker or boundary check needs confirmation.

## Exact next activity — collection-wide English final QA / release audit

Run the final gate across all 25 source stories. Do not start a new story collection while this gate is open.

Required checks:

- reconcile the 25 source headings against exactly 25 completed English routes;
- verify every story-local English review is **PASS** and unresolved English review items remain **0**;
- validate source-page marker presence and numeric order;
- separately validate physical content-boundary alignment and ensure the final source span/page contains substantive translated content;
- preserve witness-local routing for Story 2 `அராபியக் கதை` and Story 11 `குருவி ராமேஸ்வரம்`; do not overwrite the controlling 2008/2004 English;
- preserve Story 10 authoritative identity `இரு நிழல்கள்` and English title **Two Shadows** despite its legacy slug;
- confirm no Tamil/source text was changed merely to improve English;
- reconcile all three batch records, the English tracker, collection README, root `HANDOVER.md`, and this prompt.

If every check PASSes:

- create the final English release-audit record;
- set the 1987 English phase to **25/25 PASS / CLOSED** with pending 0 and needs review 0;
- synchronize collection README, English tracker, root `HANDOVER.md`, and `NEXT_CHAT_PROMPT.md` to the closed state;
- only then choose the next eligible archive activity.

Do not begin `நடுத்தெரு நாராயணி` while waiting for `வெள்ளிக்கிழமை` completion in the novels workflow.
