# 1987 Story-Heading Historical-Glyph Re-audit — 2026-09-06

Controlling source: `TVA_BOK_0065566_கலைஞர்_சொன்ன_குட்டிக்_கதைகள்_1987.pdf`

This re-audit was requested after an old-type `ணா` in Story 4 had been misread by modern visual resemblance. All 25 physical story-opening headings were therefore rechecked from the first story through the final story, using native/high-resolution source renders and `HISTORICAL_TAMIL_GLYPH_TRANSCRIPTION_GUIDE.md`.

## Result

All **25 / 25** headings now have a high-resolution source-supported Unicode reading. A later direct banner recheck on **2026-09-07** corrected Story 10; that stronger source finding supersedes the earlier Story-10 entry in this audit.

Four earlier inventory readings required correction:

1. Story 2: `அரசாபிமானக் கதை` → **`அராபியக் கதை`**.
2. Story 4: `நாராயணு! நாராயணு!` → **`நாராயணா ! நாராயணா !`**. This is a historical **`ணா`** decoding, not a spelling modernization. The printed spacing before each `!` is preserved.
3. Story 6: `முல்லை முத்துக்குமரன்` → **`மூளி மூக்குக்காரன்`**.
4. Story 10: `இரு நிகழ்வுகள்` → **`இரு நிழல்கள்`**. The stylized lower-scan-20 banner was reopened at native/high resolution on 2026-09-07; the corrected reading also agrees with the opening sentence `இலக்கியத்தில் இரண்டு நிழல்கள் குறிப்பிடப்படுகின்றன` but the banner pixels, not context, control the correction.

No other heading currently requires a lexical/title correction.

## Authoritative heading list

| # | Scan | Source-faithful Unicode heading | High-resolution glyph note |
|---:|---:|---|---|
| 1 | 5 | `மன்னனும் குருவியும்!` | PASS |
| 2 | 6 | `அராபியக் கதை` | corrected from earlier misread |
| 3 | 7 | `தென்னை மரத்தில் புல்` | `னை` family explicitly checked |
| 4 | 8 | `நாராயணா ! நாராயணா !` | historical `ணா` explicitly decoded; punctuation spacing preserved |
| 5 | 10 | `துறவியும் சீடர்களும்` | PASS |
| 6 | 12 | `மூளி மூக்குக்காரன்` | corrected from earlier misread |
| 7 | 13 | `சொர்க்கத்திற்குச் சென்றுவந்த அழகி!` | PASS |
| 8 | 15 | `புத்தர் உணர்த்திய உண்மை` | PASS |
| 9 | 18 | `கஜினி முகமதுவும் கவிஞர் பார்டோசியும்` | PASS |
| 10 | 20 | `இரு நிழல்கள்` | corrected on 2026-09-07 by direct native/high-resolution banner recheck |
| 11 | 23 | `குருவி ராமேஸ்வரம்` | PASS |
| 12 | 24 | `சாமியாரும் பூக்காரியும்` | PASS |
| 13 | 25 | `ஹஜ்ரத் அலியும் யூதனும்` | PASS |
| 14 | 27 | `புகழேந்திப் புலவர் கதை` | PASS |
| 15 | 29 | `மன மாற்றம்` | PASS |
| 16 | 31 | `குறிக்கோள்` | stylized banner rechecked at high resolution |
| 17 | 32 | `பாலும் தண்ணீரும்` | PASS |
| 18 | 34 | `ஜெயத்ரதனின் வீழ்ச்சி` | PASS |
| 19 | 37 | `தெனாலிராமன் கதை` | historical `னா` family explicitly checked |
| 20 | 39 | `வல்வில் ஓரி` | PASS |
| 21 | 41 | `யசோதர காவியம்` | PASS |
| 22 | 44 | `காடு சென்ற குமணன்` | PASS |
| 23 | 45 | `அகத்திணை அன்பு!` | historical `ணை` family explicitly checked |
| 24 | 46 | `தெனாலிராமன் பூனை` | historical `னா` + `னை` families explicitly checked |
| 25 | 48 | `குழந்தையும் கிளியும்` | PASS |

Scan 50 remains the blank/damaged terminal leaf with no story continuation.

## Historical-glyph-sensitive title findings

The heading-level second pass explicitly checked the known reform-sensitive families wherever present. The clearest title-level examples are:

- Story 3 `தென்னை...` — old `னை` form;
- Story 4 `நாராயணா...` — old `ணா` form; this was the previously missed case;
- Story 19 `தெனாலிராமன்...` — old `னா` form;
- Story 23 `அகத்திணை...` — old `ணை` form;
- Story 24 `தெனாலிராமன் பூனை` — old `னா` and `னை` forms.

Story 10's correction is an ordinary title-reading correction, not a historical-glyph-family decoding.

These are glyph-decoding decisions only where explicitly classified as such. Source wording was not modernized.

## Mandatory two-pass lexical workflow from this checkpoint

For every 1987 page from now on:

### Pass 1 — initial transcription

- transcribe source-faithfully from the controlling scan;
- preserve spelling, grammar, compounds, punctuation, spacing and page boundaries;
- apply the historical-glyph guide during transcription;
- unresolved clusters remain `needs-review`.

### Pass 2 — independent high-resolution historical-glyph check

**After the initial transcription is complete, reopen the same physical page at native/high resolution and perform a separate glyph-only verification round.**

- check all 13 known families again: `ணா / ணை / ணொ / ணோ / லை / ளை / றா / றொ / றோ / னா / னை / னொ / னோ`;
- compare suspicious forms with clearer same-edition occurrences;
- check full words/phrases, not isolated curls or strokes;
- record every correction from apparent reading → source-supported Unicode identity;
- never global-replace;
- do not use another edition to force the 1987 wording;
- a page cannot become final `verified` merely from the initial transcription pass; the high-resolution glyph second pass must also close.

This two-pass rule controls the remaining lexical/glyph batches and should be retained for future historical-Tamil source work unless a later explicit instruction supersedes it.
