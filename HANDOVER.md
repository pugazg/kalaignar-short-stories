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
- Final high-resolution unresolved-reading pass: **complete**
- Final assembled Tamil synchronization: **complete**
- Assembly consistency review: **PASS**
- English translation workflow: **initialized**
- English story prose drafted: **none yet**
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

`stories/kizhavan-kanavu/sections/kizhavan-kanavu.md` has been regenerated from the finalized page records.

Confirmed synchronization:

- scan 8 contains `பூகோள பூரணர்த்திக`;
- scan 14 contains `என் நெற்றியை?`, `திராட்சையைச் சாப்பிடேன்`, `மந்த காசத்தினிடையே`;
- scan 18 contains `விட்டிருந்து`;
- scans 15, 17, 21 and 22 carry the same explicit `blocked-by-source` markers as their page records;
- all 16 story scan markers occur in order;
- scan 22 publisher/printer footer is not included in the story assembly;
- scan 23 errata is not silently merged.

`ASSEMBLY_REVIEW.md` has been rerun and is now **PASS — FINAL TAMIL STORY ASSEMBLY SYNCHRONIZED**.

## Important archival rules / findings

1. **Do not reconstruct stamp-hidden words from context.**
2. **Do not silently modernize source forms.** Unusual forms confirmed during audit remain as printed.
3. **Do not infer scan 7 pagination.**
4. **Errata is a separate layer.** All 10 corrections from scan 23 remain separate from archival page readings and the assembled story.
5. **Scan 13 distinction:** page prints `வைத்திருந்தான்`; errata says `வைத்திருந்தாள்`.
6. **Advertisements/back cover are physical-source records, not story prose.**
7. **Source PDF remains outside GitHub.**
8. **`blocked` is a terminal source-condition status for this copy.** Do not repeatedly guess at those locations.

## English translation workflow

The translation plan is defined in:

`stories/kizhavan-kanavu/translations/en/TRANSLATION_PLAN.md`

Source-page/batch mapping is fixed in:

`stories/kizhavan-kanavu/translations/en/SOURCE_MAP.md`

Planned batches:

1. **Batch 1 — scans 7–10**
2. **Batch 2 — scans 11–14**
3. **Batch 3 — scans 15–18**
4. **Batch 4 — scans 19–22**

Mandatory translation rules:

- translate source-supported Tamil only;
- retain source scan markers in English;
- preserve each `blocked-by-source` gap at the same textual position;
- never invent English for missing Tamil;
- do not silently substitute scan 23 errata into archival translation prose;
- source-review each batch before beginning the next one.

## Next exact activity

Begin **English Translation Batch 1 — scans 7–10 only**.

1. Re-read final Tamil page records for scans 7, 8, 9 and 10.
2. Create `stories/kizhavan-kanavu/translations/en/batches/01-scans-07-10.md`.
3. Retain source-scan / printed-page markers.
4. Translate faithfully without modernization or expansion.
5. Compare the completed English batch directly against all four Tamil page records.
6. Mark the batch `source-reviewed` only after omissions, additions, names, rhetoric and page boundaries are checked.
7. Update translation workspace status and this handover.
8. Do **not** begin Batch 2 until Batch 1 source review passes.
