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
- Tamil source processing complete: **28 / 37**
- remaining unprocessed anthology stories: **9 / 37**
- English translation started for anthology stories: **0 / 37**

## Durable story-source state

Stories **1–28** have committed canonical Tamil workspaces and are fully synchronized into the anthology/root progress controls.

Story 28 workspace checkpoint:

`6651f06f8d497b5e055247c2d67ee5e272ee4eb3` — `Complete Story 28 canonical workspace`

### Story 28 — TOC `புரட்சிப்படம்`, opening `புரட்சிப் படம்` — FULLY CLOSED

Canonical workspace: `stories/puratchip-padam/`

- printed TOC title: **`புரட்சிப்படம்`**
- story-opening heading: **`புரட்சிப் படம்`**
- printed pages: **185–189**
- anthology scans: **194–198**
- page records: **5 / 5**
- verified: **5 / 5**
- needs-review status pages: **0**
- blocked: **0**
- unresolved story text: **0**
- Tamil assembly: complete
- source audit: **PASS**
- persistent human possible-error queue: present
- English translation: not started

Boundary / continuation checks completed during source work:

- scan **194** visibly opens with heading `புரட்சிப் படம்`;
- printed **185→186** / scans **194→195**: `...மக்களத்` → `திருத்தும் வகையில்...`;
- printed **186→187** / scans **195→196**: `...பாடல்கள் தேன்பாகு` → `கற்கண்டு!`;
- printed **187→188** / scans **196→197**: `...என்ற சேதி` → `நாடெங்கும் பரவிற்று;`;
- printed **188→189** / scans **197→198**: question about the censor's two cuts → answer beginning `ஆமாம் தோழர்களே!`;
- scan **198** contains the final censor punchline and closing ornament;
- scan **199** visibly opens Story 29 `திடுக்கிடும் கதை`;
- no Story 29 text is included in Story 28.

The source-title variance is a controlling-source fact and must not be normalized: printed TOC **`புரட்சிப்படம்`** ↔ opening heading **`புரட்சிப் படம்`**. The canonical workspace/display follows the opening heading while both forms remain recorded.

High-value source-close forms retained in `stories/puratchip-padam/POSSIBLE_ERRORS_FOR_REVIEW.md` include `படப் பிடிப்பு`, `அறிவுக்கதை யொன்றை`, `படப்பிடிப்புவேலை`, `விளக்குவதாகயிருந்தது`, `ஆஷாடபூதித்தனங்கள்`, `படந்தான்`, `தாராசசாங்கத்தைப்`, `பாரபக்ஷம்`, `எதாவது`, `ஏமாற்றுதே`, `பரவிற்று`, `திலகநகரத்திலே`, `வெளுப்பாயிருந்தது`, `முற்றிற்று`, repeated `வெட்டினர்கள்`, and `வீசிற்று`. These remain source-faithful review-queue entries, not confirmed errors.

The root README, collection README, collection story inventory and collection scan map are synchronized to Story 28 completion: **28 / 37 complete, 9 remaining**.

## NEXT EXACT ACTIVITY — STORY 29 SOURCE WORK ONLY

Story 29 — **`திடுக்கிடும் கதை`**:

- printed pages: **190–195**
- anthology scans: **199–204**
- scan **199** is already visually confirmed as its opening while closing Story 28;
- before Story 29 closure, inspect scan **205** and confirm it begins Story 30 **`கடைசிக் கட்டம்`**;
- do not include scan-205 Story 30 text in Story 29.

When the user says **“Proceed with next activity”**:

1. fetch live `main` and preserve any newer completed work;
2. confirm no existing matching canonical Story 29 workspace needs deduplication/attachment handling;
3. use the controlling PDF for Story 29 scans **199–204** only;
4. create/process the canonical Story 29 workspace under the permanent guides;
5. complete direct visual/full-span verification and physical boundary checks;
6. confirm scan **205** is the Story 30 opening boundary witness `கடைசிக் கட்டம்`;
7. synchronize Story 29 into all downstream anthology/root controls;
8. update `HANDOVER.md` and `NEXT_CHAT_PROMPT.md` to Story 30 only after Story 29 is fully closed;
9. do **not** start Story 30 in the same activity.

## Current closure state

**FULLY SYNCHRONIZED THROUGH STORY 28.**

- Tamil source passes complete: **28 / 37**
- remaining: **9**
- next exact story: **29 — `திடுக்கிடும் கதை`**

## New-chat readiness

**READY FOR CONTINUATION.** The next chat may begin Story 29 source work after mandatory startup and controlling-source resolution.
