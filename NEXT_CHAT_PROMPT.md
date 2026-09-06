# NEXT CHAT PROMPT — Kalaignar Short Stories Archive — supplemental English / அணில் குஞ்சு

Continue directly in `pugazg/kalaignar-short-stories`, branch `main`.

## LIVE MAIN IS AUTHORITATIVE

Fetch live `main` first. Preserve newer durable work. Do not reopen a closed phase merely because a copied prompt or prior chat contains an older checkpoint.

## Mandatory startup

Read before translation-dependent writes:

1. `ENGLISH_TRANSLATION_GUIDE.md`
2. `SHORT_STORY_PROCESSING_GUIDE.md`
3. `COLLECTION_SOURCE_GUIDE.md`
4. `HANDOVER.md`
5. this `NEXT_CHAT_PROMPT.md`
6. `NEW_STORY_ENGLISH_TRANSLATION_PROGRESS.md`
7. `collections/2009-16-kathaiyinile/README.md`
8. `stories/anil-kunju/README.md`
9. `stories/anil-kunju/sections/anil-kunju.md`
10. `stories/anil-kunju/indexes/page-map.md`
11. all `stories/anil-kunju/pages/*.md` records
12. `stories/anil-kunju/audit.md`
13. `stories/anil-kunju/POSSIBLE_ERRORS_FOR_REVIEW.md`
14. `stories/anil-kunju/visual-fidelity.md`

## Closed phases — do not reopen

- 1977 canonical anthology: Tamil/visual/English **37/37 PASS**.
- 2008 collection: Tamil/visual/English **40/40 PASS**.
- 2004 collection: Tamil/visual/English **34/34 PASS**.
- 2009 new-story Tamil onboarding: **5/5 COMPLETE / CLOSED**.
- 2009 existing-canonical additional-witness comparison: **11/11 COMPLETE / CLOSED**.

The 2009 comparison ledger is:

`collections/2009-16-kathaiyinile/ADDITIONAL_WITNESS_COMPARISON.md`

Do not use later-edition witness readings to silently modify canonical 1977 Tamil/English.

## ACTIVE PHASE — supplemental English translation — 2 / 6

This phase covers the six Tamil-complete stories that lacked English when the user authorized the phase.

1. `நண்பனா?` — **PASS**.
2. `காந்தி தேசம்` — **PASS**.
3. `அணில் குஞ்சு` — **NEXT / pending**.
4. `கொள்ளைபுரம்` — pending.
5. `எழுத்தாளர் ஏகலைவன்` — pending.
6. `மலரவில்லை` — pending.

Tracker: `NEW_STORY_ENGLISH_TRANSLATION_PROGRESS.md`.

### Completed 1 / 6 — `நண்பனா?`

- source: 1997 `திராவிட இயக்க எழுத்தாளர் சிறுகதைகள்`
- scans **104–106 / printed 94–96**
- English: `stories/nanbana/translations/en/nanbana.md`
- review: `stories/nanbana/TRANSLATION_REVIEW.md`
- translation result: **PASS**
- physical source-page anchoring: **PASS**
- Tamil changed during translation: **No**

### Completed 2 / 6 — `காந்தி தேசம்`

- source: 2009 `16 கதையினிலே`
- scans **6–18 / printed 1–13**
- English: `stories/gandhi-desam/translations/en/gandhi-desam.md`
- review: `stories/gandhi-desam/TRANSLATION_REVIEW.md`
- translation result: **PASS**
- physical source-page anchoring: **PASS — 13/13**
- Sornambikai letter / telegram / Bombay revelation: **complete**
- source recheck queue silently corrected: **No**
- Tamil changed during translation: **No**

## CURRENT EXACT ACTIVITY — supplemental English 3 / 6 — `அணில் குஞ்சு`

Source/canonical coordinates:

- source collection: **`16 கதையினிலே`**, Fourth Edition, March 2009
- source filename: `TVA_BOK_0065745_16_கதையினிலே.pdf`
- registered SHA-256: `21daed58600d2e927dec4341fd1e0eab597f12d50f8c444458de9bc4ad18a859`
- story: **`அணில் குஞ்சு`**
- collection item: **2 / 16**
- scans: **19–28**
- printed pages: **14–23**
- canonical workspace: `stories/anil-kunju/`
- next-story boundary: scan **29**, opening `கொள்ளைபுரம்`

Required procedure:

1. confirm the Tamil/source and visual-fidelity gates remain PASS and no unresolved story text has appeared on newer live `main`;
2. read the complete canonical Tamil assembly and every persistent recheck item before translating;
3. translate the verified Tamil actually preserved in the repository — do not import outside corrections or normalize suspicious Tamil forms;
4. create `stories/anil-kunju/translations/en/anil-kunju.md` with source-page markers aligned to the actual physical Tamil page transitions;
5. preserve meaningful dialogue, quotations, display structure, names and source-significant repetition without inserting outside explanation;
6. create `stories/anil-kunju/TRANSLATION_REVIEW.md` documenting title treatment, difficult choices, marker presence/order and physical content-boundary alignment separately;
7. if translation exposes a likely Tamil issue, reopen that exact Tamil source span before changing anything; do not correct Tamil from English expectation;
8. update the story README, 2009 collection controls as relevant, root README, `NEW_STORY_ENGLISH_TRANSLATION_PROGRESS.md`, `HANDOVER.md` and this prompt to **3 / 6 complete**;
9. re-fetch live `main` and changed controls before declaring closure;
10. stop before `கொள்ளைபுரம்` unless the user explicitly expands the batch.

`நடுத்தெரு நாராயணி` remains reserved for separate short-novel handling and is outside this short-story English queue.
