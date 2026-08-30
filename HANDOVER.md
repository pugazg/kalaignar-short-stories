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
- Tamil source processing complete: **25 / 37**
- remaining unprocessed anthology stories: **12 / 37**
- English translation started for anthology stories: **0 / 37**

## Durable story-source state

Stories **1–25** have committed canonical Tamil workspaces and are fully synchronized into the anthology/root progress controls.

Story 25 workspace checkpoint:

`2c0a2d528a6c3bcb70b440d4e27288b2ab0b4bfd` — `Complete Story 25 canonical workspace`

### Story 25 — `வாழ முடியாதவர்கள்` — FULLY CLOSED

Canonical workspace: `stories/vazha-mudiyathavargal/`

- printed pages: **164–171**
- anthology scans: **173–180**
- page records: **8 / 8**
- verified: **8 / 8**
- needs-review status pages: **0**
- blocked: **0**
- unresolved story text: **0**
- Tamil assembly: complete
- source audit: **PASS**
- persistent human possible-error queue: present
- English translation: not started

Boundary / continuation checks completed during source work:

- scan **173** opens `வாழ முடியாதவர்கள்`;
- scans 173→174 and 174→175 were directly checked with no omitted or duplicated text;
- scans 175→176: `...உட்கார்ந்திருந்த அவனிடம்,` → `வான வெளியில்...`;
- printed 167→168 / scans 176→177: `...பருவ` → `மடைந்து...`;
- printed 168→169 / scans 177→178: `...பவளக் கட்டி` → `யும்,...`;
- printed 169→170 / scans 178→179: `...எடுத்துக்` → `காட்டிற்று.`;
- scans 179→180 were directly checked with no omission or duplication;
- scan **180** contains Story 25's final paragraph and closing ornament;
- scan **181** opens Story 26 `அபாக்ய சிந்தாமணி`;
- no Story 26 text is included in Story 25.

High-value source-close forms are retained in `stories/vazha-mudiyathavargal/POSSIBLE_ERRORS_FOR_REVIEW.md`, including `கம்ப ரசம்`, `கேட்கிறயா`, `பரவாயில்ல`, `பிடித்தமில்லே`, `கவாட்டா`, `‘காலேஜ் வேடர்’ களும்`, `சிறகை படித்துக் கொண்டன`, `சின்னசாமி`, `ஜீலு ஜீலுப்பைப்`, `கல்யாண எழவா`, `கேட்கவேண்டிய தில்ல`, `‘கிம்பள சான்ஸ்’`, `பெண்ணுல்தான்`, `அகட்டிப்`, `விஷமேறி`, `அழுக்கியது`, `கற்பினைக் பெயரால்`, `தீவிதி` and `தீவிதிக்காளான`. Source-sensitive readings remain in the later human-recheck queue without changing verified page status.

The root README, collection README, collection story inventory and collection scan map are synchronized to Story 25 completion: **25 / 37 complete, 12 remaining**.

## NEXT EXACT ACTIVITY — STORY 26 SOURCE WORK ONLY

Story 26 — **`அபாக்ய சிந்தாமணி`**:

- printed pages: **172–179**
- anthology scans: **181–188**
- scan **181** is already visually confirmed as its opening while closing Story 25;
- before Story 26 closure, inspect scan **189** and confirm it begins Story 27 **`பாலைவன ரோஜா`**;
- do not include scan-189 Story 27 text in Story 26.

When the user says **“Proceed with next activity”**:

1. fetch live `main` and preserve any newer completed work;
2. confirm no existing matching canonical Story 26 workspace needs deduplication/attachment handling;
3. use the controlling PDF for Story 26 scans **181–188** only;
4. create/process the canonical Story 26 workspace under the permanent guides;
5. complete direct visual/full-span verification and physical boundary checks;
6. confirm scan **189** is the Story 27 opening boundary witness;
7. synchronize Story 26 into all downstream anthology/root controls;
8. update `HANDOVER.md` and `NEXT_CHAT_PROMPT.md` to Story 27 only after Story 26 is fully closed;
9. do **not** start Story 27 in the same activity.

## Current closure state

**FULLY SYNCHRONIZED THROUGH STORY 25.**

- Tamil source passes complete: **25 / 37**
- remaining: **12**
- next exact story: **26 — `அபாக்ய சிந்தாமணி`**

## New-chat readiness

**READY FOR CONTINUATION.** The next chat may begin Story 26 source work after mandatory startup and controlling-source resolution.