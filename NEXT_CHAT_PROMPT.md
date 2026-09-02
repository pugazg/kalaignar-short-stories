# NEXT CHAT PROMPT — Kalaignar Short Stories Archive

Repository: `https://github.com/pugazg/kalaignar-short-stories`
Branch: `main`
Controlling anthology source: `TVA_BOK_0064142_கலைஞர்_கருணாநிதியின்_சிறுகதைகள்.pdf`

## LIVE MAIN IS AUTHORITATIVE

Fetch live `main` first and preserve newer durable work.

## DURABLE STATE

- Tamil source processing: **37 / 37 complete**
- visual fidelity: **37 / 37 complete**
- English translation/review: **37 / 37 complete**
- English final structural/control QA: **PASS**
- English pending: **0 / 37**
- English needs review: **0**
- unresolved anthology story text: **0**
- final story: `நுனிக்கரும்பு`, scans **253–259 / printed 244–250**
- scan **260**: verified anthology back cover

Final English batch:

35. `சுமந்தவள்` — **PASS**
36. TOC `சித்தார்த்தன்` / opening `சித்தார்த்தன் சிலை` — **PASS**
37. `நுனிக்கரும்பு` — **PASS**

Every anthology story has a committed English file and `TRANSLATION_REVIEW.md`, with source-page markers retained and canonical Tamil unchanged during translation.

The post-translation structural/control audit is recorded in `ENGLISH_TRANSLATION_FINAL_QA.md` and remains **PASS**.

## Post-completion Story-29 source correction

On 2026-09-02, downstream Digital Library Wave-2 ingestion exposed that Story 29 `திடுக்கிடும் கதை` had ordered English source-page markers whose **content anchoring was wrong from scan 200 onward**. The English prose was complete; the final scan-204 marker section was empty.

The markers were re-anchored against all six verified Tamil page records without changing English prose or canonical Tamil. The Story-29 review preserves the history and is **PASS after re-verification**. `ENGLISH_TRANSLATION_GUIDE.md` now requires content-boundary validation, with `scripts/validate-english-page-anchors.py` and the Story-29 `translations/en/page-anchors.json` manifest as the regression guard.

The old downstream source pin `a9b333f12128686785ee981f97313a64af12e29b` predates this correction and must not be reused for Wave 2. A downstream source freeze must be recomputed from current live `main`.

There is **no pending anthology story translation or source correction activity**.

For any future work, fetch live `main` and read the repository guides, `ENGLISH_TRANSLATION_PROGRESS.md`, `ENGLISH_TRANSLATION_FINAL_QA.md`, `PROJECT_COMPLETION.md`, `HANDOVER.md`, and this prompt before changes. Preserve the documented TOC/opening-title differences. If a future English revision suggests a Tamil-source problem, recheck that exact Tamil span against the controlling source before changing the source layer.

Do not start modernization, adaptation, republication, release packaging, Digital Library onboarding, or another new project phase unless the user explicitly requests it.
