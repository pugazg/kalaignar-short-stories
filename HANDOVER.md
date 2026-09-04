# HANDOVER — Kalaignar Short Stories Archive

## Repository

- Repository: `pugazg/kalaignar-short-stories`
- Branch: `main`
- Story workflow: `SHORT_STORY_PROCESSING_GUIDE.md`
- Collection workflow: `COLLECTION_SOURCE_GUIDE.md`
- Text-fidelity workflow/tracker: `TEXT_FIDELITY_CHECK_GUIDE.md` / `TEXT_FIDELITY_PROGRESS.md`
- 1977 visual workflow/tracker: `VISUAL_FIDELITY_CHECK_GUIDE.md` / `VISUAL_FIDELITY_PROGRESS.md`
- 2008 visual workflow/tracker: `collections/2008-kalaignar-sonna-kathaigal/VISUAL_FIDELITY_GUIDE.md` / `collections/2008-kalaignar-sonna-kathaigal/VISUAL_FIDELITY_PROGRESS.md`
- English workflow: `ENGLISH_TRANSLATION_GUIDE.md`

## Authoritative-state rule

Always fetch live `main` first and preserve newer durable work. Source PDFs / renders / crops are not committed.

## Permanent source rules

- controlling scan first; no silent modernization or normalization;
- running headers and printed page numbers are page furniture, not body text;
- shared physical scans preserve exact story boundaries;
- source-supported textual corrections propagate through page, assembly, audit/review and dependent layers;
- `POSSIBLE_ERRORS_FOR_REVIEW.md` is a human-review queue, not proof of error.

## Closed 1977 anthology

`கலைஞர் கருணாநிதியின் சிறுகதைகள்` remains fully closed:

- Tamil source: **37 / 37 complete**;
- visual fidelity: **37 / 37 complete**;
- English translation/review: **37 / 37 complete**;
- final English structural/control QA: **PASS**;
- unresolved story text: **0**;
- scan **260**: verified back cover.

Story 29 `திடுக்கிடும் கதை` retains the later marker-only provenance correction. Obsolete Wave-2 pin `a9b333f12128686785ee981f97313a64af12e29b` must not be reused.

## 2008 collection — closed source and text fidelity

Collection: **கலைஞர் சொன்ன கதைகள்**  
Workspace: `collections/2008-kalaignar-sonna-kathaigal/`  
Controlling source: `TVA_BOK_0065857_கலைஞர்_சொன்ன_கதைகள்.pdf`

- represented edition: **Second Edition, December 2008**;
- PDF scans: **82**;
- story text: scans **9–81 / printed pages 7–79**;
- scan **82**: verified back cover, no further story text;
- Tamil source: **40 / 40 complete**, 0 blocked / 0 unresolved;
- word-by-word text fidelity: **40 / 40 complete**;
- text-fidelity split: **19 PASS / 21 PASS — corrected**;
- English from this collection: **0 / 40**.

Nine TOC/opening-heading differences remain registered and must not be normalized: Stories **2, 11, 24, 27, 28, 29, 35, 36, 39**.

## Closed phase — 2008 visual fidelity

Standing collection batch rule was **10 stories per iteration**.

### Final durable state

- total: **40**;
- complete: **40 / 40**;
- `PASS`: **40**;
- `PASS — corrected`: **0**;
- pending: **0**;
- needs recheck: **0**;
- unresolved visual-fidelity issues: **0**;
- story-local `visual-fidelity.md`: **40 / 40**.

All four visual-fidelity iterations are closed:

1. Stories **1–10** — scans **9–27** — all `PASS`;
2. Stories **11–20** — scans **27–43** — all `PASS`;
3. Stories **21–30** — scans **43–66** — all `PASS`;
4. Stories **31–40** — scans **66–82** — all `PASS`.

The final iteration directly confirmed:

- Story 31's three verse/display blocks across scans 67–68;
- Story 35's TOC/opening-heading difference, quoted dialogue and rhythmic `தும் / பம் / தீம்` structure;
- Story 36's TOC/opening-heading difference and two-line `நல் வழி` verse;
- Story 37's incomplete/completed poetic display and source-sensitive asymmetric quotation punctuation;
- Story 38's seven-line quoted poem;
- Story 39's TOC/opening-heading difference;
- Story 40's three op-pāri/song display blocks and final `*`;
- scan **82** is the physical back cover only and contributes no Story-40 text.

Across the collection, boxed story sequence numbers, vertical gutter rules and opening horizontal title rules are collection-design furniture and remain outside canonical prose. Printed page numbers and running headers remain excluded as page furniture. The centered single `*` is a source-significant story-ending ornament and is preserved for all forty stories.

No Tamil wording or meaningful page/assembly structure required correction during the 2008 visual-fidelity phase.

## Current phase gate

The 2008 collection now has:

- Tamil source processing: **40 / 40 complete**;
- word-by-word text fidelity: **40 / 40 complete**;
- visual fidelity: **40 / 40 complete**;
- English translation: **0 / 40**.

There is no remaining source/text-fidelity/visual-fidelity activity and there is no Story 41.

Do **not** automatically begin English translation, modernization, adaptation, republication or Digital Library onboarding. The next downstream phase must be explicitly authorized by the user. Live `main` remains authoritative at every fresh-chat start.
