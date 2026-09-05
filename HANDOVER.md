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
- English `PASS`: **11 / 34**
- pending: **23 / 34**
- `NEEDS REVIEW`: **0**
- visual-fidelity prerequisites closed: **11 / 34**
- canonical Tamil changed during English work through Story 11: **No**

### Completed English Stories 1–11

Stories **1–6** remain closed and unchanged.

Latest user-authorized five-story batch — **Stories 7–11**:

1. **Story 7 `நாதம் எழாது - நரம்புதான் அறும்`** — scan 14→15; visual PASS + English PASS; marker aligned inside the nested quote at the source `‘நான்` break; visibly unclosed outer quotation preserved without invention.
2. **Story 8 `அவள் சொன்னாள்`** — scan 15 only; visual PASS + English PASS; complete two-paragraph same-page unit isolated between Stories 7 and 9.
3. **Story 9 `இருவரும் கூடியிருப்பது ஆத்தி மாலைதான்`** — scan 15→16; visual PASS + English PASS; four verse/display units retained; no external standard verse imported.
4. **Story 10 `கொல்லப்பட வேண்டியது புலி, ஆனால்...`** — scan 16→17; visual PASS + English PASS; source ellipses retained; scan-17 marker aligned inside the quoted cross-page sentence immediately before translation of `எய்தாய்.`.
5. **Story 11 `அந்தக் காலத்திலே!`** — scan 17 only; visual PASS + English PASS; differing `...` / `....` punctuation retained; scan 18 directly checked as the next-story witness.

No Tamil source issue was reopened and no Tamil text changed in the batch.

## Current exact next activity

Close the **Story 12 `ஆண்டவன் தரிசனம் கொடுத்த ஊர்` visual-fidelity prerequisite**.

1. Fetch live `main` first.
2. Ensure the controlling 2004 PDF is attached/resolved.
3. Read Story-12 README, page map, page record, Tamil assembly, audit and `POSSIBLE_ERRORS_FOR_REVIEW.md`.
4. Directly inspect **scan 18 / printed page 17**. Story 11 ended on scan 17; Story 13 `வீரவாடி` begins later on scan 18 and is the lower same-page boundary witness.
5. Check exact heading/opening/ending, paragraph/dialogue/display structure, separators, page furniture and exclusion of Story 13.
6. Create `stories/aandavan-dharisanam-kodutha-oor/visual-fidelity.md` only if source-supported; make only independently source-supported Tamil corrections if required.
7. Do not create Story-12 English prose until the visual gate is durably PASS.
8. Unless the user explicitly expands batching again, process one story per activity.

After Story 12 visual PASS, the following activity is Story-12 English translation and `TRANSLATION_REVIEW.md`.
