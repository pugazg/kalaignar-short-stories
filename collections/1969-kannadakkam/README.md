# கண்ணடக்கம் — 1969 collection source

Physical-source workspace for the attached **`கண்ணடக்கம்`** short-story collection.

## Source snapshot

- source PDF: `TVA_BOK_0064095_கண்ணடக்கம்.pdf`
- byte size: **50,321,052**
- PDF scans: **43**
- printed title: **கண்ணடக்கம்**
- printed author: **மு. கருணாநிதி**
- publisher/imprint: **திராவிடப்பண்ணை**
- represented edition: **இரண்டாம் பதிப்பு — 1969**
- visible price: **ரூ. 1-00**
- source type: **image-only scan**
- source PDF committed to GitHub: **No**
- SHA-256: **PENDING** — raw-byte hashing was unavailable in the current execution environment; do not invent a checksum

The attached PDF itself is the controlling source for this edition. No external website is needed for source-dependent work.

## Intake state

**SOURCE INTAKE PASS / PHYSICAL COMPLETENESS OPEN**

The visible source contains four story blocks:

| # | Opening heading | PDF scans | Printed pages | Canonical result | Current action |
|---:|---|---:|---:|---|---|
| 1 | `கண்ணடக்கம்` | 4–10 | 3–9 | existing canonical — `stories/kannadakkam/` | comparison witness only |
| 2 | `நெருப்பு` | 11–24 | 10–23 | `stories/neruppu/` — **new canonical active** | **P1 Stage 2 COMPLETE / PASS 5/5; Stage 3 NEXT** |
| 3 | `வேணியின் காதலன்` | 25–31 | 24–30 | existing canonical — `stories/veniyin-kadhalan/` | comparison witness only |
| 4 | `அமிர்தமதி` | 32–41 | 53–62* | existing canonical — `stories/amirthamathi/` | comparison witness only |

* Scan 32 is the story-opening page; scan 33 visibly carries printed folio **54**, so the opening is structurally inferred as printed page **53**.

## Critical physical discontinuity

The supplied PDF jumps from:

- scan **31** / printed page **30**, ending `வேணியின் காதலன்`,
- directly to scan **32**, opening `அமிர்தமதி`, whose next page is printed **54**.

Therefore printed pages **31–52 — 22 pages — are absent from the supplied PDF**.

Do not infer the missing story titles, text or boundaries from later editions or general knowledge. The visible four story blocks can be processed source-faithfully, but this physical collection must not be called source-complete while the missing printed span remains unresolved.

See `SOURCE_COMPLETENESS.md`.

## Back matter

- scan 42 — advertisement headed `அண்ணாவின் அரிய நூல்கள்`;
- scan 43 — rear leaf / publisher device; no story text.

## Canonical deduplication result

Repository inspection found existing canonical workspaces for:

- `கண்ணடக்கம்`;
- `வேணியின் காதலன்`;
- `அமிர்தமதி`.

Those three must be handled as **comparison-only witnesses**. Do not create duplicate Tamil transcriptions or duplicate English translations.

No repository canonical match was found for **`நெருப்பு`**. Its canonical workspace is now activated at `stories/neruppu/`; source intake is PASS and all 14 page records are initialized without prose transcription.

## Active progress — `நெருப்பு`

P1 scans **11–15 / printed 10–14**:

- Stage 1: **COMPLETE 5/5**
- Stage 2 visual text fidelity: **COMPLETE / PASS 5/5**
- Stage-2 corrections: **15**
- Stage-2 unresolved ordinary fidelity issues: **0**
- Stage 3 historical glyph: **NEXT**
- Stage 4 final check: not started
- page state: **needs-review**

## Exact next activity

Process **`நெருப்பு` P1 Stage 3 — historical Tamil glyph audit**, scans **11–15 / printed pages 10–14**.

Do not begin `வேணியின் காதலன்` witness comparison until `நெருப்பு` Tamil/source work closes.