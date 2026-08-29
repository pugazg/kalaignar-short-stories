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

## Collection structure

```text
collections/1977-kalaignar-karunanidhiyin-sirukathaigal/
  README.md
  metadata/
    source.md
  indexes/
    story-inventory.md
    scan-map.md
```

## Inventory / processing state

The printed contents on scans **8–9** has been transcribed into a 37-story inventory. Every calculated story-start scan was visually checked against the actual story-opening heading.

- story inventory: **37 / 37 registered**
- start-page visual checks: **37 / 37**
- Tamil source processing complete: **1 / 37**
- not yet transcribed: **36 / 37**
- English translation: **0 / 37 started**

Completed from this collection:

### 1. புகழேந்தி

- canonical workspace: [`../../stories/pugazhendhi/`](../../stories/pugazhendhi/)
- printed pages: **1–6**
- source scans: **10–15**
- page records: **6 / 6 verified**
- blocked / missing source text: **0**
- Tamil assembly: complete
- source audit: **PASS**
- persistent human possible-error queue: created
- English translation: not started

The human review queue deliberately retains unusual readings for later source checking without silently correcting them.

See [`indexes/story-inventory.md`](indexes/story-inventory.md).

## Source-title differences

Two edition-level TOC/opening-heading differences were found during registration:

1. TOC `புரட்சிப்படம்` ↔ opening heading `புரட்சிப் படம்`
2. TOC `சித்தார்த்தன்` ↔ opening heading `சித்தார்த்தன் சிலை`

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

The first anthology story, `புகழேந்தி`, now has its own canonical workspace. Later stories should only receive workspaces when they become active.

## Next exact activity

Process Story 2 **`நளாயினி`**:

- printed pages **7–14**
- anthology scans **16–23**

Before starting it, confirm no matching canonical workspace has appeared on live `main`; then follow the same page-by-page visual/full-span workflow used for `புகழேந்தி`.
