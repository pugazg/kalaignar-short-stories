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
- Tamil source processing complete: **34 / 37**
- remaining unprocessed anthology stories: **3 / 37**
- English translation started for anthology stories: **0 / 37**

## Durable story-source state

Stories **1–34** have committed canonical Tamil workspaces and are synchronized into the anthology/root progress controls.

Story 34 canonical-workspace checkpoint:

`debf8b7c9a83b555163af931742f0976dd4882dd` — `Complete Story 34 canonical workspace`

### Story 34 — `அமிர்தமதி` — FULLY CLOSED

Canonical workspace: `stories/amirthamathi/`

- printed pages: **222–229**
- anthology scans: **231–238**
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

- scan **231** visibly opens `அமிர்தமதி`;
- scans **231→232**: narrator's account of a `கோர நிகழ்ச்சி` continues into சுந்தரின் questioning without omission or duplication;
- scans **232→233**: `அதுதான் சகோதரா! குதர்களால் களவாடப்பட்டு விட்டது!` → `“தலைப்புதானே!”`;
- scans **233→234**: சுந்தரின் `மெளனமாக இரு!` → narrator's `முடியாது சுந்தர்!`;
- scans **234→235**: exact physical continuation `...அவர்கள் ஓடி, ஆடிப்பாடி` → `அரசனை அழைத்து வருவர்.`;
- scans **235→236**: `தோழி வாயிலாகக் கவிஞர் கூறுகிறார் கேள்:—` → quoted verse beginning `‘நரம்புகள்விசித்த மெய்யன்...`;
- scans **236→237**: exact physical continuation `...அவனையே தீர்த்துக்கட்டி` → `விட்டாள், அந்தப் பாகனின் பாட்டிலே சுகம் கண்ட பாதகி.`;
- scans **237→238**: `இந்த அக்கிரமத்திற்கு அழிவே கிடையாதா?` → `“ஏன் கிடையாது!...”`;
- scan **238** contains the final dialogue and closing ornament;
- scan **239** visibly opens Story 35 `சுமந்தவள்`;
- no Story 35 text is included in Story 34.

High-value source-close forms retained in `stories/amirthamathi/POSSIBLE_ERRORS_FOR_REVIEW.md` include `தாங்க முடியவில்ல`, `பிள்ளையில்ல பென்கிறார்கள்`, `அதுவுமில்ல`, `பேசுகிறேன்பென்று`, `வராத்து வந்துவிடவில்ல`, `சொன்னுய்`, `குதர்களால்`, `எதாவது`, `படித்த தில்ல`, `படித்ததில்ல?`, `வித்தியாச மில்ல`, `ஆண்மேல் அம்பாரியா?`, `பூண் ரோமத்தால் மிதியடியா?`, `பலவாறுக`, `அண்ணத்து மகிழத்தான்`, `நாளொருமேனியாக`, `அட்டபங்கன்`, `விலா விலே`, `சொன்னுயே`, and `பென்று`. These remain source-faithful review-queue entries, not confirmed errors.

The root README, collection README, story inventory and scan map are synchronized to Story 34 completion: **34 / 37 complete, 3 remaining**.

## NEXT EXACT ACTIVITY — STORY 35 SOURCE WORK ONLY

Story 35 — **`சுமந்தவள்`**:

- printed pages: **230–240**
- anthology scans: **239–249**
- scan **239** is already visually confirmed as its opening while closing Story 34;
- before Story 35 closure, inspect scan **250** and confirm it begins Story 36 with story-opening heading **`சித்தார்த்தன் சிலை`** (TOC title **`சித்தார்த்தன்`**);
- do not include scan-250 Story 36 text in Story 35.

When the user says **“Proceed with next activity”**:

1. fetch live `main` and preserve any newer completed work;
2. confirm no existing matching canonical Story 35 workspace needs deduplication/attachment handling;
3. use the controlling PDF for Story 35 scans **239–249** only;
4. create/process the canonical Story 35 workspace under the permanent guides;
5. complete direct visual/full-span verification, with explicit attention to old Tamil glyph forms, and physical boundary checks;
6. confirm scan **250** is the Story 36 opening boundary witness `சித்தார்த்தன் சிலை` while preserving TOC title `சித்தார்த்தன்`;
7. synchronize Story 35 into all downstream anthology/root controls;
8. update `HANDOVER.md` and `NEXT_CHAT_PROMPT.md` to Story 36 only after Story 35 is fully closed;
9. do **not** start Story 36 in the same activity.

Expected result after Story 35 closure: **35 / 37 fully synchronized complete, 2 remaining**.

## Current closure state

**FULLY SYNCHRONIZED THROUGH STORY 34.**

- Tamil source passes complete: **34 / 37**
- remaining: **3**
- next exact story: **35 — `சுமந்தவள்`**

## New-chat readiness

**READY FOR CONTINUATION.** The next chat may begin Story 35 source work after mandatory startup and controlling-source resolution.
