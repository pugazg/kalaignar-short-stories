# கிழவன் கனவு

கலைஞர் மு. கருணாநிதியின் **கிழவன் கனவு** என்ற சிறுகதைப் பதிப்பை supplied source scan-ஐ controlling source ஆகக் கொண்டு page-by-page மின்னாக்கும் archival work folder.

## Source snapshot

- Title as printed: **கிழவன் கனவு**
- Authorship line: **தீட்டியவர்: மு. கருணாநிதி.**
- Edition statement on cover: **இரண்டாம் பதிப்பு.**
- Scan pages: **26**
- Source PDF stored in repository: **No**
- SHA-256: `cdea0e1c0d2ad657fc4163ed77c58027c18abbe58058221be7f32724b7ef8121`

Full source registration: [`metadata/source.md`](metadata/source.md).

## Current archival status

- Source manifest: **26 / 26 pages complete**
- Page records: **26 / 26**
- `verified`: **20**
- `blocked`: **4**
- `needs-review`: **2** — front matter scans 3–4 only
- Story scans 7–22 directly audited: **16 / 16**
- Story scans `verified`: **12 / 16**
- Story scans `blocked`: **4 / 16**
- Story scans still awaiting Tamil review: **0**
- Final assembled Tamil synchronization: **complete**
- Assembly consistency review: **PASS**
- English source-reviewed coverage: **16 / 16 story scans**
- English source batches completed: **4 / 4**

Page-level status: [`indexes/page-map.md`](indexes/page-map.md).  
Tamil audit: [`audit.md`](audit.md).

## Final Tamil layer

- [`sections/kizhavan-kanavu.md`](sections/kizhavan-kanavu.md) — synchronized story assembly for scans 7–22;
- [`sections/kizhavan-kanavu-errata.md`](sections/kizhavan-kanavu-errata.md) — all 10 scan-23 publisher corrections kept separately;
- [`ASSEMBLY_REVIEW.md`](ASSEMBLY_REVIEW.md) — final Tamil consistency review: **PASS**.

The four terminal source-limited story pages remain scans **15, 17, 21 and 22**. Their gaps are explicit and have not been reconstructed.

## English translation workspace

Control files:

- [`translations/en/README.md`](translations/en/README.md)
- [`translations/en/TRANSLATION_PLAN.md`](translations/en/TRANSLATION_PLAN.md)
- [`translations/en/SOURCE_MAP.md`](translations/en/SOURCE_MAP.md)

All four translation batches are now **source-reviewed**:

| Batch | Scans | Status |
|---:|---|---|
| 1 | 7–10 | **source-reviewed** |
| 2 | 11–14 | **source-reviewed** |
| 3 | 15–18 | **source-reviewed** |
| 4 | 19–22 | **source-reviewed** |

Batch files:

- [`translations/en/batches/01-scans-07-10.md`](translations/en/batches/01-scans-07-10.md)
- [`translations/en/batches/02-scans-11-14.md`](translations/en/batches/02-scans-11-14.md)
- [`translations/en/batches/03-scans-15-18.md`](translations/en/batches/03-scans-15-18.md)
- [`translations/en/batches/04-scans-19-22.md`](translations/en/batches/04-scans-19-22.md)

Across Batches 3–4, **8 explicit SOURCE BLOCKED story locations** are preserved: scan 15 ×2, scan 17 ×1, scan 21 ×4, scan 22 ×1. No missing Tamil was reconstructed from context or outside knowledge.

Batch 4 also excludes scan 22's publisher/printer/footer material from English story prose, while preserving the final source-blocked story phrase in place.

## Important source distinctions

- scan 7 printed page is not inferred;
- scan 13 visible `வைத்திருந்தான்` and scan-23 errata `வைத்திருந்தாள்` remain distinct;
- scan 23 remains a separate publisher errata layer;
- source PDF remains outside GitHub;
- source-blocked text remains terminal for this copy unless a genuinely clearer source is later introduced.

## Next exact activity

Assemble all four source-reviewed English batches into `translations/en/kizhavan-kanavu-en.md`. Preserve all 16 source-page markers and all 8 source-blocked positions, remove only batch scaffolding/duplicate boundary notes, and then perform a full English editorial/source consistency review before release.