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

## Files currently created

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

## Status after front-matter batch

- Source registered: **yes**
- 26-page manifest: **complete**
- Page records: **6 / 26**
- `verified`: **4** — scans 1, 2, 5, 6
- `needs-review`: **2** — scans 3, 4
- `not-started`: **20** — scans 7–26
- Scans 2–6 direct visual transcription: **completed to the limit supported by the scan**
- Story-body transcription: **not started**
- Tamil audit: **not started**
- English translation: **do not start yet**

## Front-matter results / unresolved items

1. **Scan 2 — verified.** `மதிப்புரை.` by A. P. ஜனார்த்தனம் has been transcribed and visually checked.
2. **Scan 3 — needs-review.** The `“குடியரசு”` review has several printed words physically covered by a large library stamp. Readable text has been transcribed; hidden wording is represented explicitly as stamp-obscured and must not be reconstructed from context. The lower `“தொழிலாளர்”` review is readable and transcribed.
3. **Scan 4 — needs-review.** The publisher/editorial note is transcribed, but one short phrase in the middle cannot be distinguished confidently in the supplied scan. It remains explicitly unresolved rather than guessed.
4. **Scans 5–6 — verified.** `வணக்கம் பல!...` and `எழுதியது; ஏன்?` are fully transcribed and directly checked.
5. The cover imprint remains recorded as visible in the source; do not normalize the spelling/punctuation into a modern bibliographic form.
6. Internal dates printed in reviews/notes are not proof of the second edition's publication year.
7. Back-matter advertisements belong to the physical source record but must not be assembled into the story text.

## Next exact activity

Begin the **story body scans 7–10**.

1. Re-open source scans 7, 8, 9 and 10.
2. Create:
   - `pages/0007-kizhavan-kanavu-01.md`
   - `pages/0008-kizhavan-kanavu-02.md`
   - `pages/0009-kizhavan-kanavu-03.md`
   - `pages/0010-kizhavan-kanavu-04.md`
3. Do **not** infer a printed page number for scan 7.
4. Record scan 8 as printed page `4`, scan 9 as `5`, scan 10 as `6` only because those numbers are visibly printed.
5. Transcribe word-for-word by direct visual comparison; preserve dialogue punctuation, paragraph boundaries, historical spelling and unusual grammar.
6. Record library stamps / physical marks separately from printed story text.
7. Use `verified` only after direct page audit; otherwise use `needs-review` or `partial` with the exact unresolved reading noted.
8. Update `indexes/page-map.md`, story `README.md`, root `README.md`, and this `HANDOVER.md` after the batch.
