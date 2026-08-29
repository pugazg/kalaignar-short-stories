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
| [`சபலம்`](stories/sabalam/README.md) | **7 / 7 pages verified; 0 blocks; manual recheck queue open** | not started |
| [`ஆட்டக்காவடி`](stories/aattakkavadi/README.md) | **8 / 8 pages verified; 0 blocks; manual recheck queue open** | not started |
| [`குப்பைத்தொட்டி`](stories/kuppai-thotti/README.md) | **8 / 8 pages verified; 0 blocks; manual recheck queue open** | not started |
| [`சந்தனக்கிண்ணம்`](stories/santhana-kinnam/README.md) | **10 / 10 pages verified; 0 blocks; manual recheck queue open** | not started |
| [`சங்கிலிச்சாமி`](stories/sangilichami/README.md) | **12 / 12 pages verified; 0 blocks; manual recheck queue open** | not started |

Manual possible-error review queues are retained inside each completed story workspace.

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
- Tamil source processing complete from anthology: **7 / 37** — `புகழேந்தி`, `நளாயினி`, `சபலம்`, `ஆட்டக்காவடி`, `குப்பைத்தொட்டி`, `சந்தனக்கிண்ணம்`, `சங்கிலிச்சாமி`
- anthology stories not yet transcribed: **30 / 37**
- English translation started from anthology: **0 / 37**

Exact source metadata:

- [`metadata/source.md`](collections/1977-kalaignar-karunanidhiyin-sirukathaigal/metadata/source.md)

Exact 37-story inventory:

- [`indexes/story-inventory.md`](collections/1977-kalaignar-karunanidhiyin-sirukathaigal/indexes/story-inventory.md)

Scan / printed-page ranges:

- [`indexes/scan-map.md`](collections/1977-kalaignar-karunanidhiyin-sirukathaigal/indexes/scan-map.md)

## Completed anthology Tamil source passes

1. **புகழேந்தி** — printed **1–6**, scans **10–15**, **6/6 verified**, audit PASS, 0 blocked.
2. **நளாயினி** — printed **7–14**, scans **16–23**, **8/8 verified**, audit PASS, 0 blocked.
3. **சபலம்** — printed **15–21**, scans **24–30**, **7/7 verified**, audit PASS, 0 blocked.
4. **ஆட்டக்காவடி** — printed **22–29**, scans **31–38**, **8/8 verified**, audit PASS, 0 blocked.
5. **குப்பைத்தொட்டி** — printed **30–37**, scans **39–46**, **8/8 verified**, audit PASS, 0 blocked.
6. **சந்தனக்கிண்ணம்** — printed **38–47**, scans **47–56**, **10/10 verified**, audit PASS, 0 blocked.
7. **சங்கிலிச்சாமி** — printed **48–59**, scans **57–68**, **12/12 verified**, audit PASS, 0 blocked.

All seven have **0 unresolved story text**, complete Tamil assemblies and persistent human-review queues. English translation has not been started for these anthology stories.

### Story 7 — சங்கிலிச்சாமி

Canonical workspace: [`stories/sangilichami/`](stories/sangilichami/README.md)

- printed pages **48–59**
- PDF scans **57–68**
- page records: **12 / 12 verified**
- Tamil assembly: complete
- Tamil audit: **PASS**
- source blocks / unresolved story text: **0**
- human possible-error queue: created
- scan **69** confirmed as the opening of next story `கங்கையின் காதல்`
- English: not started

Representative source-close readings retained for human recheck include `அஷ்டமா சித்துபுரி`, `‘நமப்பார்வதி படே’`, `பிள்ளையில்ல....அருள் தேவை`, `செக்கச் செவேன்னு`, `மூடாத்மா ஞானத்மாவாக`, `தவறுக என்னை மதிக்காதீர்`, `அவசரந் தாங்காத`, and `கொலைகாரனுக்கிவிட்டாயே`. Enlarged source review resolved `ஆகட்டும் ஸ்வாமி` and `மாபெரும் மடம்`.

### Edition-level title differences already preserved

- TOC `புரட்சிப்படம்` ↔ story-opening heading `புரட்சிப் படம்`
- TOC `சித்தார்த்தன்` ↔ story-opening heading `சித்தார்த்தன் சிலை`

These are source facts and must not be silently normalized.

## Repository organization

Anthology folders preserve physical collection identity. Canonical story text always lives under `stories/<slug>/`. If a later anthology entry matches an already-existing story, register the anthology as an additional edition/witness rather than creating a duplicate canonical story.

## Next exact activity

Process anthology Story **8 — `கங்கையின் காதல்`** only:

- printed pages **60–63**
- PDF scans **69–72**

First confirm live `main` has no existing matching canonical workspace. Then visually confirm scan **69** opens `கங்கையின் காதல்`, scan **72** contains its ending, and scan **73** begins Story 9 `தாய்மை`. Complete the Tamil source pass for Story 8 only and do not begin Story 9 in the same activity.
