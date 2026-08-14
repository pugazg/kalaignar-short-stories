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

## Publication structure

1. Scan 1 — cover.
2. Scans 2–6 — reviews / publisher-editorial notes / author note.
3. Scans 7–22 — **கிழவன் கனவு** story body.
4. Scan 23 — printed **`பிழை திருத்தம்.`** table plus tobacco advertisement.
5. Scans 24–25 — commercial advertisements.
6. Scan 26 — back cover with a small child illustration.

## Current archival status

- Source manifest: **26 / 26 pages complete**
- Page records: **26 / 26**
- `verified`: **20**
- `blocked`: **4**
- `needs-review`: **2** — front matter scans 3–4 only
- `not-started`: **0**
- Story scans 7–22 directly audited: **16 / 16**
- Story scans `verified`: **12 / 16**
- Story scans `blocked`: **4 / 16**
- Story scans still awaiting Tamil review: **0**
- Final high-resolution unresolved-reading pass: **complete**
- Final assembled Tamil synchronization: **complete**
- Assembly consistency review: **PASS**
- English translation gate: **OPEN**
- English Batch 1 / scans 7–10: **SOURCE-REVIEWED**

Page-level status: [`indexes/page-map.md`](indexes/page-map.md).  
Tamil audit: [`audit.md`](audit.md).

## Final high-resolution findings

Three previously unresolved story pages were resolved and promoted to `verified`:

- scan **8 / printed 4** — `பூகோள பூரணர்த்திக`;
- scan **14 / printed 10** — `என் நெற்றியை?`, `திராட்சையைச் சாப்பிடேன்`, `மந்த காசத்தினிடையே`;
- scan **18 / printed 14** — `விட்டிருந்து`.

Four pages reached the limit of the supplied physical source and are formally `blocked`, not pending review:

- scan **15** — worn word + library-stamp-obscured temple-history text;
- scan **17** — one visually indistinct phrase after `பார்வதியை`;
- scan **21** — four visually indistinct historical/political readings;
- scan **22** — stamp-obscured final story phrase and footer/imprint.

Each unrecoverable story location is marked `blocked-by-source`; no hidden text is reconstructed from context, mythology, history or another edition.

## Final assembled Tamil reading layer

- [`sections/kizhavan-kanavu.md`](sections/kizhavan-kanavu.md) — synchronized final story assembly for scans 7–22;
- [`sections/kizhavan-kanavu-errata.md`](sections/kizhavan-kanavu-errata.md) — all 10 scan-23 corrections mapped separately;
- [`ASSEMBLY_REVIEW.md`](ASSEMBLY_REVIEW.md) — final assembly/source consistency review: **PASS**.

The assembled story contains all final scan-8/14/18 readings and the exact `blocked-by-source` markers from scans 15/17/21/22.

## English translation workspace

Translation-control files:

- [`translations/en/README.md`](translations/en/README.md)
- [`translations/en/TRANSLATION_PLAN.md`](translations/en/TRANSLATION_PLAN.md)
- [`translations/en/SOURCE_MAP.md`](translations/en/SOURCE_MAP.md)

Batch progress:

| Batch | Scans | Status |
|---:|---|---|
| 1 | 7–10 | **source-reviewed** |
| 2 | 11–14 | not-started |
| 3 | 15–18 | not-started |
| 4 | 19–22 | not-started |

Completed Batch 1:

- [`translations/en/batches/01-scans-07-10.md`](translations/en/batches/01-scans-07-10.md)
- source scans represented: **4 / 4**;
- blocked source gaps: **0**;
- direct Tamil-to-English source review: **PASS**;
- source-specific `வஸ்திராபரண` and `பூரணர்த்திக` were not silently regularized;
- scan 10's sentence continuation into scan 11 is explicitly marked rather than completed from outside Batch 1.

Every future `blocked-by-source` location must remain explicit in English and may not be guessed or smoothed over.

## Important source distinctions

- scan 7 opens the story, but its printed page number is not clearly visible; `(3)` is not inferred.
- scan 8 begins the visible numbered run at printed page `(4)`, continuing through scan 22 / printed page `(18)`.
- scan 13 / printed page 9 visibly reads **`வைத்திருந்தான்`**; scan 23's printed errata separately corrects this to **`வைத்திருந்தாள்`**.
- scan 23 is the verified printed errata layer plus tobacco advertisement.
- source PDF remains outside GitHub.

## Source-first rules

- Do not silently modernize spelling, punctuation, grammar, names or wording.
- Do not infer missing printed pagination.
- Treat library stamps, handwriting, illustrations and advertisements separately from printed story text.
- Do not reconstruct text hidden by stamps from context.
- Keep printed errata as a separate documented source layer.
- In English, preserve every `blocked-by-source` gap at the same textual position and do not invent missing wording.
- Do not upload the source PDF.

## Next exact activity

Begin **English Translation Batch 2 — scans 11–14 only**. Re-read those four finalized Tamil page records, translate the scan-10/11 mechanical continuation carefully, retain source-page markers, and complete direct source review before beginning Batch 3.
