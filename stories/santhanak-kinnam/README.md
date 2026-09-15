# சந்தனக்கிண்ணம்

Canonical story workspace for **சந்தனக்கிண்ணம்**, controlled by the user-supplied 1953 first edition of **நாடும் நாடகமும்**.

## Controlling source

- source filename: `TVA_BOK_0064193_நாடும்_நாடகமும்.pdf`
- collection: `collections/1953-naadum-naadagamum/`
- edition: **முதல் பதிப்பு — 1953**
- publisher: **திராவிடப்பண்ணை**
- physical range: **scans 37–51**
- printed pages: **29–43**
- source PDF scans: **80**
- source bytes: **119,943,631**
- source SHA-256: **`f852f0d0e5501cf74109c491ec8ae7ba9cb0840289524c95556144423beb887f`**
- source type: **image-only; direct scan pixels control**
- source PDF committed: **No**

No OCR, web copy, Wikisource, catalogue text, alternate edition, or contextual reconstruction may supply accepted wording.

## Canonical activation

**NEW CANONICAL STORY — ACTIVATED.**

Fresh live-`main` deduplication immediately before activation found:

- exact title `சந்தனக்கிண்ணம்`: **no match**
- spaced title variant `சந்தன கிண்ணம்`: **no match**
- obvious title/slug route: **no match**
- unique opening/content phrase searches: **no match**
- character/content searches using `கமலா`, `விஜயா`, the wedding setting, and the source's `சந்தனக்கிண்ணம்` gift description: **no match**

Direct source review establishes a distinct story centered on the wedding of Kamala and Sandhan, Kamala's close friend Vijaya, and the symbolic `சந்தனக்கிண்ணம்` gift. No existing canonical story in live `main` matched the title or the distinctive content anchors.

Therefore this 1953 unit is activated as canonical:

`stories/santhanak-kinnam/`

This is a repository deduplication decision, not a claim that no differently titled version can ever exist outside the evidence currently held by the repository.

## Physical boundaries

- scan **37 / printed 29** — story title and opening
- scans **37–51 / printed 29–43** — complete story block
- scan **52 / printed 44** — separately opens `ஆலமரத்துப் புறாக்கள்`; excluded

## Four-stage workflow

`Stage 1 first-pass → Stage 2 visual fidelity → Stage 3 historical-glyph audit → Stage 4 final independent source check`

Only Stage 4 may promote pages to `verified`.

Default batch size: **5 physical scans**.

## Current state

- canonical activation: **COMPLETE**
- page map initialized: **15/15**
- Stage 1: **NEXT — scans 37–41 / printed 29–33**
- Stage 2: **NOT STARTED**
- Stage 3: **NOT STARTED**
- Stage 4: **NOT STARTED**
- verified: **0/15**
- needs-review: **0/15**
- not-started: **15/15**

Durable page map: [`indexes/page-map.md`](indexes/page-map.md)

## Exact next activity

Run **Stage 1 first-pass transcription** for scans **37–41 / printed 29–33** using only direct source pixels.

Preserve source wording, punctuation, spacing, paragraphing, verse layout, historical forms, and physical page joins. Record uncertainty explicitly rather than guessing. Create five page records as `needs-review`, create `STAGE1_BATCH_001.md`, synchronize collection controls, commit Stage 1 separately, and stop before Stage 2.
