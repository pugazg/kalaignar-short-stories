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
- Old Tamil glyph shapes must be interpreted from the source typeface rather than modern glyph expectations.
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
- Tamil source processing complete: **31 / 37**
- remaining unprocessed anthology stories: **6 / 37**
- English translation started for anthology stories: **0 / 37**

## Durable story-source state

Stories **1–31** have committed canonical Tamil workspaces and are synchronized into the anthology/root progress controls.

Story 31 canonical-workspace checkpoint:

`043e9c6e37bd0a3555ce74357393a7857a5b4b97` — `Complete Story 31 canonical workspace`

### Story 31 — `அய்யோ ராஜா!` — FULLY CLOSED

Canonical workspace: `stories/ayyo-raja/`

- printed pages: **202–208**
- anthology scans: **211–217**
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

- scan **211** visibly opens `அய்யோ ராஜா!`;
- scans **211→212**: scan 211 closes the gate-vendor setup and scan 212 continues the waiting-at-the-gate scene, with no omission or duplication;
- printed **203→204** / scans **212→213**: `...கண்ணாடி வளையல்கள் கல கல வென` → `ஒலிக்க, அவள் ஈ ஓட்டிக்கொண்டு...`;
- scans **213→214**: scan 213 closes `அவள் மேற்கொண்டிருக்கிற தொழில் அப்படிப்பட்டது!` and scan 214 begins `பகலிலே முறுக்கு மசால்வடை...`;
- printed **205→206** / scans **214→215**: `...நெற்றியிலே குங்குமம்—தலையிலே பூ—கையிலே` → `கண்ணாடி வளையல்கள்—கருப்பு ரவிக்கை—வெள்ளைப் புடவை.`;
- printed **206→207** / scans **215→216**: `...முடியாது என்பதை உணர்ந்` → `தாள். இரவு முழுதும் குழந்தையோடு...`;
- scans **216→217**: scan 216 closes `...போக்கு வரத்தே தடைப்பட்டுப் போயிருந்தது.` and scan 217 continues with the rickshaw driver's question;
- scan **217** contains the final paragraph and closing ornament;
- scan **218** visibly opens Story 32 `விஷம் இனிது`;
- no Story 32 text is included in Story 31.

### Old-glyph correction — durable

On scan **217**, an earlier provisional reading `என்றுள்` was reopened after user correction. Native-source reinspection confirms **`என்றாள் முத்தம்மா`**. The older Tamil `றா` glyph caused the misread. The corrected reading is propagated through the page record, Tamil assembly, metadata, review queue, audit and Story 31 README.

High-value source-close forms retained in `stories/ayyo-raja/POSSIBLE_ERRORS_FOR_REVIEW.md` include `சபிக்காதவர்கள்`, `மட்டுந்தான்`, `இவர்களைத் தவிர`, `சோகரசக்`, `பாத்திரந்தான்`, `கருத்தைப் பறிகொடுக்காதார்`, `ஒன்றுமாயிற்று`, `தரித்திரம் தாங்கமுடியாமல்`, `பல்காரக் கூடையிலே`, `‘நீச நிகழ்ச்சி’க்கும்`, `காமப்பதுமைகள்`, `முத்தமாரி`, `இரவு என்னென்ன மருத்துவங்களோ செய்துபார்த்தாள்`, spoken `கையிலே காசில்ல?`, `போக்கு வரத்தே`, `ஜனங்களையெல்லாம்`, `வரட்டுச் சிரிப்புகளை`, and `‘கூலி’யை`. These remain source-faithful review-queue entries, not confirmed errors.

The root README, collection README, story inventory and scan map are synchronized to Story 31 completion: **31 / 37 complete, 6 remaining**.

## NEXT EXACT ACTIVITY — STORY 32 SOURCE WORK ONLY

Story 32 — **`விஷம் இனிது`**:

- printed pages: **209–215**
- anthology scans: **218–224**
- scan **218** is already visually confirmed as its opening while closing Story 31;
- before Story 32 closure, inspect scan **225** and confirm it begins Story 33 **`வேணியின் காதலன்`**;
- do not include scan-225 Story 33 text in Story 32.

When the user says **“Proceed with next activity”**:

1. fetch live `main` and preserve any newer completed work;
2. confirm no existing matching canonical Story 32 workspace needs deduplication/attachment handling;
3. use the controlling PDF for Story 32 scans **218–224** only;
4. create/process the canonical Story 32 workspace under the permanent guides;
5. complete direct visual/full-span verification, with explicit attention to old Tamil glyph forms, and physical boundary checks;
6. confirm scan **225** is the Story 33 opening boundary witness `வேணியின் காதலன்`;
7. synchronize Story 32 into all downstream anthology/root controls;
8. update `HANDOVER.md` and `NEXT_CHAT_PROMPT.md` to Story 33 only after Story 32 is fully closed;
9. do **not** start Story 33 in the same activity.

## Current closure state

**FULLY SYNCHRONIZED THROUGH STORY 31.**

- Tamil source passes complete: **31 / 37**
- remaining: **6**
- next exact story: **32 — `விஷம் இனிது`**

## New-chat readiness

**READY FOR CONTINUATION.** The next chat may begin Story 32 source work after mandatory startup and controlling-source resolution.