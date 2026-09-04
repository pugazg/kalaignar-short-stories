# HANDOVER — Kalaignar Short Stories Archive

## Repository

- Repository: `pugazg/kalaignar-short-stories`
- Branch: `main`
- Story workflow: `SHORT_STORY_PROCESSING_GUIDE.md`
- Collection workflow: `COLLECTION_SOURCE_GUIDE.md`
- Text-fidelity workflow/tracker: `TEXT_FIDELITY_CHECK_GUIDE.md` / `TEXT_FIDELITY_PROGRESS.md`
- 2008 visual workflow/tracker: `collections/2008-kalaignar-sonna-kathaigal/VISUAL_FIDELITY_GUIDE.md` / `VISUAL_FIDELITY_PROGRESS.md`
- English workflow: `ENGLISH_TRANSLATION_GUIDE.md`
- 1977 English tracker: `ENGLISH_TRANSLATION_PROGRESS.md` — closed at **37 / 37**
- 2008 English tracker: `collections/2008-kalaignar-sonna-kathaigal/ENGLISH_TRANSLATION_PROGRESS.md`

## LIVE MAIN IS AUTHORITATIVE

Always fetch live `main` first and preserve newer durable work. Source PDFs / renders / crops are not committed. Repository files reachable from live `main`, not chat memory or a copied checkpoint, are durable state.

## Permanent source / translation rules

- controlling scan first; no silent modernization or normalization;
- canonical verified Tamil is authoritative for English translation;
- running headers and printed page numbers are page furniture, not body text;
- shared physical scans preserve exact story boundaries;
- source-supported corrections propagate through page, assembly, audit/review and dependent layers;
- `POSSIBLE_ERRORS_FOR_REVIEW.md` is a human-review queue, not proof of error;
- English page markers must use exactly `<!-- source scan N; printed page M -->`;
- boundary notes belong in separate HTML comments;
- marker presence/order alone is insufficient: actual translated content boundaries must align to verified Tamil page records.

## Closed 1977 anthology

`கலைஞர் கருணாநிதியின் சிறுகதைகள்` remains fully closed:

- Tamil source **37 / 37**;
- visual fidelity **37 / 37**;
- English translation/review **37 / 37**;
- final English structural/control QA **PASS**;
- unresolved story text **0**;
- scan **260** verified back cover.

Story 29 `திடுக்கிடும் கதை` retains the later marker-only provenance correction. Obsolete Wave-2 pin `a9b333f12128686785ee981f97313a64af12e29b` must not be reused.

## 2008 collection — source / text / visual CLOSED

Collection: **கலைஞர் சொன்ன கதைகள்**  
Workspace: `collections/2008-kalaignar-sonna-kathaigal/`  
Controlling source: `TVA_BOK_0065857_கலைஞர்_சொன்ன_கதைகள்.pdf`

- represented edition: **Second Edition, December 2008**;
- PDF scans: **82**;
- story text: scans **9–81 / printed pages 7–79**;
- scan **82**: verified back cover, no further story text;
- Tamil source: **40 / 40 complete**, 0 blocked / 0 unresolved;
- word-by-word text fidelity: **40 / 40 complete — 19 PASS / 21 PASS — corrected**;
- visual fidelity: **40 / 40 complete — all 40 PASS**.

Nine TOC/opening-heading differences remain registered and must not be normalized: Stories **2, 11, 24, 27, 28, 29, 35, 36, 39**.

## 2008 English translation — ACTIVE

Current durable state:

- English complete: **25 / 40**;
- `PASS`: **25**;
- pending: **15 / 40**;
- `NEEDS REVIEW`: **0**;
- canonical Tamil changed during English work: **No**.

Stories **1–15** remain closed as previously recorded. The latest completed iteration is Stories **16–25**, all **PASS**.

## Standing English iteration rule

The user explicitly directed: **process 10 stories in each iteration**. This is now the standing English-phase batching rule.

- completed iteration: Stories **5–14** — **10 / 10 PASS**;
- Story **15** was completed individually before this standing rule was established;
- latest completed iteration: Stories **16–25** — **10 / 10 PASS**;
- next iteration: Stories **26–35**;
- final iteration: Stories **36–40**.

Do not revert to the guide's default one-story-per-activity rule unless the user changes this directive.

## Latest completed iteration — Stories 16–25

Every story in the iteration has:

- complete English under `translations/en/`;
- story-local `TRANSLATION_REVIEW.md` with result **PASS**;
- synchronized story README;
- verified source-marker order and independently checked physical content-boundary alignment;
- final source-significant `*` preserved;
- no Tamil change caused by translation.

Key controls:

16. **`அத்திரி பாச்சா`** — `stories/aththiri-paachaa/`; markers **35→36**; source `அடம்`→`பிடித்தான்` join aligned; `அத்திரிப் பாச்சா` / `அத்திரி பாச்சா` variation retained.
17. **`செருப்போடு இரு`** — markers **36→37**; corrected `போர் வீரன்படம்` used; closing admonition translated directly without an outside proverb.
18. **`இடிக்குப் பின் மழை`** — markers **37→38→39**; Socrates `தலை`→`யிலே` source split anchored; thunder/rain dialogue retained.
19. **`நடக்குமா நடக்காதா?`** — markers **39→40→41→42**; bull→goat→hen→tea chain, wager and corrected `என்னடா?` retained.
20. **`கனியும் கணையும்`** — markers **42→43**; William Tell and Republic Day/Hindi/DMK analogy retained; source-open quotation not silently closed.
21. **`இதயம் பேசுகிறது`** — markers **43→44**; speaking-heart punctuation and Tamil mother-tongue close preserved.
22. **`புலிவால்`** — markers **44→45**; quoted `நாயர் புடிச்ச`→`புலிவால்` split aligned; both applause cues retained.
23. **`தெரியாத பேச்சு`** — markers **45→46→47**; source-open concluding quotation and `லெனினைப் பற்றி` join retained.
24. TOC **`வெண்ணெய் உருகுது வெயிலில்!`** / opening **`வெண்ணெய் உருகுது வெயிலில்`** — markers **47→48→49→50→51→52→53→54**; embedded 1977 letter, Amirthamathi passage, source corrections and three-line Kuruntokai display preserved without importing outside editions.
25. **`மாமியார் உடைத்தால் மட்டும் மண்சட்டியா?`** — markers **54→55→56→57→58→59→60**; unusual source forms, Yama/party-discipline analogy, Politburo statement and final pot comparison retained without normalization or outside reconciliation.

## Current exact next activity — English iteration Stories 26–35

Process the next **10 stories in collection order**, beginning with Story 26 and ending with Story 35. Close all ten before advancing the tracker.

### Story 26 start

- title: **`பொறுமைக்கு சான்று`**;
- workspace: `stories/porumaikku-saandru/`;
- verified physical span: **lower scan 60 / printed page 58 → upper scan 61 / printed page 59**;
- Story 25 closes above Story 26 on shared scan **60**;
- Story 27 opens below Story 26's ending ornament on shared scan **61**.

### Iteration endpoint

Story 35:

- TOC: **`தும்... பம்... தீம்... தோம்`**;
- opening: **`தும் பம் தீம் தோம்`**;
- workspace: `stories/thum-pam-theem-thom/`;
- verified physical span: **lower scan 73 → scans 74–75 → upper scan 76**.

Before the iteration, read the mandatory startup controls in `NEXT_CHAT_PROMPT.md`. For each story read its README, canonical Tamil assembly, all page records, page map, audit, `POSSIBLE_ERRORS_FOR_REVIEW.md`, `text-fidelity.md` and `visual-fidelity.md`; translate from verified Tamil, not OCR; create English and review files; preserve physical page anchors and source-sensitive structure. Synchronize story READMEs and collection/root controls only after the full ten-story iteration is durable.

Modernization, adaptation, republication and Digital Library onboarding remain outside the current authorization.