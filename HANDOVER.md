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

Translation control/review files:

- `stories/kizhavan-kanavu/translations/en/README.md`
- `stories/kizhavan-kanavu/translations/en/TRANSLATION_PLAN.md`
- `stories/kizhavan-kanavu/translations/en/SOURCE_MAP.md`
- `stories/kizhavan-kanavu/translations/en/ERRATA_NOTES.md`
- `stories/kizhavan-kanavu/translations/en/EDITORIAL_CONSISTENCY_REVIEW.md`
- `stories/kizhavan-kanavu/translations/en/RELEASE_REPORT.md`

All four source batches are **SOURCE-REVIEWED**:

1. `batches/01-scans-07-10.md`
2. `batches/02-scans-11-14.md`
3. `batches/03-scans-15-18.md`
4. `batches/04-scans-19-22.md`

English source-reviewed coverage: **16 / 16 story scans**.

Full assembled English story:

- `stories/kizhavan-kanavu/translations/en/kizhavan-kanavu-en.md`

Editorial review:

- `EDITORIAL_CONSISTENCY_REVIEW.md` — **PASS**

Release review:

- `RELEASE_REPORT.md` — **PASS — RELEASE-READY WITH DOCUMENTED SOURCE LIMITATIONS**

English story-body translation status: **COMPLETE**.

## Full English release result

Confirmed:

- translated source range: scans **7–22**;
- Tamil story disposition: **12 verified / 4 source-blocked**;
- English batches source-reviewed: **4 / 4**;
- assembled English scans represented: **16 / 16**;
- source-scan / printed-page markers: **all retained**;
- duplicated/omitted story scans: **none**;
- explicit English `SOURCE BLOCKED` story locations: **8 / 8**;
- scan-22 publisher/printer/footer material: **excluded from story prose**;
- scan-23 publisher errata: **10 corrections separately documented**;
- publisher errata silently substituted: **No**;
- source PDF stored in GitHub: **No**.

### Explicit English source gaps

- scan 15 / printed 11 — **2**
- scan 17 / printed 13 — **1**
- scan 21 / printed 17 — **4**
- scan 22 / printed 18 — **1**

Total: **8**.

These are terminal source limitations for the supplied copy and must remain explicit unless a genuinely clearer source is later introduced and audited.

## Conservative translation decisions retained

The release review explicitly accepts source-close renderings where verified Tamil is unusual or semantically abrupt, including:

- `Puranarthika Iyer`
- `physician`
- `My forehead?`
- `I shall eat these grapes.`
- `amid a dull cough`
- `Aryam`
- `Kali! Kooli!`
- `the conch-blast of equal justice`
- `We lived—to be kissed by the sword.`
- `The Dravidian land is a day for Dravidians!`

Do not “improve” these during future cleanup unless a new source-based editorial layer is intentionally created.

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

## Scope completion

The **கிழவன் கனவு story-body English translation is complete and release-ready**.

The whole physical publication's Tamil audit is not yet fully closed only because front-matter scans **3–4** remain `needs-review`. They are outside the completed story-body English translation scope.

## Next exact activity

Perform the final high-resolution disposition pass on **front-matter scans 3–4**.

1. Re-open scans 3 and 4 from the supplied PDF at high resolution.
2. Compare the existing page records directly with the scan.
3. For scan 3, determine whether any stamp-obscured wording can safely be resolved; never reconstruct hidden text from context.
4. For scan 4, re-check the one short unresolved publisher-note phrase at maximum useful enlargement.
5. Promote a page to `verified` only if every visible printed reading is source-supported.
6. If the supplied copy cannot expose the hidden/indistinct text, convert the page to terminal `blocked` and mark each unrecoverable location `blocked-by-source`.
7. Update `indexes/page-map.md`, `audit.md`, story/root READMEs and this handover.
8. After that pass, the full 26-page Tamil archival audit can be considered closed for this physical copy.