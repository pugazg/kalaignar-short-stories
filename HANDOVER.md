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
- scan 24 — `ராஜேந்திரா நைஸ் புகையிலை` advertisement
- scan 25 — `தியாகராஜ விலாஸ்` advertisement / portrait
- scan 26 — back cover / small child illustration / no readable printed text

Visible story pagination:

- scan 7 — printed page not clearly visible; keep `—`, do not infer `(3)`
- scan 8 = `(4)`
- sequentially through scan 22 = `(18)`

## Core files

Root:

- `README.md`
- `SHORT_STORY_PROCESSING_GUIDE.md`
- `HANDOVER.md`

Story control:

- `stories/kizhavan-kanavu/README.md`
- `stories/kizhavan-kanavu/metadata/source.md`
- `stories/kizhavan-kanavu/indexes/page-map.md`
- `stories/kizhavan-kanavu/audit.md`
- `stories/kizhavan-kanavu/ASSEMBLY_REVIEW.md`

Page records:

- scans 1–26: complete under `stories/kizhavan-kanavu/pages/`

Final Tamil derived layer:

- `stories/kizhavan-kanavu/sections/kizhavan-kanavu.md`
- `stories/kizhavan-kanavu/sections/kizhavan-kanavu-errata.md`

English translation control layer:

- `stories/kizhavan-kanavu/translations/en/README.md`
- `stories/kizhavan-kanavu/translations/en/TRANSLATION_PLAN.md`
- `stories/kizhavan-kanavu/translations/en/SOURCE_MAP.md`

English translation batches:

- `stories/kizhavan-kanavu/translations/en/batches/01-scans-07-10.md` — **source-reviewed**
- `stories/kizhavan-kanavu/translations/en/batches/02-scans-11-14.md` — **source-reviewed**

## Current status

- Source registered: **yes**
- 26-page manifest: **complete**
- Page records: **26 / 26**
- `verified`: **20**
- `blocked`: **4**
- `needs-review`: **2** — front matter scans 3–4 only
- `not-started`: **0**
- Story scans directly audited: **16 / 16**
- Story scans `verified`: **12 / 16**
- Story scans `blocked`: **4 / 16**
- Story scans awaiting Tamil review: **0**
- Printed errata mapping: **10 / 10 entries**
- Final assembled Tamil synchronization: **complete**
- Assembly consistency review: **PASS**
- English translation workflow: **active**
- English Batch 1 / scans 7–10: **SOURCE-REVIEWED**
- English Batch 2 / scans 11–14: **SOURCE-REVIEWED**
- English Batch 3 / scans 15–18: **not-started**
- English Batch 4 / scans 19–22: **not-started**
- English source-reviewed coverage: **8 / 16 story scans**
- Translation gate: **OPEN**

## Final story scan dispositions

### Verified story scans

**7, 8, 9, 10, 11, 12, 13, 14, 16, 18, 19, 20**

Final-pass resolutions include:

- scan 8: `பூகோள பூரணர்த்திக`
- scan 14: `என் நெற்றியை?`, `திராட்சையைச் சாப்பிடேன்`, `மந்த காசத்தினிடையே`
- scan 18: `விட்டிருந்து`

Scan 13 remains the important page/errata distinction: visible page **`வைத்திருந்தான்`**; scan 23 publisher errata **`வைத்திருந்தாள்`**.

### Source-blocked story scans

1. **scan 15 / printed 11** — one worn/indistinct word plus temple-history text physically obscured by a circular library stamp.
2. **scan 17 / printed 13** — one short phrase following `பார்வதியை` remains visually indistinct.
3. **scan 21 / printed 17** — four short political/historical readings remain visually indistinct.
4. **scan 22 / printed 18** — library stamp obscures part of the final story phrase and footer/imprint material.

These pages are fully audited. Their unrecoverable story locations are explicitly labelled `blocked-by-source`; they must not return to generic `needs-review` unless a genuinely clearer source copy is introduced.

Front-matter scans **3–4** remain `needs-review` because of separate source-condition issues. They are outside the current story-body translation layer.

## Final Tamil assembly result

`stories/kizhavan-kanavu/sections/kizhavan-kanavu.md` is synchronized with the finalized page records.

Confirmed:

- all 16 story scan markers occur once and in order;
- scan 8/14/18 final readings are incorporated;
- scans 15/17/21/22 carry explicit `blocked-by-source` markers;
- scan 22 publisher/printer footer is excluded from the story assembly;
- scan 23 errata is not silently merged.

`ASSEMBLY_REVIEW.md` is **PASS — FINAL TAMIL STORY ASSEMBLY SYNCHRONIZED**.

## English translation workflow

The translation plan is defined in:

`stories/kizhavan-kanavu/translations/en/TRANSLATION_PLAN.md`

Source-page/batch mapping is fixed in:

`stories/kizhavan-kanavu/translations/en/SOURCE_MAP.md`

Batch progress:

1. **Batch 1 — scans 7–10 — SOURCE-REVIEWED**
2. **Batch 2 — scans 11–14 — SOURCE-REVIEWED**
3. **Batch 3 — scans 15–18 — not-started**
4. **Batch 4 — scans 19–22 — not-started**

### Batch 1 result

- source scans represented: **4 / 4**
- source-blocked locations: **0**
- source-page order/markers: **PASS**
- source-specific `வஸ்திராபரண` / `பூரணர்த்திக`: not silently normalized
- scan-10 continuation into scan 11: explicitly marked

### Batch 2 result

File:

`stories/kizhavan-kanavu/translations/en/batches/02-scans-11-14.md`

Source review was completed directly against scans **11, 12, 13 and 14**.

- source scans represented: **4 / 4**
- source order / printed-page markers: **PASS**
- source-blocked locations: **0**
- scan-10/11 continuation: completed without rewriting Batch 1
- scan-14/15 continuation: explicitly marked without importing Batch 3 text
- scan-13 `வைத்திருந்தான்` vs printed errata `வைத்திருந்தாள்`: documented explicitly; no silent substitution
- scan-14 verified unusual wording: translated conservatively and noted
- publisher errata silently substituted: **No**

Mandatory translation rules remain:

- translate source-supported Tamil only;
- retain source scan markers in English;
- preserve every `blocked-by-source` gap at the same textual position;
- never invent English for missing Tamil;
- do not silently substitute scan 23 errata into archival translation prose;
- source-review each batch before beginning the next one.

## Next exact activity

Begin **English Translation Batch 3 — scans 15–18 only**.

1. Re-read final Tamil page records for scans 15, 16, 17 and 18.
2. Create `stories/kizhavan-kanavu/translations/en/batches/03-scans-15-18.md`.
3. Complete the scan-14/15 continuation without altering Batch 2.
4. Preserve **both** scan-15 source-blocked locations explicitly in English.
5. Preserve the scan-17 source-blocked phrase explicitly at its exact textual position.
6. Translate verified scans 16 and 18 without smoothing over source gaps.
7. Retain all source-scan / printed-page markers.
8. Complete direct Tamil-to-English source review across all four pages.
9. Do **not** begin Batch 4 until Batch 3 passes.
