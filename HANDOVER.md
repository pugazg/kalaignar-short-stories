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
- 1987 `கலைஞர் சொன்ன குட்டிக் கதைகள்` Tamil/source phase — **CLOSED**

Do not reopen closed phases because of an older prompt.

## CLOSED — 1987 `கலைஞர் சொன்ன குட்டிக் கதைகள்`

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
- story-bearing scans **5–49 = 45 / 45 Pass 1 + independent Pass 2 COMPLETE**
- scan 50: verified blank/damaged terminal non-story leaf
- unresolved 1987 Tamil/source or historical-glyph locations: **0**
- English from the 1987 source: **not authorized / not started**

Final release record:
`collections/1987-kalaignar-sonna-kuttik-kathaigal/FINAL_TAMIL_SOURCE_RELEASE_AUDIT_2026-09-07.md`

### Authoritative title corrections — do not revert

- Story 2 `அராபியக் கதை`
- Story 4 `நாராயணா ! நாராயணா !`
- Story 6 `மூளி மூக்குக்காரன்`
- Story 10 `இரு நிழல்கள்` — direct banner recheck; earlier `இரு நிகழ்வுகள்` was wrong

Story 10 retains repository directory `stories/iru-nigazhvugal/` only for path continuity. The source-facing title is `இரு நிழல்கள்`.

### Witness-only routing — preserve

- Story 2 `அராபியக் கதை` is a completed 1987 witness for canonical `ஜாடி குட்டி போடுமா?`; the controlling 2008 Tamil/English remain unchanged.
- Story 11 `குருவி ராமேஸ்வரம்` is a completed 1987 witness for the existing 2004 canonical story; the controlling 2004 Tamil/English remain unchanged.

The final audit corrected stale summary text in those canonical README controls. Do not regress them to `NEEDS REVIEW` or the old Story-2 title misread.

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
- Story 11 1987 witness closed; 2004 canonical unchanged
- Stories 12–17 closed
- lower scan 34 opening of Story 18 verified
- unresolved L2: **0**

The L2 ledger's Story-18 partial/open wording is a historical state-at-L2-closure record and must not be rewritten merely because L3 later completed the story.

## Lexical/Glyph L3 — COMPLETE

Ledger:
`collections/1987-kalaignar-sonna-kuttik-kathaigal/LEXICAL_GLYPH_BATCH_L3_SCANS_0035_0049.md`

- scans **35–49 = 15 / 15 COMPLETE**
- Stories 18–25: **Tamil lexical/glyph PASS / closed**
- unresolved L3: **0**

Important L3 source-sensitive readings include `மூன்றாண்டுகாலம்`, `பின்னாலே`, `மன்னா`, `நோஞ்சானை`, `அந்தநாள் வந்தில அருங்கவிப் புலவோய்`, `பெற்றுஉன்`, `அன்பில்லையே`, `நன்றாக`, and historical `பூனை` / `பாலை` forms.

## Final 1987 Tamil/source release audit — PASS

The final consistency gate reconciled collection indexes, batch ledgers, story/witness status controls, title routing, shared-page boundaries, historical-glyph audit state and terminal scan 50.

Three stale **control-layer** statements were corrected during that gate:

1. Story-2 canonical README: old 1987 heading/status → `அராபியக் கதை`, witness PASS.
2. Story-2 1987 `VARIANT_COMPARISON.md`: old deferred/open lexical note → closed.
3. Story-11 canonical README: old 1987 witness `OPEN / NEEDS REVIEW` note → PASS.

No verified 1987 Tamil source text changed in the final release audit.

## Current activity

There is **no active 1987 Tamil-source work**. Preserve this closed phase and reopen only when genuinely new or stronger source evidence requires a targeted correction.

Do not begin English from the 1987 source without explicit authorization. Do not begin `நடுத்தெரு நாராயணி` while waiting for `வெள்ளிக்கிழமை` completion in the novels workflow.
