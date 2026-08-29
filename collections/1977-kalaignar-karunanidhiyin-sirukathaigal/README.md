# கலைஞர் கருணாநிதியின் சிறுகதைகள் — 1977 anthology source

This folder registers the anthology **`கலைஞர் கருணாநிதியின் சிறுகதைகள்`** as a collection-level archival source for `pugazg/kalaignar-short-stories`.

The anthology is **not** treated as one story. Its 37 stories are processed into canonical `stories/<slug>/` workspaces one at a time, while this folder preserves anthology identity, contents order, printed pagination, scan mapping and edition-specific title variants.

## Source snapshot

- Printed title: **கலைஞர் கருணாநிதியின் சிறுகதைகள்**
- Printed author: **கலைஞர் மு. கருணாநிதி**
- Publisher: **தமிழ்க்கனி பதிப்பகம், சென்னை-28**
- Edition: **முதல் பதிப்பு: 1977**
- Source filename: `TVA_BOK_0064142_கலைஞர்_கருணாநிதியின்_சிறுகதைகள்.pdf`
- SHA-256: `853032661482eaccb26c083a38d7aa75c081362d33c963c63e37d088bf20acb3`
- PDF scan pages: **260**
- Printed story pages: **1–250**
- Stories in printed contents: **37**
- Source PDF committed to GitHub: **No**

Full registration: [`metadata/source.md`](metadata/source.md).

## Inventory / processing state

The printed contents on scans **8–9** has been transcribed into a 37-story inventory. Every calculated story-start scan was visually checked against the actual story-opening heading.

- story inventory: **37 / 37 registered**
- start-page visual checks: **37 / 37**
- Tamil source processing complete: **8 / 37**
- not yet transcribed: **29 / 37**
- English translation: **0 / 37 started**

Completed from this collection:

1. `புகழேந்தி` — workspace [`../../stories/pugazhendhi/`](../../stories/pugazhendhi/) — printed **1–6**, scans **10–15**, **6/6 verified**, 0 blocked, audit PASS.
2. `நளாயினி` — workspace [`../../stories/nalayini/`](../../stories/nalayini/) — printed **7–14**, scans **16–23**, **8/8 verified**, 0 blocked, audit PASS.
3. `சபலம்` — workspace [`../../stories/sabalam/`](../../stories/sabalam/) — printed **15–21**, scans **24–30**, **7/7 verified**, 0 blocked, audit PASS.
4. `ஆட்டக்காவடி` — workspace [`../../stories/aattakkavadi/`](../../stories/aattakkavadi/) — printed **22–29**, scans **31–38**, **8/8 verified**, 0 blocked, audit PASS.
5. `குப்பைத்தொட்டி` — workspace [`../../stories/kuppai-thotti/`](../../stories/kuppai-thotti/) — printed **30–37**, scans **39–46**, **8/8 verified**, 0 blocked, audit PASS.
6. `சந்தனக்கிண்ணம்` — workspace [`../../stories/santhana-kinnam/`](../../stories/santhana-kinnam/) — printed **38–47**, scans **47–56**, **10/10 verified**, 0 blocked, audit PASS.
7. `சங்கிலிச்சாமி` — workspace [`../../stories/sangilichami/`](../../stories/sangilichami/) — printed **48–59**, scans **57–68**, **12/12 verified**, 0 blocked, audit PASS.
8. `கங்கையின் காதல்` — workspace [`../../stories/gangaiyin-kadhal/`](../../stories/gangaiyin-kadhal/) — printed **60–63**, scans **69–72**, **4/4 verified**, 0 blocked, audit PASS.

All eight have complete Tamil assemblies, zero unresolved story text, persistent possible-error queues, and no English translation started from this anthology.

For `கங்கையின் காதல்`, scan **73** was visually confirmed as the next-story opening `தாய்மை`.

## Source-title differences

Two edition-level TOC/opening-heading differences were found during registration:

1. TOC `புரட்சிப்படம்` ↔ opening `புரட்சிப் படம்`
2. TOC `சித்தார்த்தன்` ↔ opening `சித்தார்த்தன் சிலை`

Both forms are source evidence and are preserved. Neither is silently normalized.

## Pagination

The anthology story block is continuous:

- scan **10** = printed page **1**
- scan **259** = printed page **250**
- scan **260** = back cover
- story-block formula: **scan = printed page + 9**

See [`indexes/scan-map.md`](indexes/scan-map.md).

## Canonical-story policy

This anthology is a **source container**, not the canonical story namespace.

When a story is processed:

1. inspect whether a matching canonical story workspace already exists;
2. if none exists, create `stories/<slug>/`;
3. register this anthology and exact scan/printed-page range in that story's source metadata;
4. if another edition/source already exists, add this anthology as an additional witness instead of creating a duplicate story;
5. preserve TOC vs opening-heading differences as edition metadata;
6. do not use anthology text to silently overwrite another edition;
7. create a persistent `POSSIBLE_ERRORS_FOR_REVIEW.md` for unusual or easily misread source forms.

## Existing repository relationship

`கிழவன் கனவு` remains an independently processed canonical story from another source and is not in this anthology.

The first eight anthology stories now have canonical workspaces:

- `புகழேந்தி`
- `நளாயினி`
- `சபலம்`
- `ஆட்டக்காவடி`
- `குப்பைத்தொட்டி`
- `சந்தனக்கிண்ணம்`
- `சங்கிலிச்சாமி`
- `கங்கையின் காதல்`

Later stories should only receive workspaces when they become active.

## Next exact activity

Process Story 9 **`தாய்மை`**:

- printed pages **64–74**
- anthology scans **73–83**

Before starting it, confirm no matching canonical workspace has appeared on live `main`; visually confirm scan 73 opening and scan 83 ending / scan 84 next-story boundary (`தப்பிவிட்டார்கள்`), then follow the same page-by-page visual/full-span workflow. Do not begin Story 10 in the same activity.
