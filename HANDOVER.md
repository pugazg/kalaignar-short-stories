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
- Tamil source processing complete: **35 / 37**
- remaining unprocessed anthology stories: **2 / 37**
- English translation started for anthology stories: **0 / 37**

## Durable story-source state

Stories **1–35** have committed canonical Tamil workspaces and are synchronized into the anthology/root progress controls.

Story 35 canonical-workspace checkpoint:

`417406d927dc7a276b0a5ac1db9218c7a140b657` — `Assemble Story 35 Tamil text`

### Story 35 — `சுமந்தவள்` — FULLY CLOSED

Canonical workspace: `stories/sumanthaval/`

- printed pages: **230–240**
- anthology scans: **239–249**
- page records: **11 / 11**
- verified: **11 / 11**
- needs-review status pages: **0**
- blocked: **0**
- unresolved story text: **0**
- Tamil assembly: complete
- source audit: **PASS**
- persistent human possible-error queue: present
- English translation: not started

Boundary / continuation checks completed during source work:

- scan **239** visibly opens `சுமந்தவள்`;
- scans **239→240** continue the narrator's reflection on his mother into the motherhood questions without omission or duplication;
- scans **240→241**: `“ம்! மேலே சொல்லு!”` → `“தாய்மை என்றால் என்ன?...”`;
- scans **241→242**: `...உன் அண்ணி துடியாய்த் துடிக்கிறாள்.` → `அண்ணியின் மனம் கோண நீ நடக்கமாட்டாய்...`;
- scans **242→243** move from the marriage arrangement into married life without omission or duplication;
- scans **243→244**: exact physical continuation `செளந்தரியோ அந்த வீட்டு` → `மகராணிபோல ஆர்ப்பாட்டங்கள் நடத்திவந்தாள்.`;
- scans **244→245**: exact physical continuation `...அந்தக் குழந்தை அளித்த வேதனையால்` → `ஏற்கனவே அவளது உடல் இளைத்துப் போய்விட்டது.`;
- scans **245→246** move from animal-mother observations to the competing inner voice;
- scans **246→247**: `இரண்டு குழந்தைகளுக்கும் அவளே தாயாக விளங்கினாள்.` → செளந்தரியின் பாராட்டு;
- scans **247→248**: exact physical continuation `இரண்டு தொட்டில்களையும் ஆட்டுவதும் “ஆராரோ” பாடுவதும்` → `பிணிக்கு மருந்து தருவதும்...`;
- scans **248→249** move from the armed confrontation setup into `யார் வெடிக்கிற தோட்டா...`;
- scan **249** contains the final paragraph and closing ornament;
- scan **250** visibly opens Story 36 with heading `சித்தார்த்தன் சிலை`;
- Story 36 TOC title is `சித்தார்த்தன்`; the source-title variance is preserved;
- no Story 36 text is included in Story 35.

High-value source-close forms retained in `stories/sumanthaval/POSSIBLE_ERRORS_FOR_REVIEW.md` include `சுறு சுறுப்பு`, `அடுக்களை`, `திரு திருவென்று`, `குஞ்சு குளுவான்கள்`, `படுகிழம்`, `களித்துப்போய்`, `அண்ணு`, `கெளரவம்`, `ஐதர் காலத்துத் தையல் மிஷின்தான்`, `குழறல்`, `கர்ப்பவதி`, `கர்ப்பமாயிருக்கிறாளே`, `கனிமரமென`, `முழுங்கால்`, `சன சுரத்தை`, `மூனையளவு`, `மண்ணுக்கி`, `உளறினன்`, `தயங்கினன்`, `‘பெட்காபி’`, `யெளவனத்தின்`, `அலறினள்`, `தொடங்கினள்`, and `எமை விட்டு எச்சில் இலையே!`. These remain source-faithful review-queue entries, not confirmed errors.

The root README, collection README, story inventory and scan map are synchronized to Story 35 completion: **35 / 37 complete, 2 remaining**.

## NEXT EXACT ACTIVITY — STORY 36 SOURCE WORK ONLY

Story 36:

- TOC title: **`சித்தார்த்தன்`**
- story-opening heading: **`சித்தார்த்தன் சிலை`**
- printed pages: **241–243**
- anthology scans: **250–252**
- scan **250** is already visually confirmed as its opening while closing Story 35;
- before Story 36 closure, inspect scan **253** and confirm it begins Story 37 **`நுனிக்கரும்பு`**;
- do not include scan-253 Story 37 text in Story 36.

When the user says **“Proceed with next activity”**:

1. fetch live `main` and preserve any newer completed work;
2. confirm no existing matching canonical Story 36 workspace needs deduplication/attachment handling;
3. use the controlling PDF for Story 36 scans **250–252** only;
4. create/process the canonical Story 36 workspace under the permanent guides;
5. preserve both source title forms: TOC `சித்தார்த்தன்` and opening heading `சித்தார்த்தன் சிலை`;
6. complete direct visual/full-span verification, with explicit attention to old Tamil glyph forms and all physical joins;
7. confirm scan **253** is the Story 37 opening boundary witness `நுனிக்கரும்பு`;
8. synchronize Story 36 into all downstream anthology/root controls;
9. update `HANDOVER.md` and `NEXT_CHAT_PROMPT.md` to Story 37 only after Story 36 is fully closed;
10. do **not** start Story 37 in the same activity.

Expected result after Story 36 closure: **36 / 37 fully synchronized complete, 1 remaining**.

## Current closure state

**FULLY SYNCHRONIZED THROUGH STORY 35.**

- Tamil source passes complete: **35 / 37**
- remaining: **2**
- next exact story: **36 — TOC `சித்தார்த்தன்`, opening `சித்தார்த்தன் சிலை`**

## New-chat readiness

**READY FOR CONTINUATION.** The next chat may begin Story 36 source work after mandatory startup and controlling-source resolution.
