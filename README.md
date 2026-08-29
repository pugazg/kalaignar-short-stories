# கலைஞர் சிறுகதைகள் — மின்னாக்கக் களஞ்சியம்

கலைஞர் மு. கருணாநிதியின் சிறுகதைகள், தனிநூல் பதிப்புகள், மற்றும் பல சிறுகதைகளை ஒரே தொகுப்பாகக் கொண்ட anthologies-ஐ source-first முறையில் பாதுகாக்கும் repository.

## மூலக் கொள்கை

> **மூல ஸ்கேன் தான் controlling source. Markdown ஒரு பாதுகாப்பு அடுக்கு; திருத்தப்பட்ட புதிய பதிப்பு அல்ல.**

- silent modernization / normalization செய்யக்கூடாது;
- difficult story text-ஐ விரைவாக `blocked` என்று விட்டுவிடக்கூடாது — **No stones should be left unturned**;
- processed-crop confidence மட்டும் `verified`-க்கு போதாது; complete phrase/clause/sentence span source-க்கு எதிராக உறுதிப்படுத்தப்பட வேண்டும்;
- source PDF files GitHub-க்கு commit செய்யப்படாது.

Permanent guides:

- [`SHORT_STORY_PROCESSING_GUIDE.md`](SHORT_STORY_PROCESSING_GUIDE.md)
- [`COLLECTION_SOURCE_GUIDE.md`](COLLECTION_SOURCE_GUIDE.md)

## Canonical stories

| Story | Source state | English |
|---|---|---|
| [`கிழவன் கனவு`](stories/kizhavan-kanavu/README.md) | **16 / 16 story scans verified; 0 story blocks** | **complete / source-complete / release-ready** |

`கிழவன் கனவு`-க்கான manual recheck queue:

- [`stories/kizhavan-kanavu/POSSIBLE_ERRORS_FOR_REVIEW.md`](stories/kizhavan-kanavu/POSSIBLE_ERRORS_FOR_REVIEW.md)

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
- per-story transcription from this anthology: **not started**

Exact source metadata:

- [`metadata/source.md`](collections/1977-kalaignar-karunanidhiyin-sirukathaigal/metadata/source.md)

Exact 37-story inventory:

- [`indexes/story-inventory.md`](collections/1977-kalaignar-karunanidhiyin-sirukathaigal/indexes/story-inventory.md)

Scan / printed-page ranges:

- [`indexes/scan-map.md`](collections/1977-kalaignar-karunanidhiyin-sirukathaigal/indexes/scan-map.md)

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
```

Anthology folders preserve physical collection identity. Canonical story text always lives under `stories/<slug>/`. If a later anthology entry matches an already-existing story, register the anthology as an additional edition/witness rather than creating a duplicate canonical story.

## Next exact activity

Begin anthology Story **1 — `புகழேந்தி`**:

- printed pages **1–6**
- PDF scans **10–15**

Create its canonical story workspace, register this 1977 anthology as the controlling source, transcribe the six story pages page-by-page, run direct visual/full-span verification, and create its `POSSIBLE_ERRORS_FOR_REVIEW.md` queue.
