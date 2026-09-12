# English Re-Audit 2026 — ஏழை

## Scope

- anthology story: **15 / 37**
- final Tamil authority: `sections/ezhai.md`
- verified Tamil pages: scans **115–118 / printed 106–109**
- English: `translations/en/ezhai.md`
- gate: **E1 — completeness / physical-page alignment**

## Gate state

- E1: **PASS**
- E2: **PENDING**
- E3: **PENDING**
- E4: **PENDING**
- E5: **PENDING**

## E1 result

- physical pages represented: **4/4**
- source-page markers present/in order: **4/4 PASS**
- omitted Tamil story spans: **0**
- duplicated English story spans after repair: **0**
- non-adjacent moved story spans after repair: **0**
- unsupported added story content after repair: **0**
- E1 repairs: **1 page-anchor/content de-duplication repair**
- Tamil/source reopened: **No**
- unresolved E1 issues: **0**

One clear E1 defect was repaired at 115→116. The Tamil physical split is `...ஒரு சில நிமிடங்கள் கூட ஒதுக்க` → `முடியவில்லை.`. The English had already expressed the full negative before the marker and then added a second `They cannot.` after it. The sentence was minimally reshaped so the continuation remains adjacent and the redundant duplicate assertion is removed.

The next anthology story remains excluded.

## Regression check

Corrected state: **PASS**. Reconstructed prior marker/content pattern: **FAIL — page anchoring/completeness**. Restored corrected state: **PASS**.

## Disposition

**E1 PASS.** E2 remains pending until anthology-wide E1 is complete.
