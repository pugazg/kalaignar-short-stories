# Release Report — The Old Man's Dream

## Release status

**PASS — STORY-BODY ENGLISH TRANSLATION COMPLETE AND RELEASE-READY WITH DOCUMENTED SOURCE LIMITATIONS**

This report completes **Gate D** of the controlled English translation workflow for **கிழவன் கனவு / The Old Man's Dream**.

The release scope is the **story body only**, corresponding to source scans **7–22**. Front matter, scan 23 errata/advertising, commercial advertisements, and the back cover are not part of the English story translation.

The translation is complete to the limit of the supplied physical source. Eight story-text locations remain explicitly blocked because the supplied scan does not expose enough visual information for a source-faithful reading. These are documented source limitations, not unfinished translation work.

## Source identity

- Repository: `pugazg/kalaignar-short-stories`
- Work slug: `kizhavan-kanavu`
- Printed title: **கிழவன் கனவு**
- Printed author line: **தீட்டியவர்: மு. கருணாநிதி.**
- Printed edition statement: **இரண்டாம் பதிப்பு.**
- Source filename: `TVA_BOK_0014165_கிழவன்_கனவு.pdf`
- SHA-256: `cdea0e1c0d2ad657fc4163ed77c58027c18abbe58058221be7f32724b7ef8121`
- Physical scan pages: **26**
- English translated source range: **scans 7–22**
- Visible story pagination: scan 7 = `—`; scan 8 = `(4)` through scan 22 = `(18)`

The supplied scan remains the controlling source for this edition.

## Whole physical-copy Tamil audit

**PASS — CLOSED TO THE LIMIT OF THE SUPPLIED SOURCE**

All **26 / 26** physical scan pages now have terminal source dispositions:

- `verified`: **20**
- `blocked`: **6** — scans **3, 4, 15, 17, 21, 22**
- `needs-review`: **0**
- `not-started`: **0**

The final front-matter disposition pass closed the last two open records:

- scan **3** — terminal `blocked`: two short portions of the upper `“குடியரசு”` review are physically hidden by a large library stamp. Visible readings finalized in the pass include `நினைவாயிற்று`, `விபுலானந்தரும் மல்லிகாவும்`, and the lower-review ending `திராவிட மக்களின் ஆதரவு கிடைக்குமென்று நம்புகிறோம்.`;
- scan **4** — terminal `blocked`: one short phrase between `உறுதிப் பாதையிலே` and `கண்களோடு` remains visually indistinct even at maximum useful enlargement. Visible readings finalized include `ஹிட்-லரிசம்`, `திராவிடருக்கானும்`, `பயனாக ஏற்படும்`, and `ஆக்கம் தருக!`.

Neither page remains in a generic review queue. Hidden/indistinct wording was not reconstructed from context.

## Tamil story disposition

Story-body Tamil audit is complete.

- story scans audited: **16 / 16**
- `verified`: **12 / 16**
- `blocked`: **4 / 16**
- story scans still `needs-review`: **0**

Verified story scans:

`7, 8, 9, 10, 11, 12, 13, 14, 16, 18, 19, 20`

Source-blocked story scans:

- scan **15 / printed 11** — one worn/indistinct word and one temple-history passage partly hidden by a circular library stamp;
- scan **17 / printed 13** — one short worn/indistinct phrase following `பார்வதியை`;
- scan **21 / printed 17** — four short worn/indistinct readings inside the political/historical catalogue;
- scan **22 / printed 18** — one final-story phrase physically obscured by a large circular library stamp.

## Tamil assembly gate

**PASS**

`../../sections/kizhavan-kanavu.md` represents scans **7–22** once each and in source order.

`../../ASSEMBLY_REVIEW.md` is **PASS — FINAL TAMIL STORY ASSEMBLY SYNCHRONIZED**.

The Tamil assembled reading preserves source-specific historical spelling and wording, keeps terminal source gaps explicit, and does not silently apply scan 23 publisher errata.

## English batch source review

**PASS — 4 / 4 batches source-reviewed**

| Batch | Source scans | Source-blocked locations | Status |
|---:|---|---:|---|
| 1 | 7–10 | 0 | `source-reviewed` |
| 2 | 11–14 | 0 | `source-reviewed` |
| 3 | 15–18 | 3 | `source-reviewed` |
| 4 | 19–22 | 5 | `source-reviewed` |

Batch files:

- `batches/01-scans-07-10.md`
- `batches/02-scans-11-14.md`
- `batches/03-scans-15-18.md`
- `batches/04-scans-19-22.md`

Every batch was compared directly with its finalized Tamil page records before being marked `source-reviewed`.

## Full English assembly

**PASS**

Final assembled story:

- `kizhavan-kanavu-en.md`

Coverage checks:

- story scans represented: **16 / 16**;
- source range: **7–22**;
- scan order: **correct**;
- source/printed-page HTML markers: **all retained**;
- duplicated scan: **none**;
- omitted scan: **none**;
- source-blocked locations: **8 / 8 retained**;
- scan-22 publisher/printer/footer material included in story prose: **No**;
- scan-23 errata silently substituted into prose: **No**.

Mechanical cross-page and cross-batch continuations were joined only where needed for the assembled reading layer. Batch source-review files remain unchanged.

## Retained story-source limitations

The English story intentionally contains **8 explicit `SOURCE BLOCKED` locations**:

| Scan | Printed page | Count | Reason |
|---:|:---:|---:|---|
| 15 | 11 | 2 | worn type; circular library stamp covering story text |
| 17 | 13 | 1 | short phrase remains visually indistinct |
| 21 | 17 | 4 | four short worn/indistinct historical/political readings |
| 22 | 18 | 1 | final story phrase hidden by circular library stamp |

No blocked location was filled from context, grammar, mythology, historical knowledge, likely slogans, another edition, or web text.

These markers must remain visible in any archival release derived from this translation unless a genuinely clearer source copy is introduced and separately audited.

## Publisher errata treatment

**PASS — separate layer preserved**

Scan **23** prints a `பிழை திருத்தம்.` table with **10 publisher corrections**.

English editorial mapping:

- `ERRATA_NOTES.md`

Tamil source mapping:

- `../../sections/kizhavan-kanavu-errata.md`

The errata is not silently substituted into the archival Tamil or English reading text.

Key example:

- scan 13 archival page: `வைத்திருந்தான்`;
- scan 23 publisher errata: `வைத்திருந்தாள்`.

The English phrase `had kept` does not expose that Tamil gender difference, so the distinction is retained explicitly in the editorial record.

## Editorial consistency gate

**PASS**

`EDITORIAL_CONSISTENCY_REVIEW.md` confirms consistency for recurring names and titles, source-specific name shortening, religious/cultural terminology, political/caste/social vocabulary, tense and narrative voice, dialogue style, recurring metaphors, cross-page joins, all eight story source-block markers, and publisher-errata separation.

Editorial review did not become source normalization.

## Deliberately conservative translation choices

The following renderings remain intentionally source-close because the verified Tamil is itself unusual, abrupt, historically specific, or semantically difficult:

- `Puranarthika Iyer` for `பூரணர்த்திக`;
- `physician` for `வைத்தியர்` on scan 8;
- `My forehead?` for `என் நெற்றியை?`;
- `I shall eat these grapes.` for `திராட்சையைச் சாப்பிடேன்`;
- `amid a dull cough` for `மந்த காசத்தினிடையே`;
- `Aryam` for `ஆரியம்`;
- `Kali! Kooli!` for `காளி கூலி`;
- `the conch-blast of equal justice` for `சமதர்ம சங்கநாதம்`;
- `We lived—to be kissed by the sword.` for `வாழ்—வாள் முத்தமிட வாழ்ந்தோம்`;
- `The Dravidian land is a day for Dravidians!` for `திராவிட நாடு திராவிடருக்கான தினம்!`.

These are not unresolved source readings. They are conservative translation decisions and should not be silently rewritten into smoother modern English.

## Translation questions remaining

No source-supported story passage remains awaiting Tamil review.

The only unresolved story-text content is the **8 terminal source-blocked locations** documented above. They cannot be solved through stylistic editing.

A future clearer physical copy or independently established edition may be introduced as a new source layer, but must not silently overwrite this edition's archival record.

## Final English file inventory

Control and review:

- `README.md`
- `TRANSLATION_PLAN.md`
- `SOURCE_MAP.md`
- `ERRATA_NOTES.md`
- `EDITORIAL_CONSISTENCY_REVIEW.md`
- `RELEASE_REPORT.md`

Source-reviewed batches:

- `batches/01-scans-07-10.md`
- `batches/02-scans-11-14.md`
- `batches/03-scans-15-18.md`
- `batches/04-scans-19-22.md`

Assembled English story:

- `kizhavan-kanavu-en.md`

## Source PDF repository check

**PASS — source PDF is not stored in GitHub.**

The repository policy says source PDFs are not committed. A repository search for the exact source filename `TVA_BOK_0014165_கிழவன்_கனவு.pdf` returned no file result. The source is represented in GitHub only by metadata, checksum, scan mapping and derived archival text.

## Release decision

**RELEASE-READY WITH DOCUMENTED SOURCE LIMITATIONS.**

For the defined English scope — **கிழவன் கனவு story body, scans 7–22** — the archival translation is complete:

- Tamil story source audit complete to the limit of the supplied copy;
- Tamil assembly review PASS;
- 4 / 4 English batches source-reviewed;
- 16 / 16 story scans represented in the English assembly;
- 8 / 8 source-blocked story locations retained explicitly;
- editorial consistency review PASS;
- all 10 publisher errata entries separately documented;
- source PDF absent from GitHub.

Separately, the **entire 26-page physical-copy Tamil audit is now closed**: 20 pages are verified and 6 are terminally blocked, with no `needs-review` pages remaining.

## Completion state

**English story-body translation: COMPLETE.**

**Physical-publication archival page coverage: COMPLETE — 26 / 26 terminal dispositions.**

**கிழவன் கனவு processing for this supplied copy: CLOSED.**

## Next archival activity

Do not reopen terminal blocked readings unless a genuinely clearer source is introduced and audited.

The next repository activity is source registration and inspection for the **next Kalaignar short-story PDF** when supplied.
