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

### Completed new stories

- `காந்தி தேசம்` — `stories/gandhi-desam/` — scans **6–18 / printed 1–13** — **13/13 verified**, Tamil audit PASS, visual PASS, 0 unresolved, English not started.
- `அணில் குஞ்சு` — `stories/anil-kunju/` — scans **19–28 / printed 14–23** — **10/10 verified**, Tamil audit PASS, visual PASS, 0 unresolved, English not started.
- `கொள்ளைபுரம்` — `stories/kollaipuram/` — scans **29–37 / printed 24–32** — **9/9 verified**, Tamil audit PASS, visual PASS, 0 unresolved, English not started.
- `எழுத்தாளர் ஏகலைவன்` — `stories/ezhuthalar-ekalaivan/` — scans **38–49 / printed 33–44** — **12/12 verified**, Tamil audit PASS, visual PASS, 0 unresolved, English not started.

### Active story — `மலரவில்லை`

Canonical workspace now exists: `stories/malaravillai/`. **Do not recreate it.**

- printed pages: **45–58**
- scans: **50–63**
- scan **50** opens `மலரவில்லை`
- scan **63 / printed 58** contains the conclusion and five circular closing ornaments
- scan **64** opens `சுமந்தவள்` and is excluded
- page-coordinate records: **14 / 14 present**
- page status: **14 / 14 `needs-review`**
- verified Tamil pages: **0 / 14**
- Tamil assembly: **not yet created**
- Tamil audit: **PENDING**
- visual-fidelity closure: **PENDING**; physical boundary/layout checks recorded
- English: **not started**

The page records intentionally contain no guessed/OCR-reconstructed prose. They are a durable source-coordinate checkpoint only. Fill each page from direct visual comparison with the controlling scan and promote to `verified` only after full-span difficult-reading checks.

New-story processing state for the 2009 source: **4 / 5 complete + 1 / 5 in progress**.

## Current exact next activity

Continue **`மலரவில்லை` only**:

1. fetch live `main`; preserve the existing `stories/malaravillai/` workspace;
2. read the permanent guides, this handover, `NEXT_CHAT_PROMPT.md`, the 2009 collection controls, and `stories/malaravillai/README.md`;
3. fill and directly verify the 14 page records for scans **50–63 / printed 45–58** from the controlling PDF;
4. apply the exhaustive difficult-reading protocol; do not infer from OCR, memory, or context;
5. build `sections/malaravillai.md` only from verified page text and audit it back against all scans;
6. close Tamil audit and visual fidelity only when justified;
7. synchronize collection/root controls and then mark the five new 2009 stories **5 / 5 complete**;
8. do **not** begin `சுமந்தவள்`, English translation, or additional-witness comparison in the same activity;
9. do **not** process `நடுத்தெரு நாராயணி` as a short story.
