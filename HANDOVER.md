# HANDOVER — Kalaignar Short Stories Archive

## Repository

- Repository: `pugazg/kalaignar-short-stories`
- Branch: `main`
- Story workflow: `SHORT_STORY_PROCESSING_GUIDE.md`
- Anthology workflow: `COLLECTION_SOURCE_GUIDE.md`
- Visual-fidelity workflow: `VISUAL_FIDELITY_CHECK_GUIDE.md`
- Visual-fidelity tracker: `VISUAL_FIDELITY_PROGRESS.md`
- Cross-chat resume prompt: `NEXT_CHAT_PROMPT.md`
- Source PDFs / generated renders / crops are **not** committed to GitHub.

## Authoritative-state rule

Always fetch live GitHub `main` first. Live `main` is authoritative over chat summaries, prompts and remembered checkpoints. Preserve any newer durable state.

## Permanent source rules

- **Controlling scan first.** Do not silently modernize spelling, grammar, punctuation, names, sandhi or source anomalies.
- Old Tamil glyph shapes must be interpreted from the source typeface and full span, not modern-font expectation.
- Difficult readings require full-span visual escalation before terminal `blocked` status.
- `POSSIBLE_ERRORS_FOR_REVIEW.md` is a human-review queue, not a list of confirmed errors.
- Running headers, printed page numbers and printer signatures are page furniture, not story body.
- A source-supported textual correction must be propagated through all affected page, assembly, audit and control layers.
- Do not commit the source PDF or generated page renders/crops.

## Mandatory startup before visual-fidelity source work

1. fetch live `main` and preserve newer work;
2. read completely:
   - `SHORT_STORY_PROCESSING_GUIDE.md`
   - `COLLECTION_SOURCE_GUIDE.md`
   - `VISUAL_FIDELITY_CHECK_GUIDE.md`
   - `VISUAL_FIDELITY_PROGRESS.md`
   - `HANDOVER.md`
   - `NEXT_CHAT_PROMPT.md`
   - collection `README.md`
   - collection `indexes/story-inventory.md`
   - collection `indexes/scan-map.md`;
3. inspect the active story's page records, Tamil assembly, audit and page map;
4. use the controlling PDF for all source-dependent decisions.

## Active collection source — 1977 anthology

- title: **கலைஞர் கருணாநிதியின் சிறுகதைகள்**
- filename: `TVA_BOK_0064142_கலைஞர்_கருணாநிதியின்_சிறுகதைகள்.pdf`
- SHA-256: `853032661482eaccb26c083a38d7aa75c081362d33c963c63e37d088bf20acb3`
- file size: **268,486,609 bytes**
- PDF scans: **260**
- edition: **முதல் பதிப்பு: 1977**
- printed story pagination: **1–250**
- story block scans: **10–259**
- scan **260**: verified back cover
- registered stories: **37 / 37**

## Completed Tamil source-text milestone

**1977 ANTHOLOGY TAMIL SOURCE PASS COMPLETE AND FULLY SYNCHRONIZED.**

- Tamil source processing: **37 / 37 complete**
- remaining source transcription: **0 / 37**
- story-text coverage: scans **10–259 / printed pages 1–250**
- all 37 story workspaces have complete Tamil assemblies and source audits
- all 37 have **0 blocked / 0 unresolved story text**
- English translation from this anthology: **0 / 37 started**

Edition-level title variances remain preserved:
- TOC `புரட்சிப்படம்` ↔ opening `புரட்சிப் படம்`
- TOC `சித்தார்த்தன்` ↔ opening `சித்தார்த்தன் சிலை`

## USER-AUTHORIZED CURRENT PHASE — VISUAL FIDELITY CHECK

The user explicitly authorized **visual fidelity check** after Tamil source transcription. This phase preserves source-significant structure without facsimile typography.

### Current visual-fidelity progress

- total stories: **37**
- complete: **9 / 37**
- pending: **28 / 37**
- needs recheck: **0**
- current target: **Story 10 — `தப்பிவிட்டார்கள்`**

Stories 1–9 are closed with `PASS — corrected` and story-local `visual-fidelity.md` records.

## Story 9 — `தாய்மை` — VISUAL FIDELITY CLOSED

Canonical workspace: `stories/thaaymai/`

- printed pages: **64–74**
- scans: **73–83**
- boundary witness: scan **84**, opening `தப்பிவிட்டார்கள்`
- pages directly inspected: **11 / 11**, plus boundary witness
- result: **PASS — corrected**
- story-local record: `stories/thaaymai/visual-fidelity.md`

Direct visual review checked opening/ending roles, paragraph/dialogue structure, display emphasis, page furniture and all ten internal joins.

Structural corrections/annotations:
1. scan 73 / assembly: recorded the long horizontal rule beneath `தாய்மை`;
2. scan 73 / assembly: recorded the enlarged opening `ச` in `சரசத்தாலும்`;
3. scan 74: printer signature `க—5` explicitly classified as excluded page furniture;
4. scan 82 / assembly: represented source-bold `“நிறுத்தாதே! ஊது!! ஊது!” என்று.`;
5. scan 83: `story-conclusion` → `story-ending`;
6. scan 83 / assembly: recorded the centered short ornamental closing rule with central geometric flourish;
7. page map synchronized with roles, emphasis, furniture, corrected paragraphs and joins;
8. scan 84 independently opens Story 10 `தப்பிவிட்டார்கள்` beneath its own heading and horizontal rule.

The visual review also exposed source-supported textual omissions/misreadings. Complete source spans were reopened before correction and synchronized through page records, Tamil assembly, audit, story README and review queue. Key corrections include:
- scan 74: `குணதிசையங்களைக்` → `குணதிசயங்களைக்`; `...சித்திக்கும் யோசனைகள் தரவும்` → `...சித்திக்கும் யோசனைகளைத் தரவும்`;
- scan 75: `இன்னென்று கொடு` → `இன்னொன்று கொடு`;
- scan 77: restored `படையெடுப்புக்கு ஏற்ற நேரமாகி விட்டது`, `முடிசூடியை`, `வெள்ளைக் கொடியைப்`, and omitted `மனக் கோட்டையைச் சுக்கு நூறாக்கி, நொறுங்கிப்போன`;
- scan 79: restored `கடைசியில் அந்தக் காம்பை எறிந்து விடுவார்கள்!` and the source paragraph break;
- scan 80: `சுமலியின்` → `சுழலியின்`; restored `—அழகே உருவெடுத்த அரசிளங்குமரன் ஆர்ப்பித்து விட்டான்`; `குழலிலே பிறந்து` → `குழலிலேயிருந்து`; `தன்னே` → `தன்னை`;
- scan 81: restored `அவன் என்ன கண்டான்—எதிரே உயிர் வாங்கும் பாம்பு...` and the following paragraph break;
- scan 82: restored the omitted warning passage including source-variant `இன்ப சாகரா!` and the complete source paragraph through `ஆகி விட்டான்!`;
- scan 83: `பார்த்துக்கொள்ளுங்கள்` → `பார்த்துக் கொள்ளுங்கள்`.

**Story wording changed during Story 9 visual-fidelity review: Yes — only where directly supported by the controlling scan.** Remaining unusual-but-legible readings stay in the persistent human recheck queue.

## NEXT EXACT ACTIVITY — STORY 10 VISUAL FIDELITY ONLY

Story 10 — **`தப்பிவிட்டார்கள்`**:

- canonical workspace: `stories/thappivittargal/`
- printed pages: **75–82**
- anthology scans: **84–91**
- boundary witness: scan **92**, opening Story 11 **`தப்பவில்லை`**

When the user says **“Proceed with next activity”**:

1. fetch live `main` first and preserve newer work;
2. inspect scans **84–91** directly from the controlling PDF;
3. compare all eight pages against `stories/thappivittargal/pages/` and its Tamil assembly under `VISUAL_FIDELITY_CHECK_GUIDE.md`;
4. inspect scan **92** only as the next-story boundary witness;
5. check opening/ending roles, paragraph/dialogue structure, verse/display/emphasis, non-text marks, page furniture and every physical join;
6. apply only source-supported structural corrections; if wording itself is wrong, verify the complete source span before correction and propagate all affected layers;
7. create `stories/thappivittargal/visual-fidelity.md`;
8. update `VISUAL_FIDELITY_PROGRESS.md`, `HANDOVER.md` and `NEXT_CHAT_PROMPT.md`;
9. re-fetch live `main` and changed controls before declaring Story 10 visually complete;
10. **do not begin Story 11 in the same activity**.

Expected result after Story 10 closure: **10 / 37 visual-fidelity complete, 27 pending**.

## Downstream phase guard

Do **not** begin English translation, modernization, republication or another downstream phase unless separately authorized after visual-fidelity work or mandated by newer live repository state.

## Current closure state

- Tamil source pass: **37 / 37 COMPLETE**
- visual fidelity: **9 / 37 COMPLETE**
- next exact activity: **Story 10 `தப்பிவிட்டார்கள்` visual fidelity**
