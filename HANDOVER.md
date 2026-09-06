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
- an additional edition witness must not silently overwrite a canonical controlling edition;
- textual differences belong in explicit comparison/audit records;
- if a later witness appears to correct a canonical reading, reopen the exact canonical controlling scan before changing Tamil/English/control layers;
- source PDFs are not committed.

## Closed prior collections

- **1977 — கலைஞர் கருணாநிதியின் சிறுகதைகள்:** Tamil 37/37, visual 37/37, English 37/37, final English QA PASS, unresolved 0.
- **2008 — கலைஞர் சொன்ன கதைகள்:** Tamil 40/40, text fidelity 40/40, visual 40/40, English 40/40, final English QA PASS, unresolved 0.
- **2004 — கலைஞரின் குட்டிக் கதைகள்:** Tamil 34/34, visual 34/34, English 34/34, final English QA PASS, unresolved 0.

Do not reopen these closed phases merely to create work. A specifically authorized independent-witness comparison is different from reopening the closed canonical source pass.

## New source 1 — 1997 `திராவிட இயக்க எழுத்தாளர் சிறுகதைகள்`

Workspace: `collections/1997-dravida-iyakka-ezhuthalar-sirukathaigal/`

- source: `TVA_BOK_0064315_திராவிட_இயக்க_எழுத்தாளர்_சிறுகதைகள்.pdf`
- SHA-256: `ead34f2d1e983568b79ef9d6185006844ee3e5d6443695633124975ecb77227c`
- scans: **115**
- `நண்பனா?`: **3/3 verified**, Tamil audit PASS, visual PASS, 0 unresolved, English not started.
- `நடுத்தெரு நாராயணி`: explicitly deferred for separate short-novel handling.

The 1997 new-short-story onboarding is complete.

## 2009 source — `16 கதையினிலே`

Workspace: `collections/2009-16-kathaiyinile/`

- source: `TVA_BOK_0065745_16_கதையினிலே.pdf`
- SHA-256: `21daed58600d2e927dec4341fd1e0eab597f12d50f8c444458de9bc4ad18a859`
- size: **384,978,955 bytes**
- registered scans: **183**
- represented edition: **Fourth Edition, March 2009**
- TOC: **16 stories**
- story block: scans **6–182**
- scan **183**: back cover
- source completeness: **complete — all 16 stories present**
- preserved anomaly: TOC places `சங்கிலிச்சாமி` at p105, while physical p105 on scan 110 still closes `குப்பைத் தொட்டி`; `சங்கிலிச்சாமி` begins on scan 111.

The earlier 150-scan/incomplete-source statement is false. A conversation working copy may be truncated at scan 150; it does not replace the registered 183-scan source identity.

### New-story onboarding — COMPLETE / CLOSED — 5 / 5

- `காந்தி தேசம்` — scans **6–18 / printed 1–13** — 13/13 verified, Tamil/visual PASS, 0 unresolved.
- `அணில் குஞ்சு` — scans **19–28 / printed 14–23** — 10/10 verified, Tamil/visual PASS, 0 unresolved.
- `கொள்ளைபுரம்` — scans **29–37 / printed 24–32** — 9/9 verified, Tamil/visual PASS, 0 unresolved.
- `எழுத்தாளர் ஏகலைவன்` — scans **38–49 / printed 33–44** — 12/12 verified, Tamil/visual PASS, 0 unresolved.
- `மலரவில்லை` — scans **50–63 / printed 45–58** — 14/14 verified, Tamil/visual PASS, 0 unresolved.

English for these new stories remains a separate future phase.

## ACTIVE PHASE — 2009 additional-witness comparison of existing canonical stories

The user explicitly authorized this phase after the 5/5 onboarding closure. Stories 6–16 are compared **one at a time** against their already-existing canonical editions.

Progress: **2 / 11 complete**.

### Completed comparison 1 / 11 — `சுமந்தவள்`

- 2009 coordinates: scans **64–81 / printed 59–76**
- canonical workspace: `stories/sumanthaval/`
- canonical controlling edition: 1977 anthology, scans **239–249 / printed 230–240**
- witness record: `stories/sumanthaval/witnesses/2009-16-kathaiyinile/`
- comparison coverage: **18 / 18 scans**, plus scan 82 boundary
- result: **materially revised/expanded edition, not a simple reprint**
- major finding: 2009 adds a three-year epilogue on scans **80–81** after an internal five-ornament break; the represented 1977 edition closes earlier after the doctor/illness scene
- representative recheck candidates created by the later witness: 1977 `திரு திருவென்று` ↔ 2009 `துருதுருவென்று`; `அவள் உள்ளத்தில்` ↔ `அவா, உள்ளத்தில்`; `முழுங்கால்` ↔ `முழங்கால்`; `சன சுரத்தை` ↔ `ஈன குரத்தை`
- 1977 controlling PDF was not available for a fresh scan-level recheck during this comparison
- canonical 1977 Tamil changed: **No**
- canonical English changed: **No**

### Completed comparison 2 / 11 — `புகழேந்தி`

- 2009 coordinates: scans **82–89 / printed 77–84**
- canonical workspace: `stories/pugazhendhi/`
- canonical controlling edition: 1977 anthology, scans **10–15 / printed 1–6**
- witness record: `stories/pugazhendhi/witnesses/2009-16-kathaiyinile/`
- comparison coverage: **8 / 8 scans**, plus scan 90 boundary
- result: **same narrative arc and same `மேதை வாழ்க!` ending; editorially revised/regularized rather than expanded**
- no 2009-only epilogue or major new narrative block identified
- high-value later-witness recheck evidence: 1977 `புகழ்தரும் தீவலி` ↔ 2009 `புகழ்தரும் தலைவலி`; `வயித்துக்கிடக்கிறது` ↔ `லயித்துக் கிடக்கிறது`; `காதற் கண்கள்` ↔ `காதற் கணைகள்`; `கால்ப் பணிவிடைகள்` ↔ `காலைப் பணிவிடைகள்`
- the unusual 1977 `ஏறெடுத்தும் பாராமல்` is corroborated by the 2009 witness
- 1977 controlling PDF was not available for a fresh scan-level recheck during this comparison
- canonical 1977 Tamil changed: **No**
- canonical English changed: **No**

Later-edition wording must remain edition evidence until the exact canonical controlling scan is reopened. Do not import the 2009 `சுமந்தவள்` epilogue into 1977, and do not silently replace the `புகழேந்தி` recheck candidates from later wording alone.

## CURRENT EXACT NEXT ACTIVITY — comparison 3 / 11 — `நளாயினி`

Process only the 2009 additional witness for **`நளாயினி`**:

- 2009 collection sequence: **8 / 16**
- TOC/opening heading: **`நளாயினி`**
- printed pages: **85–94**
- PDF scans: **90–99**
- canonical workspace: `stories/nalayini/`
- next-story boundary witness: scan **100**, opening `குப்பைத் தொட்டி`

Required procedure:

1. fetch live `main` first;
2. read `SHORT_STORY_PROCESSING_GUIDE.md`, `COLLECTION_SOURCE_GUIDE.md`, this `HANDOVER.md`, `NEXT_CHAT_PROMPT.md`, collection README/source/inventory/scan-map, and the canonical `stories/nalayini/` source/audit/recheck/visual controls;
3. inspect 2009 scans **90–99** and scan **100** directly;
4. compare wording, punctuation, structure, title and ending against the canonical controlling edition;
5. keep the 2009 edition separate; do not silently overwrite canonical Tamil;
6. if the 2009 witness suggests a canonical error, record a recheck candidate and change canonical text only after direct inspection of its own controlling scan;
7. create/update durable witness comparison records under the existing canonical workspace;
8. synchronize collection/root controls to **3 / 11** when complete;
9. advance the next prompt to `குப்பைத் தொட்டி` scans **100–110**, with scan **111 `சங்கிலிச்சாமி`** as its boundary witness;
10. do **not** begin `குப்பைத் தொட்டி` in the same activity.

Do not process `நடுத்தெரு நாராயணி` as a short story.
