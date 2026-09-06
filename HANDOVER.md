# HANDOVER — Kalaignar Short Stories Archive

## Repository

- repository: `pugazg/kalaignar-short-stories`
- branch: `main`
- story workflow: `SHORT_STORY_PROCESSING_GUIDE.md`
- collection workflow: `COLLECTION_SOURCE_GUIDE.md`
- English workflow: `ENGLISH_TRANSLATION_GUIDE.md`

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

- `நண்பனா?`: **3/3 verified**, Tamil audit PASS, visual PASS, 0 unresolved, English not started.
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

English for these five remains a separate future phase.

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

## CURRENT STATE / NEXT ACTIVITY

There is **no automatic next story in the 2009 queue**. Both its new-story onboarding and existing-canonical witness comparison phases are closed.

Do not automatically start:

- English translation of the five newly onboarded stories;
- canonical corrections from 2009 witness readings;
- `நடுத்தெரு நாராயணி` as a short story;
- another collection or source.

Wait for the user's next authorized activity. If the user supplies the 1977 controlling PDF and explicitly asks to resolve the recheck candidates, that can be a separate source-correction phase. `நடுத்தெரு நாராயணி` remains a separate short-novel project.