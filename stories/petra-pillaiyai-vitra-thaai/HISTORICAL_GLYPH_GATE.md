# Historical Tamil Glyph Gate — பெற்ற பிள்ளையை விற்ற தாய்

Gate status: **PENDING**  
Scope: PDF scans **7–28 / printed pages 5–26**  
Input state: **22 / 22 first-pass transcriptions complete; 0 / 22 final verified**

## User-directed phase boundary

This 1982 book contains a high density of historical Tamil glyphs. The user has explicitly required **one dedicated historical-glyph gate after transcription**.

Therefore the workflow for this story is:

1. complete the full first-pass transcription;
2. stop with all pages `needs-review`;
3. run this independent historical-glyph gate over the complete transcription;
4. only after this gate PASSes may pages advance toward final source verification / release.

The gate is not satisfied by having noticed old forms during transcription.

## Authority

Use `HISTORICAL_TAMIL_GLYPH_TRANSCRIPTION_GUIDE.md` and the controlling source scan.

Core rule: **read character identity, not modern visual resemblance**. Glyph decoding is not spelling modernization.

## Mandatory minimum families

Every page must be reopened at native/high resolution and checked explicitly for:

`ணா / ணை / ணொ / ணோ / லை / ளை / றா / றொ / றோ / னா / னை / னொ / னோ`

This is a minimum set, not an exhaustive list.

## Gate method

For every scan 7–28:

- inspect the complete page, not isolated characters;
- compare suspicious clusters against enlarged/native source pixels;
- compare clearer same-edition / same-font examples when useful;
- prove the complete word/phrase span, not only a single loop or vowel mark;
- encode only the proven historical character identity in normal modern Unicode;
- preserve source spelling, grammar, sandhi, vocabulary, spacing and punctuation otherwise;
- never use global replacement;
- never correct a word merely because modern Tamil would normally prefer another form;
- leave a genuinely unresolved cluster `needs-review` rather than guessing from context.

## Correction log

| Scan | Printed page | Earlier / first-pass reading | Source-supported reading | Historical family | Evidence | Status |
|---:|---:|---|---|---|---|---|
| — | — | — | — | — | — | pending gate |

Every correction discovered in the gate must be added here and synchronized into the corresponding `pages/*.md` record and the assembled `sections/petra-pillaiyai-vitra-thaai.md` file.

## Closure conditions

The gate may be marked **PASS** only when:

- all 22 pages were independently reopened after transcription;
- all 13 known families were checked on every page;
- all suspicious candidates in `POSSIBLE_ERRORS_FOR_REVIEW.md` were revisited;
- all source-supported glyph corrections were recorded individually;
- no global replacement or silent modernization was used;
- unresolved glyph clusters are **0**, or any genuinely unrecoverable source damage is explicitly documented under the repository's escalation policy;
- page and assembled-text layers agree after corrections.

Until then: **Story 1 is transcribed, but not source-verified and not eligible for English.**
