# Assembly consistency review — கிழவன் கனவு

## Review result

**PASS — FINAL TAMIL STORY ASSEMBLY SYNCHRONIZED**

The assembled Tamil reading layer has been regenerated from the final-audited page records and rechecked after the high-resolution unresolved-reading pass.

Controlling source: `TVA_BOK_0014165_கிழவன்_கனவு.pdf`.

## Scope checked

- `sections/kizhavan-kanavu.md`
- `sections/kizhavan-kanavu-errata.md`
- story page records `pages/0007-...` through `pages/0022-...`
- scan 23 errata page
- `audit.md`
- `indexes/page-map.md`

## Assembly coverage

**PASS**

- Story body begins at scan **7** and concludes at scan **22**.
- All **16 / 16** story scan pages are represented exactly once and in source order.
- Every source-page boundary remains visible as an HTML marker.
- Scan 7 retains printed page `—`; `(3)` is not inferred.
- Scan 8 = printed page `(4)`, continuing sequentially through scan 22 = `(18)`.
- Scan 23 errata/advertisement is not merged into story prose.
- Scans 24–26 advertisements/back cover are not merged into story prose.

## Final page-layer synchronization

**PASS**

The assembly now contains the final source-supported readings resolved in the last high-resolution pass:

| Scan | Printed page | Final reading synchronized into assembly |
|---:|---:|---|
| 8 | 4 | `பூகோள பூரணர்த்திக` |
| 14 | 10 | `என் நெற்றியை?` |
| 14 | 10 | `திராட்சையைச் சாப்பிடேன்` |
| 14 | 10 | `மந்த காசத்தினிடையே` |
| 18 | 14 | `விட்டிருந்து` |

No older generic unresolved marker remains at those resolved locations.

## Source-blocked synchronization

**PASS**

The four terminal source-limited story pages are copied into the assembly with explicit `blocked-by-source` markers:

| Scan | Printed page | Final limitation |
|---:|---:|---|
| 15 | 11 | one worn/indistinct word and temple-history wording physically covered by a circular library stamp |
| 17 | 13 | one short worn/indistinct phrase after `பார்வதியை` |
| 21 | 17 | four short worn/indistinct readings in the political/historical catalogue |
| 22 | 18 | final story phrase physically obscured by library stamp |

The publisher/printer/footer material on scan 22 is outside the assembled story text and remains documented at page level.

No context, later edition, web transcription, historical memory or semantic reconstruction has been used to fill any blocked location.

## Story-source disposition

- Story scans directly audited: **16 / 16**
- Story scans `verified`: **12** — 7, 8, 9, 10, 11, 12, 13, 14, 16, 18, 19, 20
- Story scans `blocked`: **4** — 15, 17, 21, 22
- Story scans `needs-review`: **0**
- Whole-publication status: **20 verified / 4 blocked / 2 front-matter needs-review**

The two remaining `needs-review` records are front-matter scans **3–4** and do not belong to the story-body translation source.

## Errata-layer consistency

**PASS**

`sections/kizhavan-kanavu-errata.md` continues to preserve all **10 / 10** corrections printed on scan 23 as a separate layer.

The assembled archival reading does **not** silently apply those corrections. The intended distinction remains:

1. archival page reading — what the story page visibly prints;
2. publisher errata — the correction printed on scan 23.

Example: scan 13 visibly prints **`வைத்திருந்தான்`** while the publisher errata says **`வைத்திருந்தாள்`**. Both remain separately documented.

## Repository-policy consistency

**PASS**

- Source PDF is not committed to GitHub.
- Page records remain the primary archival layer.
- The assembled Tamil text is explicitly a derived reading layer.
- Historical/unusual source forms are not silently modernized.
- Source-blocked wording is not guessed.
- Errata remains separate.
- Commercial advertisements and physical-copy marks remain outside story prose.

## Translation gate

**OPEN — CONTROLLED ENGLISH TRANSLATION MAY BEGIN.**

The Tamil story source is now stable to the limit of the supplied physical copy. English translation may proceed under these mandatory conditions:

- translate only source-supported Tamil;
- preserve every `blocked-by-source` location explicitly and do not invent English wording for it;
- do not silently translate the publisher's errata correction in place of the archival page reading;
- keep a source-page mapping so every English passage can be traced to scans 7–22;
- front matter remains outside the current story-body translation scope unless separately commissioned.

## Next exact activity

Create the English translation workflow/plan under `translations/en/` before translating prose. Define file structure, batch order, treatment of blocked source gaps, errata policy, fidelity/style rules, and review gates. Translation prose should begin only after that plan exists.
