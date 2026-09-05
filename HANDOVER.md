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
- physical English source markers must align to actual source content transitions, not merely appear in numeric order.

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

- user authorization: **granted / OPEN**
- English `PASS`: **21 / 34**
- pending: **13 / 34**
- `NEEDS REVIEW`: **0**
- visual-fidelity prerequisites closed: **21 / 34**
- canonical Tamil changed during English work through Story 21: **No**

### Latest completed five-story batch — Stories 17–21

1. **Story 17 `ஆடிக் காற்றே!`** — scan 24 only; visual PASS + English PASS; rhetorical/display structure and political metaphors retained.
2. **Story 18 `இலங்கை மன்னர் பரம்பரை`** — scans 25→27; visual PASS + English PASS; source framing and scan-26→27 `அனுப்பு` → `கிறான்.` split remain traceable; translation does not independently endorse or correct the historical claim.
3. **Story 19 `கழுத்திலே ஒரு முடிச்சு... அதற்கு ஒரு கதை`** — scans 27→28; visual PASS + English PASS; title/body ellipses, four-dot punctuation and mythological vocabulary retained.
4. **Story 20 `சிறை கொடியது`** — scans 28→29; visual PASS + English PASS; display-poem lineation and physical page break preserved.
5. **Story 21 `விஞ்ஞானிக்குத் தோன்றாது...`** — scan 29 only; visual PASS + English PASS; scan-confirmed heading, `முகத்தான` and internal ellipsis retained without Tamil normalization.

No Tamil source issue was reopened and no Tamil text changed in the batch.

## Current exact next activity

Close the **Story 22 `அடுத்த பிறவியில் ஐந்து கணவன்` visual-fidelity prerequisite**.

1. Fetch live `main` first.
2. Ensure the controlling 2004 PDF is attached/resolved.
3. Read Story-22 README, page map, all three page records, Tamil assembly, audit and `POSSIBLE_ERRORS_FOR_REVIEW.md`.
4. Directly inspect **lower scan 29 / printed 28 → scan 30 / printed 29 → upper scan 31 / printed 30**. Story 21 ends above Story 22 on scan 29; Story 23 `புகழே நீ ஒரு புதிர்` begins below Story 22 on scan 31.
5. Check exact heading/opening/ending, paragraph/dialogue/display structure, physical page joins, separators and page furniture.
6. Create `stories/adutha-piraviyil-aindhu-kanavan/visual-fidelity.md` only if source-supported; make only independently source-supported Tamil corrections if required.
7. Do not create Story-22 English prose until the visual gate is durably PASS.
8. Unless the user explicitly expands batching again, process one story per activity.

After Story 22 visual PASS, the following activity is Story-22 English translation and `TRANSLATION_REVIEW.md`.
