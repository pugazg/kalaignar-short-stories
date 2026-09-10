# NEXT CHAT PROMPT — 1977 anthology re-audit / `நளாயினி` dual-gate repair

Continue in `pugazg/kalaignar-short-stories`, branch `main`. **LIVE MAIN IS AUTHORITATIVE.**

## Controlling source

Use the attached exact 1977 source:

`TVA_BOK_0064142_கலைஞர்_கருணாநிதியின்_சிறுகதைகள்.pdf`

- first edition: **1977**
- physical scans: **260**
- bytes: **268,486,609**
- SHA-256: `853032661482eaccb26c083a38d7aa75c081362d33c963c63e37d088bf20acb3`
- exact match to the repository's registered source identity
- image-only controlling source
- do not commit the PDF

## Critical user directive

The user does **not** want retranscription of already-existing stories.

For this entire 37-story re-audit:

- existing repository Tamil is the comparison baseline;
- compare it directly against the controlling 1977 scans;
- correct only source-proven mismatches;
- do not create duplicate transcriptions;
- do not normalize source language;
- no global replacements.

## Why this re-audit exists

A definite canonical transcription error was confirmed in `நளாயினி`, scan **17 / printed page 8**:

- repository: `தாசிநாதீனத்தொழு!`
- 1977 source: `காசிநாதனைத்தொழு!`

The earlier 37/37 PASS state is therefore legacy only. All 37 stories are reopened under:

`collections/1977-kalaignar-karunanidhiyin-sirukathaigal/RE_AUDIT_2026.md`.

Current state: **0 / 37 dual-gate complete**.

## Mandatory startup

Read completely before changing source-dependent files:

1. `SHORT_STORY_PROCESSING_GUIDE.md`
2. `HISTORICAL_TAMIL_GLYPH_TRANSCRIPTION_GUIDE.md`
3. root `HANDOVER.md`
4. this prompt
5. `collections/1977-kalaignar-karunanidhiyin-sirukathaigal/README.md`
6. `collections/1977-kalaignar-karunanidhiyin-sirukathaigal/RE_AUDIT_2026.md`
7. `collections/1977-kalaignar-karunanidhiyin-sirukathaigal/OLD_TAMIL_GLYPH_REAUDIT_GATE.md`
8. collection `indexes/story-inventory.md`
9. collection `indexes/scan-map.md`
10. `stories/nalayini/README.md`
11. `stories/nalayini/sections/nalayini.md`
12. all 8 canonical page records for `நளாயினி`
13. `stories/nalayini/POSSIBLE_ERRORS_FOR_REVIEW.md` and audit / historical-glyph records present in that workspace
14. `stories/nalayini/witnesses/1976-nalayini/VARIANT_COMPARISON.md`

## Active story

`நளாயினி`

- canonical workspace: `stories/nalayini/`
- 1977 source scans: **16–23**
- printed pages: **7–14**
- existing canonical records: **8/8**
- legacy status: verified / audit PASS — **REOPENED**

## Gate A — source-fidelity comparison

Compare **all 8 existing canonical page records and assembled Tamil** directly against scans 16–23.

Check every source span for:

- wrong / omitted / duplicated words;
- wrong word forms;
- punctuation / meaningful spacing;
- paragraphing;
- page-boundary continuations;
- headings / separators / ornaments / note layer;
- known possible-error readings.

Do not retranscribe the story from scratch. Repair only proven mismatches.

High-value candidates that must be settled against the 1977 source include:

- `தாசிநாதீனத்தொழு!` → already proven wrong; source `காசிநாதனைத்தொழு!`;
- `வலிக்குந்த உடம்பை` vs 1976 `வலி மிகுந்த உடம்பை`;
- `அவள்` vs 1976 `அவன்`;
- `கண்ணாடை` vs 1976 `கண்ஜாடை`;
- `அண்டெடுத்து` vs 1976 `அணைத்தெடுத்து`.

Do not assume the 1976 reading is correct; use the attached 1977 source to decide canonical text.

## Gate B — independent Old Tamil Glyph verification

This is a **separate gate** and cannot be inferred from Gate A.

Independently reopen scans **16–23** at high/native resolution and explicitly check:

`ணா / ணை / ணொ / ணோ / லை / ளை / றா / றொ / றோ / னா / னை / னொ / னோ`

Also inspect other suspicious old ligatures / faint vowel marks.

- no global replacement;
- character identity only, not spelling modernization;
- record corrections individually;
- unresolved glyph count must be **0** for PASS.

Follow collection `OLD_TAMIL_GLYPH_REAUDIT_GATE.md`.

## Closure in this activity

If all 8 pages can be settled:

1. apply all source-proven corrections to canonical page records;
2. synchronize `sections/nalayini.md`;
3. update story audit / possible-error / historical-glyph records;
4. update existing English only where a corrected Tamil reading materially affects it;
5. reclassify the 1976 comparison: distinguish true edition variants from canonical transcription defects;
6. update `RE_AUDIT_2026.md` with Gate A PASS + Gate B PASS and correction counts;
7. update collection README / root HANDOVER / NEXT prompt;
8. commit and re-fetch live `main`;
9. stop/report.

Do **not** begin `புகழேந்தி` in the same activity.

After `நளாயினி` closes, next story is `புகழேந்தி` scans **10–15**, then Story 3 onward in anthology order.

## Parallel 1976 work

The 1976 duplicate-story comparison is **paused** until this canonical 1977 `நளாயினி` re-audit closes. Do not resume 1976 scans 8–12 first.
