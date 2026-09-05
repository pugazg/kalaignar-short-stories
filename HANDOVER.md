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
- **2008 — கலைஞர் சொன்ன கதைகள்:** Tamil 40/40, text fidelity 40/40, visual 40/40, English 40/40, final English structural/control QA PASS, unresolved 0, scan 82 back cover.

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
- visual-fidelity prerequisites closed: **22 / 34**
- canonical Tamil changed during English/visual work through Story 22 visual closure: **No**

### Latest completed English batch — Stories 17–21

Stories 17–21 remain visual PASS + English PASS. No Tamil source issue was reopened and no Tamil text changed in that batch.

### Latest visual closure — Story 22

**Story 22 `அடுத்த பிறவியில் ஐந்து கணவன்`** is now visual-fidelity **PASS**.

- span: **lower scan 29 / printed 28 → scan 30 / printed 29 → upper scan 31 / printed 30**;
- Story 21 ends above on scan 29 and is excluded;
- Story 23 `புகழே நீ ஒரு புதிர்` begins below on scan 31 and is excluded;
- both physical page transitions occur between complete dialogue turns;
- source-sensitive review-queue forms and asymmetric quotation punctuation remain unchanged;
- Tamil correction during visual review: **None**.

## Current exact next activity

Translate **Story 22 `அடுத்த பிறவியில் ஐந்து கணவன்`** into English and create `TRANSLATION_REVIEW.md`.

1. Fetch live `main` first.
2. Read `ENGLISH_TRANSLATION_GUIDE.md`, the collection English tracker, Story-22 README, canonical Tamil assembly, visual-fidelity record and `POSSIBLE_ERRORS_FOR_REVIEW.md`.
3. Translate from verified canonical Tamil only; do not alter the Tamil layer.
4. Insert physical provenance markers for scans **29, 30 and 31** at the actual source page transitions, which fall between complete dialogue turns.
5. Exclude Story 21 above and Story 23 below.
6. Review completeness, tone, source-sensitive terms and marker alignment in `TRANSLATION_REVIEW.md`.
7. Do not begin Story 23 in this activity unless the user explicitly expands batching.

After Story 22 English PASS, the following activity is Story 23 `புகழே நீ ஒரு புதிர்` visual-fidelity prerequisite.
