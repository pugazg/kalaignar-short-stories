# கிழவன் கனவு — English Translation Workspace

## Status

**All four source batches — scans 7–22: SOURCE-REVIEWED.**

The final Tamil story assembly has passed consistency review, and the controlled English translation is now source-reviewed across the complete story body.

- Batch 1 — scans 7–10: **source-reviewed**
- Batch 2 — scans 11–14: **source-reviewed**
- Batch 3 — scans 15–18: **source-reviewed**
- Batch 4 — scans 19–22: **source-reviewed**

English source-reviewed coverage: **16 / 16 story scans**.

## Translation basis

Primary source layer:

- `../../pages/0007-kizhavan-kanavu-01.md` through `../../pages/0022-kizhavan-kanavu-16.md`

Supporting control layers:

- `../../sections/kizhavan-kanavu.md`
- `../../audit.md`
- `../../ASSEMBLY_REVIEW.md`
- `../../sections/kizhavan-kanavu-errata.md`

Workflow rules:

- [`TRANSLATION_PLAN.md`](TRANSLATION_PLAN.md)
- [`SOURCE_MAP.md`](SOURCE_MAP.md)

## Story-source state

- scans in translation scope: **16 / 16** — scans 7–22
- `verified`: **12**
- `blocked-by-source`: **4 pages** — scans 15, 17, 21, 22
- story scans awaiting Tamil review: **0**

A blocked Tamil reading remains explicitly blocked in English. No translation invents missing wording.

## Batch progress

| Batch | Source scans | Source gaps | Status | File |
|---:|---|---:|---|---|
| 1 | 7–10 | 0 | **source-reviewed** | [`batches/01-scans-07-10.md`](batches/01-scans-07-10.md) |
| 2 | 11–14 | 0 | **source-reviewed** | [`batches/02-scans-11-14.md`](batches/02-scans-11-14.md) |
| 3 | 15–18 | **3 locations** — scan 15 ×2; scan 17 ×1 | **source-reviewed** | [`batches/03-scans-15-18.md`](batches/03-scans-15-18.md) |
| 4 | 19–22 | **5 locations** — scan 21 ×4; scan 22 ×1 | **source-reviewed** | [`batches/04-scans-19-22.md`](batches/04-scans-19-22.md) |

Total explicit story-source gaps preserved across the English batches: **8 locations**.

## Batch 4 source-review result

**PASS**

Checks completed against finalized Tamil scans **19, 20, 21 and 22**:

- scans represented: **4 / 4** and in source order;
- printed-page markers preserved;
- scan-18/19 continuation completed without changing Batch 3;
- verified scans 19 and 20 represented without omission;
- scan-20/21 and scan-21/22 mechanical continuations preserved;
- scan 21 source gaps: **4 / 4 preserved separately**;
- scan 22 final-story source gap: **1 / 1 preserved at the exact textual position**;
- total Batch 4 `SOURCE BLOCKED` locations: **5 / 5**;
- no historical names, slogans, punishments or phrases supplied from outside knowledge to fill blocked Tamil;
- scan-22 publisher/printer/footer material excluded from English story prose;
- publisher errata silently applied: **No**.

## Full-English assembly gate

**OPEN.**

All four batches have independently passed direct Tamil-to-English source review. The next derived file may now be created:

`kizhavan-kanavu-en.md`

Assembly must:

- preserve all 16 source-scan markers in order;
- join only mechanical cross-batch continuations without altering source meaning;
- preserve all **8** `SOURCE BLOCKED` locations;
- avoid duplicate text at batch boundaries;
- keep scan 23 publisher errata separate;
- exclude scan-22 publisher/printer/footer material from story prose.

## Next exact activity

Assemble the four source-reviewed batch files into `kizhavan-kanavu-en.md`, then perform a full cross-batch editorial/source consistency review before any release report or polished edition is created.