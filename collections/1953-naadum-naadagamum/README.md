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

The non-short-story material is mapped here only to preserve the physical source structure. It is **not** activated for transcription in this short-stories repository.

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

## Short-story inventory

| # | Opening heading | PDF scans | Printed pages | Repository routing |
|---:|---|---:|---:|---|
| 1 | `ஆலமரத்துப் புறாக்கள்` | 52–68 | 44–60 | existing canonical `stories/aalamarathup-puraakkal/` — **earlier witness** |
| 2 | `பெண்கள்` | 69–75 | 61–67 | **new-canonical candidate**; no exact title / obvious title-derived slug found on live `main` at intake |
| 3 | `இரகசியம்!` | 76–80 | 68–72 | existing canonical `stories/iragasiyam/` — **earlier witness** |

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
- short-story inventory: **3/3 COMPLETE**
- short-story opening scans visually checked: **3/3**
- final source boundary checked: **PASS — scan 80**
- non-story components classified: **COMPLETE**
- story transcription / witness comparison: **NOT STARTED**
- English: **NOT STARTED**

## Exact next activity

Process short-story item 1 **`ஆலமரத்துப் புறாக்கள்`**, scans **52–68 / printed 44–60**, as an **earlier-edition witness** to the existing canonical story.

Before comparison:

1. fetch live `main`;
2. reread the short-story and collection guides plus this intake;
3. confirm the canonical route remains `stories/aalamarathup-puraakkal/`;
4. visually recheck scan 52 opening, scan 68 ending, and scan 69 `பெண்கள்` boundary;
5. create a witness workspace under the existing canonical story and compare the 17 source scans without overwriting the 1977 canonical text.

Do **not** begin `பெண்கள்` in the same activity unless the user explicitly changes the one-story-at-a-time rule.
