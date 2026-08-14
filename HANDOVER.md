# HANDOVER — Kalaignar Short Stories Archive

## Repository

- Repository: `pugazg/kalaignar-short-stories`
- Default branch: `main`
- Permanent workflow guide: `SHORT_STORY_PROCESSING_GUIDE.md`
- Source PDFs are **not** committed to the repository.

## Current story

- Work slug: `kizhavan-kanavu`
- Title as printed: **கிழவன் கனவு**
- Author line as printed: **தீட்டியவர்: மு. கருணாநிதி.**
- Edition statement: **இரண்டாம் பதிப்பு.**
- Source filename: `TVA_BOK_0014165_கிழவன்_கனவு.pdf`
- SHA-256: `cdea0e1c0d2ad657fc4163ed77c58027c18abbe58058221be7f32724b7ef8121`
- File size: **11,017,627 bytes**
- Scan pages: **26**

## Source structure

- scan 1 — cover
- scans 2–6 — reviews / publisher-editorial material / author note
- scans 7–22 — `கிழவன் கனவு` story body
- scan 23 — **`பிழை திருத்தம்.`** errata table + tobacco advertisement
- scan 24 — advertisement
- scan 25 — advertisement / portrait
- scan 26 — back cover

Visible story pagination:

- scan 7 — printed page not clearly visible; keep `—`, do not infer `(3)`
- scan 8 = `(4)`
- sequentially through scan 22 = `(18)`

## Current Tamil source state

- Source registered: **yes**
- Page records: **26 / 26**
- Whole-publication status: **20 verified / 4 blocked / 2 front-matter needs-review / 0 not-started**
- Story scans directly audited: **16 / 16**
- Story scans `verified`: **12 / 16**
- Story scans `blocked`: **4 / 16** — scans 15, 17, 21, 22
- Story scans awaiting Tamil review: **0**
- Printed errata mapping: **10 / 10 entries**
- Final Tamil assembly: **complete and synchronized**
- `ASSEMBLY_REVIEW.md`: **PASS**

Tamil control/derived files:

- `stories/kizhavan-kanavu/pages/`
- `stories/kizhavan-kanavu/sections/kizhavan-kanavu.md`
- `stories/kizhavan-kanavu/sections/kizhavan-kanavu-errata.md`
- `stories/kizhavan-kanavu/audit.md`
- `stories/kizhavan-kanavu/ASSEMBLY_REVIEW.md`

## English translation state

Translation control files:

- `stories/kizhavan-kanavu/translations/en/README.md`
- `stories/kizhavan-kanavu/translations/en/TRANSLATION_PLAN.md`
- `stories/kizhavan-kanavu/translations/en/SOURCE_MAP.md`

All four source batches are now **SOURCE-REVIEWED**:

1. `batches/01-scans-07-10.md` — scans 7–10
2. `batches/02-scans-11-14.md` — scans 11–14
3. `batches/03-scans-15-18.md` — scans 15–18
4. `batches/04-scans-19-22.md` — scans 19–22

English source-reviewed coverage: **16 / 16 story scans**.

### Explicit English source gaps

There are **8 terminal SOURCE BLOCKED story locations** across the four batches:

- scan 15 — **2**
- scan 17 — **1**
- scan 21 — **4**
- scan 22 — **1**

These are preserved at their exact source positions and must remain visible in every assembled/release English layer unless a genuinely clearer source copy is introduced.

## Batch 4 result

File:

`stories/kizhavan-kanavu/translations/en/batches/04-scans-19-22.md`

Direct source review was completed against the finalized Tamil page records for scans **19, 20, 21 and 22**.

Confirmed:

- scans represented: **4 / 4**;
- scan order / printed-page markers: **PASS**;
- scan-18/19 continuation: completed without rewriting Batch 3;
- scans 19 and 20: represented without omission;
- scan-20/21 continuation: preserved;
- scan 21 blocked readings: **4 / 4 preserved separately**;
- scan 22 final-story blocked reading: **1 / 1 preserved**;
- scan-21/22 continuation: preserved;
- no blocked wording reconstructed from historical knowledge, context, another edition, likely slogans or web text;
- scan-22 publisher/printer/footer material: **excluded from English story prose**;
- publisher errata silently substituted: **No**.

Batch 4 translator notes also preserve conservative treatment of unusual verified source forms and historical/political rhetoric rather than silently normalizing them.

## Permanent archival rules

1. **The supplied scan is the controlling source for this edition.**
2. Do not reconstruct stamp-hidden or worn text from context.
3. Do not silently modernize unusual source forms.
4. Do not infer scan 7 pagination.
5. Keep scan 23 publisher errata as a separate layer.
6. Scan 13 visible `வைத்திருந்தான்` and errata `வைத்திருந்தாள்` remain distinct.
7. Advertisements, library marks and printer/footer matter are separate from story prose.
8. Source PDF stays outside GitHub.
9. In English, every SOURCE BLOCKED marker must remain explicit and in position.

## Next exact activity

Create the full assembled English story:

`stories/kizhavan-kanavu/translations/en/kizhavan-kanavu-en.md`

Procedure:

1. Use only the four **source-reviewed** batch files as the English input layer.
2. Represent scans **7–22 exactly once and in order**.
3. Preserve all source-scan / printed-page HTML markers.
4. Join mechanical cross-batch sentence continuations carefully, removing only editorial batch-boundary scaffolding—not source meaning.
5. Preserve all **8 SOURCE BLOCKED** positions exactly.
6. Do not import scan-22 publisher/printer/footer material.
7. Do not silently apply scan-23 errata.
8. After assembly, create/run `EDITORIAL_CONSISTENCY_REVIEW.md` and verify completeness, names, terminology, blocked-marker count, cross-page joins and source traceability.
9. Do not create `RELEASE_REPORT.md` until the assembled English review passes.