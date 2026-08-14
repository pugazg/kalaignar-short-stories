# HANDOVER — Kalaignar Short Stories Archive

## Repository

- Repository: `pugazg/kalaignar-short-stories`
- Default branch: `main`
- Permanent workflow guide: `SHORT_STORY_PROCESSING_GUIDE.md`
- Source PDFs are **not** committed to the repository.

## Current story

- Work slug: `kizhavan-kanavu`
- Title as printed: **கிழவன் கனவு**
- Author line as printed: **தீட்டியவர்: மு. கருணாநிதி.**
- Edition statement: **இரண்டாம் பதிப்பு.**
- Source filename: `TVA_BOK_0014165_கிழவன்_கனவு.pdf`
- SHA-256: `cdea0e1c0d2ad657fc4163ed77c58027c18abbe58058221be7f32724b7ef8121`
- File size: **11,017,627 bytes**
- Scan pages: **26**

## Source structure confirmed from the scan

- scan 1 — cover
- scans 2–6 — reviews / publisher-editorial material / author note
- scans 7–22 — `கிழவன் கனவு` story body
- scans 23–25 — catalogue / advertisements
- scan 26 — back cover

Visible story-body pagination:

- scan 8 = printed page `(4)`
- sequentially through scan 22 = printed page `(18)`
- scan 7's printed page number is not clearly visible; do **not** infer `(3)` into the archival record.

## Files already created

Root:

- `README.md`
- `SHORT_STORY_PROCESSING_GUIDE.md`
- `HANDOVER.md`

Story:

- `stories/kizhavan-kanavu/README.md`
- `stories/kizhavan-kanavu/metadata/source.md`
- `stories/kizhavan-kanavu/indexes/page-map.md`
- `stories/kizhavan-kanavu/pages/0001-cover.md`
- `stories/kizhavan-kanavu/pages/0002-mathippurai.md`
- `stories/kizhavan-kanavu/pages/0003-reviews.md`
- `stories/kizhavan-kanavu/pages/0004-en-veliyitten.md`
- `stories/kizhavan-kanavu/pages/0005-vanakkam-pala.md`
- `stories/kizhavan-kanavu/pages/0006-ezhuthiyathu-yen.md`

## Status

- Source registered: **yes**
- 26-page manifest: **complete**
- Page records: **6 / 26**
- `verified`: **1** (scan 1)
- `partial`: **5** (scans 2–6)
- `not-started`: **20** (scans 7–26)
- Story-body transcription: **not started**
- Tamil audit: **not started**
- English translation: **do not start yet**

## Important unresolved / caution items

1. Scans 2–6 only contain confirmed headings, dates, signatures and physical-page notes so far. Their full body text is still pending.
2. Scan 3 has library stamp/ink interference over printed text. Do not reconstruct hidden wording from context.
3. The cover imprint has been visually read as **அஜீஸ் பதிப்பக வெளியீடு, விஜயபுரம் ::: திருவாரூர்.** Preserve the source spelling/punctuation; do not normalize it into a modern bibliographic form.
4. Internal dates printed in reviews/notes are not proof of the second edition's publication year.
5. Back-matter advertisements belong to the physical source record but must not be assembled into the story text.

## Next exact activity

1. Re-open source scans **2–6**.
2. Transcribe them word-for-word by direct visual comparison.
3. Preserve old spelling and punctuation exactly where readable.
4. Mark genuinely obscured readings explicitly; do not guess.
5. Promote each page from `partial` to `verified` only after full visual audit.
6. Update `indexes/page-map.md`, `stories/kizhavan-kanavu/README.md`, root `README.md`, and this `HANDOVER.md`.
7. Then begin story body scans **7–10** as the next batch.
