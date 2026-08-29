# Source Registration — கலைஞர் கருணாநிதியின் சிறுகதைகள் (1977)

## Identity

- Source filename: `TVA_BOK_0064142_கலைஞர்_கருணாநிதியின்_சிறுகதைகள்.pdf`
- SHA-256: `853032661482eaccb26c083a38d7aa75c081362d33c963c63e37d088bf20acb3`
- File size: **268,486,609 bytes**
- PDF scan pages: **260**
- Source PDF stored in repository: **No**
- Source type: **short-story anthology / collection**
- Printed title: **கலைஞர் கருணாநிதியின் சிறுகதைகள்**
- Printed author line: **கலைஞர் மு. கருணாநிதி**
- Publisher imprint: **தமிழ்க்கனி பதிப்பகம், சென்னை-28**
- Edition statement: **முதல் பதிப்பு: 1977**
- Printed price: **ரூ. 10/-**
- Cover-art credit: **முகப்பு ஓவியம்: அருணோதன்**

## Front matter observed

| Scan | Printed page | Material |
|---:|:---:|---|
| 1 | — | front cover — anthology title / illustration |
| 2 | — | inside-cover / gift label: `பேராசிரியர். தி.வ. மெய்கண்டார் அவர்களின் அன்பளிப்பு` |
| 3 | — | title page — title, author, publisher imprint |
| 4 | — | publication/copyright page — first edition 1977, price, cover-art credit, printer line |
| 5 | — | `என்னுரை` — signed `மு. கருணாநிதி`, dated `சென்னை 5-9-77` |
| 6–7 | — | `பதிப்புரை` — signed `தமிழ்க்கனி பதிப்பகத்தார்`, dated `சென்னை-28 25-9-77` |
| 8–9 | — | `பொருளடக்கம்` — 37 stories with printed starting pages |
| 10 | 1 | Story 1 begins: `புகழேந்தி` |

## Pagination model

The anthology's story text uses continuous printed pagination.

- Printed story pages: **1–250**
- PDF scans carrying printed story pages: **10–259**
- Verified relation across the story block: **scan page = printed page + 9**
- Scan **260**: back cover

The relation was checked at the beginning (`புகழேந்தி`, printed page 1 / scan 10), at all 37 story-opening scans, and at the end (`நுனிக்கரும்பு`, printed page 249 on scan 258 and printed page 250 on scan 259).

## Contents / collection size

The printed `பொருளடக்கம்` lists **37 short stories**. Full inventory and source-title comparison:

- [`../indexes/story-inventory.md`](../indexes/story-inventory.md)

Scan/front-matter mapping:

- [`../indexes/scan-map.md`](../indexes/scan-map.md)

## Source-title anomalies already identified

The contents list and story-opening headings are not always identical.

1. TOC: `புரட்சிப்படம்` — opening heading: `புரட்சிப் படம்`
2. TOC: `சித்தார்த்தன்` — opening heading: `சித்தார்த்தன் சிலை`

These are preserved as source-layer differences. They must not be silently normalized.

## Repository relationship

At registration time the repository contains one existing canonical story workspace:

- `stories/kizhavan-kanavu/`

`கிழவன் கனவு` is **not** in this anthology's 37-story contents list. Therefore this anthology currently introduces **37 unprocessed story entries** relative to the existing repository state.

Future rule: if any anthology story later matches an already-created canonical story from another source, do not create a duplicate canonical story. Register this anthology as an additional edition/witness under that story and compare source readings explicitly.

## Current processing state

- anthology identity registered: **complete**
- front-matter structure mapped: **complete at structural level**
- 37-story contents inventory: **complete**
- 37 story start pages visually checked: **complete**
- per-story transcription: **not started**
- per-story visual fidelity audit: **not started**
- English translation: **not started**

## Next exact activity

Begin with Story 1, **`புகழேந்தி`**, printed pages **1–6**, PDF scans **10–15**:

1. create its canonical `stories/<slug>/` workspace;
2. treat this anthology as its controlling source;
3. transcribe scans 10–15 page by page;
4. perform direct visual/full-span fidelity review before marking any page `verified`;
5. create a `POSSIBLE_ERRORS_FOR_REVIEW.md` queue for suspicious readings rather than hiding uncertainty.
