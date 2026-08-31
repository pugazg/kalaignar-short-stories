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
- Tamil source processing complete: **32 / 37**
- remaining unprocessed anthology stories: **5 / 37**
- English translation started for anthology stories: **0 / 37**

## Durable story-source state

Stories **1–32** have committed canonical Tamil workspaces and are synchronized into the anthology/root progress controls.

Story 32 canonical-workspace checkpoint:

`976e4e4fd5b4094416aa11899acdaa66371f0f8d` — `Audit Story 32 Tamil source`

### Story 32 — `விஷம் இனிது` — FULLY CLOSED

Canonical workspace: `stories/visham-inidhu/`

- printed pages: **209–215**
- anthology scans: **218–224**
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

- scan **218** visibly opens `விஷம் இனிது`;
- printed **209→210** / scans **218→219**: `...நான் சத்தியவதியை` → `தவறு கூறுகிறேன் என்று கருதாதே.`;
- printed **210→211** / scans **219→220**: `...ஆலயம் மிகச் சிறப்புடையதாயிருக்க` → `வேண்டும்; அதற்கு ஏராளமான பொன் வேண்டும்...`;
- printed **211→212** / scans **220→221**: `...நாம் வைரங்களை ரகசியமாகச்` → `சேமித்து, வைகுந்த நாதனின் கோயிலைக் கட்டி முடித்து விடுவோம்!`;
- printed **212→213** / scans **221→222**: `...ராமகீர்த்தனை பாடிக்கொண்டிருக்` → `கிறாள் சத்தியவதி.`;
- scans **222→223**: scan 222 closes ஜெகவீரனின் `பாசாங்கு செய்யாதே!` accusation and scan 223 continues with சத்தியவதியின் `பிரபு! என் கற்பை இகழாதீர்கள்.`;
- scans **223→224**: scan 223 closes the poison-test demand and scan 224 begins அர்தோலின் `சாப்பிடுகிறேன்.` reply;
- scan **224** contains the final paragraph and closing ornament;
- scan **225** visibly opens Story 33 `வேணியின் காதலன்`;
- no Story 33 text is included in Story 32.

High-value source-close forms retained in `stories/visham-inidhu/POSSIBLE_ERRORS_FOR_REVIEW.md` include `தீக்குளித்த திலகங்களைப்`, `அப்படி யெல்லாம்`, `அன்பழைப்பு`, `புலி யொன்றினால்`, `வரிப்பளுவைத்`, `சாகசக்காரியா?`, `கண்டெடுக்கிறேன்`, `அர்த்த ராத்திரியிலும்`, `சுக மடைய`, `கோயில்கொள்ளப்போகிறான்`, `காஞ்சரங் கனியே`, `பேசுகிறாய்க்கும்?`, `பாஷாணம்`, `இல்லை யென்பதை`, `என் அண்ணை`, `தகாப் போக்குடையோன்`, `அவதூறிலிருந்துகாப்பாற்றுகிறாய்`, and final `ஆண்டவனை விட ஆலஹாலம் இனிது`. These remain source-faithful review-queue entries, not confirmed errors.

The root README, collection README, story inventory and scan map are synchronized to Story 32 completion: **32 / 37 complete, 5 remaining**.

## NEXT EXACT ACTIVITY — STORY 33 SOURCE WORK ONLY

Story 33 — **`வேணியின் காதலன்`**:

- printed pages: **216–221**
- anthology scans: **225–230**
- scan **225** is already visually confirmed as its opening while closing Story 32;
- before Story 33 closure, inspect scan **231** and confirm it begins Story 34 **`அமிர்தமதி`**;
- do not include scan-231 Story 34 text in Story 33.

When the user says **“Proceed with next activity”**:

1. fetch live `main` and preserve any newer completed work;
2. confirm no existing matching canonical Story 33 workspace needs deduplication/attachment handling;
3. use the controlling PDF for Story 33 scans **225–230** only;
4. create/process the canonical Story 33 workspace under the permanent guides;
5. complete direct visual/full-span verification, with explicit attention to old Tamil glyph forms, and physical boundary checks;
6. confirm scan **231** is the Story 34 opening boundary witness `அமிர்தமதி`;
7. synchronize Story 33 into all downstream anthology/root controls;
8. update `HANDOVER.md` and `NEXT_CHAT_PROMPT.md` to Story 34 only after Story 33 is fully closed;
9. do **not** start Story 34 in the same activity.

Expected result after Story 33 closure: **33 / 37 fully synchronized complete, 4 remaining**.

## Current closure state

**FULLY SYNCHRONIZED THROUGH STORY 32.**

- Tamil source passes complete: **32 / 37**
- remaining: **5**
- next exact story: **33 — `வேணியின் காதலன்`**

## New-chat readiness

**READY FOR CONTINUATION.** The next chat may begin Story 33 source work after mandatory startup and controlling-source resolution.
