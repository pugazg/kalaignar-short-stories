# Historical Tamil Glyph Transcription Guide

## Purpose

This is a reusable source-first guide for transcribing older Tamil print into modern Unicode without silently changing the source text.

It was created from:

1. the user-supplied Periyar எழுத்துச் சீர்திருத்தம் reference chart; and
2. direct scan-review failures/corrections encountered across this archive, including `பெரிய இடத்துப் பெண்`, `புதையல்`, and the 1987 `கலைஞர் சொன்ன குட்டிக் கதைகள்` title re-audit.

Use this document for future novels, stories, speeches, essays, poems, letters, newspapers and other older Tamil printed sources whenever historical typeforms may occur.

---

# 1. Core principle

> **Read character identity, not modern visual resemblance.**

Older Tamil type can use glyph shapes that look like a different modern Tamil sequence. A transcription must determine what character the historical type represents and then encode that character in normal modern Unicode.

This is **glyph decoding**, not modernization of the text.

Therefore:

- preserve the source's word, spelling, grammar, vocabulary, spacing and punctuation;
- convert only the proven historical glyph identity into its correct modern Unicode representation;
- do not reproduce an old glyph according to the modern character it merely resembles;
- do not use a historical-glyph finding as permission to rewrite the word into expected modern Tamil.

Example:

- apparent modern-shape reading `நன்றுக`;
- historical identity `றா`;
- source-supported Unicode transcription **`நன்றாக`**.

The source wording remains the source wording; only the character identity is decoded correctly.

---

# 2. Known Periyar-reform-sensitive forms

The user-supplied reference chart establishes the following **minimum** set that must be checked explicitly in older print:

| Modern Unicode identity | Example | Audit family |
|---|---|---|
| `ணா` | `அண்ணா` | `ணா` |
| `ணை` | `அணை` | `ணை` |
| `ணொ` | `மண்ணொடு` | `ணொ` |
| `ணோ` | `கண்ணோடு` | `ணோ` |
| `லை` | `தலை` | `லை` |
| `ளை` | `களை` | `ளை` |
| `றா` | `சிறார்` | `றா` |
| `றொ` | `மற்றொரு` | `றொ` |
| `றோ` | `காற்றோடு` | `றோ` |
| `னா` | `மன்னா` | `னா` |
| `னை` | `வினை` | `னை` |
| `னொ` | `என்னொடு` | `னொ` |
| `னோ` | `என்னோடு` | `னோ` |

This is not exhaustive. Remain alert for other old ligatures, faint vowel marks, worn type, broken ink, touching characters, edition-specific forms and stylized display lettering.

---

# 3. Why visual resemblance is dangerous

A modern reader, OCR system or language model may map an old glyph to the closest-looking current glyph. That can produce a plausible-looking but false transcription.

Confirmed archive examples include:

| Source | Incorrect visual reading | Correct reading | Cause |
|---|---|---|---|
| `பெரிய இடத்துப் பெண்` | `ஆவிலைக்` | `ஆவலைக்` | historical `லை` |
| `பெரிய இடத்துப் பெண்` | `நின்றூர்` | `நின்றார்` | historical `றா` |
| `பெரிய இடத்துப் பெண்` | `போகிறயே` | `போகிறாயே` | historical `றா` |
| `பெரிய இடத்துப் பெண்` | `நன்றுக` | `நன்றாக` | historical `றா` |
| `பெரிய இடத்துப் பெண்` | `வேலை மட்டுந்தானு?` | `வேலை மட்டுந்தானா?` | historical `னா` |
| 1987 `கலைஞர் சொன்ன குட்டிக் கதைகள்`, Story 4 heading | `நாராயணு! நாராயணு!` | `நாராயணா ! நாராயணா !` | historical `ணா`; source punctuation spacing also preserved |

A related failure in `புதையல்` showed that a faint/old `லை` may look like bare `ல்`, tempting a false shortening.

The lesson:

> **Never infer character identity from ordinary-zoom appearance alone.**

---

# 4. Mandatory page-level workflow

For every page from a potentially historical Tamil edition:

1. inspect the whole page first;
2. understand typeface, ink, damage, bleed-through, stamps and repeated glyph behaviour;
3. use enlarged/native pixels for difficult characters;
4. check all 13 known reform-sensitive families;
5. read the complete glyph cluster, not only one curl/loop/vowel mark;
6. compare clearer same-edition occurrences when uncertain;
7. separate glyph identity from lexical expectation;
8. encode only the positively supported identity in modern Unicode;
9. preserve spelling, grammar, sandhi, compounds, spacing, vocabulary and punctuation otherwise;
10. if still ambiguous, keep `needs-review`;
11. never global-replace.

---

# 5. Mandatory two-pass verification — NEW PERMANENT RULE

Initial transcription and historical-glyph closure are **separate passes**.

## Pass 1 — initial transcription

- transcribe directly from the controlling scan;
- preserve source wording and physical boundaries;
- decode obvious historical identities where positively supported;
- record uncertain clusters explicitly;
- do not claim final glyph closure merely because the paragraph reads plausibly.

## Pass 2 — independent native/high-resolution glyph audit

**After Pass 1 transcription exists, reopen the same physical page at native/high resolution and perform a separate glyph-focused review.**

During Pass 2:

1. explicitly recheck `ணா / ணை / ணொ / ணோ / லை / ளை / றா / றொ / றோ / னா / னை / னொ / னோ`;
2. search the transcribed page for words containing or plausibly containing those families;
3. compare each suspicious form against the actual high-resolution source cluster;
4. compare same-edition/same-font examples where useful;
5. verify full words, phrases and neighboring characters rather than isolated strokes;
6. record every correction as apparent/earlier reading → source-supported reading → historical family;
7. never global-replace even when the same visual pattern recurs;
8. if a cluster remains uncertain, retain `needs-review`.

> **A page may not be promoted to final `verified` from Pass 1 alone. Pass 2 must also close.**

This rule applies even when the first transcription was already performed at enlarged resolution. The second pass is intentionally independent so that transcription momentum/context does not hide a systematic old-glyph error.

---

# 6. Glyph decoding is not spelling correction

Allowed:

- source old form represents `றா` → encode `றா`.

Not allowed:

- changing a word because modern Tamil would normally be written differently.

Preserve unless the source pixels prove otherwise:

- old spelling;
- unusual sandhi;
- colloquial forms;
- archaic vocabulary;
- odd grammar;
- repeated words;
- unusual punctuation;
- period-specific compounds and spacing.

A historical-glyph correction changes **character identity only**. A lexical correction requires separate positive scan evidence.

---

# 7. Same-edition comparison method

When a glyph is uncertain:

1. identify the likely consonant/vowel family;
2. locate clearer instances in the same book/issue/font;
3. compare stroke direction, loop placement, vowel-mark attachment and surrounding spacing;
4. prefer same-edition evidence over a generic chart;
5. use the reform chart to identify candidate families, not to force a reading.

A chart tells you what forms can exist. The scan tells you what is printed here.

---

# 8. OCR policy

OCR may be used only as a discovery aid.

Do not trust OCR for historical Tamil glyph identity because it may:

- map an old glyph to the closest-looking modern character;
- drop faint vowel marks;
- merge neighbors;
- split one historical ligature;
- normalize a rare source form into a common word.

The controlling authority is the source image.

---

# 9. Difficult-reading escalation

Before leaving story text terminally unresolved:

1. inspect native embedded scan image if available;
2. use progressively enlarged crops;
3. compare nearest-neighbour and high-quality resampling;
4. try non-destructive contrast/gamma/sharpening/grayscale variants;
5. distinguish stamp/seal strokes from print strokes where relevant;
6. compare same-font characters elsewhere on the page/work;
7. inspect page-boundary continuation and split words;
8. verify any user-supplied reading against source pixels;
9. use an independent secondary witness only as provenance-aware corroboration;
10. never silently import secondary-witness wording.

`blocked` should be terminal only when the physical source and documented corroboration cannot recover a defensible reading.

---

# 10. Recommended page record note

```markdown
## Historical-glyph audit

### Pass 1 — initial transcription
- source-faithful transcription completed / partial;
- uncertainty recorded explicitly;
- no global replacement or modernization.

### Pass 2 — native/high-resolution glyph check
- complete page reopened at high resolution;
- checked: `ணா / ணை / ணொ / ணோ / லை / ளை / றா / றொ / றோ / னா / னை / னொ / னோ`;
- representative source occurrences: `<word>` (`<family>`);
- same-edition comparisons used where needed;
- corrections recorded individually;
- remaining unresolved clusters: `<count/list>`;
- final status: `needs-review` / `verified`.
```

If a correction is made:

```markdown
- apparent/earlier reading: `...`
- source-supported Unicode reading: `...`
- historical identity: `றா`
- evidence: native/high-resolution source-pixel comparison
```

---

# 11. Recommended work-level audit table

```markdown
| Scan | Printed page | Pass | Earlier/apparent reading | Source-supported reading | Historical family | Evidence | Status |
|---:|:---:|---|---|---|---|---|---|
| 24 | 23 | high-res second pass | `நன்றுக` | `நன்றாக` | `றா` | native scan | needs-review |
```

Keep historical-glyph corrections separate from ordinary lexical corrections.

---

# 12. Decision tree

```text
Initial transcription
        |
        v
Separate native/high-resolution second pass
        |
        v
Check all 13 known families + suspicious clusters
        |
        v
Compare same-edition forms if needed
        |
        v
Is character identity positively supported?
       / \
     yes  no
      |    |
      v    v
Encode      Keep `needs-review`;
correct     do not guess from context
Unicode
      |
      v
Preserve source wording unchanged
```

---

# 13. Page breaks and glyphs are separate problems

A word may be physically split across lines/pages while also containing an old glyph. Resolve independently:

- determine character identity from the printed glyph;
- separately record physical boundary;
- join fragments only in an assembled layer when the join is positively established and provenance remains reversible.

Do not use a likely cross-page word to force an uncertain glyph.

---

# 14. Verification policy

Recommended states:

- `not-started` — no transcription;
- `partial` — transcription incomplete;
- `needs-review` — text exists but one or more verification gates remain open;
- `verified` — source transcription **and** independent high-resolution glyph second pass both closed under project policy;
- `blocked` — source evidence genuinely unavailable/insufficient after escalation.

If a systematic glyph error is discovered after pages were called verified, reopen affected coverage to `needs-review` and perform a retrospective high-resolution audit.

---

# 15. Reusable startup / closure checklist

Before transcribing:

- [ ] identify publication/edition and scan condition;
- [ ] inspect representative pages;
- [ ] determine whether historical typeforms occur;
- [ ] keep the 13-form reference available;
- [ ] record project-specific glyph policy;
- [ ] transcribe from source pixels, not OCR authority.

After initial transcription of each page:

- [ ] reopen the same page at native/high resolution;
- [ ] perform the independent 13-family second pass;
- [ ] compare same-edition examples when uncertain;
- [ ] record every correction with scan provenance;
- [ ] preserve source spelling/grammar/punctuation/spacing;
- [ ] avoid global replacements;
- [ ] leave unresolved pages `needs-review`;
- [ ] only then consider `verified`.

Before release/translation:

- [ ] complete work-level historical-glyph audit;
- [ ] confirm zero unexamined historical-family candidates;
- [ ] confirm every `verified` page has evidence of the second high-resolution pass.

---

# 16. Short rule to remember

> **Old shape ≠ modern look-alike. Transcribe first, then independently re-open the page at high resolution and prove the historical character identity before final verification.**
