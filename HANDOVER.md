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
3. Inspect the latest completed story workspace (`stories/thaaymai/`) as structural reference.
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
- Tamil source processing complete: **9 / 37**
- stories not yet transcribed: **28 / 37**
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
9. `தாய்மை` — `stories/thaaymai/` — printed **64–74**, scans **73–83**, **11/11 verified**, 0 blocked, 0 unresolved, audit PASS.

All completed anthology stories have complete Tamil assemblies and persistent human possible-error queues.

## Story 9 — தாய்மை — COMPLETE TAMIL SOURCE PASS

Canonical workspace: `stories/thaaymai/`

- page records: **11 / 11**
- verified: **11 / 11**
- blocked: **0**
- unresolved story text: **0**
- Tamil assembly: complete
- source audit: **PASS**
- English: not started

Boundary / continuation checks:

- scan 73 opens `தாய்மை`.
- scans 74→75: `...சித்திக்கும் யோசனைகள் தரவும்` → `நான் தயங்கமாட்டேன்.`
- scans 78→79: `...தெரியாதவள்போல` → `அவள், ...`.
- scans 80→81: `...அந்த அழகுப் பிறை நிலவு,` → `சின்னம்மா கற்றுத்தந்த...`.
- scan 83 contains the conclusion and closing ornament.
- scan 84 opens Story 10 `தப்பிவிட்டார்கள்`; Story 10 text is not included.

High-value enlarged resolutions include scan 76 `அவள் மடியில் சாய்ந்தான்—பிடியில் சிக்கினான்.` and scan 81 `வயிற்றிலே கிடந்த வைடூரியம்! அதை விஷத்தால் குளிப்பாட்டி வேகவைக்க எதிரே மரணத்தின் மயக்கம் நிறைந்த சதிராட்டம்!`.

## Next exact activity

Process anthology Story **10 — `தப்பிவிட்டார்கள்`** only.

- printed pages: **75–82**
- anthology scans: **84–91**

Boundary checks:

- scan **84** must open `தப்பிவிட்டார்கள்`;
- scan **91** must close Story 10;
- scan **92** must be checked as the opening of Story 11 `தப்பவில்லை`.

Actions:

1. fetch live `main` and confirm no matching canonical workspace exists;
2. visually verify scans 84 / 91 / 92;
3. create the Story 10 workspace only after canonical check;
4. create **8** page records for scans 84–91 / printed 75–82;
5. transcribe directly from scan and perform full-span visual review;
6. exhaust difficult readings before `blocked` and maintain a human possible-error queue;
7. create assembled Tamil, audit, source metadata and story README;
8. synchronize anthology/root control files;
9. **do not begin Story 11 (`தப்பவில்லை`) in the same activity.**

## New-chat readiness

**READY FOR CONTINUATION.**
