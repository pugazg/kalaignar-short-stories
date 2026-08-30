# HANDOVER — Kalaignar Short Stories Archive

## Repository

- Repository: `pugazg/kalaignar-short-stories`
- Branch: `main`
- Story workflow: `SHORT_STORY_PROCESSING_GUIDE.md`
- Anthology workflow: `COLLECTION_SOURCE_GUIDE.md`
- Cross-chat resume prompt: `NEXT_CHAT_PROMPT.md`
- Source PDFs are **not** committed to GitHub.

## Authoritative-state rule

Always fetch live GitHub `main` first. Live `main` is authoritative over chat summaries, prompts and remembered checkpoints.

Only files reachable from live `main` are durable project state. Local files, generated crops, unreferenced Git blobs/trees, and statements from an earlier chat are not authoritative until committed and reachable from `main`.

## Permanent source rules

- **Controlling scan first.** Do not silently modernize spelling, grammar, punctuation, names, sandhi or source anomalies.
- **No stones should be left unturned.** Difficult story readings must receive full-span visual escalation before terminal `blocked` status.
- **Processed-crop confidence is not source confidence.** Verify the complete phrase/clause/sentence against the source span.
- `POSSIBLE_ERRORS_FOR_REVIEW.md` is a human-review queue, not a list of confirmed errors.
- A later source-supported correction must be propagated through all affected story, collection and control files.
- Do not commit source PDFs, generated page renders or crops.

## Mandatory cross-chat startup

Before source-dependent writes:

1. fetch live `main` and record its HEAD;
2. read completely:
   - `SHORT_STORY_PROCESSING_GUIDE.md`
   - `COLLECTION_SOURCE_GUIDE.md`
   - `HANDOVER.md`
   - `NEXT_CHAT_PROMPT.md`
   - `collections/1977-kalaignar-karunanidhiyin-sirukathaigal/README.md`
   - `collections/1977-kalaignar-karunanidhiyin-sirukathaigal/indexes/story-inventory.md`
   - `collections/1977-kalaignar-karunanidhiyin-sirukathaigal/indexes/scan-map.md`;
3. inspect the latest committed story workspace relevant to the handover;
4. do not redo completed/verified source work without new correction evidence or repository inconsistency;
5. when the user says **“Proceed with next activity”**, execute the exact activity recorded below without routine clarification.

## Active collection source — 1977 anthology

- title: **கலைஞர் கருணாநிதியின் சிறுகதைகள்**
- filename: `TVA_BOK_0064142_கலைஞர்_கருணாநிதியின்_சிறுகதைகள்.pdf`
- SHA-256: `853032661482eaccb26c083a38d7aa75c081362d33c963c63e37d088bf20acb3`
- file size: **268,486,609 bytes**
- PDF scans: **260**
- edition: **முதல் பதிப்பு: 1977**
- printed story pagination: **1–250**
- story block scans: **10–259**
- relation: **scan = printed page + 9**
- registered stories: **37 / 37**
- story-start visual checks: **37 / 37**
- English translation started for anthology stories: **0 / 37**

## Durable story-source state

Stories **1–19** now have committed canonical Tamil workspaces. Stories 1–18 were already fully synchronized before the current Story 19 pass.

Story 19 source-work checkpoint commit:

`d12bb38dc45627b7d5ba9edcf1f780892907b025` — `Complete Story 19 Pretha Visaranai workspace`

### Story 19 — `பிரேத விசாரணை` — SOURCE WORK COMPLETE

Canonical workspace: `stories/pretha-visaranai/`

- printed pages: **131–136**
- anthology scans: **140–145**
- page records: **6 / 6**
- verified: **6 / 6**
- needs-review: **0**
- blocked: **0**
- unresolved story text: **0**
- Tamil assembly: complete
- source audit: **PASS**
- persistent human possible-error queue: present
- English translation: not started

Boundary / continuation checks:

- scan **140** opens `பிரேத விசாரணை`;
- printed 131→132 / scans 140→141: `...சாவிக் கொத்தை எடுத்து விரலில்` → `சுழற்றிக்கொண்டே நகர ஆரம்பித்தார் நாயுடுகாரு.`;
- printed 133→134 / scans 142→143: `...‘ஆம்படையா—’ அவதி தாங்க` → `மாட்டாமல் அனலிடைப் புழுப்போல்...`;
- 141→142, 143→144 and 144→145 were also directly checked with no omission or duplication;
- scan **145** contains Story 19's final paragraph and closing ornament;
- scan **146** opens Story 20 `கண்டதும் காதல் ஒழிக!`;
- no Story 20 text is included in Story 19.

High-value source-close readings are recorded in `stories/pretha-visaranai/POSSIBLE_ERRORS_FOR_REVIEW.md`, including `கண்ணப்புக் கண்ணத்தபடி`, `சம்மதந்தானே`, `தினை விதைச்சவங்க`, `வாசற்படியண்டை`, `அடியசைந்து`, `ஒப்பத்திரவம்`, source-printed caste-language quotations, `சம்மட்டியால் தாக்கப்பட்ட வைரத்தைப் போல`, `அனலிடைப் புழுப்போல்`, `மண்ணவது!`, `மூஷிக விநாயகர்`, `ஆலயப் பிரவேச சீசனில்`, `பகீரதப் பிரயத்தனங்கள்`, `கர்ப்பக் கிரகத்திற்கு`, `அப்பீல் பறைச்சியால்`, `தேசப் பிரஷ்டம்`, `கட்டுமஸ்தான தேகம்`, `குழந்தையை யாவது`, `அங்குமிங்கும்`, `எறங்க`, `அடுக்கவில்ல`, `மற்றுமிருவரின்`, and `கர்ப்பவதியப்பா`.

## IMPORTANT — partial closure / synchronization state

The **Story 19 workspace itself is committed and complete**, but the anthology/root progress-control files were deliberately not advanced in the Story 19 workspace commit. At this handover boundary, the following files may still say **18 / 37 complete** and may still name Story 19 as the next activity:

- root `README.md`;
- collection `README.md`;
- collection `indexes/story-inventory.md`;
- collection `indexes/scan-map.md`.

That is a known, explicit synchronization debt — **do not interpret it as Story 19 needing retranscription**.

Until those four downstream controls are synchronized, distinguish the states as follows:

- **committed story workspaces complete:** 19 / 37;
- **collection/root closure counters:** may still show 18 / 37;
- **remaining unprocessed stories after Story 19:** 18.

## NEXT EXACT ACTIVITY — STORY 19 CLOSURE SYNCHRONIZATION ONLY

Do **not** re-transcribe Story 19 and do **not** start Story 20 during this closure activity.

1. Fetch live `main`. If it has moved beyond this handover, preserve newer work.
2. Confirm `stories/pretha-visaranai/` is reachable from live `main` and remains 6/6 verified, 0 blocked, 0 unresolved.
3. Synchronize the four stale downstream controls:
   - root `README.md`;
   - collection `README.md`;
   - collection `indexes/story-inventory.md`;
   - collection `indexes/scan-map.md`.
4. Set anthology Tamil source progress to **19 / 37 complete, 18 remaining**.
5. Mark Story 19 `பிரேத விசாரணை` as complete — printed **131–136**, scans **140–145**, 6/6 verified, audit PASS.
6. Advance the collection's next exact story to Story 20 **`கண்டதும் காதல் ஒழிக!`** — printed **137–141**, scans **146–150**.
7. Update `HANDOVER.md` and `NEXT_CHAT_PROMPT.md` again after synchronization so they point cleanly to Story 20.
8. Re-fetch live `main` and the synchronized files before announcing closure.
9. **Do not begin Story 20 source transcription in this same closure-synchronization activity.**

Expected state after this exact activity: **19 / 37 fully synchronized complete, 18 remaining**.

## Following source activity — only after closure synchronization

Story 20 — **`கண்டதும் காதல் ஒழிக!`**:

- printed pages: **137–141**
- anthology scans: **146–150**
- scan **146** is already visually confirmed as its opening while closing Story 19;
- before Story 20 closure, inspect scan **151** to confirm the opening of Story 21 `ஆலமரத்துப் புறாக்கள்`;
- attach/resolve the controlling PDF before any Story 20 transcription or verification.

## New-chat readiness

**READY FOR CONTINUATION.** The next chat must first finish Story 19 closure synchronization; Story 19 source work itself must not be redone.