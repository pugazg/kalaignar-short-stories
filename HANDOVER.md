# HANDOVER — Kalaignar Short Stories Archive

## Repository

- repository: `pugazg/kalaignar-short-stories`
- branch: `main`
- **LIVE MAIN IS AUTHORITATIVE**

## Closed durable layers

- 1977 Tamil dual-gate: **37/37 CURRENT PASS / CLOSED**
- 1977 English E1–E5 re-audit: **37/37 PASS / CLOSED**
- 1987 `கலைஞர் சொன்ன குட்டிக் கதைகள்`: **Tamil/source + English CLOSED**
- 1976 `நளாயினி` reconciliation: **CLOSED / PASS**
- 1982 `முடியாத தொடர்கதை`: **Tamil/source + English CLOSED**
- 2004, 2008, 2009 and the completed supplemental English layers remain closed under their collection trackers.

## Active source — 1950 `வாழமுடியாதவர்கள்`

Controlling attached source:

`TVA_BOK_0064034_வாழமுடியாதவர்கள்.pdf`

Collection workspace:

`collections/1950-vazha-mudiyathavargal/`

Source identity:

- bytes: **89,680,849**
- SHA-256: **`9fdc7a7049b74291047bb3212bb48851a8e6eb483d3f7e8ed3bc6f4ce016654e`**
- physical scans: **64**
- source type: **image-only; direct scan pixels control**
- title: **வாழமுடியாதவர்கள்**
- author: **மு. கருணாநிதி**
- publisher: **முன்னேற்றப் பண்ணை, சென்னை-1**
- visible date anchor: **மதிப்புரை signed சென்னை 1-1-50 by இரா. நெடுஞ்செழியன்**
- explicit edition statement: **not visible**
- source PDF committed: **No**

Front matter:

- scan 1 — cover
- scan 2 — title / author / publisher
- scan 3 — rights / price / printer
- scans 4–5 — `மதிப்புரை`
- no printed TOC
- scan 64 — advertisement/back matter

Story pagination:

- scans **6–63**
- printed pages **5–62**
- relation: **scan = printed page + 1**

Physical limitations:

- scans **14–15** — severe paper loss; substantial Story-1 text physically missing
- scan **37** — story-heading region damaged
- never reconstruct missing 1950 text from later editions

Inventory — **6/6 COMPLETE**:

1. `வாழ முடியாதவர்கள்` — scans **6–15 / printed 5–14** — existing canonical witness
2. `ஒரிஜினலில் உள்ளபடி!` — scans **16–24 / printed 15–23** — existing canonical witness
3. `கங்கையின் காதல்` — scans **25–29 / printed 24–28** — existing canonical witness
4. `கண்டதும் காதல் ஒழிக!` — scans **30–36 / printed 29–35** — existing canonical witness
5. damaged heading; work identity `ஏழை` — scans **37–41 / printed 36–40** — existing canonical witness
6. `பிள்ளையோ பிள்ளை!` — scans **42–63 / printed 41–62** — same underlying work as canonical `பெற்ற பிள்ளையை விற்ற தாய்`; preserve source-specific title

Current state:

- source registration: **COMPLETE**
- story inventory: **6/6 COMPLETE**
- new canonical stories: **0**
- witness comparisons started: **0/6**
- canonical Tamil/English changes: **0 / 0**

## Queued source — 1953 `தப்பிவிட்டார்கள்`

Controlling attached source:

`TVA_BOK_0064098_தப்பிவிட்டார்கள்.pdf`

Collection workspace:

`collections/1953-thappivittargal/`

Source identity:

- bytes: **50,916,676**
- SHA-256: **`435a2e8afbf036bce7daff27283722050ca9e03b92cd2dbb077dea339447a36b`**
- physical scans: **34**
- edition: **நான்காம் பதிப்பு — ஆகஸ்ட் '53**
- publisher: **திராவிடன் பதிப்பகம், வேலூர் (வ. ஆ.)**
- source type: **image-only**
- source PDF committed: **No**

Story pagination:

- scans **7–34**
- printed pages **5–32**
- relation: **scan = printed page + 2**

Inventory — **4/4 COMPLETE**:

1. `தப்பிவிட்டார்கள்` — scans **7–15 / printed 5–13** — existing canonical witness
2. `சபலம்` — scans **16–23 / printed 14–21** — existing canonical witness
3. `விலையால் வாங்கலையோ` — scans **24–31 / printed 22–29** — **new-canonical candidate**
4. `முந்நூறு ரூபாய்` — scans **32–34 / printed 30–32** — existing canonical witness

Fresh repository-wide assembled-section checks found no duplicate for `விலையால் வாங்கலையோ`; repeat the duplicate check immediately before activation.

## Exact next activity — current

Process the active 1950 Story 1 witness:

- title: **`வாழ முடியாதவர்கள்`**
- 1950 scans: **6–15**
- printed pages: **5–14**
- total: **10 physical source pages**
- target canonical: `stories/vazha-mudiyathavargal/`
- controlling canonical source remains the verified 1977 edition
- compare direct 1950 pixels by text anchors
- document lexical / morphology / punctuation / structural variants
- scans 14–15 have severe physical loss; do **not** reconstruct missing 1950 wording
- any possible canonical defect exposed by the witness becomes a recheck candidate only
- stop after scan 15

Do not begin Story 2 in the same activity unless the user explicitly changes the one-story-at-a-time rule.

## Closed source — 1956 `தாய்மை`

Controlling attached source: `TVA_BOK_0064112_தாய்மை.pdf`.

Collection workspace: `collections/1956-thaaymai/`.

Source identity:

- bytes: **104,030,458**
- SHA-256: **`b02873fd00b8e7b2afb568d833b07d9541922bddcd0a0600d6ed3ffabc037b78`**
- physical scans: **87**
- printed title: **தாய்மை**
- author: **மு. கருணாநிதி**
- publisher: **மோகன் பதிப்பகம், சென்னை-5**
- edition: **முதல் பதிப்பு — மார்ச்சு, 1956**
- source type: **image-only; direct scan pixels control**
- source PDF committed: **No**

Physical routing:

1. `தாய்மை` — scans **7–22 / printed 5–20**
2. `ஆட்டக் காவடி` — scans **23–33 / printed 21–31**
3. `நடுத்தெரு நாராயணி` — scans **34–59 / printed 32–57**
4. `அரும்பு` — scans **60–81 / printed 58–79**, then **82–87 / printed 82–87**

Critical source limitation:

- scan **81** = printed **79**
- scan **82** = printed **82**
- printed pages **80–81 are absent**
- do not reconstruct them from the 1978 witness.

### Witness 1 — `தாய்மை`

**CLOSED / PASS — 16/16.**

- workspace: `stories/thaaymai/witnesses/1956-thaaymai/`
- narrative structure equivalent: **Yes**
- material edition variants: **11**
- canonical Tamil / English changed: **No / No**
- unresolved: **0**

### Witness 2 — `ஆட்டக் காவடி`

**CLOSED / PASS — 11/11.**

- workspace: `stories/aattakkavadi/witnesses/1956-thaaymai/`
- narrative structure equivalent: **Yes**
- canonical Tamil / English changed: **No / No**
- unresolved: **0**
- canonical-recheck candidate remains open:
  - 1956 `நாளெல்லாம் பாடுபட்டாலும்`
  - current 1977 canonical `நாவெல்லாம் பாடுபட்டாலும்`
- closing-span edition variants include:
  - 1956 `ஈனஸ்தாயியில்` ↔ 1977 `ஈனக் குரலில்`
  - 1956 `மனத்திற்கு விரோதமாக` ↔ 1977 `மனத் தீர்க்கு விரோதமாக`
- scan **33 / printed 31** closes the story; scan **34** opens `நடுத்தெரு நாராயணி`.

### Witness 3 — `நடுத்தெரு நாராயணி`

Canonical repository: `pugazg/kalaignar-novels`

Workspace:

`works/nadutheru-narayani/witnesses/1956-thaaymai/`

Current state:

- witness extent: **26 scans — 34–59 / printed 32–57**
- reviewed: **26/26 — CLOSED / PASS**
- narrative structure in reviewed span: **equivalent overall; one localized 1956-only dialogue line recorded**
- material variants recorded: **16**
- canonical Tamil / English changed: **No / No**
- unresolved witness readings: **0**
- canonical-recheck candidates:
  1. 1956 `ஆண்களின் கர்வமடக்கும்` ↔ current 1978 `ஆண்களின் கருவமடக்கும்`
  2. 1956 `பிராமணோத்தமரே!` ↔ current 1978 `பிராமணத் தமரே!`
  3. 1956 `தனது கைகளால்` ↔ current 1978 `தனது கண்களால்`
  4. 1956 `ஏழெட்டு உறுப்பினர்களை` ↔ current 1978 `ஏழெட்டு உறுப்பினர்களே`
- localized 1956-only dialogue line: `அடி விபசாரி! உனக்கு இவ்வளவு கொழுப்பா?`
- do not repair any candidate without direct recheck of the exact 1978 controlling scans.

### User batching rule

Process **10 physical source pages per iteration**. Crossing a work/repository boundary is allowed only when necessary to fill the 10-page batch, while preserving separate witness workspaces and canonical authority.

### Witness 4 — `அரும்பு`

Canonical repository: `pugazg/kalaignar-novels`

Workspace: `works/arumbu/witnesses/1956-thaaymai/`

Current state:

- witness physical extent: **28 scans — 60–87**
- printed pages: **58–79**, then **82–87**
- source gap: **printed 80–81 absent**
- reviewed: **28/28 physical scans — CLOSED FOR ALL SOURCE-VISIBLE PAGES**
- visible narrative structure: **equivalent outside the documented source gap**
- material variants recorded: **11**
- canonical Tamil / English changed: **No / No**
- unresolved witness readings: **0**
- canonical-recheck candidates open: **0**
- 1956 independently confirms protected 1978 `எனக்குப் பொய் அம்மா வேணும்!` and `பேசினேன்`
- final 1956 page preserves the `இரு இலை, ஒரு மொட்டு` ending image and carries a terminal star

## 1956 `தாய்மை` final disposition

**SOURCE-VISIBLE WITNESS PROCESSING CLOSED.**

- `தாய்மை` — **16/16 CLOSED / PASS**
- `ஆட்டக் காவடி` — **11/11 CLOSED / PASS**
- `நடுத்தெரு நாராயணி` — **26/26 CLOSED / PASS**
- `அரும்பு` — **28/28 physical scans reviewed / CLOSED FOR ALL SOURCE-VISIBLE PAGES**
- printed pages **80–81** in `அரும்பு` — **ABSENT FROM SUPPLIED PDF**
- missing pages reconstructed — **No**
- canonical Tamil changed from witness evidence — **No**
- canonical English changed from witness evidence — **No**

Separate recheck backlog:

- `ஆட்டக் காவடி`: **1** candidate
- `நடுத்தெரு நாராயணி`: **4** candidates
- `அரும்பு`: **0** candidates

Those candidates require the exact later controlling scans and are **not** an automatic continuation of the 1956 page-processing workflow.

## Exact next activity — current

**NONE for 1956 `தாய்மை`. Await the user's next anthology.**

The previously deferred 1958 `தேனலைகள்` remains deferred; do not resume it unless the user explicitly returns to that PDF.

## Deferred source — 1958 `தேனலைகள்`

Controlling attached source: `TVA_BOK_0064030_தேனலைகள்.pdf`.

Collection workspace: `collections/1958-thenalaigal/`.

Source identity:

- bytes: **111,904,021**
- SHA-256: **`6d27bbf95f4a91e275b720d9a7d573c5649245dbfeb8a9ac2768ead7755652c7`**
- physical scans: **112**
- first edition: **December 1958**
- publisher: **முத்துவேல் பதிப்பகம்**
- source type: **image-only; rendered scan pixels are controlling**
- source PDF committed: **No**

Front matter:

- scan 1 — cover;
- scan 2 — edition / rights / price / printer;
- scans 3–4 — `வணக்கம்` publisher note;
- scan 5 — `என்னுரை`;
- scan 6 — non-story reverse/blank;
- no printed TOC is visible.

Story block:

- scans **7–111**
- printed pages **1–105**
- pagination relation: **scan = printed page + 6**
- scan **112** — `புது வெளியீடுகள்` advertisement/back matter
- internal printed-story-page gaps detected: **0**

Story inventory — **12/12 mapped; transcription not started**:

1. `முத்தாரம்` — scans **7–17 / printed 1–11**
2. `மயிலிறகு` — scans **18–29 / printed 12–23**
3. `முத்துமாலை` — scans **30–38 / printed 24–32**
4. `மடல்` — scans **39–44 / printed 33–38**
5. `தோழி` — scans **45–52 / printed 39–46**
6. `மருதாணி` — scans **53–60 / printed 47–54**
7. `அருவி` — scans **61–67 / printed 55–61**
8. `முறம்` — scans **68–74 / printed 62–68**
9. `யாழ்` — scans **75–82 / printed 69–76**
10. `சிற்பி` — scans **83–95 / printed 77–89**
11. `சேவல் சண்டை` — scans **96–104 / printed 90–98**
12. `ஆண்டு விழா` — scans **105–111 / printed 99–105**

Preliminary canonical deduplication on live `main` found no exact Tamil-title or obvious slug match for these twelve headings. All twelve are **new-canonical candidates**, but the check must be repeated immediately before each story is activated.

Durable intake files:

- `collections/1958-thenalaigal/README.md`
- `collections/1958-thenalaigal/metadata/source.md`
- `collections/1958-thenalaigal/indexes/scan-map.md`
- `collections/1958-thenalaigal/indexes/story-inventory.md`

Current processing state:

- source registration: **COMPLETE**
- scan map: **COMPLETE**
- story inventory: **COMPLETE 12/12**
- story workspaces created: **0**
- page records created: **0**
- Stage 1 transcription: **0/12 stories**
- English: **NOT STARTED**

## Exact next activity — current

Story 1 **`முத்தாரம்`**, scans **7–17 / printed 1–11**.

Before writing story text:

1. fetch live `main`;
2. reread `SHORT_STORY_PROCESSING_GUIDE.md`, `COLLECTION_SOURCE_GUIDE.md`, this handover, `NEXT_CHAT_PROMPT.md`, and the 1958 collection intake files;
3. reconfirm no canonical duplicate exists;
4. visually confirm scan 7 opening and scan 17 ending / scan 18 `மயிலிறகு` boundary;
5. create the Story 1 canonical workspace/page records;
6. begin **Stage 1 first-pass transcription** for `முத்தாரம்`.

Do not begin Story 2 in the same activity unless the user explicitly changes the one-story-at-a-time rule.

## Closed source — 1969 `கண்ணடக்கம்`

Controlling attached source: `TVA_BOK_0064095_கண்ணடக்கம்.pdf`.

Printed pages **31–52 (22 pages)** are absent from the only copy available to the user. This is a **known terminal source limitation**, not a pending search for another copy. Do not guess those missing story identities/text.

Visible routing:

1. `கண்ணடக்கம்` scans 4–10 — **existing canonical witness — COMPARISON CLOSED / PASS**
2. `நெருப்பு` scans 11–24 — **NEW canonical — TAMIL/SOURCE CLOSED**
3. `வேணியின் காதலன்` scans 25–31 — **existing canonical witness — COMPARISON CLOSED / PASS**
4. `அமிர்தமதி` scans 32–41 — **existing canonical witness — COMPARISON CLOSED / PASS**

`நெருப்பு` Tamil/source work is closed. All visible comparison-only witness work is also closed.

## `நெருப்பு` current state

Workspace: `stories/neruppu/`

- source intake: **PASS**
- story range: scans **11–24 / printed 10–23**
- page records: **14/14**
- Stage 1 first-pass: **14/14**
- Stage 2 visual fidelity: **14/14**
- Stage 3 historical glyph: **14/14**
- Stage 4 final check: **14/14**
- verified: **14/14**
- needs-review: **0/14**
- not-started: **0/14**
- blocked: **0**
- Tamil assembly: **PASS / CLOSED**
- reading layer: `stories/neruppu/sections/neruppu.md`
- source closure: `stories/neruppu/TAMIL_SOURCE_CLOSURE.md`
- Tamil/source release gate for translation: **CLOSED by explicit user-authorized visible-scope decision**
- English translation: **PASS / COMPLETE**
- English file: `stories/neruppu/translations/en/neruppu.md`
- English review: `stories/neruppu/TRANSLATION_REVIEW.md`
- English page traceability: **14/14 PASS**

### P1 — scans 11–15 / printed 10–14

**CLOSED / VERIFIED 5/5.**

- Stage 2 ordinary fidelity corrections: **15**
- Stage 3 character-identity corrections: **0**
- Stage 4 final source-proven corrections: **6**
- interim 16-correction revalidation: **SUPERSEDED; 12 over-corrections reverted**
- final unresolved: **0**

### P2 — scans 16–20 / printed 15–19

- Stage 1 first-pass: **COMPLETE 5/5**
- Stage 2 visual fidelity: **COMPLETE / PASS 5/5**
- Stage-2 source-proven corrections: **6**
- Stage-1 source-sensitive queue resolved: **6/6**
- Stage-2 unresolved ordinary fidelity issues: **0**
- pages: **`verified` 5/5**
- Stage 3 historical glyph: **COMPLETE / PASS 5/5**
- Stage-3 character-identity corrections: **0**
- Stage-3 unresolved glyph clusters: **0**
- Stage 4: **COMPLETE / PASS 5/5**
- Stage-4 source-proven corrections: **2**
- Stage-4 final unresolved issues: **0**
- blocked: **0**

## Mandatory four-stage cadence

1. first-pass transcription → commit + sync
2. visual text-fidelity audit → commit + sync
3. historical Tamil glyph audit → commit + sync
4. final independent source check → commit + sync; only then `verified`

### P3 — scans 21–24 / printed 20–23

**CLOSED / VERIFIED 4/4.**

- Stage 1 first-pass: **COMPLETE 4/4**
- Stage 2 visual fidelity: **COMPLETE / PASS 4/4**
- Stage 3 historical glyph: **COMPLETE / PASS 4/4**
- Stage 4 final independent source check: **COMPLETE / PASS 4/4**
- Stage-2 interim changes reviewed at final gate: **14**
- Stage-2 over-corrections reverted: **6**
- Stage-2 correction refined: **1**
- additional Stage-4 source corrections: **2**
- corrective changes applied during Stage 4: **9**
- final net source-fidelity differences from P3 Stage 1: **10**
- Stage-3 character-identity corrections: **0**
- Stage-3 unresolved glyph clusters: **0**
- final unresolved issues: **0**
- scan 24 ending sentence + closing ornament: **PASS**
- blocked: **0**

All **14/14** `நெருப்பு` page records are four-gate verified.

## `நெருப்பு` Tamil/source closure

**PASS / CLOSED.**

- verified page records: **14/14**
- assembled reading layer: `stories/neruppu/sections/neruppu.md`
- page provenance markers: **14/14**
- scan sequence: **11–24 exactly once**
- printed pages: **10–23 exactly once**
- scan 20→21 continuation: **PASS**
- scan 24 ending + ornament boundary: **PASS**
- scan 25: **excluded / opens `வேணியின் காதலன்`**
- unresolved source readings: **0**

## 1969 comparison-only witness progress

### `கண்ணடக்கம்` — scans 4–10 / printed 3–9

**CLOSED / PASS — 7/7 witness scans compared end-to-end.**

- witness workspace: `stories/kannadakkam/witnesses/1969-kannadakkam/`
- same narrative / hospital-frame ending: **PASS**
- major added / omitted blocks: **0**
- resolved 1977 recheck: exact scan 166 confirms `வாளை மீனுக்கோ`; 1969 and 2009 witnesses independently agree
- 1969 independently supports current canonical `துணி ஏணை` and `நமனுலகு`
- canonical Tamil / English / status changed: **No**
- unresolved witness issues: **0**

### `வேணியின் காதலன்` — scans 25–31 / printed 24–30

**CLOSED / PASS — 7/7 witness scans compared end-to-end.**

- witness workspace: `stories/veniyin-kadhalan/witnesses/1969-kannadakkam/`
- narrative structure / fatal ending: **equivalent**
- major added / omitted blocks: **0**
- canonical `கூண்டுக் கிளி ஆக்குவேனென்றான்`: **independently supported**
- canonical unusual `கந்தனு?`: **independently supported**
- 1969 `யோசனைதான்!` vs canonical `யோசனை தான்!`: **edition spacing variant**
- 1969 `என் வாழ்வைத் துண்டித்த` vs canonical `வாழ்க்கைத் துண்டித்த`: **edition wording variant**
- canonical Tamil / English / status changed: **No**
- unresolved witness issues: **0**

### `அமிர்தமதி` — scans 32–41 / printed 53–62

**CLOSED / PASS — 10/10 witness scans compared end-to-end.**

- witness workspace: `stories/amirthamathi/witnesses/1969-kannadakkam/`
- narrative / embedded `யசோதர காவியம்` structure: **equivalent**
- major added / omitted blocks: **0**
- 1977 ten historical-glyph repair identities: **independently supported**
- quoted verse lexical sequence: **independently supported**
- scan 41 ending: **PASS**
- scan 42 advertisement/back-matter boundary: **PASS**
- canonical Tamil / English / status changed: **No**
- unresolved witness issues: **0**

## 1969 collection current state

All **visible** story blocks are dispositioned:

1. `கண்ணடக்கம்` — comparison **CLOSED / PASS**
2. `நெருப்பு` — Tamil/source **CLOSED / PASS**
3. `வேணியின் காதலன்` — comparison **CLOSED / PASS**
4. `அமிர்தமதி` — comparison **CLOSED / PASS**

The collection itself is **NOT source-complete**: printed pages **31–52 (22 pages)** are absent.

## User-authorized Tamil release-gate decision

The physical-completeness finding remains unchanged. The user explicitly instructed the repository to **record the missing-span caveat, close the Tamil/source release gate for the fully processed visible scope, and proceed with `நெருப்பு` English**.

Durable distinction:

- physical collection completeness: **OPEN**
- visible Tamil/source work: **CLOSED / PASS**
- Tamil/source release gate for translation: **CLOSED for visible authorized scope**
- missing printed pages 31–52: **still unresolved / documented**
- `நெருப்பு` English: **PASS / COMPLETE**
- English source pages represented: **14/14**
- Tamil changed during translation: **No**
- unresolved English issues: **0**

Tracker: `collections/1969-kannadakkam/ENGLISH_TRANSLATION_PROGRESS.md`.

## Final 1969 collection disposition

The user confirms that this 43-scan PDF is **the only copy available**. There is no second or fuller source expected for this collection.

Therefore:

- printed pages **31–52** remain **absent / unrecoverable under current evidence**;
- the gap is preserved permanently as a source limitation;
- visible/source-supported work is **CLOSED**;
- `நெருப்பு` Tamil/source is **CLOSED / PASS**;
- `நெருப்பு` English is **CLOSED / PASS**;
- comparison witnesses are **CLOSED / PASS**;
- no source-completeness hold remains waiting for another copy.

## 1969 exact next activity

**NONE — 1969 `கண்ணடக்கம்` is CLOSED UNDER THE ONLY AVAILABLE COPY.**

Any future reopening would require genuinely new evidence or an explicitly requested separate canonical recheck. There is no automatic pending activity for this collection.


## Resolved canonical recheck — `கண்ணடக்கம்`

The exact 1977 controlling scan **166 / printed 157** was freshly reopened at enlarged resolution after the user flagged the reading. It reads **`வாளை மீனுக்கோ`**, not `வான மீனுக்கோ`.

- canonical Tamil: corrected
- canonical English: synchronized to “vaalai fish in the river”
- source-proven repair count: **10**
- unresolved: **0**
- 1969 witness: agrees
- 2009 witness: agrees
- recheck candidate: **CLOSED**
