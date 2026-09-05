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
- English `PASS`: **16 / 34**
- pending: **18 / 34**
- `NEEDS REVIEW`: **0**
- visual-fidelity prerequisites closed: **16 / 34**
- canonical Tamil changed during English work through Story 16: **No**

### Latest completed five-story batch — Stories 12–16

1. **Story 12 `ஆண்டவன் தரிசனம் கொடுத்த ஊர்`** — scan 18 only; visual PASS + English PASS; exact unusual opening and quoted `‘புலையர்கள்’` retained.
2. **Story 13 `வீரவாடி`** — scan 18→19; visual PASS + English PASS; page marker aligned inside the final sentence at the verified source join.
3. **Story 14 `சொர்க்கத்திற்கு வந்தது எப்படி?`** — scans 19→22; visual PASS + English PASS; four source markers, speaker labels and parenthetical remarks retained; the Kotpuli quotation's page break is aligned.
4. **Story 15 `கள்ளியும் ரோஜாவும்`** — scans 22→23; visual PASS + English PASS; source page break after `ஒரு` is preserved in the English marker placement.
5. **Story 16 `ஆபாசமே ஆபாசம்!`** — scans 23→24; visual PASS + English PASS; scan-verified title and source-sensitive names/forms retained.

No Tamil source issue was reopened and no Tamil text changed in the batch.

## Current exact next activity

Close the **Story 17 `ஆடிக் காற்றே!` visual-fidelity prerequisite**.

1. Fetch live `main` first.
2. Ensure the controlling 2004 PDF is attached/resolved.
3. Read Story-17 README, page map, page record, Tamil assembly, audit and `POSSIBLE_ERRORS_FOR_REVIEW.md`.
4. Directly inspect **scan 24 / printed page 23**. Story 16 ends above Story 17 on the same scan and is excluded; Story 18 `இலங்கை மன்னர் பரம்பரை` begins on scan 25 and is the following boundary witness.
5. Check exact heading/opening/ending, paragraph/dialogue/display structure, separators and page furniture.
6. Create `stories/aadik-kaatre/visual-fidelity.md` only if source-supported; make only independently source-supported Tamil corrections if required.
7. Do not create Story-17 English prose until the visual gate is durably PASS.
8. Unless the user explicitly expands batching again, process one story per activity.

After Story 17 visual PASS, the following activity is Story-17 English translation and `TRANSLATION_REVIEW.md`.
