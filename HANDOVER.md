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
3. Inspect the latest completed story workspace (`stories/seththaval-kathai/`) as structural reference.
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
- Tamil source processing complete: **18 / 37**
- stories not yet transcribed: **19 / 37**
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
17. `பனங்குலை` — 5/5 verified.
18. `செத்தவள் கதை` — `stories/seththaval-kathai/` — printed **122–130**, scans **131–139**, **9/9 verified**, 0 blocked, 0 unresolved, audit PASS.

All completed anthology stories have complete Tamil assemblies and persistent human possible-error queues.

## Story 18 — செத்தவள் கதை — COMPLETE TAMIL SOURCE PASS

Canonical workspace: `stories/seththaval-kathai/`

- page records: **9 / 9**
- verified: **9 / 9**
- blocked: **0**
- unresolved story text: **0**
- Tamil assembly: complete
- source audit: **PASS**
- English: not started

Boundary / continuation checks:

- scan 131 opens `செத்தவள் கதை`.
- scans 134→135 / printed 125→126: `...ஒரு சிறு இரும்புக் கம்பி ஆடிக்` → `கொண்டிருந்தது.`.
- scans 135→136 / printed 126→127: `...வார்த்தையின் ஒவ்வொரு எழுத்தும்` → `நடுங்கின.`.
- scans 138→139 / printed 129→130: `...என் நெஞ்சிலே உன்னைப் ‘போட்டோ’ படமாக்கி` → `வச்சிருந்தேன்! எல்லாத்தையும்...`.
- the remaining physical boundaries were visually checked with no omission/duplication.
- scan 139 contains the final `‘மங்களம்’` sentence and closing ornament.
- scan 140 opens Story 19 `பிரேத விசாரணை`; Story 19 text is not included.

High-value source-close/full-span rechecks recorded in the story workspace include scan 131 `கேட்கத் தூண்டும்`, `ஓட்டப்பம் வீட்டைச் சுடும்` and the opening verse; scan 132 `போடுறியே`; scan 133 `அடுக்கினுக்குள்`; scan 134 `காலோடிய நின்றாள்` and `திமிரென்று முனைத்ததுபோல்`; scan 135 `வருணையா வாரும்`; scan 136 `அதைக் கோதினன்`; scan 137 `ஜீவே`; scan 138 `சமுதாயக் கோளாறுன்னு சங்க நாதம்`; and scan 139 `பேச்சால்`, `கோசா வாக முழிக்கமாட்டேன்`, `தெருவினொப்பாரி` and the final verse. Unusual readings remain in `stories/seththaval-kathai/POSSIBLE_ERRORS_FOR_REVIEW.md` for later human checking without downgrading verified page status.

## Next exact activity

Process anthology Story **19 — `பிரேத விசாரணை`** only.

- printed pages: **131–136**
- anthology scans: **140–145**

Boundary checks:

- scan **140** must open `பிரேத விசாரணை`;
- scan **145** must close Story 19;
- scan **146** must be checked as the opening of Story 20 `கண்டதும் காதல் ஒழிக!`.

Actions:

1. fetch live `main` and confirm no matching canonical `பிரேத விசாரணை` workspace exists;
2. visually verify scans 140 / 145 / 146 from the controlling PDF;
3. create the Story 19 workspace only after canonical-story check;
4. create **6** page records for scans 140–145 / printed pages 131–136;
5. transcribe directly from scan and perform full-span visual review on every page;
6. exhaust difficult readings before `blocked` and maintain a human possible-error queue;
7. create assembled Tamil, audit, source metadata, page map and story README;
8. verify every physical page-boundary continuation and confirm no omitted/duplicated pages;
9. synchronize anthology/root control files;
10. **do not begin Story 20 (`கண்டதும் காதல் ஒழிக!`) in the same activity.**

Expected progress after successful Story 19 closure: **19 / 37 complete, 18 remaining**.

## New-chat readiness

**READY FOR CONTINUATION.**
