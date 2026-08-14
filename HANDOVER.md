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

Derived Tamil layer:

- `stories/kizhavan-kanavu/sections/kizhavan-kanavu.md`
- `stories/kizhavan-kanavu/sections/kizhavan-kanavu-errata.md`

## Current status

- Source registered: **yes**
- 26-page manifest: **complete**
- Page records: **26 / 26**
- `verified`: **17**
- `needs-review`: **9**
- `not-started`: **0**
- Story-body direct visual transcription: **complete**
- Tamil source audit: **complete with seven genuine unresolved story pages**
- Story assembly: **complete — scans 7–22 / 16 pages represented**
- Printed errata mapping: **10 / 10 entries**
- Assembly consistency review: **complete**
- English translation: **blocked**

## Verified story scans

**7, 9, 10, 11, 12, 13, 16, 19, 20**

Scan 13 was reconciled after audit and is now verified. Its visible page reading **`வைத்திருந்தான்`** is preserved. Scan 23 separately gives publisher correction **`வைத்திருந்தாள்`**.

## Remaining story `needs-review` scans

1. **scan 8 / printed 4** — one unclear word after `பூகோள`.
2. **scan 14 / printed 10** — two short unclear readings in the dream passage.
3. **scan 15 / printed 11** — one unclear word plus large library-stamp obstruction over temple-history text.
4. **scan 17 / printed 13** — one short phrase after `பார்வதியை` is unclear.
5. **scan 18 / printed 14** — one short opening phrase is unclear.
6. **scan 21 / printed 17** — four short political/historical readings remain unclear.
7. **scan 22 / printed 18** — library stamp obscures part of the story conclusion and footer.

Front matter scans **3–4** also remain `needs-review` because of source-condition issues.

## Important archival rules / findings

1. **Do not reconstruct stamp-hidden words from context.**
2. **Do not silently modernize source forms.** Unusual forms confirmed during audit remain as printed.
3. **Do not infer scan 7 pagination.**
4. **Errata is a separate layer.** All 10 corrections from scan 23 are mapped in `sections/kizhavan-kanavu-errata.md` and are not silently applied to `pages/` or the assembled archival reading text.
5. **Scan 13 distinction:** page prints `வைத்திருந்தான்`; errata says `வைத்திருந்தாள்`.
6. **Advertisements/back cover are physical-source records, not story prose.**
7. **Source PDF remains outside GitHub.**

## Assembly consistency review result

`ASSEMBLY_REVIEW.md` records:

- scans 7–22 present in source order: **PASS**
- source-page trace markers: **PASS**
- unresolved markers preserved: **PASS**
- printed errata kept separate: **PASS**
- advertisements excluded from story assembly: **PASS**
- translation gate: **NOT YET OPEN**

## Next exact activity

Perform a **final high-resolution unresolved-reading pass** on scans **8, 14, 15, 17, 18, 21 and 22**.

1. Re-open the highest-quality supplied page images/crops.
2. Revisit only the explicit unresolved locations.
3. Resolve a reading only when the scan itself supports it with source-faithful confidence.
4. Do not use another edition, web text or historical knowledge unless deliberately introduced as a separately documented secondary source.
5. Anything still hidden by library stamps or genuinely illegible after this pass must be formally classified as **source-blocked** in the page record/audit rather than guessed.
6. Update `page-map.md`, `audit.md`, story/root README and this handover.
7. Re-run the translation gate after source-block classification.
8. Do **not** start English translation unless the gate is explicitly opened.
