# HANDOVER — Kalaignar Short Stories Archive

## Repository

- repository: `pugazg/kalaignar-short-stories`
- branch: `main`
- workflows: `SHORT_STORY_PROCESSING_GUIDE.md`, `COLLECTION_SOURCE_GUIDE.md`, `HISTORICAL_TAMIL_GLYPH_TRANSCRIPTION_GUIDE.md`

## LIVE MAIN IS AUTHORITATIVE

Always fetch live `main` first and preserve newer durable state.

## Permanent source rules

- controlling scan first; no silent normalization;
- prove canonical identity before creating a new story workspace;
- preserve shared physical page boundaries;
- additional witnesses never overwrite controlling canonical editions;
- decode historical Tamil type by character identity, never by modern visual resemblance alone;
- never global-replace historical-looking forms;
- source PDFs / inspection crops are not committed.

## Mandatory two-pass historical-glyph rule

Every historical-Tamil story page requires:

1. Pass 1 direct source-faithful transcription.
2. Pass 2: reopen the same physical page at native/high resolution and independently recheck  
   `ணா / ணை / ணொ / ணோ / லை / ளை / றா / றொ / றோ / னா / னை / னொ / னோ`
   plus suspicious old-type clusters.

Final `verified` requires both passes.

## Closed phases — preserve

- 1977 — Tamil/visual/English **37/37 PASS**
- 2008 — Tamil/visual/English **40/40 PASS**
- 2004 — Tamil/visual/English **34/34 PASS**
- 2009 new-story onboarding — **5/5 CLOSED**
- 2009 existing-canonical witness comparison — **11/11 CLOSED**
- supplemental English — **6/6 PASS / CLOSED**

Do not reopen these because of an older prompt.

## ACTIVE — 1987 `கலைஞர் சொன்ன குட்டிக் கதைகள்`

Workspace: `collections/1987-kalaignar-sonna-kuttik-kathaigal/`

Controlling source: `TVA_BOK_0065566_கலைஞர்_சொன்ன_குட்டிக்_கதைகள்_1987.pdf`

- 50 scans
- 107,757,858 bytes
- SHA-256 `29c986812f95c43105eec4b38fa9e02c3c4f66cf3c4e8a686b81dd28c1164f0f`
- Second Edition, 1987
- headings: **25 / 25 PASS**
- canonical identity: **25 / 25 COMPLETE**
- distinct: **23**
- witness-only: **2**

### Authoritative title corrections — do not revert

- Story 2 `அராபியக் கதை`
- Story 4 `நாராயணா ! நாராயணா !`
- Story 6 `மூளி மூக்குக்காரன்`
- Story 10 `இரு நிழல்கள்` — direct banner recheck; earlier `இரு நிகழ்வுகள்` was wrong

## Lexical/Glyph L1 — COMPLETE

Ledger:
`collections/1987-kalaignar-sonna-kuttik-kathaigal/LEXICAL_GLYPH_BATCH_L1_SCANS_0005_0019.md`

- scans **5–19 = 15 / 15 COMPLETE**
- unresolved: **0**

## Retrospective historical-glyph correction — CLOSED through scan 34

Durable record:
`collections/1987-kalaignar-sonna-kuttik-kathaigal/RETROSPECTIVE_GLYPH_REAUDIT_L1_L2_2026-09-07.md`

Important corrected identities include:

`சொன்னாராம்`, `பேசினார்கள்`, `நிலைமையை`, `பேசினான்`, `பின்னால்`, `வினவினான்`, `அவனா!`, `இட்டானாம்`, and Story-18 `பின்னாலிருந்து`.

`அந்நிலை` was rechecked and remains unchanged.

## Lexical/Glyph L2 — COMPLETE

Ledger:
`collections/1987-kalaignar-sonna-kuttik-kathaigal/LEXICAL_GLYPH_BATCH_L2_SCANS_0020_0034.md`

- scans **20–34 = 15 / 15 COMPLETE**
- Story 9: closed
- Story 10 `இரு நிழல்கள்`: closed
- Story 11: 1987 witness closed; 2004 canonical unchanged
- Stories 12–17: closed
- lower scan 34 opening of Story 18: verified
- unresolved L2: **0**

## Lexical/Glyph L3 — COMPLETE

Ledger:
`collections/1987-kalaignar-sonna-kuttik-kathaigal/LEXICAL_GLYPH_BATCH_L3_SCANS_0035_0049.md`

- scans **35–49 = 15 / 15 COMPLETE**
- Stories 18–25: **Tamil lexical/glyph PASS / closed**
- unresolved L3: **0**

Important L3 source-sensitive readings include `மூன்றாண்டுகாலம்`, `பின்னாலே`, `மன்னா`, `நோஞ்சானை`, `அந்தநாள் வந்தில அருங்கவிப் புலவோய்`, `பெற்றுஉன்`, `அன்பில்லையே`, `நன்றாக`, and historical `பூனை` / `பாலை` forms.

## 1987 lexical/glyph state after L3

- story-bearing scans **5–49 = 45 / 45 Pass 1 + independent Pass 2 COMPLETE**
- unresolved lexical/glyph locations across L1–L3: **0**
- scan 50: verified blank/damaged terminal non-story leaf
- English: **not authorized**

## Exact next activity — 1987 final Tamil/source consistency & release audit

Do **not** routinely retranscribe closed pages.

Perform a collection-wide reconciliation of:

1. all story-local `pages/*.md` records against assembled Tamil `sections/*.md`;
2. story-local page maps against authoritative shared physical boundaries;
3. Tamil source audits and `HISTORICAL_GLYPH_AUDIT.md` states;
4. title corrections and historical-glyph-sensitive headings;
5. Story 2 and Story 11 witness routing so their controlling canonical editions remain unchanged;
6. collection README, story inventory and scan map counts/statuses;
7. unresolved/`needs-review`/`partial`/`pending` markers that may be stale after L3 closure;
8. scan 50 terminal-leaf state;
9. absence of unauthorized 1987 English work.

Reopen source pixels only where this reconciliation exposes a mismatch, stale status, unresolved marker or stronger source evidence. If all gates pass with zero unresolved Tamil/source issues, create a durable final-audit record and mark the **1987 Tamil/source phase CLOSED**.

Do not begin English without explicit authorization. Do not begin `நடுத்தெரு நாராயணி` while waiting for `வெள்ளிக்கிழமை` completion in the novels workflow.
