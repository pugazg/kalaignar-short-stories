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
- Tamil source processing complete: **27 / 37**
- remaining unprocessed anthology stories: **10 / 37**
- English translation started for anthology stories: **0 / 37**

## Durable story-source state

Stories **1–27** have committed canonical Tamil workspaces and are fully synchronized into the anthology/root progress controls.

Story 27 workspace checkpoint:

`03a6c287886ce6dca1ccd3d925459a62cbdb0e4c` — `Complete Story 27 canonical workspace`

### Story 27 — `பாலைவன ரோஜா` — FULLY CLOSED

Canonical workspace: `stories/palaivana-roja/`

- printed pages: **180–184**
- anthology scans: **189–193**
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

- scan **189** opens `பாலைவன ரோஜா`;
- scans **189→190** were directly checked: scan 189 closes `...திகழ்ந்தான் கந்தையா.` and scan 190 begins a new quotation, with no omitted or duplicated text;
- scans **190→191** were directly checked: scan 190 closes `...அவர்கள் எதிர்காலம்.` and scan 191 opens `பாவம்!`, with no omission or duplication;
- printed **182→183** / scans **191→192**: `...அவர்கள்` → `எல்லாருமே இப்போது குமாஸ்தாக்கள்”`;
- printed **183→184** / scans **192→193**: `...குன்றென உலவு` → `கிறான்.`;
- scan **193** contains Story 27's final paragraph and closing ornament;
- scan **194** opens Story 28 with heading `புரட்சிப் படம்`;
- Story 28's printed TOC title is `புரட்சிப்படம்`; that source-title variance is preserved;
- no Story 28 text is included in Story 27.

High-value source-close forms retained in `stories/palaivana-roja/POSSIBLE_ERRORS_FOR_REVIEW.md` include `ஜாக்கையை`, `படை யெடுக்கும்`, `மேடனிக் காட்சி`, `வசிஷ்ட மண்டலமென`, `பெர்ணட்ஷாவைப்`, `இங்கர்சாலைக்`, `துதிபாடி`, `‘பெஞ்சி’லே`, `‘ஈன்ஸ்டினின் தியரி’`, `மாறுத புகழ்`, `மாசமருவின்றித்`, `மாயமாலக்காரி`, `கந்தையாக்கள்`, `அறிஞனைத் திகழ்வான்`, `கூட்டாளிகெல்லாம்`, `அத்திம்பேர்`, `செக்ரெட்டரியெட்டில்`, `கவிதா சிரோன்மணி`, `இஞ்சினீயர்`, `வெள்ளெருக்கை`, `மாசுபடிந்த`, and `கண்—நீர்தான்`. Source-sensitive readings remain in the later human-recheck queue without changing verified page status.

The root README, collection README, collection story inventory and collection scan map are synchronized to Story 27 completion: **27 / 37 complete, 10 remaining**.

## NEXT EXACT ACTIVITY — STORY 28 SOURCE WORK ONLY

Story 28 has a source-title variance:

- printed TOC title: **`புரட்சிப்படம்`**;
- story-opening heading: **`புரட்சிப் படம்`**;
- printed pages: **185–189**;
- anthology scans: **194–198**;
- scan **194** is already visually confirmed as its opening while closing Story 27;
- before Story 28 closure, inspect scan **199** and confirm it begins Story 29 **`திடுக்கிடும் கதை`**;
- preserve both Story 28 title forms and do not silently normalize them;
- do not include scan-199 Story 29 text in Story 28.

When the user says **“Proceed with next activity”**:

1. fetch live `main` and preserve any newer completed work;
2. confirm no existing matching canonical Story 28 workspace under either `புரட்சிப்படம்` or `புரட்சிப் படம்` needs deduplication/additional-witness handling;
3. use the controlling PDF for Story 28 scans **194–198** only;
4. create/process the canonical Story 28 workspace under the permanent guides, explicitly documenting the TOC/opening-heading variance;
5. complete direct visual/full-span verification and physical boundary checks;
6. confirm scan **199** is the Story 29 opening boundary witness `திடுக்கிடும் கதை`;
7. synchronize Story 28 into all downstream anthology/root controls;
8. update `HANDOVER.md` and `NEXT_CHAT_PROMPT.md` to Story 29 only after Story 28 is fully closed;
9. do **not** start Story 29 in the same activity.

## Current closure state

**FULLY SYNCHRONIZED THROUGH STORY 27.**

- Tamil source passes complete: **27 / 37**
- remaining: **10**
- next exact story: **28 — TOC `புரட்சிப்படம்`, opening `புரட்சிப் படம்`**

## New-chat readiness

**READY FOR CONTINUATION.** The next chat may begin Story 28 source work after mandatory startup and controlling-source resolution.
