# HANDOVER — Kalaignar Short Stories Archive

## Repository

- Repository: `pugazg/kalaignar-short-stories`
- Branch: `main`
- Story workflow: `SHORT_STORY_PROCESSING_GUIDE.md`
- Anthology workflow: `COLLECTION_SOURCE_GUIDE.md`
- Text-fidelity workflow: `TEXT_FIDELITY_CHECK_GUIDE.md`
- Text-fidelity tracker: `TEXT_FIDELITY_PROGRESS.md`
- Visual-fidelity workflow: `VISUAL_FIDELITY_CHECK_GUIDE.md`
- English-translation workflow: `ENGLISH_TRANSLATION_GUIDE.md`
- Source PDFs / renders / crops are **not** committed.

## Authoritative-state rule

Always fetch live `main` first and preserve newer durable work.

## Permanent source rules

- controlling scan first; no silent modernization of spelling, punctuation, grammar, sandhi, names or source anomalies;
- running headers/page numbers are furniture, not body text;
- `POSSIBLE_ERRORS_FOR_REVIEW.md` is a human-review queue, not proof of error;
- source-supported corrections propagate through page, assembly, audit/review and dependent layers;
- shared physical boundary scans preserve each story's exact source span;
- do not commit controlling PDFs or inspection artefacts.

## Closed 1977 anthology

`கலைஞர் கருணாநிதியின் சிறுகதைகள்` remains durably closed:

- Tamil source: **37 / 37 complete**, 0 blocked / 0 unresolved;
- visual fidelity: **37 / 37 complete**;
- English translation/review: **37 / 37 complete**;
- final English structural/control QA: **PASS**;
- scan **260**: verified back cover.

Story 29 `திடுக்கிடும் கதை` retains its later marker-only provenance correction. Canonical Tamil and English prose were unchanged; old Wave-2 pin `a9b333f12128686785ee981f97313a64af12e29b` is obsolete.

## Closed Tamil source pass — கலைஞர் சொன்ன கதைகள்

Collection workspace: `collections/2008-kalaignar-sonna-kathaigal/`

Controlling source: `TVA_BOK_0065857_கலைஞர்_சொன்ன_கதைகள்.pdf`

- printed author: **டாக்டர் கலைஞர் மு. கருணாநிதி**;
- scanned edition: **Second Edition, December 2008**;
- source SHA-256: `1b2bf86892717776b1b3dc7fcb18dc146d5bfd0d60986509dc9cbbf5f235444b`;
- file size: **24,840,000 bytes**;
- PDF scans: **82**;
- contents entries: **40**;
- story text: scans **9–81 / printed 7–79**;
- scan **82**: verified back cover, no further story text;
- relation: **scan = printed page + 2**;
- canonical workspaces / Tamil source complete: **40 / 40**;
- Tamil source pending: **0 / 40**;
- blocked / unresolved source story text: **0**;
- English from this collection: **0 / 40**.

Nine TOC/opening-heading differences remain registered and must not be normalized: Stories **2, 11, 24, 27, 28, 29, 35, 36, 39**.

## Closed phase — word-by-word text fidelity

The user explicitly authorized **text fidelity for every word** with **10 stories per iteration**. That phase is now durably complete.

### Final status

- total: **40**
- fidelity complete: **40 / 40**
- `PASS`: **19**
- `PASS — corrected`: **21**
- pending: **0 / 40**
- needs recheck: **0**
- unresolved fidelity issues: **0**
- story-local `text-fidelity.md`: **40 / 40**

Existing source-pass `verified` status was not treated as proof. Every story was re-read directly against the controlling scans for words, joined/separated forms, punctuation, quotation marks, paragraph boundaries and physical page joins.

### Fidelity iteration 1 — Stories 1–10

Stories **1, 4, 5, 7, 8 and 10** passed unchanged. Stories **2, 3, 6 and 9** required source-supported corrections.

### Fidelity iteration 2 — Stories 11–20

Stories **11 and 16** passed unchanged. Stories **12, 13, 14, 15, 17, 18, 19 and 20** required source-supported corrections.

Recovered readings include `தொடவும்`, `ஊடுதல் செயலாளராக`, first `காப்புமுற்றிருக்கின்றது`, `உயர் ஜாதிக்காரனுக்குக்`, `போர் வீரன்படம்`, `பேச்சைக்`, `என்னடா?`, and Story-20 comma/period punctuation.

### Fidelity iteration 3 — Stories 21–30

Stories **21, 22, 23, 26, 27, 29 and 30** passed unchanged. Stories **24, 25 and 28** required source-supported corrections.

Recovered details include Story-24 `தூக்கி நிறுத்திய`, `கடிதமாகத் தீட்டினேன்`, `தொடுவான்! துவளமாட்டான்.`, `சல்லாபத்`, `தொடங்குவதற்கு`; Story-25 `புராணிகள் கூறுவர்`, `முதல்வராக அமர்ந்து அரசோச்சியவர்`, `தீர்ப்பையொட்டி`, `சொர்க்கத்தில் இருக்கலாம்`, `சொர்க்கம் செல்பவனின்`; and Story-28 `பதைத்துப் போன புலவர்`.

### Fidelity iteration 4 — Stories 31–40

Stories **36, 38, 39 and 40** passed unchanged. Stories **31, 32, 33, 34, 35 and 37** are **PASS — corrected**.

Important recovered source details:

- Story 31: `மாட்டா (து)` → **`மாட்டா(து)`**; `எவ்வளவு நான்` → **`எவ்வளவு நாள்`**;
- Story 32: source double quotation marks restored; `மாத்திர மல்ல`; `வருகின்ற வரை`; `குட்டியைத் தேடி`;
- Story 33: `கரம் இழந்தான்,` → **`கரம் இழந்தான்.`**;
- Story 34: `ஒவ்வொருவருவாக` → **`ஒவ்வொருவராக`**;
- Story 35: `ஊதுவார்களா?`, source `அப்போது புகழேந்தி.`, source double quotation marks on scan 75, and scan-76 **`(தும், ‘தும்’, ‘பம்’, ‘பம்’, ‘தீம்..... தீம்’)`**;
- Story 37: the completed scan-78 couplet preserves its visibly asymmetric source quotation punctuation — single opening quote and double closing quote.

All confirmed corrections are synchronized through affected page records, Tamil assemblies, audits, review queues and story-local fidelity records.

## Current phase gate

There is **no remaining text-fidelity work** for the 2008 collection and there is no Story 41. Do not silently begin English translation, visual-fidelity review, Digital Library onboarding, adaptation, modernization or another downstream phase.

The next activity must be explicitly authorized by the user. Live `main` remains authoritative at every fresh-chat start.
