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
- Final high-resolution unresolved-reading pass: **complete**
- English translation gate: **conditionally open after assembled-text synchronization**

Page-level status: [`indexes/page-map.md`](indexes/page-map.md).  
Tamil audit: [`audit.md`](audit.md).

## Final high-resolution findings

Three previously unresolved story pages were resolved and promoted to `verified`:

- scan **8 / printed 4** — `பூகோள பூரணர்த்திக`;
- scan **14 / printed 10** — `என் நெற்றியை?`, `திராட்சையைச் சாப்பிடேன்`, `மந்த காசத்தினிடையே` and the corrected opening readings;
- scan **18 / printed 14** — `விட்டிருந்து`.

Four pages reached the limit of the supplied physical source and are now formally `blocked`, not left in an indefinite review state:

- scan **15** — worn word + library-stamp-obscured temple-history text;
- scan **17** — one visually indistinct phrase after `பார்வதியை`;
- scan **21** — four visually indistinct historical/political readings;
- scan **22** — stamp-obscured final story phrase and footer/imprint.

Each unrecoverable location is marked `blocked-by-source`; no hidden text is reconstructed from context or another edition.

## Assembled Tamil reading layer

Existing derived files:

- [`sections/kizhavan-kanavu.md`](sections/kizhavan-kanavu.md) — scans 7–22 assembled in source order;
- [`sections/kizhavan-kanavu-errata.md`](sections/kizhavan-kanavu-errata.md) — all 10 scan-23 corrections mapped separately;
- [`ASSEMBLY_REVIEW.md`](ASSEMBLY_REVIEW.md) — consistency review.

The page records are currently the finalized source layer. The assembled story file still needs a synchronization pass to incorporate the three newly resolved readings and convert the four terminal unresolved locations to `blocked-by-source` markers.

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
- Do not upload the source PDF.

## Next exact activity

Synchronize `sections/kizhavan-kanavu.md` and `ASSEMBLY_REVIEW.md` with the finalized page records. Once that consistency check passes, create the English translation workflow/plan with strict preservation of every `blocked-by-source` gap.
