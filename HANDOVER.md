# HANDOVER — Kalaignar Short Stories Archive

## Repository

- Repository: `pugazg/kalaignar-short-stories`
- Branch: `main`
- Story workflow: `SHORT_STORY_PROCESSING_GUIDE.md`
- Anthology workflow: `COLLECTION_SOURCE_GUIDE.md`
- Cross-chat resume prompt: `NEXT_CHAT_PROMPT.md`
- Source PDFs are **not** committed to GitHub.

## Permanent source rules

- **Controlling scan first.** Do not silently modernize spelling, grammar, punctuation, names, sandhi or source anomalies.
- **No stones should be left unturned.** Difficult story readings must receive full-span visual escalation before terminal `blocked` status.
- **Processed-crop confidence is not source confidence.** Verify the complete phrase/clause/sentence against the source span.
- `POSSIBLE_ERRORS_FOR_REVIEW.md` is a human-review queue, not a list of confirmed errors.
- A later source-supported correction must be propagated through all affected story, collection and control files.

## Cross-chat restart rules

1. Fetch live GitHub `main` first and treat it as authoritative.
2. Read completely: `SHORT_STORY_PROCESSING_GUIDE.md`, `COLLECTION_SOURCE_GUIDE.md`, `HANDOVER.md`, `NEXT_CHAT_PROMPT.md`, collection README, story inventory and scan map.
3. Inspect the latest completed story workspace (`stories/panangulai/`) as structural reference.
4. Do not redo completed stories without new correction evidence or repository inconsistency.
5. The controlling PDF must be available before transcription/visual verification.
6. When the user says **“Proceed with next activity”**, execute the exact activity below without routine clarification.
7. Process one anthology story at a time.
8. Synchronize story workspace + anthology inventory + collection README + root README + scan map + HANDOVER + NEXT_CHAT_PROMPT before closure.

## Active collection source — 1977 anthology

- filename: `TVA_BOK_0064142_கலைஞர்_கருணாநிதியின்_சிறுகதைகள்.pdf`
- SHA-256: `853032661482eaccb26c083a38d7aa75c081362d33c963c63e37d088bf20acb3`
- file size: **268,486,609 bytes**
- PDF scans: **260**
- edition: **முதல் பதிப்பு: 1977**
- printed story pagination: **1–250**
- story block scans: **10–259**
- relation: **scan = printed page + 9**

Anthology processing state:

- contents inventory: **37 / 37**
- story-start visual checks: **37 / 37**
- Tamil source processing complete: **17 / 37**
- stories not yet transcribed: **20 / 37**
- English translation started: **0 / 37**

## Completed anthology stories

1. `புகழேந்தி` — 6/6 verified.
2. `நளாயினி` — 8/8 verified.
3. `சபலம்` — 7/7 verified.
4. `ஆட்டக்காவடி` — 8/8 verified.
5. `குப்பைத்தொட்டி` — 8/8 verified.
6. `சந்தனக்கிண்ணம்` — 10/10 verified.
7. `சங்கிலிச்சாமி` — 12/12 verified.
8. `கங்கையின் காதல்` — 4/4 verified.
9. `தாய்மை` — 11/11 verified.
10. `தப்பிவிட்டார்கள்` — 8/8 verified.
11. `தப்பவில்லை` — 10/10 verified.
12. `ஆதரிக்கிறார்` — 6/6 verified.
13. `இரகசியம்!` — 4/4 verified.
14. `முந்நூறு ரூபாய்` — 3/3 verified.
15. `ஏழை` — 4/4 verified.
16. `ஒரிஜினலில் உள்ளபடி` — 7/7 verified.
17. `பனங்குலை` — `stories/panangulai/` — printed **117–121**, scans **126–130**, **5/5 verified**, 0 blocked, 0 unresolved, audit PASS.

All completed anthology stories have complete Tamil assemblies and persistent human possible-error queues.

## Story 17 — பனங்குலை — COMPLETE TAMIL SOURCE PASS

Canonical workspace: `stories/panangulai/`

- page records: **5 / 5**
- verified: **5 / 5**
- blocked: **0**
- unresolved story text: **0**
- Tamil assembly: complete
- source audit: **PASS**
- English: not started

Boundary / continuation checks:

- scan 126 opens `பனங்குலை`.
- scans 128→129 / printed 119→120: `...அன்றைய இரவு இன்ப கீதம் பாடி, மெல்ல மெல்ல` → `நகர்ந்தது.`.
- scans 129→130 / printed 120→121: `...போட்டுவிட்டுப் போய்விட்டார்களாம். அதன்` → `பிறகே, அனாதை இல்லம் உன்னை எடுத்து வளர்த்ததாம்.`.
- the 126→127 and 127→128 boundaries were also visually checked with no omission/duplication.
- scan 130 contains the final sentence `இப்படியும் பல பிறவிகள் உண்டு உலகத்தில்!` and closing ornament.
- scan 131 opens Story 18 `செத்தவள் கதை`; Story 18 text is not included.

High-value source-close/full-span rechecks recorded in the story workspace include scan 126 `கண் காணாத சீமைக்கு` and `கரங்கள்தாம்`; scan 127 `பனை நுங்கு`, `பனங் குலைகள்`, `சொந்தந்தானே`; scan 128 `திருடுகிறு?`, `சபலக் குறி தல காட்டியது`, `பாத்தியதை`; scan 129 `சேவல் கூவிற்று`, `ஆணில் வயதேறிக் காணப்படும்`, `மீனாட்சியைத்`, `உன்னைப் பறி கொடுத்ததாக`; and scan 130 the printed colon in `உன் தங்கையைத்:தேடிப்`, plus `பிரக்ஞையற்றுக்`, `இவளைக் தட்டிக்`, `தீக்குச்சியைக் கிழித்து`, `குணாளர்`, and `வீட்டுக்குப்போய்`. Unusual readings remain in `stories/panangulai/POSSIBLE_ERRORS_FOR_REVIEW.md` for later human checking without downgrading verified page status.

## Next exact activity

Process anthology Story **18 — `செத்தவள் கதை`** only.

- printed pages: **122–130**
- anthology scans: **131–139**

Boundary checks:

- scan **131** must open `செத்தவள் கதை`;
- scan **139** must close Story 18;
- scan **140** must be checked as the opening of Story 19 `பிரேத விசாரணை`.

Actions:

1. fetch live `main` and confirm no matching canonical `செத்தவள் கதை` workspace exists;
2. visually verify scans 131 / 139 / 140 from the controlling PDF;
3. create the Story 18 workspace only after canonical-story check;
4. create **9** page records for scans 131–139 / printed pages 122–130;
5. transcribe directly from scan and perform full-span visual review on every page;
6. exhaust difficult readings before `blocked` and maintain a human possible-error queue;
7. create assembled Tamil, audit, source metadata, page map and story README;
8. verify every physical page-boundary continuation and confirm no omitted/duplicated pages;
9. synchronize anthology/root control files;
10. **do not begin Story 19 (`பிரேத விசாரணை`) in the same activity.**

Expected progress after successful Story 18 closure: **18 / 37 complete, 19 remaining**.

## New-chat readiness

**READY FOR CONTINUATION.**
