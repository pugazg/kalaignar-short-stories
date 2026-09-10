# NEXT CHAT PROMPT — 1977 anthology re-audit / `கங்கையின் காதல்` dual-gate

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

## Critical directive

This is **comparison repair, not retranscription**.

For all 37 stories:

- existing repository Tamil is the comparison baseline;
- compare directly against controlling 1977 pixels;
- correct only source-proven mismatches;
- preserve source spelling, punctuation, meaningful spacing, paragraphing, page boundaries and source marks;
- do not normalize old/source-odd Tamil from lexical expectation;
- no global replacements;
- complete an independent Gate B for every physical page.

## Current durable state

Tracker: `collections/1977-kalaignar-karunanidhiyin-sirukathaigal/RE_AUDIT_2026.md`.

Current state: **OPEN — 7 / 37 dual-gate complete**.

Closed under the 2026 standard:

- `புகழேந்தி` — 9 repairs / 0 unresolved;
- `நளாயினி` — 15 / 0;
- `சபலம்` — 6 / 0;
- `ஆட்டக்காவடி` — 7 / 0;
- `குப்பைத்தொட்டி` — **4 / 0**, including Story-7-triggered historical-`னா` regression `போதுதானு` → `போதுதானா`;
- `சந்தனக்கிண்ணம்` — 3 / 0;
- `சங்கிலிச்சாமி` — Gate A/B **12/12 PASS**, **6 / 0**: `என்னு`→`என்னா`; `தவறுக`→`தவறாக`; `தானு?`→`தானா?`; `கூறினன்`→`கூறினான்`; `கொலைகாரனுக்கிவிட்டாயே`→`கொலைகாரனாக்கிவிட்டாயே`; `காட்டினன்`→`காட்டினான்`.

Do not reopen these seven stories unless genuinely new direct source evidence appears.

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
10. all controls / page records / assembly / audit / possible-error files under `stories/gangaiyin-kadhal/`

## Exact next activity — `கங்கையின் காதல்`

Workspace: `stories/gangaiyin-kadhal/`.

Source range:

- physical scans: **69–72**
- printed pages: **60–63**
- existing canonical pages: **4 / 4**
- scan **73** is the boundary witness opening Story 9 `தாய்மை`

### Gate A — source fidelity

Compare all four existing canonical page records and the assembled Tamil directly against scans **69–72**. Check words, characters, punctuation/meaningful spacing, paragraphing, physical joins, heading/separators/ornaments/note layers, and every possible-error candidate.

### Gate B — independent Old Tamil Glyph verification

Independently reopen every scan **69–72** at native/high resolution and explicitly consider:

`ணா / ணை / ணொ / ணோ / லை / ளை / றா / றொ / றோ / னா / னை / னொ / னோ`

Also remain alert for old ligatures, faint vowel marks, broken/touching type and `ர/ற`, `ன/ண`, `ல/ள` confusions. Story 7 proved that apparent modern `னு`/`ன` shapes can encode historical `னா`; distinguish them from genuine `னு` by direct same-edition comparison.

## Closure requirements

If all four pages settle:

1. apply source-proven corrections individually;
2. synchronize Tamil assembly and story controls;
3. update English only where corrected Tamil materially changes meaning;
4. create/update the durable 2026 Gate A/B record;
5. advance collection tracker **7/37 → 8/37** only with Gate A 4/4 + Gate B 4/4 + 0 unresolved;
6. synchronize inventory, scan map, collection README, root HANDOVER / README / NEXT prompt;
7. commit, re-fetch live `main`, stop/report.

Do **not** begin Story 9 `தாய்மை` in the same activity.
