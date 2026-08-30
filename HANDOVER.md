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
3. Inspect the latest completed story workspace (`stories/originalil-ullapadi/`) as structural reference.
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
- Tamil source processing complete: **16 / 37**
- stories not yet transcribed: **21 / 37**
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
16. `ஒரிஜினலில் உள்ளபடி` — `stories/originalil-ullapadi/` — printed **110–116**, scans **119–125**, **7/7 verified**, 0 blocked, 0 unresolved, audit PASS.

All completed anthology stories have complete Tamil assemblies and persistent human possible-error queues.

## Story 16 — ஒரிஜினலில் உள்ளபடி — COMPLETE TAMIL SOURCE PASS

Canonical workspace: `stories/originalil-ullapadi/`

- page records: **7 / 7**
- verified: **7 / 7**
- blocked: **0**
- unresolved story text: **0**
- Tamil assembly: complete
- source audit: **PASS**
- English: not started

Boundary / continuation checks:

- scan 119 opens `ஒரிஜினலில் உள்ளபடி`.
- scans 120→121 / printed 111→112: `...“மகாகும்பாபிஷேகம்..........ம்......மட உலகம்......” அலட்சியம்` → `நிறைந்த வெறுப்பு அவன் முகத்தில் கோடுகளைக் கிழித்தது.`.
- scans 121→122 / printed 112→113: `...செட்டியாரின் தோளில்` → `போட்டுவிட்டான்.`.
- scans 122→123 / printed 113→114: `...செட்டியார் உத்தரவுப்` → `படி ‘பத்தாயிரம் நோட்டீசை’யும் ஊரெங்கும்...`.
- the 119→120, 123→124 and 124→125 boundaries were also visually checked and do not split story text.
- scan 125 contains the final explanation and closing ornament.
- scan 126 opens Story 17 `பனங்குலை`; Story 17 text is not included.

High-value source-close/full-span rechecks recorded in the story workspace include scan 119 `போட்டாமல்`; scan 120 old-form `திரெளபதி`, `எளனம்`, and `அலக் கழியும்`; scan 121 `வெங்கடாசலபதி கீர்த்தின் வைரங்களைப் பெயர்த்து` and `“என்று கம்பாசிட்டர், ஆச்சா?”`; scan 122 source `நாறு`; scan 123 final character-level confirmation of `படி ‘பத்தாயிரம் நோட்டீசை’யும்...`, `‘லக்னம்’`, and `உபன்யாசத்திற்காகச்`; scan 124 the deliberately distinct `விபசாரம்` / `விபச்சாரம்` forms and `உடன் யாசிப்பார்கள்`; and scan 125 `சித்தரிக்கப்பட்டிருக்கிறள்`, `காமக் காண்டா மிருகம்`, and `பொறும்`. Unusual readings remain in `stories/originalil-ullapadi/POSSIBLE_ERRORS_FOR_REVIEW.md` for later human checking without downgrading verified page status.

## Next exact activity

Process anthology Story **17 — `பனங்குலை`** only.

- printed pages: **117–121**
- anthology scans: **126–130**

Boundary checks:

- scan **126** must open `பனங்குலை`;
- scan **130** must close Story 17;
- scan **131** must be checked as the opening of Story 18 `செத்தவள் கதை`.

Actions:

1. fetch live `main` and confirm no matching canonical `பனங்குலை` workspace exists;
2. visually verify scans 126 / 130 / 131 from the controlling PDF;
3. create the Story 17 workspace only after canonical-story check;
4. create **5** page records for scans 126–130 / printed pages 117–121;
5. transcribe directly from scan and perform full-span visual review on every page;
6. exhaust difficult readings before `blocked` and maintain a human possible-error queue;
7. create assembled Tamil, audit, source metadata, page map and story README;
8. verify every physical page-boundary continuation and confirm no omitted/duplicated pages;
9. synchronize anthology/root control files;
10. **do not begin Story 18 (`செத்தவள் கதை`) in the same activity.**

Expected progress after successful Story 17 closure: **17 / 37 complete, 20 remaining**.

## New-chat readiness

**READY FOR CONTINUATION.**
