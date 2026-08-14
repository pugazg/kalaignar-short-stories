# Assembly consistency review — கிழவன் கனவு

## Current review state

**RE-SYNC REQUIRED AFTER FINAL SOURCE AUDIT**

The earlier assembly review passed against the then-current page records. A subsequent final high-resolution unresolved-reading pass changed the authoritative story page layer, so `sections/kizhavan-kanavu.md` must now be synchronized and this review rerun before it can return to `PASS`.

The controlling source remains `TVA_BOK_0014165_கிழவன்_கனவு.pdf`.

## What remains structurally valid

- Story body source range remains scans **7–22**.
- All **16** story scan pages are represented in the existing assembly and remain in source order.
- Source-page boundary comments remain present.
- Scan **23** errata is a separate layer and is not merged into story prose.
- Scans **24–26** advertisements/back cover remain outside the story assembly.
- Scan 7 printed page remains `—`; `(3)` is not inferred.
- Scan 8 = printed `(4)` through scan 22 = printed `(18)`.

## Final page-layer changes that the assembly must absorb

### Newly resolved

| Scan | Printed page | Final page-record reading |
|---:|---:|---|
| 8 | 4 | `பூகோள பூரணர்த்திக` |
| 14 | 10 | `என் நெற்றியை?`; `திராட்சையைச் சாப்பிடேன்`; `மந்த காசத்தினிடையே` |
| 18 | 14 | `விட்டிருந்து` |

### Final `blocked-by-source` locations

| Scan | Printed page | Source limitation |
|---:|---:|---|
| 15 | 11 | one worn/indistinct word + temple-history text physically covered by library stamp |
| 17 | 13 | one short indistinct phrase after `பார்வதியை` |
| 21 | 17 | four short indistinct political/historical readings |
| 22 | 18 | library-stamp-obscured final story phrase and footer/imprint |

These four pages are fully audited and now have terminal `blocked` status for this source copy. The assembly must copy the page records' `blocked-by-source` markers rather than retain older generic `[வாசிப்பு தெளிவில்லை]` text.

## Current source-layer status

- Story scans 7–22 directly audited: **16 / 16**
- Story scans `verified`: **12** — 7, 8, 9, 10, 11, 12, 13, 14, 16, 18, 19, 20
- Story scans `blocked`: **4** — 15, 17, 21, 22
- Story scans `needs-review`: **0**
- Printed errata rows mapped: **10 / 10**
- Whole-publication page status: **20 verified / 4 blocked / 2 front-matter needs-review**

## Errata-layer consistency

The errata policy remains unchanged:

1. archival page reading = what the story page visibly prints;
2. printed errata = publisher correction from scan 23.

Do **not** silently apply errata to `sections/kizhavan-kanavu.md`.

Scan 13 remains the clearest example: page reads **`வைத்திருந்தான்`** while the printed errata says **`வைத்திருந்தாள்`**.

## Translation gate

**CONDITIONALLY OPEN, BUT ASSEMBLY SYNC MUST PASS FIRST.**

The story-body source audit is complete to the limit of the supplied physical source. Translation can proceed after the assembly is synchronized and this consistency review is rerun, provided every `blocked-by-source` gap is preserved explicitly and no missing Tamil is guessed.

## Next exact activity

1. Synchronize `sections/kizhavan-kanavu.md` with the final page records for scans 8, 14, 15, 17, 18, 21 and 22.
2. Recheck all scan markers 7–22 for order and duplication.
3. Verify all 10 scan-23 errata entries remain separate.
4. Rerun this consistency review and restore `PASS` only when page records and assembly match exactly at all changed locations.
5. Then create the English translation plan/workflow; do not translate prose before the synchronization check passes.
