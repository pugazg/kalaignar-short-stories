# HANDOVER — Kalaignar Short Stories Archive

## Repository

- repository: `pugazg/kalaignar-short-stories`
- branch: `main`
- story workflow: `SHORT_STORY_PROCESSING_GUIDE.md`
- collection workflow: `COLLECTION_SOURCE_GUIDE.md`
- English workflow: `ENGLISH_TRANSLATION_GUIDE.md`

## LIVE MAIN IS AUTHORITATIVE

Always fetch live `main` first. Preserve newer durable state. Repository files reachable from live `main`, not copied prompts or chat memory, are authoritative.

## Permanent rules

- controlling scan first; no silent normalization;
- shared physical boundaries must remain exact;
- `POSSIBLE_ERRORS_FOR_REVIEW.md` is a review queue, not proof of error;
- English may begin only after Tamil/source audit and story-local visual-fidelity PASS;
- physical source markers must align to actual content transitions, not merely appear in numeric order.

## Closed prior collections

- **1977 — கலைஞர் கருணாநிதியின் சிறுகதைகள்:** Tamil 37/37, visual 37/37, English 37/37, final English QA PASS, unresolved 0, scan 260 back cover.
- **2008 — கலைஞர் சொன்ன கதைகள்:** Tamil 40/40, text fidelity 40/40, visual 40/40, English 40/40, final English QA PASS, unresolved 0, scan 82 back cover.

## 2004 collection — கலைஞரின் குட்டிக் கதைகள்

Workspace: `collections/2004-kalaignarin-kuttik-kathaigal/`

Controlling source: `TVA_BOK_0065567_கலைஞரின்_குட்டிக்_கதைகள்_2004.pdf`

- SHA-256: `33bdfb4f47bc688750fff11f967a0d2b95a93a9aa09044c0467107dae583ab04`
- size: **98,897,868 bytes**
- scans: **50**
- publisher: **பாரதி பதிப்பகம்**
- represented edition: **Second Edition, March 2004**
- story block: scans **4–49 / printed pages 3–48**
- direct heading inventory: **34 / 34**
- scan 50: verified back cover

### Tamil

**COMPLETE / CLOSED — 34 / 34 PASS, 0 pending, 0 unresolved.**

### English

The user explicitly authorized the English phase.

- English `PASS`: **6 / 34**
- pending: **28 / 34**
- `NEEDS REVIEW`: **0**
- visual-fidelity prerequisites closed: **6 / 34**
- canonical Tamil changed during English work through Story 6: **No**

### Completed English Stories 1–6

1. **`வள்ளுவர் சொன்ன பொய்`** — English PASS; scan 4 → top scan 5.
2. **`நீயும் கைதி - நானும் கைதி`** — English PASS; scan 5 only; two closing prisoner lines preserved separately.
3. **`குருவி ராமேஸ்வரம்`** — visual PASS + English PASS; scan 5 → 6; cross-page Rama question/answer marker aligned.
4. **`பெண்களுக்கு ஏன் - மீசை தாடியில்லை?`** — visual PASS + English PASS; scans 6 → 11; six markers aligned, including two mid-sentence/quote page transitions.
5. **`கடலைத் தூர்ப்பது மிக எளிது`** — visual PASS + English PASS; scans 11 → 13; scan-11→12 sentence transition and two-line dream close preserved.
6. **`மனைவி சொன்ன விளக்கம்`** — visual PASS + English PASS; scans 13 → 14; marker aligned immediately before the source `மனைவியை` continuation; nested quotations preserved.

The latest user-authorized batch contained **five stories: Stories 2–6**. No Tamil source issue was reopened and no Tamil text changed.

## Current exact next activity

Close the **Story 7 `நாதம் எழாது - நரம்புதான் அறும்` visual-fidelity prerequisite**.

1. Fetch live `main` first.
2. Ensure the controlling 2004 PDF is attached/resolved.
3. Read Story-7 README, page map, both page records, Tamil assembly, audit and `POSSIBLE_ERRORS_FOR_REVIEW.md`.
4. Directly inspect **scan 14 → scan 15**. Story 6 closes above the Story-7 opening on scan 14; Story 8 `அவள் சொன்னாள்` is the following boundary witness on scan 15.
5. Create `stories/naatham-ezhaathu-narambuthaan-arum/visual-fidelity.md` if source-supported; make only source-supported corrections if independently required.
6. Do not create Story-7 English prose until the visual prerequisite is PASS.
7. Unless the user explicitly expands batching again, process one story per activity.

After Story 7 visual PASS, the following activity is its English translation and `TRANSLATION_REVIEW.md`.
