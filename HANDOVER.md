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
3. Inspect the latest completed story workspace (`stories/thappivittargal/`) as structural reference.
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
- Tamil source processing complete: **10 / 37**
- stories not yet transcribed: **27 / 37**
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
10. `தப்பிவிட்டார்கள்` — `stories/thappivittargal/` — printed **75–82**, scans **84–91**, **8/8 verified**, 0 blocked, 0 unresolved, audit PASS.

All completed anthology stories have complete Tamil assemblies and persistent human possible-error queues.

## Story 10 — தப்பிவிட்டார்கள் — COMPLETE TAMIL SOURCE PASS

Canonical workspace: `stories/thappivittargal/`

- page records: **8 / 8**
- verified: **8 / 8**
- blocked: **0**
- unresolved story text: **0**
- Tamil assembly: complete
- source audit: **PASS**
- English: not started

Boundary / continuation checks:

- scan 84 opens `தப்பிவிட்டார்கள்`.
- scans 84→85 / printed 75→76: `...ராமதுரை அன்று இரவு ஏழு மணிக்கு` → `இறந்துவிட்டார்!......`.
- scans 86→87 / printed 77→78: `...விட்டலின் பயங்கரக் கவலைகளை` → `யெல்லாம் எத்தனையோ முறை...`.
- scans 90→91 / printed 81→82: `...சோகத்தை அதிகமாக்கின. கரையில்` → `ஏறிக்கொண்டு பலங் கொண்ட மட்டும்...`.
- scan 91 contains the conclusion and closing ornament.
- scan 92 opens Story 11 `தப்பவில்லை`; Story 11 text is not included.

High-value enlarged full-span resolutions recorded in the story workspace include scan 89 `தங்களிருவர்களிடையே ஏற்பட்டுப்போகும் பெரியதொரு பயங்கரமான நிகழ்ச்சி, அவர்களைப் பைத்தியம்போல ஆட்டிவைத்தது.` and scan 91 `தங்கம் தன் ஆசையனைத்தையும் ஒருசேர உதட்டில் சேர்த்து விட்டலை முத்தமிட்டாள்.` Unusual or enhancement-sensitive forms remain in `stories/thappivittargal/POSSIBLE_ERRORS_FOR_REVIEW.md` for later human checking without downgrading the verified page status.

## Next exact activity

Process anthology Story **11 — `தப்பவில்லை`** only.

- printed pages: **83–92**
- anthology scans: **92–101**

Boundary checks:

- scan **92** must open `தப்பவில்லை`;
- scan **101** must close Story 11;
- scan **102** must be checked as the opening of Story 12 `ஆதரிக்கிறார்`.

Actions:

1. fetch live `main` and confirm no matching canonical `தப்பவில்லை` workspace exists;
2. visually verify scans 92 / 101 / 102 from the controlling PDF;
3. create the Story 11 workspace only after canonical-story check;
4. create **10** page records for scans 92–101 / printed pages 83–92;
5. transcribe directly from scan and perform full-span visual review on every page;
6. exhaust difficult readings before `blocked` and maintain a human possible-error queue;
7. create assembled Tamil, audit, source metadata, page map and story README;
8. verify every physical page-boundary continuation and confirm no omitted/duplicated pages;
9. synchronize anthology/root control files;
10. **do not begin Story 12 (`ஆதரிக்கிறார்`) in the same activity.**

Expected progress after successful Story 11 closure: **11 / 37 complete, 26 remaining**.

## New-chat readiness

**READY FOR CONTINUATION.**
