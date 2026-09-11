# NEXT CHAT PROMPT — 1977 anthology re-audit / `தப்பிவிட்டார்கள்` dual-gate

Continue in `pugazg/kalaignar-short-stories`, branch `main`. **LIVE MAIN IS AUTHORITATIVE.**

## Controlling source

Use the exact 1977 source:

`TVA_BOK_0064142_கலைஞர்_கருணாநிதியின்_சிறுகதைகள்.pdf`

- edition: **முதல் பதிப்பு: 1977**
- physical scans: **260**
- bytes: **268,486,609**
- SHA-256: `853032661482eaccb26c083a38d7aa75c081362d33c963c63e37d088bf20acb3`
- image-only controlling source
- do not commit the PDF

## Critical directive

This is **comparison repair, not retranscription**.

- existing repository Tamil is the comparison baseline;
- compare directly against controlling 1977 pixels;
- correct only source-proven mismatches;
- preserve source spelling, punctuation, meaningful spacing, paragraphing, page boundaries and source marks;
- do not normalize old/source-odd Tamil from lexical expectation;
- no global replacements;
- Gate B is independent for every physical page.

## Durable state

Collection tracker: **OPEN — 9 / 37 dual-gate complete**.

Closed under the 2026 standard: Stories **1–9**. Most recent closure:

- `தாய்மை` — scans **73–83 / printed 64–74** — Gate A **11/11 PASS**, Gate B **11/11 PASS**, **42 repairs / 0 unresolved**;
- English is synchronized to the corrected Tamil;
- scan 84 was used only as the boundary witness and opens Story 10 `தப்பிவிட்டார்கள்`.

Do not reopen Stories 1–9 unless genuinely new direct source evidence appears.

## Mandatory startup

Read completely before source-dependent changes:

1. `SHORT_STORY_PROCESSING_GUIDE.md`
2. `HISTORICAL_TAMIL_GLYPH_TRANSCRIPTION_GUIDE.md`
3. root `HANDOVER.md`
4. this prompt
5. collection `README.md`
6. collection `RE_AUDIT_2026.md`
7. collection `OLD_TAMIL_GLYPH_REAUDIT_GATE.md`
8. collection `indexes/story-inventory.md`
9. collection `indexes/scan-map.md`
10. all controls / page records / assembly / audit / possible-error files under `stories/thappivittargal/`

## Exact next activity — `தப்பிவிட்டார்கள்`

Workspace: `stories/thappivittargal/`.

Source range:

- physical scans: **84–91**
- printed pages: **75–82**
- existing canonical pages: **8 / 8**
- scan **92** is the boundary witness opening Story 11 `தப்பவில்லை`

### Gate A — source fidelity

Compare all eight existing canonical page records and the assembled Tamil directly against scans **84–91**. Check wrong/omitted/duplicated words, character forms, punctuation and meaningful spacing, paragraphing, physical page continuations, heading/separators/ornaments/note layers, and every existing possible-error candidate.

### Gate B — independent Old Tamil Glyph verification

Independently reopen every scan **84–91** at native/high resolution and explicitly consider:

`ணா / ணை / ணொ / ணோ / லை / ளை / றா / றொ / றோ / னா / னை / னொ / னோ`

Also remain alert for old ligatures, faint vowel marks, broken/touching type and `ர/ற`, `ன/ண`, `ல/ள` confusions. Adjudicate by source pixels and same-edition comparison, not grammar.

## Closure requirements

If all eight pages settle:

1. apply all source-proven corrections individually;
2. synchronize assembled Tamil and story controls;
3. update existing English only where corrected Tamil materially changes meaning;
4. create/update the durable 2026 Gate A/B record;
5. advance collection tracker **9/37 → 10/37** only with Gate A 8/8 + Gate B 8/8 + 0 unresolved;
6. synchronize inventory, scan map, collection README, root HANDOVER / README / NEXT prompt;
7. commit, re-fetch live `main`, stop/report.

Do **not** begin Story 11 `தப்பவில்லை` in the same activity.
