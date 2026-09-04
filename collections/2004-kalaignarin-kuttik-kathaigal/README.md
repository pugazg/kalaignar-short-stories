# கலைஞரின் குட்டிக் கதைகள் — 2004 second-edition collection source

This folder registers **`கலைஞரின் குட்டிக் கதைகள்`** as the active collection-level source in `pugazg/kalaignar-short-stories`.

## Source snapshot

- source filename: `TVA_BOK_0065567_கலைஞரின்_குட்டிக்_கதைகள்_2004.pdf`
- printed title: **கலைஞரின் குட்டிக் கதைகள்**
- publisher: **பாரதி பதிப்பகம்**
- colophon: **Revised Edition: Aug. 1998; Second Edition: March 2004**
- represented edition: **Second Edition, March 2004**
- PDF scans: **50**
- story-text scans: **4–49**
- printed story pages: **3–48**
- direct story-heading inventory: **34 / 34**
- printed contents page: **none visible**
- scan **50**: physical back cover; no further story text
- source PDF committed to GitHub: **No**

Full identity and scan-condition notes are in [`metadata/source.md`](metadata/source.md).

## Inventory method

The scan moves from the colophon on scan 3 directly into story text on scan 4. Because no printed contents page is present, the 34-story inventory is based on direct sequential visual inspection of the printed story-opening headings across scans **4–49**. No TOC wording has been invented.

## Pagination model

Across the story block, **PDF scan = printed page + 1**.

## Tamil source-processing state

- canonical story workspaces activated: **12 / 34**
- Tamil source processing complete: **12 / 34**
- Tamil source processing pending: **22 / 34**
- completed-story blocked / unresolved story text: **0**
- English translation for this collection: **not opened**

### Completed stories

| # | Story | Workspace | Verified source span | Tamil |
|---:|---|---|---|---|
| 1 | `வள்ளுவர் சொன்ன பொய்` | `stories/valluvar-sonna-poi/` | scan 4 → top scan 5 | PASS |
| 2 | `நீயும் கைதி - நானும் கைதி` | `stories/neeyum-kaithi-naanum-kaithi/` | scan 5 only | PASS |
| 3 | `குருவி ராமேஸ்வரம்` | `stories/kuruvi-rameswaram/` | scan 5 → scan 6 | PASS |
| 4 | `பெண்களுக்கு ஏன் - மீசை தாடியில்லை?` | `stories/pengalukku-en-meesai-thadiyillai/` | scan 6 → scan 11 | PASS |
| 5 | `கடலைத் தூர்ப்பது மிக எளிது` | `stories/kadalai-thoorppathu-miga-elithu/` | scan 11 → scan 13 | PASS |
| 6 | `மனைவி சொன்ன விளக்கம்` | `stories/manaivi-sonna-vilakkam/` | scan 13 → scan 14 | PASS |
| 7 | `நாதம் எழாது - நரம்புதான் அறும்` | `stories/naatham-ezhaathu-narambuthaan-arum/` | scan 14 → scan 15 | PASS |
| 8 | `அவள் சொன்னாள்` | `stories/aval-sonnaal/` | scan 15 only | PASS |
| 9 | `இருவரும் கூடியிருப்பது ஆத்தி மாலைதான்` | `stories/iruvarum-koodiyiruppathu-aathi-maalaithaan/` | scan 15 → scan 16 | PASS |
| 10 | `கொல்லப்பட வேண்டியது புலி, ஆனால்...` | `stories/kollappada-vendiyathu-puli-aanaal/` | scan 16 → scan 17 | PASS |
| 11 | `அந்தக் காலத்திலே!` | `stories/anthak-kaalathile/` | scan 17 only | PASS |
| 12 | `ஆண்டவன் தரிசனம் கொடுத்த ஊர்` | `stories/aandavan-dharisanam-kodutha-oor/` | scan 18 only | PASS |

The user-authorized 11-story iteration, Stories **2–12**, is therefore **11 / 11 source-complete**.

## Shared-page controls closed through Story 12

- scan **5 / printed 4**: Story 1 ending, complete Story 2, Story 3 opening;
- scan **6 / printed 5**: Story 3 ending, Story 4 opening;
- scan **11 / printed 10**: Story 4 ending, Story 5 opening;
- scan **13 / printed 12**: Story 5 ending, Story 6 opening;
- scan **14 / printed 13**: Story 6 ending, Story 7 opening;
- scan **15 / printed 14**: Story 7 ending, complete Story 8, Story 9 opening;
- scan **16 / printed 15**: Story 9 ending, Story 10 opening;
- scan **17 / printed 16**: Story 10 ending and complete Story 11;
- scan **18 / printed 17**: complete Story 12 followed by Story 13 opening.

## Canonical deduplication gate

Every remaining story still requires a fresh live-`main` exact-title / alternate-title / distinctive-content equivalence check before activation. Do not create placeholder story folders from the inventory.

## Next exact activity

Process **Story 13 — `வீரவாடி`**.

- opens: scan **18 / printed page 17**, below completed Story 12;
- next boundary witness: Story 14 **`சொர்க்கத்திற்கு வந்தது எப்படி?`** opens on scan **19 / printed page 18**.

Do not begin Story 13 until live `main` is fetched again and the canonical duplicate/content-equivalence check is complete.
