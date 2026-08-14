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

## Current status after final unresolved-reading pass

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
- Printed errata mapping: **10 / 10 entries**
- Final high-resolution unresolved-reading pass: **complete**
- English translation gate: **conditionally open only after assembled-text synchronization**

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

These pages are fully audited. Their unresolved locations are now explicitly labelled `blocked-by-source`; they must not return to generic `needs-review` unless a genuinely clearer source copy is introduced.

Front-matter scans **3–4** remain `needs-review` because of separate source-condition issues. They are outside the story-body translation layer.

## Important archival rules / findings

1. **Do not reconstruct stamp-hidden words from context.**
2. **Do not silently modernize source forms.** Unusual forms confirmed during audit remain as printed.
3. **Do not infer scan 7 pagination.**
4. **Errata is a separate layer.** All 10 corrections from scan 23 are mapped in `sections/kizhavan-kanavu-errata.md` and are not silently applied to archival page records.
5. **Scan 13 distinction:** page prints `வைத்திருந்தான்`; errata says `வைத்திருந்தாள்`.
6. **Advertisements/back cover are physical-source records, not story prose.**
7. **Source PDF remains outside GitHub.**
8. **`blocked` is a terminal source-condition status for this copy.** Do not repeatedly guess at those locations.

## Assembled Tamil layer status

The existing `sections/kizhavan-kanavu.md` was assembled before the final high-resolution pass. It still needs synchronization with the finalized page records:

- scan 8 unresolved marker → `பூரணர்த்திக`
- scan 14 old unresolved/provisional readings → finalized high-resolution readings
- scan 18 unresolved marker → `விட்டிருந்து`
- scans 15, 17, 21, 22 unresolved markers → explicit `blocked-by-source` wording

Until that synchronization is complete, **page records are the authoritative current Tamil source layer**.

`ASSEMBLY_REVIEW.md` must then be rerun/updated against the synchronized assembly.

## Translation gate

The story-body audit itself is complete to the limit of the supplied source. Translation may be opened **after assembly synchronization and consistency review pass**, with strict rules:

- translate source-supported Tamil only;
- retain every `blocked-by-source` gap explicitly;
- do not infer missing Tamil in English;
- keep printed errata separately documented rather than silently rewriting the archival source.

## Next exact activity

Synchronize the assembled Tamil layer and re-run its consistency review.

1. Update `stories/kizhavan-kanavu/sections/kizhavan-kanavu.md` from the finalized page records.
2. Preserve scan boundaries and source pagination markers.
3. Incorporate the resolved scan 8/14/18 readings exactly.
4. Convert terminal gaps on scans 15/17/21/22 to `blocked-by-source` markers exactly matching the page records.
5. Do not silently apply scan 23 errata.
6. Update `ASSEMBLY_REVIEW.md` and verify page-record ↔ assembly ↔ errata consistency.
7. Only after that PASS, create the English translation plan/workflow. Do not start translating prose before the synchronization check is complete.
