# பழக்கூடை — 1979 collection source intake

Physical-source workspace for the user-supplied **`பழக்கூடை`** anthology.

## Source snapshot

- source PDF: `TVA_BOK_0064146_பழக்கூடை.pdf`
- byte size: **74,336,202**
- SHA-256: **`b62a13eadc3c520721c9690e3c99fd949072a1abbcb388627262dc4ac841b11d`**
- PDF scans: **65**
- printed title: **பழக்கூடை**
- printed author: **மு. கருணாநிதி**
- publisher: **திராவிடப்பண்ணை**
- represented printed edition: **மூன்றாம் பதிப்பு — 1979**
- printed price: **ரூ. 2-00**
- printer: **ராஜேந்திரா பிரிண்டர்ஸ், சிந்தாமணி, திருச்சிராப்பள்ளி-2**
- source type: **image-only scan; no usable parsed text layer**
- source PDF committed to GitHub: **No**

A handwritten note on scan 3 appears to mention an earlier 1955 publication date. It is retained only as a provenance annotation and is **not** used to override the printed edition statement. This workspace represents the printed **1979 third edition**.

The attached PDF itself is the controlling source. Rendered scan pixels govern all source-dependent decisions.

## Front matter

- scan **1** — illustrated front cover;
- scan **2** — title / author / publisher page;
- scan **3** — printed edition / price / printer page;
- scans **4–5** — publisher note headed `பழக்கூடை`, signed `பதிப்பகத்தார்`;
- no printed contents page is visible;
- scan **6** opens the first story.

## Story block / pagination

Story text occupies scans **6–65** and printed pages **5–64**.

Across the story block:

**PDF scan = printed page + 1**

The source ends on scan **65 / printed 64** with the end of `அபாக்ய சிந்தாமணி`. No later advertisement/back-matter scan is present in the supplied PDF.

## Story inventory

| # | Source opening heading | PDF scans | Printed pages | Repository routing |
|---:|---|---:|---:|---|
| 1 | `தொடர்கதை` | 6–35 | 5–34 | same work as canonical `stories/mudiyatha-thodarkathai/` — title variant / additional witness |
| 2 | `கடைசிக் கட்டம்` | 36–41 | 35–40 | existing canonical `stories/kadaisi-kattam/` — additional witness |
| 3 | `புகழேந்தி` | 42–48 | 41–47 | existing canonical `stories/pugazhendhi/` — additional witness |
| 4 | `திடுக்கிடும் கதை` | 49–55 | 48–54 | existing canonical `stories/thidukkidum-kathai/` — additional witness |
| 5 | `அபாக்ய சிந்தாமணி` | 56–65 | 55–64 | existing canonical `stories/abagya-chinthamani/` — additional witness |

Detailed records:

- [`metadata/source.md`](metadata/source.md)
- [`indexes/scan-map.md`](indexes/scan-map.md)
- [`indexes/story-inventory.md`](indexes/story-inventory.md)

## Canonical deduplication intake

Live `main` was checked before registration.

All five source stories already correspond to canonical works. Therefore this collection contributes **five additional witnesses and zero new canonical stories**.

The Story-1 title is a source-specific shorter form:

- 1979 source: **`தொடர்கதை`**
- canonical later title: **`முடியாத தொடர்கதை`**

Same-work identity is confirmed by the distinctive opening architecture: section numeral **1**, scene **`சிறைச்சாலை—இரவு நேரம்`**, and the opening conversation between **சங்கு** and **சந்தனம்**, matching the canonical work.

No duplicate canonical story folder was created.

## Current state

- source registration: **COMPLETE**
- scan map: **COMPLETE**
- story inventory: **5/5 COMPLETE**
- story openings visually checked: **5/5**
- final source boundary checked: **PASS**
- existing-canonical witness routes: **5/5**
- new canonical stories: **0**
- witness comparison: **IN PROGRESS — Story 1 `தொடர்கதை` CLOSED / PASS 30/30; Stories 2–5 pending**
- English: **not part of witness comparison; canonical English remains unchanged**

## Story 1 witness — `தொடர்கதை`

Canonical target:

`stories/mudiyatha-thodarkathai/`

The source heading **`தொடர்கதை`** remains an edition-specific shorter title for canonical **`முடியாத தொடர்கதை`**.

**CLOSED / PASS — 30/30 witness scans.**

- Batch 1: scans **6–20 / printed 5–19** — **CLOSED / PASS**
- Batch 2: scans **21–35 / printed 20–34** — **CLOSED / PASS**
- material variant groups: **13**
- canonical confirmations: **5**
- major scene-level additions / omissions: **0**
- canonical recheck candidates: **0**
- unresolved witness readings: **0**
- canonical Tamil / English changed: **No / No**
- scan **35** ending / ornament: **PASS**
- scan **36** separate `கடைசிக் கட்டம்` opening: **PASS**

Representative variants:

- `அனுச் சஞ்சலமும்` ↔ `அனுச்சரணமும்`;
- `உளறிவைத்த ... சொல் அலங்காரத்துக்குப்` ↔ `ஊற்றி வைத்த ... சொல்லலங்காரத்துக்குப்`;
- `சூதுக்குப் பெயர் காதல்` ↔ `தூதுக்குப் பெயர் காதல்`;
- `நம்மிருவரின் காதல்` ↔ `நம்மிருவரின் காதலை`;
- `உருக்கியபடி இருந்தது` ↔ `உருக்கிக் கொண்டிருந்தது`;
- `மூடத்தனத்திற்கு` ↔ canonical `முடத்தனத்திற்கு`.

Durable witness:
`stories/mudiyatha-thodarkathai/witnesses/1979-pazhakkoodai/`

## Exact next activity

User batching rule: **15 physical source pages per iteration**.

Next source batch:

**scans 36–50 / printed 35–49 — 15 pages**

This crosses three already-existing canonical story routes:

1. scans **36–41** — complete `கடைசிக் கட்டம்` → `stories/kadaisi-kattam/`;
2. scans **42–48** — complete `புகழேந்தி` → `stories/pugazhendhi/`;
3. scans **49–50** — first two pages of `திடுக்கிடும் கதை` → `stories/thidukkidum-kathai/`.

Process all 15 source pages comparison-only, maintain separate witness records per canonical story, and stop after scan 50.
