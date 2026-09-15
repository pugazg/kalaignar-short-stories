# நாடும் நாடகமும் — 1953 mixed-source intake

Physical-source workspace for the user-supplied **`நாடும் நாடகமும்`** publication.

## Source snapshot

- source PDF: `TVA_BOK_0064193_நாடும்_நாடகமும்.pdf`
- byte size: **119,943,631**
- SHA-256: **`f852f0d0e5501cf74109c491ec8ae7ba9cb0840289524c95556144423beb887f`**
- PDF scans: **80**
- printed title: **நாடும் நாடகமும்**
- printed author line: **மு. கருணாநிதி**
- publisher: **திராவிடப்பண்ணை**
- publisher location on cover: **தெப்பக்குளம், திருச்சி**
- represented edition: **முதல் பதிப்பு — 1953**
- visible price: **ரூ. 1-0-0**
- source type: **image-only scan; no usable parsed text layer**
- source PDF committed to GitHub: **No**

The attached PDF itself is the controlling source. Rendered scan pixels govern all source-dependent decisions.

## Publication classification

This is a **mixed publication**, not a pure short-story anthology.

Current source-supported body inventory:

1. prose/discourse `நாடும் நாடகமும் (ஆசிரியர் பேச்சிலே)`;
2. play `தெருக்கூத்து`;
3. short-story block `சந்தனக்கிண்ணம்`;
4. short story `ஆலமரத்துப் புறாக்கள்`;
5. short story `பெண்கள்`;
6. short story `இரகசியம்!`.

Per explicit user instruction, the prose/discourse and play remain in this short-stories repository.

## Front matter / physical structure

- scan **1** — title/cover;
- scan **2** — edition / price / printer-imprint page;
- scans **3–4** — `பதிப்புரை`;
- no printed contents page is visible;
- scan **5** begins `நாடும் நாடகமும் (ஆசிரியர் பேச்சிலே)`;
- scan **80 / printed 72** closes `இரகசியம்!` with the terminal star.

## Pagination model

The publication has an inserted four-page sequence after printed page 16:

- scans **5–20** = printed pages **1–16**;
- scans **21–24** = printed **16-A, 16-B, 16-C, 16-D**;
- scans **25–80** = printed pages **17–72**.

From scan 25 onward:

**PDF scan = printed page + 8**

## Corrected body-unit inventory

| # | Opening heading | Type | PDF scans | Printed pages | Repository routing |
|---:|---|---|---:|---:|---|
| 1 | `நாடும் நாடகமும் (ஆசிரியர் பேச்சிலே)` | prose/discourse | 5–24 | 1–16, 16-A–16-D | retained here — **CLOSED / VERIFIED 20/20** |
| 2 | `தெருக்கூத்து` | play | **25–36** | **17–28** | retained here — **Stage 1 COMPLETE 12/12** |
| 3 | `சந்தனக்கிண்ணம்` | short-story block | **37–51** | **29–43** | **new-canonical candidate / transcription not started** |
| 4 | `ஆலமரத்துப் புறாக்கள்` | short story | 52–68 | 44–60 | existing canonical — earlier witness |
| 5 | `பெண்கள்` | short story | 69–75 | 61–67 | new-canonical candidate |
| 6 | `இரகசியம்!` | short story | 76–80 | 68–72 | existing canonical — earlier witness |

### Boundary correction

The earlier provisional map `தெருக்கூத்து = scans 25–51` is **superseded**.

Direct Stage-1 processing shows:

- scan **36 / printed 28** explicitly ends `தெருக்கூத்து` with `[தெருக்கூத்தும் முடிகிறது]`;
- scan **37 / printed 29** opens `சந்தனக்கிண்ணம்`;
- scan **51 / printed 43** is the final page before scan 52's new `ஆலமரத்துப் புறாக்கள்` heading.

## Canonical-deduplication snapshot

- `ஆலமரத்துப் புறாக்கள்` — existing canonical `stories/aalamarathup-puraakkal/`;
- `இரகசியம்!` — existing canonical `stories/iragasiyam/`;
- `பெண்கள்` — intake-level new-canonical candidate;
- `சந்தனக்கிண்ணம்` — exact-title / obvious slug search on live `main` returned no match; **intake-level new-canonical candidate**, subject to content-level deduplication immediately before activation.

## Current state

- source registration: **COMPLETE**
- whole-source scan map: **CORRECTED / COMPLETE**
- full body-unit inventory: **6/6 COMPLETE**
- repository-retained special works: **2/2**
- short-story inventory: **4/4 COMPLETE**
- canonical witness routes: **2**
- new-canonical candidates: **2 — `சந்தனக்கிண்ணம்`, `பெண்கள்`**
- retained work 1 `நாடும் நாடகமும் (ஆசிரியர் பேசுகிறார்)`: **CLOSED / VERIFIED 20/20**
- retained work 2 `தெருக்கூத்து`:
  - corrected source span: **25–36 / printed 17–28**
  - user-expanded Stage 1: **COMPLETE 12/12**
  - Stage 2 visual text-fidelity audit: **COMPLETE / PASS 12/12**
  - Stage-2 source-supported corrections: **11**
  - Stage-2 corrected scans: **27, 31, 32, 34, 35, 36**
  - Stage-2 unresolved ordinary source-text issues: **0**
  - baseline: `therukoothu.md` used as non-authoritative draft
  - direct scan confirmation: **12/12**
  - page records: **12/12**
  - page status: **needs-review 12/12**
  - guessed readings: **0**
  - work-ending boundary: **PASS — scan 36**
  - scan 37 witness: **PASS — `சந்தனக்கிண்ணம்`**
  - Stage 3 historical-glyph audit: **NEXT**
  - durable Stage-1 record: `works/therukoothu/STAGE1_BATCH_001.md`
  - durable Stage-2 record: `works/therukoothu/STAGE2_BATCH_001.md`
- `சந்தனக்கிண்ணம்`: **NOT STARTED**
- remaining witness comparison: **NOT STARTED**
- English: **NOT STARTED**

## Exact next activity

Run **`தெருக்கூத்து` Stage 3 historical Tamil glyph audit** for scans **25–36 / printed 17–28**.

Stage 2 is now **COMPLETE / PASS 12/12** with **11** source-supported ordinary-fidelity corrections and **0** unresolved ordinary text issues.

Audit all mandatory historical-glyph families directly against the scans, record present/absent disposition and any character-identity corrections, keep all pages `needs-review`, synchronize controls, commit Stage 3, and stop before Stage 4.

Do not begin `சந்தனக்கிண்ணம்` in the same activity.
