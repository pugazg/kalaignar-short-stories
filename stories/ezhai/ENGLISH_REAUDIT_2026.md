# English Re-Audit 2026 — ஏழை

## Scope

- anthology story: **15 / 37**
- final Tamil authority: `sections/ezhai.md`
- verified Tamil pages: scans **115–118 / printed 106–109**
- English: `translations/en/ezhai.md`
- gate: **E1 — completeness / physical-page alignment**

## Gate state

- E1: **PASS**
- E2: **PASS**
- E3: **PASS**
- E4: **PASS**
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


## E2 — meaning fidelity

**PASS — complete sentence-by-sentence comparison against the final canonical Tamil.**

The complete English was checked sentence-by-sentence against the final canonical Tamil, including the 2026 `விநாடிகூட` repair and the E1 de-duplication across 115→116. No E2 prose repair was required. The contrast between the employer couple's leisure and Parvathi's deprivation, her desire to meet her husband, the nose-stud/kiss fantasy, storm imagery, class satire, Banu rescue and Parvathi's abandonment/death remain semantically intact. Opaque cultural/source-close `kaappa bag` is left for E3 terminology work rather than guessed here.

- English fidelity repairs: **0**
- Tamil/source reopened: **No**
- Tamil changed: **No**
- unresolved E2 issues: **0**
- E2 result: **PASS**

Programme next activity remains the next anthology story in E2 order.


## E3 — terminology / names / cultural consistency

**PASS.**

Personal names **Parvathi, Banu, Nallakkannu Pillai** and **Karunambal** are stable throughout the story. **Parvathi** is a human character name here and is deliberately not mechanically rewritten to the deity convention **Parvati**. Culturally marked **Aththaan, Appa, Ayyo** and the source-close `kaappa bag` remain as established. No E3 repair was required.

- E3 English repairs: **0**
- Tamil/source reopened: **No**
- unresolved E3 issues: **0**
- E3 result: **PASS**


## E4 — English quality without changing meaning

**PASS.**

One readability repair removed a redundant literal construction while preserving the source's point that the child's play repeatedly interrupts the couple's private leisure.

- E4 English-quality repairs: **1**
- Tamil changed: **No**
- E2/E3 decisions altered: **No**
- source reopened: **No**
- unresolved E4 issues: **0**
- E4 result: **PASS**
