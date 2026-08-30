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
- Tamil source processing complete: **22 / 37**
- remaining unprocessed anthology stories: **15 / 37**
- English translation started for anthology stories: **0 / 37**

## Durable story-source state

Stories **1–22** have committed canonical Tamil workspaces and are fully synchronized into the anthology/root progress controls.

Story 22 workspace checkpoint:

`f56bf3b16c1b08450dd6af7e42c12e2dee7b1089` — `Complete Story 22 canonical workspace`

### Story 22 — `தொத்துக்கிளி` — FULLY CLOSED

Canonical workspace: `stories/thothukkili/`

- printed pages: **147–151**
- anthology scans: **156–160**
- page records: **5 / 5**
- verified: **5 / 5**
- needs-review: **0**
- blocked: **0**
- unresolved story text: **0**
- Tamil assembly: complete
- source audit: **PASS**
- persistent human possible-error queue: present
- English translation: not started

Boundary / continuation checks completed during source work:

- scan **156** opens `தொத்துக்கிளி`;
- printed 147→148 / scans 156→157: `...பற்றிக் கவலைகொள்ள` → `வில்லை. ஆனால்...`;
- scans 157→158 were directly checked with no omission or duplication;
- printed 149→150 / scans 158→159: `...அவள் முன்னே கண்ணகி` → `யும், மாதவியும் வந்து வந்து போயினர்.`;
- scans 159→160 were directly checked with no omission or duplication;
- scan **160** contains Story 22's final paragraph and closing ornament;
- scan **161** opens Story 23 `காதல் கடிதம்`;
- no Story 23 text is included in Story 22.

High-value source-close forms are retained in `stories/thothukkili/POSSIBLE_ERRORS_FOR_REVIEW.md`, including `அண்ணுமலை`, `குஷ்டரோகம்பிடித்த`, `‘ஜூலியட்’டுக்குத்தான்`, `சேல் கெண்டைக்கு`, `‘களுக்’`, `திரும்பினன்`, `அக்கத்தாகக் குத்திக் கொன்றுவிட்டாள்`, `ஒவ்வொரு திங்களும்`, `“டிசை”னில்`, `‘டால்’ அடிக்கும்`, `“மேக்-அப்” பையும்`, `படுமடுவிலே`, `காம்பொடிக்கப் பட்ட`, `யொழிய`, `சிக்கினள்`, `வேட்டை யாடுகிறான்`, `அவள் புலியானாள்!`, `விமலா முக்கி முனகிக் கொண்டே`, `கொட்டினள்`, `கருகு தாளிக்கப் பட்டது`, `“நைட்ரிக் ஆசிடைக்”`, `அக்கினித் திராவகத்தை!` and `குரூபியாக்கப்பட்டுக்`.

The root README, collection README, collection story inventory and collection scan map are synchronized to Story 22 completion: **22 / 37 complete, 15 remaining**.

## NEXT EXACT ACTIVITY — STORY 23 SOURCE WORK ONLY

Story 23 — **`காதல் கடிதம்`**:

- printed pages: **152–156**
- anthology scans: **161–165**
- scan **161** is already visually confirmed as its opening while closing Story 22;
- before Story 23 closure, inspect scan **166** and confirm it begins Story 24 **`கண்ணடக்கம்`**;
- do not include scan-166 Story 24 text in Story 23.

When the user says **“Proceed with next activity”**:

1. fetch live `main` and preserve any newer completed work;
2. confirm no existing matching canonical Story 23 workspace needs deduplication/attachment handling;
3. use the controlling PDF for Story 23 scans **161–165** only;
4. create/process the canonical Story 23 workspace under the permanent guides;
5. complete direct visual/full-span verification and physical boundary checks;
6. synchronize Story 23 into all downstream anthology/root controls;
7. update `HANDOVER.md` and `NEXT_CHAT_PROMPT.md` to Story 24 only after Story 23 is fully closed;
8. do **not** start Story 24 in the same activity.

## Current closure state

**FULLY SYNCHRONIZED THROUGH STORY 22.**

- Tamil source passes complete: **22 / 37**
- remaining: **15**
- next exact story: **23 — `காதல் கடிதம்`**

## New-chat readiness

**READY FOR CONTINUATION.** The next chat may begin Story 23 source work after mandatory startup and controlling-source resolution.
