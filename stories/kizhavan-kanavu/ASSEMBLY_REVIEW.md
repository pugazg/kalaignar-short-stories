# Assembly consistency review — கிழவன் கனவு

## Scope

Reviewed artifacts:

- `sections/kizhavan-kanavu.md`
- `sections/kizhavan-kanavu-errata.md`
- page records `pages/0007-...` through `pages/0023-...`
- `audit.md`
- `indexes/page-map.md`

The controlling source remains the supplied scan `TVA_BOK_0014165_கிழவன்_கனவு.pdf`.

## Assembly coverage

**PASS**

- Story body begins at scan **7**.
- Story body concludes at scan **22**.
- All **16** story scan pages are represented in order in `sections/kizhavan-kanavu.md`.
- Each source page boundary is retained as an HTML source marker so the assembled text remains traceable to the archival page layer.
- Scan **23** errata/advertisement text is not merged into the story body.
- Scans **24–26** advertisements/back cover are not merged into the story body.

## Source fidelity

**PASS WITH EXPLICIT LIMITATIONS**

The assembled text follows the audited page records without modernizing spelling, grammar, punctuation, names or unusual historical forms. Mechanical page continuations are not silently rewritten into a normalized edition.

Unresolved source readings remain visible in the assembled text at the same locations as the archival pages:

| Scan | Printed page | Remaining issue in assembled text |
|---:|---:|---|
| 8 | 4 | one unclear word after `பூகோள` |
| 14 | 10 | two short unclear readings in the dream passage |
| 15 | 11 | one unclear word plus library-stamp-obscured temple-history text |
| 17 | 13 | one short unclear phrase after `பார்வதியை` |
| 18 | 14 | one short unclear reading in the opening paragraph |
| 21 | 17 | four short unclear readings in the political/historical catalogue |
| 22 | 18 | library stamp obscures part of the final story conclusion |

No external edition, web transcription or contextual reconstruction was used to fill these gaps.

## Scan 13 reconciliation

**PASS**

Scan **13 / printed page 9** was reconciled after the first audit report. The archival page now preserves source-supported readings including:

- `காப்பாத்து`
- `கரகமும் கப்பரையும்`
- `பனிரெண்டு`
- `தழுவிக்கொண்டன`
- `ஆலிங்கனம்`

The visible page reading remains **`வைத்திருந்தான்`**. The publisher's printed errata separately gives **`வைத்திருந்தாள்`**. This distinction is correctly maintained in both the page record and the assembled/errata layers.

## Errata-layer consistency

**PASS**

`sections/kizhavan-kanavu-errata.md` contains all **10** corrections printed on scan 23 and maps each printed page to its corresponding scan/page record.

The errata is not silently applied to `sections/kizhavan-kanavu.md`. This preserves two explicit layers:

1. archival page reading;
2. publisher's printed correction.

## Page-order and pagination consistency

**PASS**

- scan 7 retains printed page `—`; `(3)` is not inferred.
- scan 8 = printed page `(4)`.
- sequence continues through scan 22 = printed page `(18)`.
- assembled order follows scan 7 → scan 22 without omission or duplication.

## Repository-policy consistency

**PASS**

- Source PDF is not committed to the repository.
- Page records remain the primary archival layer.
- Assembled text is clearly labelled as a derived reading layer, not a replacement for page records.
- Errata remains separate.
- Advertisements and physical-copy marks are not silently mixed into story prose.

## Translation gate

**NOT YET OPEN**

The assembled Tamil layer is now structurally complete and internally consistent, but English translation should remain blocked because seven story scans still contain genuine unresolved source readings. Translation from those passages would either omit or guess text.

## Current story-layer status after assembly

- Story scans 7–22 represented in assembly: **16 / 16**
- Story scans verified: **9** — 7, 9, 10, 11, 12, 13, 16, 19, 20
- Story scans needs-review: **7** — 8, 14, 15, 17, 18, 21, 22
- Printed errata rows mapped: **10 / 10**
- Assembled Tamil text: **complete with explicit unresolved markers**
- Assembly consistency review: **complete**
- English translation: **blocked**

## Next exact activity

Perform a **final unresolved-reading pass** on scans **8, 14, 15, 17, 18, 21 and 22** using the highest-quality supplied scan views/crops available. Resolve only readings supported by the scan itself. Anything physically hidden by stamps or still genuinely illegible after that pass should be formally marked `blocked-by-source` in the audit/handover rather than repeatedly guessed. After that, decide whether the Tamil source layer is sufficiently stable to open a translation workflow with explicit source gaps.
