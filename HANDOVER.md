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

## Tamil source state

- Source registered: **yes**
- Page records: **26 / 26**
- Whole-publication status: **20 verified / 4 blocked / 2 front-matter needs-review / 0 not-started**
- Story scans audited: **16 / 16**
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
- `stories/kizhavan-kanavu/translations/en/ERRATA_NOTES.md`

All four source batches are **SOURCE-REVIEWED**:

1. `batches/01-scans-07-10.md`
2. `batches/02-scans-11-14.md`
3. `batches/03-scans-15-18.md`
4. `batches/04-scans-19-22.md`

English source-reviewed coverage: **16 / 16 story scans**.

Full assembled English story:

- `stories/kizhavan-kanavu/translations/en/kizhavan-kanavu-en.md`

Editorial review:

- `stories/kizhavan-kanavu/translations/en/EDITORIAL_CONSISTENCY_REVIEW.md` — **PASS**

Release report:

- `stories/kizhavan-kanavu/translations/en/RELEASE_REPORT.md` — **not created yet**

## Full English assembly result

`kizhavan-kanavu-en.md` is assembled from the four source-reviewed batches only.

Confirmed:

- scans represented: **16 / 16**;
- scan order: **7 → 22**;
- source-scan / printed-page markers: **all retained**;
- duplicated source scans: **none**;
- omitted source scans: **none**;
- scan 7 pagination remains `—`;
- total explicit `SOURCE BLOCKED` story locations: **8 / 8**;
- scan-22 publisher/printer/footer material: **excluded from story prose**;
- scan-23 errata silently substituted: **No**.

### Explicit English source gaps

- scan 15 / printed 11 — **2**
- scan 17 / printed 13 — **1**
- scan 21 / printed 17 — **4**
- scan 22 / printed 18 — **1**

Total: **8**.

These gaps remain terminal for this supplied copy and must stay explicit in every release layer unless a genuinely clearer source copy is later introduced.

## Assembly-only boundary handling

Mechanical cross-batch continuations were joined only in `kizhavan-kanavu-en.md`. Batch files remain unchanged.

Notable joins documented in `EDITORIAL_CONSISTENCY_REVIEW.md`:

- scan 10 → 11 — Garuda sentence;
- scan 14 → 15 — duplicated Mallika boundary wording reduced to a pronoun in the assembled reading;
- scan 17 → 18 — mechanically split `floating` wording joined across the page marker;
- scan 18 → 19 — duplicated conditional boundary wording removed so the one Tamil condition is represented once.

These are assembly mechanics, not source normalization.

## Editorial consistency result

`EDITORIAL_CONSISTENCY_REVIEW.md` is **PASS**.

Reviewed and accepted:

- recurring names/titles;
- religious/cultural terminology;
- political and caste/social vocabulary;
- tense and narrative voice;
- quotation/dialogue style;
- recurring metaphors;
- all 8 blocked markers;
- cross-page joins;
- errata-note consistency.

Deliberately difficult/source-specific renderings remain conservative rather than being modernized or repaired from context.

## Errata state

`ERRATA_NOTES.md` records all **10** publisher corrections from scan 23 separately.

Key distinction:

- scan 13 archival page: `வைத்திருந்தான்`;
- scan 23 errata: `வைத்திருந்தாள்`.

The English phrase `had kept` does not expose that Tamil gender distinction, so the editorial note preserves the distinction explicitly.

## Permanent archival rules

1. The supplied scan is the controlling source for this edition.
2. Do not reconstruct stamp-hidden or worn text from context.
3. Do not silently modernize unusual source forms.
4. Do not infer scan 7 pagination.
5. Keep scan 23 publisher errata as a separate layer.
6. Keep scan 13 `வைத்திருந்தான்` and errata `வைத்திருந்தாள்` distinct.
7. Advertisements, library marks and printer/footer matter are separate from story prose.
8. Source PDF stays outside GitHub.
9. Every English `SOURCE BLOCKED` marker must remain explicit and in position.
10. Editorial consistency is not permission to normalize source oddities.

## Next exact activity — Gate D release review

Create:

`stories/kizhavan-kanavu/translations/en/RELEASE_REPORT.md`

The release review must document:

1. translated source range: scans **7–22**;
2. Tamil story disposition: **12 verified / 4 source-blocked**;
3. English batches: **4 / 4 source-reviewed**;
4. assembled English coverage: **16 / 16 scans**;
5. retained source gaps: **8**;
6. publisher errata: **10 corrections**, separately documented;
7. deliberately conservative/unresolved translation choices;
8. final repository file inventory;
9. confirmation that the source PDF is not stored in GitHub;
10. final completion/release status.

Do not fill or remove any blocked marker during release review.