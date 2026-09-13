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

## Active source — 1958 `தேனலைகள்`

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
