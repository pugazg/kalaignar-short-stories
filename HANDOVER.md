# HANDOVER — Kalaignar Short Stories Archive

## Repository

- Repository: `pugazg/kalaignar-short-stories`
- Branch: `main`
- Story workflow: `SHORT_STORY_PROCESSING_GUIDE.md`
- Collection workflow: `COLLECTION_SOURCE_GUIDE.md`
- Text-fidelity workflow/tracker: `TEXT_FIDELITY_CHECK_GUIDE.md` / `TEXT_FIDELITY_PROGRESS.md`
- 2008 visual workflow/tracker: `collections/2008-kalaignar-sonna-kathaigal/VISUAL_FIDELITY_GUIDE.md` / `collections/2008-kalaignar-sonna-kathaigal/VISUAL_FIDELITY_PROGRESS.md`
- English workflow: `ENGLISH_TRANSLATION_GUIDE.md`
- 1977 English tracker: `ENGLISH_TRANSLATION_PROGRESS.md` — closed at **37 / 37**
- 2008 English tracker: `collections/2008-kalaignar-sonna-kathaigal/ENGLISH_TRANSLATION_PROGRESS.md`

## LIVE MAIN IS AUTHORITATIVE

Always fetch live `main` first and preserve newer durable work. Source PDFs / renders / crops are not committed. Repository files reachable from live `main`, not chat memory or local preparation, are durable state.

## Permanent source / translation rules

- controlling scan first; no silent modernization or normalization;
- canonical verified Tamil is authoritative for English translation;
- running headers and printed page numbers are page furniture, not body text;
- shared physical scans preserve exact story boundaries;
- source-supported textual corrections propagate through page, assembly, audit/review and dependent layers;
- `POSSIBLE_ERRORS_FOR_REVIEW.md` is a human-review queue, not proof of error;
- English page markers must use exactly `<!-- source scan N; printed page M -->`;
- boundary notes belong in separate HTML comments;
- marker presence/order alone is insufficient: actual translated content boundaries must align to the verified Tamil page records.

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

Current durable state after the latest user-expanded batch:

- English complete: **14 / 40**;
- `PASS`: **14**;
- pending: **26 / 40**;
- `NEEDS REVIEW`: **0**;
- canonical Tamil changed during English work: **No**.

Stories **1–4** remain individually closed as previously recorded.

### Latest batch — Stories 5–14

The user explicitly changed the default one-story-per-activity rule for this activity by requesting **10 stories**. Stories **5–14** were therefore processed as one English batch and are all **PASS**.

5. **`கூட்டணி`** — workspace `stories/koottani/`; span lower **17 / 15 → upper 18 / 16**; boundary aligned; source quotation asymmetry and one-prey/two-prey close retained.
6. **`சீற வேண்டாமா?`** — `stories/seera-vendama/`; lower **18 / 16 → upper 19 / 17**; corrected source `ஒரு சீறு சீறி காட்டக்கூடாது என்றா சொன்னேன்.` translated without Tamil normalization; reflective close retained.
7. **`கழுதையின் கதை`** — `stories/kazhuthaiyin-kathai/`; lower **19 / 17 → 20 / 18 → upper 21 / 19**; physical ending on scan 21 retained despite shorter TOC-derived routing; colloquial forms not normalized.
8. **`உனக்கு வயதென்ன?`** — `stories/unakku-vayathenna/`; lower **21 / 19 → upper 22 / 20**; `ஆட்சி மொழி` → `ஆவது?` join aligned; final public-life statement preserved.
9. **`தமிழன் என்று சொல்லடா!`** — `stories/thamizan-endru-sollada/`; lower **22 / 20 → 23–24 → upper 25 / 23**; `பெட்டி கலெக்டர்`, joined `அந்ததமிழருக்கு`, and final `சொல்லடா.. தலைநிமிர்ந்து நில்லடா...` treated as source facts.
10. **`கடமை கண்ணியம் கட்டுப்பாடு`** — `stories/kadamai-kanniyam-kattuppadu/`; lower **25 / 23 → 26 / 24 → upper 27 / 25**; physical ending on scan 27, riddle, squirrel passage, three-line **Duty / Dignity / Discipline** display and `*` retained.
11. TOC **`சாவிதான் இல்லை`** / opening **`சாவி தான் இல்லை`** — `stories/saavi-thaan-illai/`; lower **27 / 25 → 28 / 26**; title variance preserved; source political analogy translated directly without outside constitutional or partisan gloss.
12. **`கண்ணில் கால்`** — `stories/kannil-kaal/`; **29 / 27 → upper 30 / 28**; physical ending on scan 30 retained; corrected `தொடவும்` translated from current verified Tamil.
13. **`மயில் ராவணன்`** — `stories/mayil-ravanan/`; lower **30 / 28 → 31 / 29**; verified unusual `ஊடுதல் செயலாளராக` handled conservatively as **`ooduthal secretary`** rather than normalized; both `(பலத்த கைதட்டல்)` cues preserved.
14. **`ஜாடி குட்டி போடுமா?`** — `stories/jaadi-kutti-poduma/`; **32 / 30 → upper 33 / 31**; distinct source `காப்புமுற்று`, first `காப்புமுற்றிருக்கின்றது`, later `காப்புமுற்றிருக்கிறது`, `காப்பு மடைவதாவது?` remain distinct in Tamil/control; laughter cues and `*` preserved.

Every Story **5–14** workspace now has:

- a complete English file under `translations/en/`;
- `TRANSLATION_REVIEW.md` with result **PASS**;
- synchronized story README;
- verified physical page-boundary alignment;
- no Tamil change caused by translation.

## Current exact next activity — Story 15 English

Return to the default **one story per activity** unless the user explicitly expands the batch again.

Story 15:

- title: **`ஒண்ணு குடுமா?`**;
- workspace: `stories/onnu-kuduma/`;
- verified physical span: **lower scan 33 / printed page 31 → scan 34 / printed page 32 → upper scan 35 / printed page 33**;
- Story 14 ends above the Story-15 opening on shared scan **33**;
- Story 16 **`அத்திரி பாச்சா`** begins below the Story-15 ending ornament on shared scan **35**.

Before Story-15 English work, read completely:

1. `SHORT_STORY_PROCESSING_GUIDE.md`;
2. `COLLECTION_SOURCE_GUIDE.md`;
3. `ENGLISH_TRANSLATION_GUIDE.md`;
4. `collections/2008-kalaignar-sonna-kathaigal/ENGLISH_TRANSLATION_PROGRESS.md`;
5. `TEXT_FIDELITY_CHECK_GUIDE.md` and `TEXT_FIDELITY_PROGRESS.md`;
6. `collections/2008-kalaignar-sonna-kathaigal/VISUAL_FIDELITY_GUIDE.md` and `VISUAL_FIDELITY_PROGRESS.md`;
7. this `HANDOVER.md`;
8. `NEXT_CHAT_PROMPT.md`;
9. collection README, source metadata, story inventory and scan map;
10. Story-15 README, canonical Tamil assembly, all Story-15 page records, page map, audit, `POSSIBLE_ERRORS_FOR_REVIEW.md`, `text-fidelity.md` and `visual-fidelity.md`.

Translate from the verified canonical Tamil assembly, not OCR. Check actual physical content-boundary alignment against the verified Story-15 page records. Create the English file and `TRANSLATION_REVIEW.md`, synchronize story/collection/root controls, re-fetch live `main`, and advance only after Story 15 is fully durable.

Modernization, adaptation, republication and Digital Library onboarding remain outside the current authorization.