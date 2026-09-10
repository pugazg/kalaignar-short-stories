# Assembly consistency review — நாட்டிய கலாராணி

## Review result

**PASS — TAMIL STORY ASSEMBLY SYNCHRONIZED / 22 OF 22 VERIFIED SOURCE PAGES / ZERO OMISSION OR DUPLICATION**

Canonical assembly: `sections/naattiya-kalarani.md`  
Controlling page layer: `pages/0025-...` through `pages/0046-...`  
Controlling source: `TVA_BOK_0065574_நளாயினி_1976.pdf`.

## Coverage gate

All **22 / 22** verified story pages are represented exactly once and in physical scan order:

| Sequence | Scan | Printed | Assembly disposition |
|---:|---:|---:|---|
| 1 | 25 | 25 | present; story heading preserved |
| 2 | 26 | 26 | present; inline boundary marker joins split `நட்டுவ` + `னரும்` |
| 3 | 27 | 27 | present |
| 4 | 28 | 28 | present; source repeated `கவிவாணர்-` boundary retained, not deduplicated |
| 5 | 29 | 29 | present |
| 6 | 30 | 30 | present |
| 7 | 31 | 31 | present |
| 8 | 32 | 32 | present |
| 9 | 33 | 33 | present |
| 10 | 34 | 34 | present; `‘அன்றொரு நாள்` → `இரவு,` continuation joined across marker |
| 11 | 35 | 35 | present; `மன்னனும் மற்றவரும்` → `கெக்கலிப்புக்...` continuation joined |
| 12 | 36 | 36 | present |
| 13 | 37 | 37 | present; `காரணம்; அவன்` → `கண்ட மற்றத் துறவிகள்...` continuation joined |
| 14 | 38 | 38 | present |
| 15 | 39 | 39 | present |
| 16 | 40 | 40 | present |
| 17 | 41 | 41 | present |
| 18 | 42 | 42 | present |
| 19 | 43 | 43 | present |
| 20 | 44 | 44 | present |
| 21 | 45 | 45 | present |
| 22 | 46 | 46 | present; final letter/signature and closing ornaments preserved |

Result: **22 present / 0 missing / 0 duplicated / 0 out of order**.

## Page-boundary gate

**PASS.** Every physical boundary is represented by an HTML source-scan marker. Five boundaries required explicit semantic checking:

1. **25 → 26:** physical split `நட்டுவ` + `னரும்` is rendered as the lexical continuation `நட்டுவனரும்` with the scan-26 marker retained inline. No source letters were added or removed.
2. **27 → 28:** scan 27 ends `கவிவாணர்-`; scan 28 visibly begins `கவிவாணர்-மதிவாணர்`. The apparent repetition is retained exactly as two source-page readings; assembly does **not** silently deduplicate it.
3. **33 → 34:** `‘அன்றொரு நாள்` continues with scan-34 `இரவு, ...`; the marker is inserted inside the continuing quotation without rewriting the wording.
4. **34 → 35:** `மன்னனும் மற்றவரும்` continues directly with `கெக்கலிப்புக் கொட்டுவார்களாமே`; the source-page marker preserves the physical boundary while the reading remains continuous.
5. **36 → 37:** `காரணம்; அவன்` continues directly with `கண்ட மற்றத் துறவிகள்...`; the assembly preserves the lexical/syntactic continuation.

No other boundary showed a split lexical item or an unresolved overlap.

## Structure / non-prose gate

**PASS.** The derived story retains all verified printed separators:

- scan 37 — one `◆     ◆` separator;
- scan 40 — one `◆     ◆     ◆` separator;
- scan 42 — two separate `◆     ◆` separators;
- scan 46 — final `◆     ◆` closing ornaments.

The scan-46 letter/signature block remains structurally separate:

`வணக்கம்,`

`இன்பசாகரன்.`

The story-ending ornaments remain after the concluding prose. Scan 47 (`விஷம் இனிது`) is excluded.

## Source-fidelity gate

**PASS.** Assembly was produced only from final `verified` page records. YAML front matter and page-level audit comments were excluded. Verified source-odd forms and punctuation were not modernized or normalized, including examples such as `தீயிலேகிடக்க`, `யாருக்குக் அளித்தது`, `நங்கள்`, `பிணத்தைநடு`, `பந்தங்களிலேஉன்னை`, `போது!`, asymmetric quotation marks, and source hyphen/dash spacing.

All page-level source/glyph queues were already closed before assembly: **22 / 22 verified, 19 source-proven corrections across P1–P4, P5 0 corrections, 0 unresolved / 0 blocked**.

## Completion state

**PASS — `நாட்டிய கலாராணி` TAMIL SOURCE / ASSEMBLY IS SOURCE-COMPLETE.**

- direct transcription: **22 / 22 COMPLETE**;
- independent historical-glyph/source verification: **22 / 22 PASS**;
- canonical Tamil assembly: **COMPLETE**;
- assembly coverage: **22 / 22**;
- omission / duplication: **0 / 0**;
- unresolved / blocked story text: **0 / 0**.

Next activity is separate: activate Story 8 **`மானம்`** from scans **73–78** through source-intake/canonical-dedup/workspace initialization. Do not begin its transcription in this assembly commit.
