# HANDOVER — Kalaignar Short Stories Archive

## Repository

- repository: `pugazg/kalaignar-short-stories`
- branch: `main`
- story workflow: `SHORT_STORY_PROCESSING_GUIDE.md`
- collection workflow: `COLLECTION_SOURCE_GUIDE.md`
- English workflow: `ENGLISH_TRANSLATION_GUIDE.md`

## LIVE MAIN IS AUTHORITATIVE

Always fetch live `main` first. Preserve newer durable state.

## Permanent rules

- controlling scan first; no silent normalization;
- shared physical boundaries must remain exact;
- do one anthology story at a time unless the user explicitly changes that rule;
- source PDFs are not committed;
- English begins only after Tamil/source and visual-fidelity gates pass.

## Closed prior collections

- **1977 — கலைஞர் கருணாநிதியின் சிறுகதைகள்:** Tamil 37/37, visual 37/37, English 37/37, final English QA PASS, unresolved 0.
- **2008 — கலைஞர் சொன்ன கதைகள்:** Tamil 40/40, text fidelity 40/40, visual 40/40, English 40/40, final English QA PASS, unresolved 0.
- **2004 — கலைஞரின் குட்டிக் கதைகள்:** Tamil 34/34, visual 34/34, English 34/34, final English QA PASS, unresolved 0. Final story scan 49 / printed 48; scan 50 back cover.

Do not reopen these closed phases merely to create work.

## New source 1 — 1997 `திராவிட இயக்க எழுத்தாளர் சிறுகதைகள்`

Workspace: `collections/1997-dravida-iyakka-ezhuthalar-sirukathaigal/`

- source: `TVA_BOK_0064315_திராவிட_இயக்க_எழுத்தாளர்_சிறுகதைகள்.pdf`
- SHA-256: `ead34f2d1e983568b79ef9d6185006844ee3e5d6443695633124975ecb77227c`
- size: **156,733,137 bytes**
- scans: **115**
- edition: **First Edition, December 1997**
- contents: **10 works**
- all 10 opening scans checked
- canonical story matches: **8**
- new short story: **`நண்பனா?`** — scans **104–106 / printed 94–96**
- **`நடுத்தெரு நாராயணி` is excluded from the short-story queue by user instruction and will be handled separately as a short-novel work.**

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
- new short stories: **5**
- canonical matches: **11**
- source completeness: **complete — all 16 stories present**
- final spans: `ஏழை` 150–154; `கண்ணடக்கம்` 155–163; `வாழ முடியாதவர்கள்` 164–173; `அய்யோ ராஜா` 174–182.
- preserved anomaly: TOC places `சங்கிலிச்சாமி` at p105, while physical p105 on scan 110 still closes `குப்பைத் தொட்டி`; heading is scan 111.

The earlier 150-scan / incomplete-source statement was incorrect and has been superseded.

## New short-story queue

1. `நண்பனா?` — scans 104–106 / printed 94–96
2. `காந்தி தேசம்` — scans 6–18 / printed 1–13
3. `அணில் குஞ்சு` — scans 19–28 / printed 14–23
4. `கொள்ளைபுரம்` — scans 29–37 / printed 24–32
5. `எழுத்தாளர் ஏகலைவன்` — scans 38–49 / printed 33–44
6. `மலரவில்லை` — scans 50–63 / printed 45–58

## Current exact next activity

Process **`நண்பனா?`** only:

1. confirm no canonical workspace has appeared on newer live `main`;
2. read the 1997 collection README/source/inventory/scan-map;
3. transcribe and visually verify scans **104–106**;
4. use scan **107**, opening `பிரேத விசாரணை`, as the physical ending boundary;
5. create the canonical story workspace and synchronize controls only after source processing is complete;
6. do not process `நடுத்தெரு நாராயணி`;
7. then advance to `காந்தி தேசம்`, one story per activity.
