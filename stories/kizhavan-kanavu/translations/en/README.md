# கிழவன் கனவு — English Translation Workspace

## Status

**FULL ENGLISH ASSEMBLY COMPLETE — EDITORIAL CONSISTENCY REVIEW: PASS**

The story-body English translation is now assembled across scans **7–22** after all four batches independently passed Tamil-to-English source review.

- Batch 1 — scans 7–10: **source-reviewed**
- Batch 2 — scans 11–14: **source-reviewed**
- Batch 3 — scans 15–18: **source-reviewed**
- Batch 4 — scans 19–22: **source-reviewed**
- Full English assembly: **complete**
- Editorial consistency review: **PASS**
- Release review/report: not started

English source-reviewed coverage: **16 / 16 story scans**.

## Translation basis

Primary Tamil source layer:

- `../../pages/0007-kizhavan-kanavu-01.md` through `../../pages/0022-kizhavan-kanavu-16.md`

Supporting Tamil/control layers:

- `../../sections/kizhavan-kanavu.md`
- `../../audit.md`
- `../../ASSEMBLY_REVIEW.md`
- `../../sections/kizhavan-kanavu-errata.md`

Workflow/control files:

- [`TRANSLATION_PLAN.md`](TRANSLATION_PLAN.md)
- [`SOURCE_MAP.md`](SOURCE_MAP.md)
- [`ERRATA_NOTES.md`](ERRATA_NOTES.md)
- [`EDITORIAL_CONSISTENCY_REVIEW.md`](EDITORIAL_CONSISTENCY_REVIEW.md)

## Story-source state

- scans in translation scope: **16 / 16** — scans 7–22
- Tamil `verified`: **12**
- Tamil `blocked`: **4 pages** — scans 15, 17, 21, 22
- Tamil story scans awaiting review: **0**
- explicit English `SOURCE BLOCKED` locations: **8**

A blocked Tamil reading remains explicitly blocked in English. No translation invents missing wording.

## Batch files

| Batch | Source scans | Source gaps | Status | File |
|---:|---|---:|---|---|
| 1 | 7–10 | 0 | **source-reviewed** | [`batches/01-scans-07-10.md`](batches/01-scans-07-10.md) |
| 2 | 11–14 | 0 | **source-reviewed** | [`batches/02-scans-11-14.md`](batches/02-scans-11-14.md) |
| 3 | 15–18 | 3 — scan 15 ×2; scan 17 ×1 | **source-reviewed** | [`batches/03-scans-15-18.md`](batches/03-scans-15-18.md) |
| 4 | 19–22 | 5 — scan 21 ×4; scan 22 ×1 | **source-reviewed** | [`batches/04-scans-19-22.md`](batches/04-scans-19-22.md) |

## Full English assembly

Final assembled reading file:

- [`kizhavan-kanavu-en.md`](kizhavan-kanavu-en.md)

Assembly checks:

- source scans represented: **16 / 16**;
- scan order: **7 → 22**;
- source/printed-page markers retained: **PASS**;
- duplicated source scan: **none**;
- omitted source scan: **none**;
- explicit `SOURCE BLOCKED` locations: **8 / 8**;
- scan-22 publisher/printer/footer material included in story prose: **No**;
- scan-23 publisher errata silently applied: **No**.

Mechanical cross-batch continuations were joined only in the assembled reading layer; the independently source-reviewed batch files remain unchanged.

## Editorial consistency review

[`EDITORIAL_CONSISTENCY_REVIEW.md`](EDITORIAL_CONSISTENCY_REVIEW.md) is **PASS**.

The review checked:

- recurring names and titles;
- religious/cultural terminology;
- political and caste/social vocabulary;
- narrative tense/voice;
- quotation/dialogue style;
- recurring metaphors;
- all 8 source-blocked positions;
- cross-page and cross-batch joins;
- scan-23 errata separation.

Editorial consistency did not become source normalization. Difficult verified forms remain deliberately conservative where the Tamil itself is unusual.

## Errata layer

[`ERRATA_NOTES.md`](ERRATA_NOTES.md) documents all **10** publisher corrections from scan 23 separately.

The key distinction remains:

- scan 13 archival page: `வைத்திருந்தான்`;
- scan 23 publisher errata: `வைத்திருந்தாள்`.

The English `had kept` does not expose that Tamil gender distinction, so the editorial note preserves it explicitly.

## Next exact activity — release gate

Create `RELEASE_REPORT.md` and perform Gate D release review. The report must document source range, Tamil source status, all 8 blocked passages, 10-entry errata treatment, conservative/unresolved translation choices, final file inventory, and confirmation that the source PDF is not stored in GitHub.

Do not remove or fill any `SOURCE BLOCKED` marker during release preparation.