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
- separately deferred work: **`நடுத்தெரு நாராயணி`** — handle separately as a short novel; do not process in this short-story queue.

### Newly onboarded — `நண்பனா?`

Canonical workspace: `stories/nanbana/`

- printed pages: **94–96**
- scans: **104–106**
- preceding boundary: scan **103**, end of `தொத்துக்கிளி`
- next boundary: scan **107**, opening `பிரேத விசாரணை`
- page records: **3 / 3 verified**
- Tamil source audit: **PASS**
- visual fidelity: **PASS**
- blocked / unresolved story text: **0**
- English: **not started**
- possible-error/recheck queue: retained; queue entries are not proof of error.

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

## Remaining new short-story queue

1. `காந்தி தேசம்` — scans **6–18 / printed 1–13**
2. `அணில் குஞ்சு` — scans **19–28 / printed 14–23**
3. `கொள்ளைபுரம்` — scans **29–37 / printed 24–32**
4. `எழுத்தாளர் ஏகலைவன்` — scans **38–49 / printed 33–44**
5. `மலரவில்லை` — scans **50–63 / printed 45–58**

## Current exact next activity

Process **`காந்தி தேசம்`** only from `TVA_BOK_0065745_16_கதையினிலே.pdf`:

1. fetch live `main` and confirm no canonical `காந்தி தேசம்` workspace has appeared;
2. read `SHORT_STORY_PROCESSING_GUIDE.md`, `COLLECTION_SOURCE_GUIDE.md`, this handover, `NEXT_CHAT_PROMPT.md`, and the 2009 collection README/source/inventory/scan-map;
3. transcribe and directly visually verify scans **6–18 / printed pages 1–13**;
4. inspect scan **19**, opening `அணில் குஞ்சு`, as the next-story boundary and exclude it from `காந்தி தேசம்`;
5. create the canonical story workspace, Tamil assembly, source metadata, audit, possible-error queue, visual-fidelity record and required controls;
6. do not begin `அணில் குஞ்சு` in the same activity;
7. do not process `நடுத்தெரு நாராயணி` as a short story.
