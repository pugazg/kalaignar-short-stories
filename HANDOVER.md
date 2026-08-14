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

## Source structure confirmed from full visual inspection

- scan 1 — cover
- scans 2–6 — reviews / publisher-editorial material / author note
- scans 7–22 — `கிழவன் கனவு` story body
- scan 23 — **`பிழை திருத்தம்.`** errata table + tobacco advertisement
- scan 24 — `ராஜேந்திரா நைஸ் புகையிலை` advertisement
- scan 25 — `தியாகராஜ விலாஸ்` advertisement / portrait
- scan 26 — back cover / small child illustration / no readable printed text

Visible story-body pagination:

- scan 8 = printed page `(4)`
- sequentially through scan 22 = printed page `(18)`
- scan 7's printed page number is not clearly visible; do **not** infer `(3)` into the archival record.

## Files created

Root:

- `README.md`
- `SHORT_STORY_PROCESSING_GUIDE.md`
- `HANDOVER.md`

Story control files:

- `stories/kizhavan-kanavu/README.md`
- `stories/kizhavan-kanavu/audit.md`
- `stories/kizhavan-kanavu/metadata/source.md`
- `stories/kizhavan-kanavu/indexes/page-map.md`

Page records:

- scans 1–6: `pages/0001-...` through `pages/0006-...`
- scans 7–22: `pages/0007-kizhavan-kanavu-01.md` through `pages/0022-kizhavan-kanavu-16.md`
- scan 23: `pages/0023-errata-advertisement.md`
- scan 24: `pages/0024-advertisement.md`
- scan 25: `pages/0025-thiyagaraja-vilas-ad.md`
- scan 26: `pages/0026-back-cover.md`

## Status after Tamil source audit

- Source registered: **yes**
- 26-page manifest: **complete**
- Page records: **26 / 26**
- `verified`: **16**
- `needs-review`: **10**
- `not-started`: **0**
- Story-body direct visual transcription: **complete for scans 7–22**
- Dedicated Tamil source audit, scans 7–23: **completed**
- Audit report: **created** at `stories/kizhavan-kanavu/audit.md`
- Back matter through back cover: **archived**
- English translation: **do not start yet**

### Scans promoted by the audit

Scans **7, 9, 10, 11, 12, 16, 19, 20 and 23** are now `verified` after direct re-comparison with the supplied scan.

### Remaining `needs-review`

Front matter:

- scan **3** — library stamp physically hides words in the upper review;
- scan **4** — one short phrase remains unclear.

Story / source pages:

- scan **8** — one visually unclear word after `பூகோள`;
- scan **13** — audit identified several corrections, but final source-faithful reconciliation of the page record remains pending; printed `வைத்திருந்தான்` and scan-23 errata `வைத்திருந்தாள்` must remain distinct layers;
- scan **14** — several worn-type readings inside the long dream passage remain ambiguous;
- scan **15** — a large library stamp physically covers story text; do not reconstruct it from context;
- scan **17** — one short phrase following `பார்வதியை` remains unclear;
- scan **18** — one short opening phrase remains unclear;
- scan **21** — four short political/historical phrases remain visually unclear;
- scan **22** — library stamp obscures part of the conclusion and publisher/printer footer.

## Important audit corrections / confirmations

- scan 7 — **`டூப்ளிகேட் கிருஷ்ணலீலா`**
- scan 9 — **`காயமேயிது`**, **`இந்த அணி`**
- scan 11 — **`சிறுபுரட்சி`**, **`இனிப்பில்`**, **`திருட்டுக் குற்றம்`**, **`அள்ளியள்ளி`**
- scan 12 — **`அதிகாரபூர்வமாக`**, **`வீடு திரும்பும்`**
- scan 16 — **`ஓராண்டு சிறையிலே`**, **`கரையில் இட்டதோர் மீன்`**, plus other corrected source readings
- scan 19 — **`காட்சி சகிக்க வொண்ணாது.`**
- scan 22 — **`வாழ்—வாள்`**, **`காதலியின்பால்`**, **`திராவிடருக்கான தினம்`**

## Scan 23 errata — fully resolved

The printed `பிழை திருத்தம்.` table is now fully readable:

- p.7 l.6 — `சிறுபுரட்சி`
- p.7 l.18 — `அள்ளியள்ளி`
- p.8 l.24 — `வண்டியோட்டி`
- p.9 l.10 — `பார்த்து`
- p.9 l.15 — `வைத்திருந்தாள்`
- p.9 l.16 — `முடியும்`
- p.12 l.11 — `வினைகளை`
- p.12 l.17 — `மல்லிகா`
- p.13 l.29 — `செம்மாந்து`
- p.15 l.2 — `கொந்தளிப்பு`

Advertisement heading below the table is **`ஸ்ரீரோஜி மார்க்`**.

### Errata rule

The printed errata remains a separate publication layer. **Do not silently overwrite** the archival page text with these corrections. Any assembled reading text must make the relationship explicit.

## Continuing cautions

1. Never reconstruct stamp-hidden words from sentence meaning.
2. Do not normalize unusual historical spellings merely because a modern form appears more natural.
3. Scan 7's missing printed page number remains `—`.
4. Internal front-matter dates are not automatically the second-edition publication year.
5. The source PDF remains outside GitHub.
6. English translation remains blocked until an assembled Tamil text and consistency review are completed.

## Next exact activity

Create `stories/kizhavan-kanavu/sections/kizhavan-kanavu.md` as the assembled Tamil reading text.

1. Assemble only from the audited page records.
2. Preserve paragraph/dialogue order and historical wording.
3. Keep unresolved readings explicit rather than smoothing them over.
4. Add a separate documented errata mapping/note; do not silently substitute scan-23 corrections into the archival reading layer.
5. Cross-check the assembled text against `pages/`, `indexes/page-map.md`, and `audit.md`.
6. Record any assembly-level discrepancies in a consistency review file.
7. Do **not** begin English translation until that review is complete.
