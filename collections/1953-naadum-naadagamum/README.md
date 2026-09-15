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

It contains:

1. prose/discourse `நாடும் நாடகமும் (ஆசிரியர் பேச்சிலே)`;
2. the dramatic work `தெருக்கூத்து`;
3. three short-story blocks:
   - `ஆலமரத்துப் புறாக்கள்`
   - `பெண்கள்`
   - `இரகசியம்!`

Per explicit user instruction, **all five body units remain in this short-stories repository**, including the prose/discourse `நாடும் நாடகமும் (ஆசிரியர் பேச்சிலே)` and the play `தெருக்கூத்து`. They are not to be moved to another repository merely because their genre differs.

For repository organization, the first two are treated as **repository-retained special works** within this source collection; the remaining three use the normal short-story canonical/witness workflow.

## Front matter / physical structure

- scan **1** — title/cover: `நாடும் நாடகமும்`, `மு. கருணாநிதி`, `திராவிடப்பண்ணை`;
- scan **2** — edition / price / printer-imprint page; **முதல் பதிப்பு — 1953**;
- scans **3–4** — `பதிப்புரை`;
- no printed contents page is visible;
- scan **5** begins `நாடும் நாடகமும் (ஆசிரியர் பேச்சிலே)`;
- scan **80** is printed page **72**, closes `இரகசியம்!`, and carries the terminal star;
- no later back-matter scan is present in the supplied PDF.

## Pagination model

The publication has an inserted four-page sequence after printed page 16:

- scans **5–20** = printed pages **1–16**;
- scans **21–24** = printed **16-A, 16-B, 16-C, 16-D**;
- scans **25–80** = printed pages **17–72**.

Thus a simple constant scan/printed-page offset does **not** apply across the entire body.

## Repository-retained work inventory

| # | Opening heading | Type | PDF scans | Printed pages | Repository routing |
|---:|---|---|---:|---:|---|
| 1 | `நாடும் நாடகமும் (ஆசிரியர் பேச்சிலே)` | prose/discourse | 5–24 | 1–16, 16-A–16-D | **retain and process in this repository** |
| 2 | `தெருக்கூத்து` | play | 25–51 | 17–43 | **retain and process in this repository** |
| 3 | `ஆலமரத்துப் புறாக்கள்` | short story | 52–68 | 44–60 | existing canonical `stories/aalamarathup-puraakkal/` — **earlier witness** |
| 4 | `பெண்கள்` | short story | 69–75 | 61–67 | **new-canonical candidate**; no exact title / obvious title-derived slug found on live `main` at intake |
| 5 | `இரகசியம்!` | short story | 76–80 | 68–72 | existing canonical `stories/iragasiyam/` — **earlier witness** |

Detailed structural records:

- [`metadata/source.md`](metadata/source.md)
- [`indexes/scan-map.md`](indexes/scan-map.md)
- [`indexes/story-inventory.md`](indexes/story-inventory.md)

## Canonical-deduplication intake

Live `main` was checked before registration.

- `ஆலமரத்துப் புறாக்கள்` already has a closed canonical workspace from the 1977 anthology.
- `இரகசியம்!` already has a closed canonical workspace from the 1977 anthology; the 1953 opening is the same work.
- `பெண்கள்` has no exact-title canonical workspace or obvious matching title-derived slug in the current story index. It is therefore an **intake-level new-canonical candidate**, subject to a fresh content-level deduplication check immediately before activation.

No new canonical story folder was created in this intake-only iteration.

## Current state

- source registration: **COMPLETE**
- whole-source scan map: **COMPLETE**
- full body-unit inventory: **5/5 COMPLETE**
- repository-retained special works: **2/2**
- short-story inventory: **3/3 COMPLETE**
- short-story opening scans visually checked: **3/3**
- final source boundary checked: **PASS — scan 80**
- retained work 1 `நாடும் நாடகமும் (ஆசிரியர் பேசுகிறார்)`: **IN PROGRESS**
  - Batch 1 scans **5–9 / printed 1–5**
  - Stage 1 first-pass: **COMPLETE 5/5**
  - Stage 2 visual fidelity: **COMPLETE 5/5**
  - Stage-2 source-proven corrections: **16**
  - Stage-2 unresolved source-text spans: **1 — scan 9 mark crossing**
  - Stage 3 historical glyph: **COMPLETE 5/5**
  - Stage-3 character-identity corrections: **0**
  - Stage 4: **COMPLETE / PASS after targeted scan-9 resolution**
  - Stage-4 source-proven corrections: **0**
  - post-closure word-by-word visual fidelity re-audit: **COMPLETE 5/5**
  - re-audit source-proven corrections: **19**
  - scans 5–9: **VERIFIED**
  - scan 9 former blocked span: **RESOLVED / VERIFIED**
  - page status: **verified 5/5**
  - Batch 2 scans **10–14 / printed 6–10**
  - Stage 1 first-pass: **COMPLETE 5/5**
  - Stage 2 visual text-fidelity: **COMPLETE 5/5**
  - Stage-2 source-proven corrections: **22**
  - Stage 3 historical glyph: **COMPLETE / PASS 5/5**
  - Stage-3 character-identity corrections: **0**
  - Stage-3 unresolved glyph clusters: **0**
  - Stage 4 final independent source check: **COMPLETE / PASS 5/5 after targeted scan-13 resolution**
  - Stage-4 additional source-supported corrections: **24**
  - targeted scan-13 source resolution: **`படுவது,`**
  - page status: **verified 5/5**
  - unresolved source-text spans: **0**
  - guessed readings: **0**
  - Batch 2 closure: **CLOSED / VERIFIED 5/5**
  - Batch 3 scans **15–19 / printed 11–15**
  - Stage 1 first-pass: **COMPLETE 5/5**
  - Stage 2 visual text-fidelity: **COMPLETE 5/5**
  - Stage-2 source-proven corrections: **7**
  - Stage 3 historical glyph: **COMPLETE / PASS 5/5**
  - mandatory glyph families audited: **13/13**
  - Stage-3 character-identity corrections: **0**
  - Stage-3 unresolved glyph clusters: **0**
  - Stage 4 final independent source check: **COMPLETE / PASS 5/5**
  - Stage-4 source-proven corrections: **2**
  - page status: **verified 5/5**
  - unresolved source-text issues: **0**
  - guessed readings: **0**
  - Batch 3 closure: **CLOSED / VERIFIED 5/5**
- final retained-work batch scans **20–24 / printed 16, 16-A–16-D**:
  - Stage 1 first-pass: **COMPLETE 5/5**
  - page records: **5/5**
  - page status: **needs-review 5/5**
  - explicit unreadable inline spans: **0**
  - guessed readings: **0**
  - scan 21→22 boundary: **PASS — `கொண்டிட` / `வேண்டாம்.`**
  - scan 22→23 boundary: **PASS — `நல்ல` / `சமூக நாடகங்கள்`**
  - scan 24: **work-ending page**
  - scan 25 boundary witness: **opens `தெருக்கூத்து` / காட்சி 1 — excluded**
  - Stage 2 visual text-fidelity: **NEXT**
  - Stage 3: **NOT STARTED**
  - Stage 4: **NOT STARTED**
  - durable Stage-1 record: `STAGE1_BATCH_004.md`
- remaining witness comparison: **NOT STARTED**
- English: **NOT STARTED**

## Exact next activity

Retained work 1 `நாடும் நாடகமும் (ஆசிரியர் பேசுகிறார்)` — **Batch 4 Stage 2 visual text-fidelity audit**, scans **20–24 / printed 16, 16-A–16-D**.

Batches 1–3, scans **5–19**, remain **CLOSED / VERIFIED 15/15**.

Batch 4 Stage 1 is durably **COMPLETE 5/5**. All five final prose/discourse pages now have page records and remain `needs-review`; explicit unreadable inline spans and guessed readings are 0. Scan 24 is the work-ending page, while scan 25 visibly opens `தெருக்கூத்து` / காட்சி 1 and is excluded.

Run Stage 2 only, synchronize controls, commit, and stop before Stage 3 or `தெருக்கூத்து`.
