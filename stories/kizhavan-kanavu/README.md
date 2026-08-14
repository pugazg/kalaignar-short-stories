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
- Story scans 7–22 directly audited: **16 / 16**
- Story scans `verified`: **12 / 16**
- Story scans `blocked`: **4 / 16**
- Story scans still awaiting Tamil review: **0**
- Final assembled Tamil synchronization: **complete**
- Assembly consistency review: **PASS**
- English translation gate: **OPEN**
- English source-reviewed coverage: **12 / 16 story scans**

Page-level status: [`indexes/page-map.md`](indexes/page-map.md).  
Tamil audit: [`audit.md`](audit.md).

## Final assembled Tamil reading layer

- [`sections/kizhavan-kanavu.md`](sections/kizhavan-kanavu.md) — synchronized final story assembly for scans 7–22;
- [`sections/kizhavan-kanavu-errata.md`](sections/kizhavan-kanavu-errata.md) — all 10 scan-23 corrections mapped separately;
- [`ASSEMBLY_REVIEW.md`](ASSEMBLY_REVIEW.md) — final assembly/source consistency review: **PASS**.

Four terminal source gaps remain only because the supplied physical copy cannot expose them safely: scans **15, 17, 21 and 22**. Each is marked `blocked-by-source`; no context, mythology, historical memory or later edition is used to reconstruct hidden wording.

## English translation workspace

Control files:

- [`translations/en/README.md`](translations/en/README.md)
- [`translations/en/TRANSLATION_PLAN.md`](translations/en/TRANSLATION_PLAN.md)
- [`translations/en/SOURCE_MAP.md`](translations/en/SOURCE_MAP.md)

Batch progress:

| Batch | Scans | Status |
|---:|---|---|
| 1 | 7–10 | **source-reviewed** |
| 2 | 11–14 | **source-reviewed** |
| 3 | 15–18 | **source-reviewed** |
| 4 | 19–22 | not-started |

Completed batches:

- [`translations/en/batches/01-scans-07-10.md`](translations/en/batches/01-scans-07-10.md)
- [`translations/en/batches/02-scans-11-14.md`](translations/en/batches/02-scans-11-14.md)
- [`translations/en/batches/03-scans-15-18.md`](translations/en/batches/03-scans-15-18.md)

Batch 3 is the first translated segment containing terminal source gaps. It preserves **three separate SOURCE BLOCKED locations**: two on scan 15 and one on scan 17. Verified scans 16 and 18 were translated without smoothing over those gaps, and the scan-18/19 continuation remains explicit for Batch 4.

## Important source distinctions

- scan 7 opens the story, but its printed page number is not clearly visible; `(3)` is not inferred.
- scan 13 / printed page 9 visibly reads **`வைத்திருந்தான்`**; scan 23's printed errata separately corrects this to **`வைத்திருந்தாள்`**.
- scan 15 contains one worn word and one library-stamp-obscured story segment; both remain explicit in English.
- scan 17 contains one worn/indistinct phrase after `பார்வதியை`; it remains explicit in English.
- scan 21 will require four distinct source-block markers in Batch 4.
- scan 22 will require one source-block marker in the final story sentence; its publisher/printer footer stays outside English story prose.
- scan 23 remains a separate publisher errata layer.
- source PDF remains outside GitHub.

## Source-first rules

- Do not silently modernize spelling, punctuation, grammar, names or wording.
- Do not reconstruct text hidden by stamps from context.
- Keep printed errata as a separate documented source layer.
- In English, preserve every `blocked-by-source` gap at the same textual position and do not invent missing wording.
- Do not upload the source PDF.

## Next exact activity

Begin **English Translation Batch 4 — scans 19–22 only**. Complete the scan-18/19 continuation, preserve all four scan-21 source gaps separately and the scan-22 final-story gap explicitly, exclude scan-22 footer/imprint from story prose, retain page markers, and complete direct source review before assembling the full English story.