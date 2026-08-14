# English Translation Plan — கிழவன் கனவு

## Status

**PLAN READY — PROSE TRANSLATION NOT YET STARTED**

Tamil source gate: **OPEN** after final story-body audit and assembly synchronization.

Controlling Tamil source for translation:

1. primary archival page records: `../../pages/0007-kizhavan-kanavu-01.md` through `../../pages/0022-kizhavan-kanavu-16.md`;
2. synchronized reading layer: `../../sections/kizhavan-kanavu.md`;
3. audit record: `../../audit.md`;
4. final assembly review: `../../ASSEMBLY_REVIEW.md`;
5. publisher errata layer: `../../sections/kizhavan-kanavu-errata.md` — **reference only, never silently substituted into the archival translation**.

The supplied physical scan remains the ultimate authority for this edition.

## Translation scope

Current English scope is the **story body only: scans 7–22**.

Not included in the current translation scope:

- cover;
- reviews;
- publisher/editorial notes;
- author note;
- scan 23 errata advertisement;
- commercial advertisements;
- back cover.

Front matter may be translated later as a separate task after its own source review.

## Final Tamil source disposition

Story scans: **16 / 16 audited**.

- `verified`: **12** — scans 7, 8, 9, 10, 11, 12, 13, 14, 16, 18, 19, 20
- `blocked`: **4** — scans 15, 17, 21, 22
- `needs-review`: **0** within the story body

The four blocked pages contain source gaps that cannot be recovered faithfully from the supplied physical copy.

## Mandatory source-gap rule

A `blocked-by-source` location must remain visible in English at the **same textual position**.

Do not:

- infer the missing Tamil from grammar or narrative context;
- reconstruct it from mythology/history;
- search for a probable quotation and silently insert it;
- borrow wording from another edition without separately documenting that edition;
- smooth over the gap by writing an English sentence that makes the passage appear complete.

Use a marker such as:

`[SOURCE BLOCKED — scan 15 / printed page 11: one word is illegible in the supplied copy]`

or:

`[SOURCE BLOCKED — scan 22 / printed page 18: text is physically obscured by a library stamp]`

The marker must be editorially distinguishable from translated prose.

## Known blocked locations

| Scan | Printed page | Translation treatment |
|---:|:---:|---|
| 15 | 11 | preserve one worn-word gap and one library-stamp-covered temple-history gap |
| 17 | 13 | preserve the short gap following `பார்வதியை` |
| 21 | 17 | preserve all four blocked political/historical readings individually |
| 22 | 18 | preserve the stamp-obscured final story phrase |

Publisher/printer footer gaps on scan 22 are outside the story translation and should not be inserted into the English story file.

## Printed errata policy

Scan 23 contains **10 publisher corrections**. They remain a separate edition layer.

The English archival translation must translate the visible story-page reading, not silently replace it with the publisher correction.

Example:

- scan 13 page text: `வைத்திருந்தான்`
- printed errata: `வைத்திருந்தாள்`

The translation should follow the archival page reading in the main text and record the publisher correction separately in an English translator/editor note file.

Planned file:

- `ERRATA_NOTES.md`

No errata correction should enter the translated prose without an explicit editorial layer.

## Translation principles

### 1. Fidelity before fluency

Preserve the meaning, rhetorical movement, repetition, irony, satire, polemic and emotional intensity of the Tamil. Do not rewrite the story into contemporary English fiction.

### 2. Do not modernize the source ideologically or linguistically

Historical expressions, religious references, caste terminology, political language, social criticism, sexual insinuation and polemical vocabulary must not be softened or replaced merely because present-day English might prefer different phrasing.

Where an expression would mislead a modern reader if translated literally, use the closest faithful English and document the issue in translation notes rather than silently rewriting the source.

### 3. Preserve structure

- retain paragraph boundaries;
- retain dialogue sequence;
- preserve emphatic repetition;
- preserve visible source-page markers in comments;
- preserve abrupt page continuations where relevant to traceability, while allowing normal English word joining when the Tamil word itself was mechanically split across scans.

### 4. Proper names and titles

Use one consistent Romanization for recurring names while preserving recognizable historical forms.

Initial working forms:

- விபுலானந்தர் — **Vipulanandar**
- மல்லிகா — **Mallika**
- லெனின் — **Lenin**
- வீராசாமி — **Veerasami**
- ராஜம் — **Rajam**
- மார்க்கண்டேய சாஸ்திரிகள் / மார்க்கண்டேயர் — **Markandeya Sastri / Markandeyar**, according to the source form and context
- ராமசாமிப்பெரியார் — **Ramasami Periyar**

Do not silently collapse source distinctions in titles/honorific forms. Final spelling consistency must be reviewed before release.

### 5. Culture-specific terms

Do not over-explain inside the prose. Translate when a clear English equivalent exists; otherwise use a stable transliteration and, only where necessary, a concise translator note.

Possible note candidates include terms such as:

- `ஸ்தல வரலாறு`
- `ராவ்பகதூர்`
- `சமதர்ம சங்கநாதம்`
- religious/mythological references whose rhetorical function depends on the period context.

Notes must explain, not reinterpret.

### 6. Quotes and slogans

Preserve their rhetorical character. A slogan, sarcastic line or political proclamation should sound like one in English; do not turn it into neutral explanatory prose.

### 7. Unusual source wording

When Tamil wording is unusual but verified, translate what it says rather than silently correcting what the translator thinks it intended to say. If the verified Tamil itself remains semantically difficult, flag it for translation review.

## File structure

Planned translation workspace:

```text
translations/en/
  README.md
  TRANSLATION_PLAN.md
  SOURCE_MAP.md
  ERRATA_NOTES.md
  batches/
    01-scans-07-10.md
    02-scans-11-14.md
    03-scans-15-18.md
    04-scans-19-22.md
  kizhavan-kanavu-en.md
  EDITORIAL_CONSISTENCY_REVIEW.md
  RELEASE_REPORT.md
```

Only `TRANSLATION_PLAN.md`, `README.md`, and `SOURCE_MAP.md` should exist before translation drafting begins. Other files are created when their stage is reached.

## Batch order

### Batch 1 — scans 7–10

- story opening;
- philosophical/religious satire dialogue;
- introduction of Lenin;
- no source-blocked passages.

### Batch 2 — scans 11–14

- Vipulanandar–Mallika backstory;
- Rajam and Veerasami;
- Markandeya Sastri dream passage;
- no remaining source-blocked passages after final audit.

### Batch 3 — scans 15–18

- temple episode;
- imprisonment / attempted abduction;
- Veerasami's intervention and death;
- contains source-blocked passages on scans **15** and **17**.

### Batch 4 — scans 19–22

- Mallika and Vipulanandar reunited;
- return to Lenin and the political dream/vision;
- conclusion;
- contains source-blocked passages on scans **21** and **22**.

## Per-batch workflow

For each batch:

1. read the corresponding final page records, not only the assembled file;
2. draft English with source-scan boundary comments retained;
3. verify every paragraph against the Tamil page record;
4. audit names, pronouns, tense and rhetorical tone;
5. verify that every `blocked-by-source` marker is preserved where applicable;
6. compare against the synchronized Tamil assembly for omissions/duplications;
7. mark the batch `draft`, then `source-reviewed` only after the comparison is complete.

Do not advance a batch to `source-reviewed` merely because the English reads smoothly.

## Batch header template

Each batch should begin with metadata similar to:

```yaml
---
story: "kizhavan-kanavu"
language: "en"
source_scans: [7, 8, 9, 10]
status: "draft"
translation_basis: "final audited Tamil page records"
blocked_source_locations: 0
---
```

For batches 3 and 4, `blocked_source_locations` must reflect the actual count/locations represented in the batch.

## Source traceability

Retain comments such as:

```html
<!-- source scan 7; printed page — -->
<!-- source scan 8; printed page 4 -->
```

This lets reviewers compare any English passage directly with its Tamil page record.

## Translation review gates

### Gate A — batch source review

All four batches must be source-reviewed independently.

### Gate B — assembled English review

After all batches pass Gate A, assemble them into `kizhavan-kanavu-en.md` and verify:

- 16 / 16 story scans represented;
- no duplication;
- no omitted paragraph;
- all blocked markers retained;
- page-marker order correct.

### Gate C — editorial consistency

Create `EDITORIAL_CONSISTENCY_REVIEW.md` and review:

- recurring names/titles;
- religious and political terminology;
- tense and narrative voice;
- quotation/dialogue style;
- recurring metaphors;
- treatment of caste/social vocabulary;
- blocked-source marker wording;
- errata-note consistency.

Editorial consistency must not become source normalization.

### Gate D — release review

Create `RELEASE_REPORT.md` documenting:

- translated source range;
- Tamil source status;
- blocked passages;
- errata treatment;
- unresolved translation questions, if any;
- final file inventory;
- confirmation that no source PDF is stored in GitHub.

## Translation completion definition

English translation is complete only when:

- all four batches are source-reviewed;
- the assembled English file contains scans 7–22 exactly once;
- blocked source gaps remain explicit;
- publisher errata remains separately documented;
- editorial consistency review passes;
- release report is complete.

## Next activity after this plan

Create `README.md` and `SOURCE_MAP.md` for the English translation workspace, then begin **Batch 1 — scans 7–10** only. Do not jump ahead to later batches before Batch 1 receives its source review.
