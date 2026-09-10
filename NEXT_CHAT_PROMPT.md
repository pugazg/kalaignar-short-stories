# NEXT CHAT PROMPT — 1977 anthology re-audit / `சங்கிலிச்சாமி` dual-gate

Continue in `pugazg/kalaignar-short-stories`, branch `main`. **LIVE MAIN IS AUTHORITATIVE.**

## Controlling source

Use the attached exact 1977 source:

`TVA_BOK_0064142_கலைஞர்_கருணாநிதியின்_சிறுகதைகள்.pdf`

- edition: **முதல் பதிப்பு: 1977**
- physical scans: **260**
- bytes: **268,486,609**
- SHA-256: `853032661482eaccb26c083a38d7aa75c081362d33c963c63e37d088bf20acb3`
- exact match to registered source identity
- image-only controlling source
- do not commit the PDF

## Critical user directive

This is **comparison repair, not retranscription**.

For all 37 stories:

- existing repository Tamil is the comparison baseline;
- compare directly against controlling 1977 pixels;
- correct only source-proven mismatches;
- preserve source spelling, punctuation, meaningful spacing, paragraphing, page boundaries and source marks;
- do not normalize old/source-odd Tamil from lexical expectation;
- no global replacements;
- use exhaustive difficult-reading inspection only where needed, but complete an independent Gate B for every physical page.

## Current durable state

Tracker: `collections/1977-kalaignar-karunanidhiyin-sirukathaigal/RE_AUDIT_2026.md`.

Current state: **OPEN — 6 / 37 dual-gate complete**.

Closed under the 2026 standard:

- `புகழேந்தி` — scans 10–15 — Gate A/B PASS; 9 repairs; 0 unresolved;
- `நளாயினி` — scans 16–23 — Gate A/B PASS; 15 repairs; 0 unresolved;
- `சபலம்` — scans 24–30 — Gate A/B PASS; 6 repairs; 0 unresolved;
- `ஆட்டக்காவடி` — scans 31–38 — Gate A/B PASS; 7 repairs; 0 unresolved;
- `குப்பைத்தொட்டி` — scans 39–46 — Gate A/B PASS; 3 repairs; 0 unresolved;
- `சந்தனக்கிண்ணம்` — scans 47–56 — Gate A 10/10 PASS; Gate B 10/10 PASS; 3 repairs; 0 unresolved. Repairs: `கள்ளச்` → `கிள்ளச்`; `தமிழ்த்தாய்கள்` → `தமிழ்த்தாய்களை`; `வந்து விட்டான என` → `வந்து விட்டான் என`. English synchronized.

Do not reopen these six closed stories from stale prompts unless genuinely new direct source evidence appears.

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
10. all controls / page records / assembly / audit / possible-error files under `stories/sangilichami/`

## Exact next activity — `சங்கிலிச்சாமி`

Workspace: `stories/sangilichami/`.

Source range:

- physical scans: **57–68**
- printed pages: **48–59**
- existing canonical pages: **12 / 12** under the legacy workflow
- scan **69** is the boundary witness opening Story 8 `கங்கையின் காதல்`

Complete both gates in **one story-bounded activity**.

### Gate A — source-fidelity comparison

Compare all twelve existing canonical page records and the assembled Tamil directly against source scans **57–68**.

Check wrong/omitted/duplicated words, character forms, punctuation and meaningful spacing, paragraphing, physical page continuations, heading/separators/ornaments/note layers, and every existing possible-error/suspicious-reading candidate.

Do not retranscribe. Repair only source-proven mismatches.

### Gate B — independent Old Tamil Glyph verification

This is a **separate independent gate** and cannot be inferred from Gate A.

Independently reopen every scan **57–68** at high/native resolution and explicitly consider:

`ணா / ணை / ணொ / ணோ / லை / ளை / றா / றொ / றோ / னா / னை / னொ / னோ`

Also remain alert for old ligatures, faint vowel marks, broken/touching type and `ர/ற`, `ன/ண`, `ல/ள` confusions.

- no global replacement;
- character identity only, not modernization;
- record every correction individually with scan / printed-page provenance;
- unresolved historical-glyph count must be **0** for PASS.

## Closure requirements

If all twelve pages settle:

1. apply all source-proven corrections to canonical page records;
2. synchronize assembled Tamil;
3. update story audit / possible-error / historical-glyph records;
4. update existing English only where corrected Tamil materially changes meaning;
5. record Gate A and Gate B results and correction counts durably in `stories/sangilichami/RE_AUDIT_2026.md`;
6. update collection tracker from **6/37** to **7/37** only if both gates PASS and unresolved count is 0;
7. synchronize story inventory, scan map, collection README, root HANDOVER / NEXT_CHAT_PROMPT and root README only if safely reconstructable;
8. commit and re-fetch live `main`;
9. stop/report.

Do **not** begin Story 8 `கங்கையின் காதல்` in the same activity.
