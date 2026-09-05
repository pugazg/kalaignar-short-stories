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
- short-story titles now represented by canonical workspaces: **9**
- `நண்பனா?`: scans **104–106 / printed 94–96**, **3/3 verified**, Tamil audit PASS, visual PASS, 0 unresolved, English not started.
- separately deferred work: **`நடுத்தெரு நாராயணி`** — handle separately as a short novel; do not process in this short-story queue.

The 1997 new-short-story onboarding is complete. The eight previously canonical titles remain additional-source witnesses until an explicit comparison activity.

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
- final spans: `ஏழை` 150–154; `கண்ணடக்கம்` 155–163; `வாழ முடியாதவர்கள்` 164–173; `அய்யோ ராஜா` 174–182.
- preserved anomaly: TOC places `சங்கிலிச்சாமி` at p105, while physical p105 on scan 110 still closes `குப்பைத் தொட்டி`; heading is scan 111.

The earlier 150-scan / incomplete-source statement was incorrect and has been superseded.

### Newly onboarded — `காந்தி தேசம்`

- canonical workspace: `stories/gandhi-desam/`
- printed pages **1–13** / scans **6–18**
- **13 / 13 verified**, Tamil audit PASS, visual PASS, 0 unresolved, English not started
- scan **19** opens `அணில் குஞ்சு`.

### Newly onboarded — `அணில் குஞ்சு`

- canonical workspace: `stories/anil-kunju/`
- printed pages **14–23** / scans **19–28**
- **10 / 10 verified**, Tamil audit PASS, visual PASS, 0 unresolved, English not started
- scan **29** opens `கொள்ளைபுரம்`.

### Newly onboarded — `கொள்ளைபுரம்`

- canonical workspace: `stories/kollaipuram/`
- printed pages **24–32** / scans **29–37**
- **9 / 9 verified**, Tamil audit PASS, visual PASS, 0 unresolved, English not started
- scan **38** opens `எழுத்தாளர் ஏகலைவன்`.

### Newly onboarded — `எழுத்தாளர் ஏகலைவன்`

Canonical workspace: `stories/ezhuthalar-ekalaivan/`

- printed pages: **33–44**
- scans: **38–49**
- next boundary: scan **50**, opening `மலரவில்லை`
- page records: **12 / 12 verified**
- Tamil source audit: **PASS**
- visual fidelity: **PASS**
- blocked / unresolved story text: **0**
- English: **not started**
- source-close rechecks retained forms including `தமிழகமுழுதும்`, `புலித்தைலம்`, `அங்கணபோயி`, `ரெண்டு மணிக்கே கீழே`, `சுலபத்தில் விடாத மணலில்`, `பத்தாம்பசலிக் கட்டுப்பெட்டிக்`, `தரையிலிட்ட மீன்`, `கரையைவிட்டகன்று`, `கண்டல் முறுக்குக் கடலை`, `பாத்தோம்`, `மெளனமானான்`, `பொழைச்சிக்கிட்டாங்க`, `என்றே தெரியாத`, `பஸ்ஸில அடிபட்டு`, and `நம்மாலியன்ற`.
- scan **49** closes with five circular ornaments; scan **50** visibly opens `மலரவில்லை`.

New-story source-processing status for this collection: **4 / 5 complete**.

## Remaining new short-story queue

1. `மலரவில்லை` — scans **50–63 / printed 45–58**

## Current exact next activity

Process **`மலரவில்லை`** only from `TVA_BOK_0065745_16_கதையினிலே.pdf`:

1. fetch live `main` and confirm no canonical `மலரவில்லை` workspace has appeared;
2. read `SHORT_STORY_PROCESSING_GUIDE.md`, `COLLECTION_SOURCE_GUIDE.md`, this handover, `NEXT_CHAT_PROMPT.md`, and the 2009 collection README/source/inventory/scan-map;
3. transcribe and directly visually verify scans **50–63 / printed pages 45–58**;
4. inspect scan **64**, opening `சுமந்தவள்`, as the next-story boundary and exclude it from `மலரவில்லை`;
5. create the canonical story workspace, Tamil assembly, source metadata, audit, possible-error queue, visual-fidelity record and required controls;
6. do not begin `சுமந்தவள்` or additional-witness comparison in the same activity;
7. after synchronization the five new 2009 stories will be **5 / 5 complete**;
8. do not process `நடுத்தெரு நாராயணி` as a short story.
