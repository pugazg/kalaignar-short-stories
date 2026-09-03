# HANDOVER — Kalaignar Short Stories Archive

## Repository

- Repository: `pugazg/kalaignar-short-stories`
- Branch: `main`
- Story workflow: `SHORT_STORY_PROCESSING_GUIDE.md`
- Anthology workflow: `COLLECTION_SOURCE_GUIDE.md`
- Visual-fidelity workflow: `VISUAL_FIDELITY_CHECK_GUIDE.md`
- English-translation workflow: `ENGLISH_TRANSLATION_GUIDE.md`
- Source PDFs / renders / crops are **not** committed.

## Authoritative-state rule

Always fetch live `main` first and preserve newer durable work.

## Permanent source rules

- Controlling scan first; do not silently modernize spelling, punctuation, grammar, sandhi, names or source anomalies.
- Running headers, printed page numbers and printer signatures are page furniture, not story body.
- `POSSIBLE_ERRORS_FOR_REVIEW.md` is a human-review queue, not proof of error.
- Source-supported corrections propagate through page records, assembly, audit/review and dependent layers.
- Shared physical boundary scans preserve the exact span of each story; do not reassign text to make TOC-derived ranges artificially non-overlapping.
- Each canonical story receives a fresh duplicate check before activation.
- Current user instruction: **process 10 stories in each iteration**. Every story still receives independent source review and closure.
- Do not commit controlling PDFs or generated visual-inspection artefacts.

## Closed 1977 anthology

The 1977 anthology `கலைஞர் கருணாநிதியின் சிறுகதைகள்` remains durably closed:

- Tamil source transcription/audit: **37 / 37 complete**, 0 blocked / 0 unresolved;
- visual fidelity: **37 / 37 complete**;
- English translation/review: **37 / 37 complete**, 0 pending / 0 needs review;
- final English structural/control QA: **PASS**;
- scan **260**: verified back cover.

Story 29 `திடுக்கிடும் கதை` has the evidence-driven marker-only page-anchor correction; canonical Tamil and English prose were unchanged. Obsolete downstream pin `a9b333f12128686785ee981f97313a64af12e29b` must not be reused.

## Active collection — கலைஞர் சொன்ன கதைகள்

Controlling source: `TVA_BOK_0065857_கலைஞர்_சொன்ன_கதைகள்.pdf`

Collection workspace: `collections/2008-kalaignar-sonna-kathaigal/`

- represented edition: **Second Edition, December 2008**;
- PDF scans: **82**;
- printed contents entries: **40**;
- story-text scans: **9–81 / printed pages 7–79**;
- scan **82**: verified back cover;
- pagination relation: **scan = printed page + 2**;
- contents / opening intake: **40 / 40 complete**;
- canonical workspaces activated: **11 / 40**;
- Tamil source processing complete: **11 / 40**;
- Tamil source processing pending: **29 / 40**;
- English translation from this collection: **0 / 40**.

## Completed first 10-story iteration

Story 1 had already been closed independently. The user then expanded execution to 10 stories per iteration. The first such iteration, **Stories 2–11**, is now source-complete.

Completed canonical workspaces:

1. `stories/appadithan-sirippen/` — Story 1 `அப்படித்தான் சிரிப்பேன்`;
2. `stories/ice-katti/` — Story 2 TOC `ஐஸ்கட்டி` / opening `ஐஸ் கட்டி`;
3. `stories/thalaiyil-malai/` — Story 3 `தலையில் மலை`;
4. `stories/verum-kai-muzham-podum/` — Story 4 `வெறும் கை முழம் போடும்`;
5. `stories/koottani/` — Story 5 `கூட்டணி`;
6. `stories/seera-vendama/` — Story 6 `சீற வேண்டாமா?`;
7. `stories/kazhuthaiyin-kathai/` — Story 7 `கழுதையின் கதை`;
8. `stories/unakku-vayathenna/` — Story 8 `உனக்கு வயதென்ன?`;
9. `stories/thamizan-endru-sollada/` — Story 9 `தமிழன் என்று சொல்லடா!`;
10. `stories/kadamai-kanniyam-kattuppadu/` — Story 10 `கடமை கண்ணியம் கட்டுப்பாடு`;
11. `stories/saavi-thaan-illai/` — Story 11 TOC `சாவிதான் இல்லை` / opening `சாவி தான் இல்லை`.

Every completed 2008 story has **0 blocked / 0 unresolved story text**. Story-level audits are PASS. English has not started.

### Newly confirmed source fact

Story 11 adds a sixth title variance: TOC **`சாவிதான் இல்லை`** ↔ opening **`சாவி தான் இல்லை`**. This is now preserved alongside the five intake variances.

## Exact next iteration — Stories 12–21

Process exactly these ten stories unless the user explicitly expands the batch:

12. `கண்ணில் கால்` — printed **27**, scan **29**, boundary **30**;
13. `மயில் ராவணன்` — printed **28–29**, scans **30–31**, boundary **32**;
14. `ஜாடி குட்டி போடுமா?` — printed **30**, scan **32**, boundary **33**;
15. `ஒண்ணு குடுமா?` — printed **31–32**, scans **33–34**, boundary **35**;
16. `அத்திரி பாச்சா` — printed **33**, scan **35**, boundary **36**;
17. `செருப்போடு இரு` — printed **34**, scan **36**, boundary **37**;
18. `இடிக்குப் பின் மழை` — printed **35–36**, scans **37–38**, boundary **39**;
19. `நடக்குமா நடக்காதா?` — printed **37–39**, scans **39–41**, boundary **42**;
20. `கனியும் கணையும்` — printed **40**, scan **42**, boundary **43**;
21. `இதயம் பேசுகிறது` — printed **41**, scan **43**, boundary **44**.

For each story: fetch/preserve live main, re-check canonical title variants, inspect the controlling source directly, preserve exact punctuation/paragraphs/non-text ornaments, inspect the next heading scan for a possible preceding-story tail, and exclude adjacent-story prose.

## Phase guard

This active phase authorizes source-first Tamil processing of `கலைஞர் சொன்ன கதைகள்`. It does not authorize modernization, adaptation, republication, Digital Library onboarding, English translation, or changes to other repositories.
