# தப்பிவிட்டார்கள் — source collection intake

## Source

- file: `TVA_BOK_0064098_தப்பிவிட்டார்கள்.pdf`
- bytes: **50,916,676**
- SHA-256: **`435a2e8afbf036bce7daff27283722050ca9e03b92cd2dbb077dea339447a36b`**
- physical scans: **34**
- source type: **image-only**
- source authority: **direct scan pixels**
- source PDF committed: **No**

Bibliographic evidence visible in the source:

- title: **தப்பிவிட்டார்கள்**
- author: **மு. கருணாநிதி**
- publisher: **திராவிடன் பதிப்பகம்**
- place: **வேலூர் (வ. ஆ.)**
- edition: **நான்காம் பதிப்பு — ஆகஸ்ட் '53**
- rights: **உரிமை ஆசிரியருக்கு**
- printed price: **0-6-0**; a later handwritten price mark is also present
- printer / proprietor line: **எம். எஸ். ராமு கம்பெனி, 236, சைனா பஜார், சென்னை-1**
- scan 5: publisher note `பதிப்புரை`, signed `பதிப்பகத்தார்`

No printed contents page is visible.

## Physical structure

- scan 1 — illustrated cover
- scan 2 — blank / ownership-label page
- scan 3 — title / author / publisher
- scan 4 — edition / rights / price / printer
- scan 5 — publisher note
- scan 6 — non-story verso / imprint area
- scans 7–34 — four-story block

Printed story pagination runs **5–32** with the stable relation:

> **PDF scan = printed page + 2**

## Story inventory

| # | Source opening title | Printed pages | PDF scans | Routing |
|---:|---|---:|---:|---|
| 1 | `தப்பிவிட்டார்கள்` | 5–13 | 7–15 | existing canonical `stories/thappivittargal/` — earlier witness |
| 2 | `சபலம்` | 14–21 | 16–23 | existing canonical `stories/sabalam/` — earlier witness |
| 3 | `விலையால் வாங்கலையோ` | 22–29 | 24–31 | canonical `stories/vilaiyal-vangalaiyo/` — **ACTIVE / T1 6/8** |
| 4 | `முந்நூறு ரூபாய்` | 30–32 | 32–34 | existing canonical `stories/munnuru-rupai/` — earlier witness |

## Deduplication result

Fresh live-main checks found existing canonical routes for Stories 1, 2 and 4.

For Story 3, `விலையால் வாங்கலையோ`:

- no matching canonical title/slug exists in the current story tree;
- a repository-wide check of existing assembled story sections found no match for distinctive opening identifiers such as `வைரக்கண்ணு` / the opening marriage-market dialogue;
- therefore it is a **new-canonical candidate**, subject to one final duplicate check immediately before activation.

Do not create its story folder during intake.

## Processing state

**INTAKE COMPLETE 4/4; STORIES 1–2 WITNESS WORK CLOSED.**

- stories inventoried: **4/4**
- existing-canonical witness routes: **3/4**
- new-canonical stories activated: **1/4 — `விலையால் வாங்கலையோ` → `stories/vilaiyal-vangalaiyo/`**
- witness comparisons completed: **2/3 existing-canonical witnesses**
- Story 3 T1 transcription: **6/8 physical pages complete — scans 24–29**
- canonical Tamil changed from witness evidence: **No**
- canonical English changed from witness evidence: **No**
- canonical-recheck candidates opened from Stories 1–2: **0**

### Story 1 — `தப்பிவிட்டார்கள்`

**CLOSED / PASS — 9/9.**

- scans **7–15 / printed 5–13**
- narrative structure: **equivalent / complete**
- notable variants: `போடக்கூடாது` ↔ `போட்டுக்கூடாது`; `மூவாயிரம் தொழிலாளர்` ↔ `மூவாயிரம் தொழிலாளர்கள்`
- layout: 1953 three-open-circle divider before Leela Mill; simple closing rule
- canonical-recheck candidates: **0**
- canonical Tamil / English changed: **No / No**
- witness workspace: `stories/thappivittargal/witnesses/1953-thappivittargal/`

### Story 2 — `சபலம்`

**CLOSED / PASS — 8/8.**

- scans **16–23 / printed 14–21**
- narrative structure: **equivalent / complete**
- high-value variants: `இமைகளைப்` ↔ `இமைகளேப்`; `பார்க்கவில்லை` ↔ `பார்க்க வில்லை`; `அழுதிடும்` ↔ `அழுதிடுங்`; `அந்த அகோரமான இருளில்` ↔ `அந்த அந்தகாரமான இருளில்`
- layout: 1953 internal three-open-circle divider; no 1977-style opening rule / enlarged `வ` / closing ornament
- canonical-recheck candidates: **0**
- canonical Tamil / English changed: **No / No**
- witness workspace: `stories/sabalam/witnesses/1953-thappivittargal/`

### Story 3 — `விலையால் வாங்கலையோ`

**CANONICAL WORKSPACE ACTIVATED / T1 IN PROGRESS — 6/8.**

- canonical route: `stories/vilaiyal-vangalaiyo/`
- duplicate/identity recheck before activation: **PASS — no existing canonical match**
- completed T1 pages: scans **24–29 / printed 22–27**
- remaining T1 pages: scans **30–31 / printed 28–29**
- verified pages: **0/8**
- Stage 2–4: **not started**
- English: **blocked until Tamil/source closure**
- durable checkpoints: `stories/vilaiyal-vangalaiyo/T1_BATCH_024_025.md`, `stories/vilaiyal-vangalaiyo/T1_BATCH_026_027.md`, `stories/vilaiyal-vangalaiyo/T1_BATCH_028_029.md`

## Exact next activity

Process only **T1 scans 30–31 / printed 28–29** for `விலையால் வாங்கலையோ`, and inspect scan **32** only as the next-story boundary witness. Then commit and synchronize before Stage 2.

Do **not** start Story 4 body processing in the same activity.

Story 4 `முந்நூறு ரூபாய்` remains a later witness task after Story 3 is dispositioned.
