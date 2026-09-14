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
- transcription / witness comparison: **NOT STARTED**
- English: **NOT STARTED**

## Exact next activity

Process repository-retained work 1 **`நாடும் நாடகமும் (ஆசிரியர் பேச்சிலே)`**, scans **5–24 / printed 1–16, 16-A–16-D**.

Before transcription:

1. fetch live `main`;
2. reread the short-story and collection guides plus this intake;
3. preserve this unit in **this repository** despite its prose/discourse genre;
4. visually recheck scan 5 opening, scan 24 ending, and scan 25 `தெருக்கூத்து` boundary;
5. create a dedicated durable workspace for this retained work within this repository;
6. begin source-faithful Stage 1 first-pass transcription only from the attached scan pixels.

After this work is closed, the next source-order retained work is **`தெருக்கூத்து`**, scans **25–51 / printed 17–43**.

Do **not** skip directly to `ஆலமரத்துப் புறாக்கள்` unless the user explicitly redirects.
