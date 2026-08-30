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
- Tamil source processing complete: **24 / 37**
- remaining unprocessed anthology stories: **13 / 37**
- English translation started for anthology stories: **0 / 37**

## Durable story-source state

Stories **1–24** have committed canonical Tamil workspaces and are fully synchronized into the anthology/root progress controls.

Story 24 workspace checkpoint:

`5915ad815e22cc5b37c5f61603d595dd79637895` — `Complete Story 24 Kannadakkam workspace`

### Story 24 — `கண்ணடக்கம்` — FULLY CLOSED

Canonical workspace: `stories/kannadakkam/`

- printed pages: **157–163**
- anthology scans: **166–172**
- page records: **7 / 7**
- verified: **7 / 7**
- needs-review status pages: **0**
- blocked: **0**
- unresolved story text: **0**
- Tamil assembly: complete
- source audit: **PASS**
- persistent human possible-error queue: present
- English translation: not started

Boundary / continuation checks completed during source work:

- scan **166** opens `கண்ணடக்கம்`;
- scans 166→167 were directly checked: scan 166 ends with a complete sentence and scan 167 begins a new paragraph, with no omission or duplication;
- scans 167→168 were directly checked: the dialogue continues with no omission or duplication;
- scans 168→169 were directly checked: the dialogue continues with no omission or duplication;
- printed 160→161 / scans 169→170: `...என் பார்வை பட்ட` → `மாத்திரத்தில் பஞ்சாய்ப் பறக்கும்.`;
- scans 170→171 were directly checked: the devotee's question is answered on the next page with no omission or duplication;
- scans 171→172 were directly checked: the public-health paragraph is followed by the dream/revelation conclusion with no omission or duplication;
- scan **172** contains Story 24's final paragraph and closing ornament;
- scan **173** opens Story 25 `வாழ முடியாதவர்கள்`;
- no Story 25 text is included in Story 24.

High-value source-close forms are retained in `stories/kannadakkam/POSSIBLE_ERRORS_FOR_REVIEW.md`, including `பூசி யிருந்த`, `ரத்தமும் சீமும்`, `திவட்டிகளோடு`, `புதியபிணம்`, `துணி ஏண்`, `அலகுகள் போலச் சிலாகைகள் போல`, `குறை நடக்கிறே`, `மிச்ச மிருப்பவர்களிடம்`, `அபயங்`, `மானுடின்ற`, `ஜீவவிட்ட உடல்களோ`, `புண்யமில்லை`, `பிணக்கொலு`, `மமதையாளன்`, `பொல பொலவென`, `நன்றியிருக்கிறதம்மா`, `நேத்திரங்களுக்கு`, `விட்டானப்பா`, `காணிக்கையப்பா`, `நம்முலகு`, `பேசினள்` and `அந்தவேதனையான`. The source-sensitive readings `துணி ஏண்`, `குறை நடக்கிறே`, `பிணக்கொலு`, and `நம்முலகு செல்லும்` remain in the later human-recheck queue without changing verified page status.

The root README, collection README, collection story inventory and collection scan map are synchronized to Story 24 completion: **24 / 37 complete, 13 remaining**.

## NEXT EXACT ACTIVITY — STORY 25 SOURCE WORK ONLY

Story 25 — **`வாழ முடியாதவர்கள்`**:

- printed pages: **164–171**
- anthology scans: **173–180**
- scan **173** is already visually confirmed as its opening while closing Story 24;
- before Story 25 closure, inspect scan **181** and confirm it begins Story 26 **`அபாக்ய சிந்தாமணி`**;
- do not include scan-181 Story 26 text in Story 25.

When the user says **“Proceed with next activity”**:

1. fetch live `main` and preserve any newer completed work;
2. confirm no existing matching canonical Story 25 workspace needs deduplication/attachment handling;
3. use the controlling PDF for Story 25 scans **173–180** only;
4. create/process the canonical Story 25 workspace under the permanent guides;
5. complete direct visual/full-span verification and physical boundary checks;
6. confirm scan **181** is the Story 26 opening boundary witness;
7. synchronize Story 25 into all downstream anthology/root controls;
8. update `HANDOVER.md` and `NEXT_CHAT_PROMPT.md` to Story 26 only after Story 25 is fully closed;
9. do **not** start Story 26 in the same activity.

## Current closure state

**FULLY SYNCHRONIZED THROUGH STORY 24.**

- Tamil source passes complete: **24 / 37**
- remaining: **13**
- next exact story: **25 — `வாழ முடியாதவர்கள்`**

## New-chat readiness

**READY FOR CONTINUATION.** The next chat may begin Story 25 source work after mandatory startup and controlling-source resolution.
