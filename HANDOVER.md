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
- do one anthology story at a time unless the user explicitly changes that rule;
- source PDFs are not committed;
- English begins only after Tamil/source and visual-fidelity gates pass.

## Closed prior collections

- **1977 — கலைஞர் கருணாநிதியின் சிறுகதைகள்:** Tamil 37/37, visual 37/37, English 37/37, final English QA PASS, unresolved 0.
- **2008 — கலைஞர் சொன்ன கதைகள்:** Tamil 40/40, text fidelity 40/40, visual 40/40, English 40/40, final English QA PASS, unresolved 0.
- **2004 — கலைஞரின் குட்டிக் கதைகள்:** Tamil 34/34, visual 34/34, English 34/34, final English QA PASS, unresolved 0.

Do not reopen these closed phases merely to create work.

## New source 1 — 1997 `திராவிட இயக்க எழுத்தாளர் சிறுகதைகள்`

Workspace: `collections/1997-dravida-iyakka-ezhuthalar-sirukathaigal/`

- source: `TVA_BOK_0064315_திராவிட_இயக்க_எழுத்தாளர்_சிறுகதைகள்.pdf`
- SHA-256: `ead34f2d1e983568b79ef9d6185006844ee3e5d6443695633124975ecb77227c`
- size: **156,733,137 bytes**
- scans: **115**
- edition: **First Edition, December 1997**
- contents: **10 works**
- `நண்பனா?`: scans **104–106 / printed 94–96**, **3/3 verified**, Tamil audit PASS, visual PASS, 0 unresolved, English not started.
- `நடுத்தெரு நாராயணி`: explicitly deferred for separate short-novel handling; do not process in this short-story queue.

The 1997 new-short-story onboarding is complete.

## New source 2 — 2009 `16 கதையினிலே`

Workspace: `collections/2009-16-kathaiyinile/`

- source: `TVA_BOK_0065745_16_கதையினிலே.pdf`
- SHA-256: `21daed58600d2e927dec4341fd1e0eab597f12d50f8c444458de9bc4ad18a859`
- size: **384,978,955 bytes**
- scans: **183**
- represented edition: **Fourth Edition, March 2009**
- TOC: **16 stories**
- story block: scans **6–182**
- scan **183**: back cover
- physical story openings checked: **16 / 16**
- new short stories at intake: **5**
- canonical matches at intake: **11**
- source completeness: **complete — all 16 stories present**
- preserved anomaly: TOC places `சங்கிலிச்சாமி` at p105, while physical p105 on scan 110 still closes `குப்பைத் தொட்டி`; `சங்கிலிச்சாமி` begins on scan 111.

The earlier 150-scan / incomplete-source statement is incorrect and superseded.

### Completed new stories — 5 / 5

- `காந்தி தேசம்` — `stories/gandhi-desam/` — scans **6–18 / printed 1–13** — **13/13 verified**, Tamil audit PASS, visual PASS, 0 unresolved, English not started.
- `அணில் குஞ்சு` — `stories/anil-kunju/` — scans **19–28 / printed 14–23** — **10/10 verified**, Tamil audit PASS, visual PASS, 0 unresolved, English not started.
- `கொள்ளைபுரம்` — `stories/kollaipuram/` — scans **29–37 / printed 24–32** — **9/9 verified**, Tamil audit PASS, visual PASS, 0 unresolved, English not started.
- `எழுத்தாளர் ஏகலைவன்` — `stories/ezhuthalar-ekalaivan/` — scans **38–49 / printed 33–44** — **12/12 verified**, Tamil audit PASS, visual PASS, 0 unresolved, English not started.
- `மலரவில்லை` — `stories/malaravillai/` — scans **50–63 / printed 45–58** — **14/14 verified**, Tamil audit PASS, visual PASS, 0 unresolved, English not started. Scan **63** closes with five circular ornaments; scan **64** opens `சுமந்தவள்` and is excluded.

`மலரவில்லை` has a complete verified page layer, `sections/malaravillai.md`, closed recheck queue, Tamil audit PASS and visual-fidelity PASS. Source-close readings are documented in its audit; do not silently normalize them or reopen the story without new evidence.

New-story processing state for the 2009 source: **5 / 5 COMPLETE / PASS**.

## Current exact state / stop boundary

The requested new-short-story onboarding phase is closed. There is **no active onboarding story**.

Do not automatically begin any of the following:

1. `சுமந்தவள்` — it already has a canonical workspace and scan 64 was used only as the `மலரவில்லை` boundary witness;
2. additional-witness comparison for the eleven pre-existing canonical stories in the 2009 anthology;
3. English translation for `நண்பனா?` or the five newly onboarded 2009 stories;
4. `நடுத்தெரு நாராயணி` as a short story — it remains reserved for separate short-novel handling.

Await explicit user direction for the next phase. Any future source-dependent work must begin by fetching live `main` and reading the relevant permanent guides and current controls.
