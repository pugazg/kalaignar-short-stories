# NEXT CHAT PROMPT — 1977 anthology re-audit / `புகழேந்தி` dual-gate

Continue in `pugazg/kalaignar-short-stories`, branch `main`. **LIVE MAIN IS AUTHORITATIVE.**

## Controlling source

Use the attached exact 1977 source:

`TVA_BOK_0064142_கலைஞர்_கருணாநிதியின்_சிறுகதைகள்.pdf`

- edition: **முதல் பதிப்பு: 1977**
- physical scans: **260**
- bytes: **268,486,609**
- SHA-256: `853032661482eaccb26c083a38d7aa75c081362d33c963c63e37d088bf20acb3`
- exact match to the repository's registered source identity
- image-only controlling source
- do not commit the PDF

## Critical user directive

This is **comparison repair, not retranscription**.

For all 37 stories:

- existing repository Tamil is the comparison baseline;
- compare it directly against the controlling 1977 scans;
- correct only source-proven mismatches;
- do not create duplicate/full retranscriptions;
- preserve source spelling, punctuation, meaningful spacing, paragraphing, page boundaries and source marks;
- do not normalize old/source-odd Tamil from lexical expectation;
- no global replacements.

## Current durable re-audit state

Tracker: `collections/1977-kalaignar-karunanidhiyin-sirukathaigal/RE_AUDIT_2026.md`.

Current state: **OPEN — 1 / 37 dual-gate complete**.

`நளாயினி` scans **16–23 / printed 7–14** is **CURRENT PASS / CLOSED** under the 2026 standard:

- Gate A: **8/8 PASS**;
- Gate B: **8/8 PASS**;
- canonical repairs: **15**;
- unresolved source readings: **0**;
- unresolved historical-glyph readings: **0**;
- Tamil assembly / audits / affected English synchronized;
- 1976 P1 witness candidates adjudicated: **8 canonical defects / 5 true edition variants / 0 unresolved**.

Do not reopen `நளாயினி` from stale prompts unless new direct source evidence appears.

## Mandatory startup

Read completely before source-dependent changes:

1. `SHORT_STORY_PROCESSING_GUIDE.md`
2. `HISTORICAL_TAMIL_GLYPH_TRANSCRIPTION_GUIDE.md`
3. root `HANDOVER.md`
4. this prompt
5. `collections/1977-kalaignar-karunanidhiyin-sirukathaigal/README.md`
6. `collections/1977-kalaignar-karunanidhiyin-sirukathaigal/RE_AUDIT_2026.md`
7. `collections/1977-kalaignar-karunanidhiyin-sirukathaigal/OLD_TAMIL_GLYPH_REAUDIT_GATE.md`
8. collection `indexes/story-inventory.md`
9. collection `indexes/scan-map.md`
10. all controls / page records / assembly / audit / possible-error files under `stories/pugazhendhi/`

## Exact next activity — `புகழேந்தி`

Workspace: `stories/pugazhendhi/`.

Source range:

- physical scans: **10–15**
- printed pages: **1–6**
- existing canonical pages: **6/6** under the legacy workflow

Complete both gates in **one story-bounded activity**.

### Gate A — source-fidelity comparison

Compare all six existing canonical page records and the assembled Tamil directly against source scans **10–15**.

Check:

- wrong / omitted / duplicated words;
- wrong character or word forms;
- punctuation and meaningful spacing;
- paragraphing;
- physical page-boundary continuations;
- heading / separators / ornaments / note layers;
- all existing possible-error / suspicious-reading candidates.

Do not retranscribe. Repair only source-proven mismatches.

### Gate B — independent Old Tamil Glyph verification

This is a **separate independent gate** and cannot be inferred from Gate A.

Independently reopen all scans **10–15** at high/native resolution and explicitly consider:

`ணா / ணை / ணொ / ணோ / லை / ளை / றா / றொ / றோ / னா / னை / னொ / னோ`

Also remain alert for other old ligatures, faint vowel marks, broken/touching type and `ர/ற`, `ன/ண`, `ல/ள` confusions.

- no global replacement;
- character identity only, not modernization;
- record every correction individually with scan / printed-page provenance;
- unresolved historical-glyph count must be **0** for PASS.

## Closure requirements

If all six pages settle:

1. apply all source-proven corrections to canonical page records;
2. synchronize assembled Tamil;
3. update story audit / possible-error / historical-glyph records;
4. update existing English only where a corrected Tamil reading materially changes meaning;
5. record Gate A and Gate B results and correction counts durably;
6. update collection tracker from **1/37** to **2/37** only if both gates PASS and unresolved count is 0;
7. update collection/root controls;
8. commit and re-fetch live `main`;
9. stop/report.

Do **not** begin Story 3 `சபலம்` in the same activity.

## Parallel 1976 work

`நளாயினி` 1976 P2 scans **8–12** comparison is now technically ready because the controlling 1977 story is repaired, but it is **DEFERRED** while the 37-story 1977 re-audit remains the active priority. Do not resume it before `புகழேந்தி` in this activity.
