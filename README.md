# கலைஞர் சிறுகதைகள் — மின்னாக்கக் களஞ்சியம்

கலைஞர் மு. கருணாநிதியின் சிறுகதைகள், தனிநூல் பதிப்புகள், மற்றும் பல சிறுகதைகளை ஒரே தொகுப்பாகக் கொண்ட anthologies-ஐ source-first முறையில் பாதுகாக்கும் repository.

## மூலக் கொள்கை

> **மூல ஸ்கேன் தான் controlling source. Markdown ஒரு பாதுகாப்பு அடுக்கு; திருத்தப்பட்ட புதிய பதிப்பு அல்ல.**

- silent modernization / normalization செய்யக்கூடாது;
- difficult story text-ஐ விரைவாக `blocked` என்று விட்டுவிடக்கூடாது — **No stones should be left unturned**;
- processed-crop confidence மட்டும் `verified`-க்கு போதாது; complete phrase/clause/sentence span source-க்கு எதிராக உறுதிப்படுத்தப்பட வேண்டும்;
- unusual source reading `verified` ஆனாலும் later human review-க்கு `POSSIBLE_ERRORS_FOR_REVIEW.md`-ல் வைத்திருக்கலாம்;
- source PDF files GitHub-க்கு commit செய்யப்படாது.

Permanent guides:

- [`SHORT_STORY_PROCESSING_GUIDE.md`](SHORT_STORY_PROCESSING_GUIDE.md)
- [`COLLECTION_SOURCE_GUIDE.md`](COLLECTION_SOURCE_GUIDE.md)

## Canonical stories

| Story | Source state | English |
|---|---|---|
| [`கிழவன் கனவு`](stories/kizhavan-kanavu/README.md) | **16 / 16 story scans verified; 0 story blocks** | **complete / source-complete / release-ready** |
| [`புகழேந்தி`](stories/pugazhendhi/README.md) | **6 / 6 pages verified; 0 blocks; manual recheck queue open** | not started |
| [`நளாயினி`](stories/nalayini/README.md) | **8 / 8 pages verified; 0 blocks; manual recheck queue open** | not started |

Manual possible-error review queues:

- [`கிழவன் கனவு`](stories/kizhavan-kanavu/POSSIBLE_ERRORS_FOR_REVIEW.md)
- [`புகழேந்தி`](stories/pugazhendhi/POSSIBLE_ERRORS_FOR_REVIEW.md)
- [`நளாயினி`](stories/nalayini/POSSIBLE_ERRORS_FOR_REVIEW.md)

## Registered anthology source

### கலைஞர் கருணாநிதியின் சிறுகதைகள் — முதல் பதிப்பு, 1977

Collection workspace:

- [`collections/1977-kalaignar-karunanidhiyin-sirukathaigal/`](collections/1977-kalaignar-karunanidhiyin-sirukathaigal/README.md)

Source registration state:

- anthology source PDF: `TVA_BOK_0064142_கலைஞர்_கருணாநிதியின்_சிறுகதைகள்.pdf`
- printed title: **கலைஞர் கருணாநிதியின் சிறுகதைகள்**
- printed author: **கலைஞர் மு. கருணாநிதி**
- publisher: **தமிழ்க்கனி பதிப்பகம், சென்னை-28**
- first edition: **1977**
- PDF scans: **260**
- printed story pages: **1–250**
- stories in contents: **37**
- story inventory: **37 / 37 registered**
- story-opening scan checks: **37 / 37 complete**
- Tamil source processing complete from anthology: **2 / 37** — `புகழேந்தி`, `நளாயினி`
- anthology stories not yet transcribed: **35 / 37**

Exact source metadata:

- [`metadata/source.md`](collections/1977-kalaignar-karunanidhiyin-sirukathaigal/metadata/source.md)

Exact 37-story inventory:

- [`indexes/story-inventory.md`](collections/1977-kalaignar-karunanidhiyin-sirukathaigal/indexes/story-inventory.md)

Scan / printed-page ranges:

- [`indexes/scan-map.md`](collections/1977-kalaignar-karunanidhiyin-sirukathaigal/indexes/scan-map.md)

### Story 1 — புகழேந்தி — completed Tamil source pass

- printed pages **1–6**
- PDF scans **10–15**
- canonical workspace: [`stories/pugazhendhi/`](stories/pugazhendhi/README.md)
- page records: **6 / 6 verified**
- Tamil assembly: complete
- Tamil audit: **PASS**
- source blocks: **0**
- human possible-error queue: created
- English: not started

### Story 2 — நளாயினி — completed Tamil source pass

- printed pages **7–14**
- PDF scans **16–23**
- canonical workspace: [`stories/nalayini/`](stories/nalayini/README.md)
- page records: **8 / 8 verified**
- Tamil assembly: complete
- Tamil audit: **PASS**
- source blocks: **0**
- human possible-error queue: created
- English: not started

Important source distinctions retained in `நளாயினி`:

- scan 17: `மெளத் கல்யர்`
- scan 18: `மெளத்கல்யர்`
- printed page 14 narrative conclusion is kept separate from the following `குறிப்பு :—`.

### Edition-level title differences already preserved

- TOC `புரட்சிப்படம்` ↔ story-opening heading `புரட்சிப் படம்`
- TOC `சித்தார்த்தன்` ↔ story-opening heading `சித்தார்த்தன் சிலை`

These are source facts and must not be silently normalized.

## Repository organization

```text
README.md
SHORT_STORY_PROCESSING_GUIDE.md
COLLECTION_SOURCE_GUIDE.md
HANDOVER.md
collections/
  1977-kalaignar-karunanidhiyin-sirukathaigal/
    README.md
    metadata/
      source.md
    indexes/
      story-inventory.md
      scan-map.md
stories/
  kizhavan-kanavu/
    ...
  pugazhendhi/
    ...
  nalayini/
    README.md
    metadata/
      source.md
    indexes/
      page-map.md
    pages/
      0016-nalayini-01.md ... 0023-nalayini-08.md
    sections/
      nalayini.md
    audit.md
    POSSIBLE_ERRORS_FOR_REVIEW.md
```

Anthology folders preserve physical collection identity. Canonical story text always lives under `stories/<slug>/`. If a later anthology entry matches an already-existing story, register the anthology as an additional edition/witness rather than creating a duplicate canonical story.

## Next exact activity

Begin anthology Story **3 — `சபலம்`**:

- printed pages **15–21**
- PDF scans **24–30**

First confirm live `main` has no existing matching canonical workspace. Then create and complete the Tamil source pass for Story 3 only; do not begin Story 4 in the same activity.
