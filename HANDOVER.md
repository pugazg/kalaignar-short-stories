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
- 2008 English tracker: `collections/2008-kalaignar-sonna-kathaigal/ENGLISH_TRANSLATION_PROGRESS.md` — closed at **40 / 40**

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

## 2008 collection — SOURCE / TEXT / VISUAL / ENGLISH CLOSED

Collection: **கலைஞர் சொன்ன கதைகள்**  
Workspace: `collections/2008-kalaignar-sonna-kathaigal/`  
Controlling source: `TVA_BOK_0065857_கலைஞர்_சொன்ன_கதைகள்.pdf`

- represented edition: **Second Edition, December 2008**;
- PDF scans: **82**;
- story text: scans **9–81 / printed pages 7–79**;
- scan **82**: verified back cover, no further story text;
- Tamil source: **40 / 40 complete**, 0 blocked / 0 unresolved;
- word-by-word text fidelity: **40 / 40 complete — 19 PASS / 21 PASS — corrected**;
- visual fidelity: **40 / 40 complete — all 40 PASS**;
- English translation/review: **40 / 40 PASS**, 0 pending, 0 `NEEDS REVIEW`;
- canonical Tamil changed during English work: **No**.

Nine TOC/opening-heading differences remain registered and must not be normalized: Stories **2, 11, 24, 27, 28, 29, 35, 36, 39**.

## Final English batching history

- Stories **1–4**: completed individually;
- Stories **5–14**: **10 / 10 PASS**;
- Story **15**: completed individually;
- Stories **16–25**: **10 / 10 PASS**;
- user-expanded final iteration Stories **26–40**: **15 / 15 PASS**.

Every 2008 story now has:

- complete English under `translations/en/`;
- story-local `TRANSLATION_REVIEW.md` with result **PASS**;
- synchronized story README;
- source-marker sequence checked;
- actual physical content-boundary alignment checked independently of marker order;
- source-significant final `*` preserved;
- no Tamil change caused merely by translation.

## Final iteration — Stories 26–40

Key controls retained:

26. **`பொறுமைக்கு சான்று`** — markers **60→61**; `வழக்கம்பொழுது` left untouched in Tamil; Prophet narrative translated conservatively.
27. TOC **`எடுக்கவோ கோக்கவோ!`** / opening **`எடுக்கவோ கோக்கவோ`** — markers **61→62**; source `சோதரைப் போர்க்களத்தில்` not silently repaired.
28. TOC **`அந்த நாள் வந்திலை...`** / opening **`அந்த நாள் வந்திலை!`** — markers **62→63→64**; corrected `பதைத்துப் போன புலவர்`; four-line verse preserved.
29. TOC **`பனித் துளியில் பனைமரம்`** / opening **`பனித்துளியில் பனை மரம்`** — markers **64→65**; physical `பக்கத்`→`திலே` split aligned.
30. **`பாரூர் போல...`** — markers **65→66**; all three source verse/display blocks preserved.
31. **`இராமனைப் பற்றி இராமன்`** — markers **66→67→68→69**; three Kamban blocks and corrected `மாட்டா(து)` / `எவ்வளவு நாள்` retained.
32. **`மானும் பெருமானும்`** — markers **69→70→71**; corrected dialogue punctuation and `மாத்திர மல்ல`, `வருகின்ற வரை`, `குட்டியைத் தேடி` retained.
33. **`எழுச்சிக்கு அடையாளம்`** — markers **71→72**; corrected `கரம் இழந்தான்.` retained.
34. **`தலையும் நுனியும்`** — markers **72→73**; corrected `ஒவ்வொருவராக` retained.
35. TOC **`தும்... பம்... தீம்... தோம்`** / opening **`தும் பம் தீம் தோம்`** — markers **73→74→75→76**; source rhythmic wordplay and parenthetical punctuation retained.
36. TOC **`நல்லவழியும் நல்ல வழியும்`** / opening **`நல்வழியும் நல்ல வழியும்`** — markers **76→77**; two-line `நல் வழி` verse preserved.
37. **`நாக்குத் தமிழ் மணக்கும்`** — markers **77→78→79**; incomplete/completed poetic display and asymmetric source quotation punctuation preserved.
38. **`நீதி தேவதையே!`** — markers **79→80**; seven-line Abdul Rahman poem preserved.
39. TOC **`நன்றி சொல்லும் நேரம்...`** / opening **`நன்றி சொல்லும் நேரம்`** — markers **80→81**; unfinished-thought physical boundary aligned.
40. **`பந்தலிலே பாகற்காய்`** — marker **81**; all three oppari/song blocks and repetitions preserved; scan **82** remains back-cover witness only.

## Current exact next activity — final 2008 English structural/control QA

No translation story remains.

Perform a final collection-wide QA across all **40** 2008 English stories before opening any new downstream phase. Verify at minimum:

1. every story has exactly one expected English file under `translations/en/` and a story-local `TRANSLATION_REVIEW.md`;
2. every review result is **PASS** and no story remains `pending`, `in progress` or `NEEDS REVIEW`;
3. validator-compatible source markers use exactly `<!-- source scan N; printed page M -->`;
4. marker sequence and printed-page values agree with the verified physical story spans;
5. actual translated content boundaries align with the verified Tamil page records, including shared scans and split words/sentences;
6. every source-significant final `*` remains present;
7. the nine TOC/opening-heading differences remain documented and unnormalized;
8. Story 40 ends on scan **81 / printed 79**, and scan **82** remains back-cover matter only;
9. story READMEs, 2008 English tracker, collection README/source metadata, root README, this `HANDOVER.md` and `NEXT_CHAT_PROMPT.md` all agree at **40 / 40 PASS**;
10. re-fetch live `main` and key controls before declaring final QA closure.

Modernization, adaptation, republication and Digital Library onboarding remain outside current authorization.