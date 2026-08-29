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
3. Inspect the latest completed story workspace (`stories/munnuru-rupai/`) as structural reference.
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
- Tamil source processing complete: **14 / 37**
- stories not yet transcribed: **23 / 37**
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
14. `முந்நூறு ரூபாய்` — `stories/munnuru-rupai/` — printed **103–105**, scans **112–114**, **3/3 verified**, 0 blocked, 0 unresolved, audit PASS.

All completed anthology stories have complete Tamil assemblies and persistent human possible-error queues.

## Story 14 — முந்நூறு ரூபாய் — COMPLETE TAMIL SOURCE PASS

Canonical workspace: `stories/munnuru-rupai/`

- page records: **3 / 3**
- verified: **3 / 3**
- blocked: **0**
- unresolved story text: **0**
- Tamil assembly: complete
- source audit: **PASS**
- English: not started

Boundary / continuation checks:

- scan 112 opens `முந்நூறு ரூபாய்`.
- scans 112→113 / printed 103→104: `...என்று எத்தனையோ` → `பேர் தங்கப்பன் யாசகம் கேட்டிருக்கிறார்கள்.`.
- scans 113→114 / printed 104→105: `...என் வெற்றிலைப் பாக்குக் கடையில் வியாபாரம் செய்ய முடியுமா?”` → `என்று அவனைக் கேட்டான்.`.
- scan 114 contains the final reversal and closing ornament.
- scan 115 opens Story 15 `ஏழை`; Story 15 text is not included.

High-value source-close/full-span rechecks recorded in the story workspace include scan 112 `ஆளே தரித்திர நாராயணனைத் துடித்தான்`, scan 113 `எழுபட்டு நாட்களாகி விட்டன` and `வரும் வழியிலே யெல்லாம் நல்ல உயிர் இல்லை`, and scan 114 `குதாகலமாய்`, `ஓடும்பிள்ளையாய்`, `பிளேயர்ஸ் சிகரெட்டைப்`, and the final `நல்லவேளை வெளியே செல்ல டிக்கெட்டாவது இருந்தது!`. Unusual readings remain in `stories/munnuru-rupai/POSSIBLE_ERRORS_FOR_REVIEW.md` for later human checking without downgrading verified page status.

## Next exact activity

Process anthology Story **15 — `ஏழை`** only.

- printed pages: **106–109**
- anthology scans: **115–118**

Boundary checks:

- scan **115** must open `ஏழை`;
- scan **118** must close Story 15;
- scan **119** must be checked as the opening of Story 16 `ஒரிஜினலில் உள்ளபடி`.

Actions:

1. fetch live `main` and confirm no matching canonical `ஏழை` workspace exists;
2. visually verify scans 115 / 118 / 119 from the controlling PDF;
3. create the Story 15 workspace only after canonical-story check;
4. create **4** page records for scans 115–118 / printed pages 106–109;
5. transcribe directly from scan and perform full-span visual review on every page;
6. exhaust difficult readings before `blocked` and maintain a human possible-error queue;
7. create assembled Tamil, audit, source metadata, page map and story README;
8. verify every physical page-boundary continuation and confirm no omitted/duplicated pages;
9. synchronize anthology/root control files;
10. **do not begin Story 16 (`ஒரிஜினலில் உள்ளபடி`) in the same activity.**

Expected progress after successful Story 15 closure: **15 / 37 complete, 22 remaining**.

## New-chat readiness

**READY FOR CONTINUATION.**
