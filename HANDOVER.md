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
3. Inspect the latest completed story workspace (`stories/ezhai/`) as structural reference.
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
- Tamil source processing complete: **15 / 37**
- stories not yet transcribed: **22 / 37**
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
15. `ஏழை` — `stories/ezhai/` — printed **106–109**, scans **115–118**, **4/4 verified**, 0 blocked, 0 unresolved, audit PASS.

All completed anthology stories have complete Tamil assemblies and persistent human possible-error queues.

## Story 15 — ஏழை — COMPLETE TAMIL SOURCE PASS

Canonical workspace: `stories/ezhai/`

- page records: **4 / 4**
- verified: **4 / 4**
- blocked: **0**
- unresolved story text: **0**
- Tamil assembly: complete
- source audit: **PASS**
- English: not started

Boundary / continuation checks:

- scan 115 opens `ஏழை`.
- scans 115→116 / printed 106→107: `...ஒரு சில நிமிடங்கள் கூட ஒதுக்க` → `முடியவில்லை.`.
- scans 116→117 / printed 107→108: `...இவைகளிலே மோதிக்கொண்டிருந்தன. இன்பக்` → `கனவு இல்லாவிட்டால்...`.
- scans 117→118 / printed 108→109: `...மரத்தடியில் நின்றுவிட்டாள்` → `பார்வதி.`.
- scan 118 contains the final reveal and closing ornament.
- scan 119 opens Story 16 `ஒரிஜினலில் உள்ளபடி`; Story 16 text is not included.

High-value source-close/full-span rechecks recorded in the story workspace include scan 115 `மழலை மொழிகட்குப்` and `அந்தத் தீராத விளையாட்டுப் பிள்ளை தொடர்ச்சி கெடுக்கும்படி`; scan 116 `காம வீணையை மீட்டதும் புலம்பவும் கடவுளை எண்ணி அழவும் போதுபோக`, `காப்பப் பையை மாற்றிப் போட்ட வசதியா`, and `இப்பேர்ப்பட்டவன்தான்`; scan 117 repeated `முக்குத்தி` and source-form `பார்வதிக்கு பானு நனைந்து விடுவாளே என்று பயந்தான்.`; and scan 118 final `யார் அது? “ஏழை”!`. Unusual readings remain in `stories/ezhai/POSSIBLE_ERRORS_FOR_REVIEW.md` for later human checking without downgrading verified page status.

## Next exact activity

Process anthology Story **16 — `ஒரிஜினலில் உள்ளபடி`** only.

- printed pages: **110–116**
- anthology scans: **119–125**

Boundary checks:

- scan **119** must open `ஒரிஜினலில் உள்ளபடி`;
- scan **125** must close Story 16;
- scan **126** must be checked as the opening of Story 17 `பனங்குலை`.

Actions:

1. fetch live `main` and confirm no matching canonical `ஒரிஜினலில் உள்ளபடி` workspace exists;
2. visually verify scans 119 / 125 / 126 from the controlling PDF;
3. create the Story 16 workspace only after canonical-story check;
4. create **7** page records for scans 119–125 / printed pages 110–116;
5. transcribe directly from scan and perform full-span visual review on every page;
6. exhaust difficult readings before `blocked` and maintain a human possible-error queue;
7. create assembled Tamil, audit, source metadata, page map and story README;
8. verify every physical page-boundary continuation and confirm no omitted/duplicated pages;
9. synchronize anthology/root control files;
10. **do not begin Story 17 (`பனங்குலை`) in the same activity.**

Expected progress after successful Story 16 closure: **16 / 37 complete, 21 remaining**.

## New-chat readiness

**READY FOR CONTINUATION.**
