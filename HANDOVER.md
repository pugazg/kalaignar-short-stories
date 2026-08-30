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
- Tamil source processing complete: **20 / 37**
- remaining unprocessed anthology stories: **17 / 37**
- English translation started for anthology stories: **0 / 37**

## Durable story-source state

Stories **1–20** have committed canonical Tamil workspaces and are fully synchronized into the anthology/root progress controls.

Story 20 workspace checkpoint:

`a94cdf55f9f13506ded6947a8b5cc01fba8e4057` — `Complete Story 20 canonical workspace`

### Story 20 — `கண்டதும் காதல் ஒழிக!` — FULLY CLOSED

Canonical workspace: `stories/kandathum-kadhal-ozhiga/`

- printed pages: **137–141**
- anthology scans: **146–150**
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

- scan **146** opens `கண்டதும் காதல் ஒழிக!`;
- scans 146→147: the audience-call sequence continues with no omission or duplication;
- scans 147→148: `...பெண்ணுரல்....?` → `நாடகக்காரி பெண்ணுரல் மட்டுமா?...`;
- printed 139→140 / scans 148→149: `...“அன்பே! சீதா! அருகில் வா!” என்று` → `முடிக்கவில்லை; கொட்டகை “சே! உள்ளே போடா!” என்று சிரித்தது.`;
- printed 140→141 / scans 149→150: `...“லங்கா தகனம்” நாடகம் ஆரம்பமாயிற்று. தீ` → `வளர்ந்து, தாவியது.`;
- scan **150** contains Story 20's final sentence and closing ornament;
- scan **151** opens Story 21 `ஆலமரத்துப் புறாக்கள்`;
- no Story 21 text is included in Story 20.

High-value source-close forms are retained in `stories/kandathum-kadhal-ozhiga/POSSIBLE_ERRORS_FOR_REVIEW.md`, including `எலிபெண்டு சிகரெட்`, `காலணு பீடி`, `பெண்ணுரல்`, `கன்னி யொருத்தியைக்`, `தருமனுய்`, `சகாதேவனுய்`, `ஒரு நடிகனைச் சேர்ந்து விடுவது!`, `திக்விஜயம்`, `ஓடினள்`, `ஓடினர்கள்`, `தீங்கனியாக`, `நன்றுக நிதானம்`, `கொள்ளிடத்து வெள்ளமாயிற்று` and `‘டோபா’ முடியை எடுத்தான்!`.

The root README, collection README, collection story inventory and collection scan map are synchronized to Story 20 completion: **20 / 37 complete, 17 remaining**.

## NEXT EXACT ACTIVITY — STORY 21 SOURCE WORK ONLY

Story 21 — **`ஆலமரத்துப் புறாக்கள்`**:

- printed pages: **142–146**
- anthology scans: **151–155**
- scan **151** is already visually confirmed as its opening while closing Story 20;
- before Story 21 closure, inspect scan **156** and confirm it begins Story 22 **`தொத்துக்கிளி`**;
- do not include scan-156 Story 22 text in Story 21.

When the user says **“Proceed with next activity”**:

1. fetch live `main` and preserve any newer completed work;
2. confirm no existing matching canonical Story 21 workspace needs deduplication/attachment handling;
3. use the controlling PDF for Story 21 scans **151–155** only;
4. create/process the canonical Story 21 workspace under the permanent guides;
5. complete direct visual/full-span verification and physical boundary checks;
6. synchronize Story 21 into all downstream anthology/root controls;
7. update `HANDOVER.md` and `NEXT_CHAT_PROMPT.md` to Story 22 only after Story 21 is fully closed;
8. do **not** start Story 22 in the same activity.

## Current closure state

**FULLY SYNCHRONIZED THROUGH STORY 20.**

- Tamil source passes complete: **20 / 37**
- remaining: **17**
- next exact story: **21 — `ஆலமரத்துப் புறாக்கள்`**

## New-chat readiness

**READY FOR CONTINUATION.** The next chat may begin Story 21 source work after mandatory startup and controlling-source resolution.
