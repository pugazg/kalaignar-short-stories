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
- Tamil source processing complete: **19 / 37**
- remaining unprocessed anthology stories: **18 / 37**
- English translation started for anthology stories: **0 / 37**

## Durable story-source state

Stories **1–19** have committed canonical Tamil workspaces and are fully synchronized into the anthology/root progress controls.

Story 19 source-work checkpoint:

`d12bb38dc45627b7d5ba9edcf1f780892907b025` — `Complete Story 19 Pretha Visaranai workspace`

### Story 19 — `பிரேத விசாரணை` — FULLY CLOSED

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

Boundary / continuation checks already completed during source work:

- scan **140** opens `பிரேத விசாரணை`;
- printed 131→132 / scans 140→141: `...சாவிக் கொத்தை எடுத்து விரலில்` → `சுழற்றிக்கொண்டே நகர ஆரம்பித்தார் நாயுடுகாரு.`;
- printed 133→134 / scans 142→143: `...‘ஆம்படையா—’ அவதி தாங்க` → `மாட்டாமல் அனலிடைப் புழுப்போல்...`;
- 141→142, 143→144 and 144→145 were also directly checked with no omission or duplication;
- scan **145** contains Story 19's final paragraph and closing ornament;
- scan **146** opens Story 20 `கண்டதும் காதல் ஒழிக!`;
- no Story 20 text is included in Story 19.

The root README, collection README, collection story inventory and collection scan map are now synchronized to Story 19 completion: **19 / 37 complete, 18 remaining**.

## NEXT EXACT ACTIVITY — STORY 20 SOURCE WORK ONLY

Story 20 — **`கண்டதும் காதல் ஒழிக!`**:

- printed pages: **137–141**
- anthology scans: **146–150**
- scan **146** is already visually confirmed as its opening while closing Story 19;
- before Story 20 closure, inspect scan **151** and confirm it begins Story 21 **`ஆலமரத்துப் புறாக்கள்`**;
- do not include scan-151 Story 21 text in Story 20.

When the user says **“Proceed with next activity”**:

1. fetch live `main` and preserve any newer completed work;
2. confirm no existing matching canonical Story 20 workspace needs deduplication/attachment handling;
3. use the controlling PDF for Story 20 scans 146–150 only;
4. create/process the canonical Story 20 workspace under the permanent guides;
5. complete direct visual/full-span verification and physical boundary checks;
6. synchronize Story 20 into all downstream anthology/root controls;
7. update `HANDOVER.md` and `NEXT_CHAT_PROMPT.md` to Story 21 only after Story 20 is fully closed;
8. do **not** start Story 21 in the same activity.

## Current closure state

**FULLY SYNCHRONIZED THROUGH STORY 19.**

- Tamil source passes complete: **19 / 37**
- remaining: **18**
- next exact story: **20 — `கண்டதும் காதல் ஒழிக!`**

## New-chat readiness

**READY FOR CONTINUATION.** The next chat may begin Story 20 source work after mandatory startup and controlling-source resolution.
