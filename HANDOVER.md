# HANDOVER — Kalaignar Short Stories Archive

## Repository

- repository: `pugazg/kalaignar-short-stories`
- branch: `main`
- story workflow: `SHORT_STORY_PROCESSING_GUIDE.md`
- collection workflow: `COLLECTION_SOURCE_GUIDE.md`
- English workflow: `ENGLISH_TRANSLATION_GUIDE.md`
- supplemental English tracker: `NEW_STORY_ENGLISH_TRANSLATION_PROGRESS.md`

## LIVE MAIN IS AUTHORITATIVE

Always fetch live `main` first and preserve newer durable state.

## Permanent rules

- controlling scan first; no silent normalization;
- shared physical boundaries must remain exact;
- an additional edition witness must not silently overwrite a canonical controlling edition;
- textual differences belong in explicit comparison/audit records;
- if a later witness appears to correct a canonical reading, reopen the exact canonical controlling scan before changing Tamil/English/control layers;
- source PDFs are not committed.

## Closed canonical collection phases

- **1977 — கலைஞர் கருணாநிதியின் சிறுகதைகள்:** Tamil 37/37, visual 37/37, English 37/37, final QA PASS, unresolved 0.
- **2008 — கலைஞர் சொன்ன கதைகள்:** Tamil 40/40, visual 40/40, English 40/40, final QA PASS, unresolved 0.
- **2004 — கலைஞரின் குட்டிக் கதைகள்:** Tamil 34/34, visual 34/34, English 34/34, final QA PASS, unresolved 0.

Do not reopen those closed phases merely to create work. A specifically authorized independent-witness comparison is distinct from reopening a canonical source pass.

## 1997 source — `திராவிட இயக்க எழுத்தாளர் சிறுகதைகள்`

Workspace: `collections/1997-dravida-iyakka-ezhuthalar-sirukathaigal/`

- `நண்பனா?`: **3/3 verified**, Tamil audit PASS, visual PASS, 0 unresolved, **English PASS**.
- English file: `stories/nanbana/translations/en/nanbana.md`
- translation review / physical page anchoring: **PASS**
- `நடுத்தெரு நாராயணி`: **explicitly reserved for separate short-novel handling**.
- new-short-story onboarding: **COMPLETE**.

## 2009 source — `16 கதையினிலே`

Workspace: `collections/2009-16-kathaiyinile/`

- source: `TVA_BOK_0065745_16_கதையினிலே.pdf`
- SHA-256: `21daed58600d2e927dec4341fd1e0eab597f12d50f8c444458de9bc4ad18a859`
- registered size: **384,978,955 bytes**
- registered scans: **183**
- represented edition: **Fourth Edition, March 2009**
- TOC: **16 stories**
- story block: scans **6–182**
- scan **183**: back cover
- source completeness: **16 / 16 physically present**
- preserved anomaly: scan 110 / printed p105 still closes `குப்பைத் தொட்டி`; `சங்கிலிச்சாமி` begins scan 111 despite the TOC assigning p105 to it.

A conversation working copy used in the final comparison iteration ends at scan **150**. It does not replace the registered 183-scan source. Wikimedia Commons independently records the same TVA file as 183 pages, and Tamil Wikisource has a proofread page set for that same `16 கதையினிலே.pdf` source through scan 182. Witness records after scan 150 explicitly preserve this provenance and avoid inventing unobserved glyph-level readings.

### New-story onboarding — COMPLETE / CLOSED — 5 / 5

- `காந்தி தேசம்` — scans 6–18 — 13/13 verified; Tamil/visual PASS; 0 unresolved.
- `அணில் குஞ்சு` — scans 19–28 — 10/10 verified; Tamil/visual PASS; 0 unresolved.
- `கொள்ளைபுரம்` — scans 29–37 — 9/9 verified; Tamil/visual PASS; 0 unresolved.
- `எழுத்தாளர் ஏகலைவன்` — scans 38–49 — 12/12 verified; Tamil/visual PASS; 0 unresolved.
- `மலரவில்லை` — scans 50–63 — 14/14 verified; Tamil/visual PASS; 0 unresolved.

## 2009 existing-canonical additional-witness comparison — COMPLETE / CLOSED — 11 / 11

Final ledger: `collections/2009-16-kathaiyinile/ADDITIONAL_WITNESS_COMPARISON.md`.

1. `சுமந்தவள்` — scans **64–81** — materially revised/expanded; added three-year epilogue on 80–81.
2. `புகழேந்தி` — scans **82–89** — same narrative/ending; strong lexical clarifications.
3. `நளாயினி` — scans **90–99** — same narrative; strong lexical clarifications; printed-note styling revised.
4. `குப்பைத் தொட்டி` — scans **100–110** — same narrative; strong lexical clarifications; p105 anomaly confirmed.
5. `சங்கிலிச்சாமி` — scans **111–125** — same narrative; devotional/dialogue regularization.
6. `தப்பிவிட்டார்கள்` — scans **126–136** — same narrative; spelling/verb-form modernization.
7. `தப்பவில்லை` — scans **137–149** — same narrative/final irony; editorial repagination.
8. `ஏழை` — scans **150–154** — same story/boundary; lexical assertions beyond local scan 150 kept deliberately conservative.
9. `கண்ணடக்கம்` — scans **155–163** — same narrative; strong later evidence including `வான மீனுக்கோ` ↔ `வாளை மீனுக்கோ` and `துணி ஏண்` ↔ `துணி ஏணை`.
10. `வாழ முடியாதவர்கள்` — scans **164–173** — same narrative; high-priority later clarification `கற்பினைக்...தீவிதி` ↔ `கற்பனைப்...தலைவிதி`.
11. `அய்யோ ராஜா` — scans **174–182** — same story/boundary; 2009 title punctuation differs from canonical `அய்யோ ராஜா!`; lexical disposition conservative where direct 2009 pixels were unavailable.

Every story has a durable witness directory under:

`stories/<canonical-slug>/witnesses/2009-16-kathaiyinile/`

### Canonical disposition

- canonical 1977 Tamil changed from 2009 evidence: **No**
- canonical 1977 English changed: **No**
- canonical verified page statuses changed: **No**
- reason: any apparent correction requires the exact 1977 controlling scan; that PDF was unavailable during the comparison phase

High-priority later-witness recheck candidates are preserved in the per-story witness records and final collection ledger.

## ACTIVE PHASE — supplemental English translation — 3 / 6

Tracker: `NEW_STORY_ENGLISH_TRANSLATION_PROGRESS.md`.

This phase was explicitly authorized after the 2009 onboarding/comparison closures. It covers the six Tamil-complete canonical stories that still lacked English at phase start.

1. `நண்பனா?` — 1997 source, scans **104–106 / printed 94–96** — **PASS**.
2. `காந்தி தேசம்` — 2009 source, scans **6–18 / printed 1–13** — **PASS**.
3. `அணில் குஞ்சு` — scans **19–28 / printed 14–23** — **PASS**.
4. `கொள்ளைபுரம்` — scans **29–37 / printed 24–32** — **NEXT / pending**.
5. `எழுத்தாளர் ஏகலைவன்` — scans **38–49 / printed 33–44** — pending.
6. `மலரவில்லை` — scans **50–63 / printed 45–58** — pending.

### Completed 1 / 6 — `நண்பனா?`

- English: `stories/nanbana/translations/en/nanbana.md`
- review: `stories/nanbana/TRANSLATION_REVIEW.md`
- physical source-page anchoring: **PASS**
- Tamil changed during translation: **No**
- result: **PASS**

### Completed 2 / 6 — `காந்தி தேசம்`

- English: `stories/gandhi-desam/translations/en/gandhi-desam.md`
- review: `stories/gandhi-desam/TRANSLATION_REVIEW.md`
- complete Tamil represented: **Yes**
- source page markers **6–18**: **complete and physically aligned**
- Sornambikai letter / telegram / Bombay reveal: **preserved**
- possible-error queue silently corrected: **No**
- Tamil changed during translation: **No**
- result: **PASS**

### Completed 3 / 6 — `அணில் குஞ்சு`

- English: `stories/anil-kunju/translations/en/anil-kunju.md`
- review: `stories/anil-kunju/TRANSLATION_REVIEW.md`
- complete Tamil represented: **Yes**
- source page markers **19–28**: **complete and physically aligned**
- public speeches / squirrel-Ramayana account / religious argument / hawk ending: **preserved**
- five closing ornaments: **preserved**
- possible-error queue silently corrected: **No**
- Tamil changed during translation: **No**
- result: **PASS**

## CURRENT EXACT NEXT ACTIVITY — supplemental English 4 / 6 — `கொள்ளைபுரம்`

Process only **`கொள்ளைபுரம்`** unless the user explicitly expands the batch:

1. fetch live `main` first;
2. read `ENGLISH_TRANSLATION_GUIDE.md`, this `HANDOVER.md`, `NEXT_CHAT_PROMPT.md`, `NEW_STORY_ENGLISH_TRANSLATION_PROGRESS.md`, and all `stories/kollaipuram/` Tamil/source/visual/recheck controls;
3. translate the complete verified Tamil assembly from scans **29–37 / printed pages 24–32**;
4. verify physical source-page anchoring against the story's `pages/*.md` records, not just marker sequence;
5. create/update `stories/kollaipuram/translations/en/kollaipuram.md` and `stories/kollaipuram/TRANSLATION_REVIEW.md`;
6. synchronize story, collection, root and phase controls to **4 / 6** when complete;
7. stop before `எழுத்தாளர் ஏகலைவன்` unless explicitly authorized otherwise.

Do not treat 2009 later-witness readings as permission to modify canonical 1977 Tamil. `நடுத்தெரு நாராயணி` remains outside the short-story queue and reserved for a separate short-novel workflow.
