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

## Source structure confirmed from full visual inspection

- scan 1 — cover
- scans 2–6 — reviews / publisher-editorial material / author note
- scans 7–22 — `கிழவன் கனவு` story body
- scan 23 — **`பிழை திருத்தம்.`** errata table + tobacco advertisement
- scan 24 — `ராஜேந்திரா நைஸ் புகையிலை` advertisement
- scan 25 — `தியாகராஜ விலாஸ்` advertisement / portrait
- scan 26 — back cover / small child illustration / no readable printed text

Visible story-body pagination:

- scan 8 = printed page `(4)`
- sequentially through scan 22 = printed page `(18)`
- scan 7's printed page number is not clearly visible; do **not** infer `(3)` into the archival record.

## Files created

Root:

- `README.md`
- `SHORT_STORY_PROCESSING_GUIDE.md`
- `HANDOVER.md`

Story control files:

- `stories/kizhavan-kanavu/README.md`
- `stories/kizhavan-kanavu/metadata/source.md`
- `stories/kizhavan-kanavu/indexes/page-map.md`

Page records:

- scans 1–6: `pages/0001-...` through `pages/0006-...`
- scans 7–22: `pages/0007-kizhavan-kanavu-01.md` through `pages/0022-kizhavan-kanavu-16.md`
- scan 23: `pages/0023-errata-advertisement.md`
- scan 24: `pages/0024-advertisement.md`
- scan 25: `pages/0025-thiyagaraja-vilas-ad.md`
- scan 26: `pages/0026-back-cover.md`

## Status after full-scan archival batch

- Source registered: **yes**
- 26-page manifest: **complete**
- Page records: **26 / 26**
- `verified`: **7** — scans 1, 2, 5, 6, 24, 25, 26
- `needs-review`: **19** — scans 3, 4, 7–23
- `not-started`: **0**
- Story-body direct visual transcription: **complete for scans 7–22**
- Back matter through back cover: **archived**
- Tamil audit: **pending**
- English translation: **do not start yet**

## Important unresolved / caution items

1. **Scan 3 — library stamp obstruction.** Several printed words in the upper review are physically hidden. Do not reconstruct them from context.
2. **Scan 4 — one short unclear phrase.** Keep explicit until a clearer source supports a reading.
3. **Scans 7–22 — provisional source readings.** The full story has been transcribed by visual comparison, but worn type / historical printing and several unclear words remain. These pages intentionally remain `needs-review` until the dedicated Tamil audit.
4. **Scan 15 — stamp over story text.** Hidden words must remain unresolved unless another source copy is deliberately introduced and documented.
5. **Scan 22 — conclusion/footer obstruction.** A large circular library stamp and handwritten `76930` obscure part of the story conclusion and publisher/printer footer. Do not guess the hidden wording.
6. **Scan 23 classification corrected.** It is **not** an `இவை கிடைக்கும்` catalogue page. It is a **`பிழை திருத்தம்.`** table plus tobacco advertising. One errata correction entry (page 7 / line 18) remains visually unclear.
7. **Errata must remain a separate layer.** Do not silently alter page transcriptions using scan 23. An audited assembled text may later reference the printed corrections explicitly.
8. **Edition year remains unresolved.** Internal dates in reviews/notes are not automatically the second-edition publication year.
9. **Source PDF remains outside GitHub.** Never commit the PDF unless the user explicitly changes the repository policy.

## Next exact activity

Perform the **full Tamil source audit of scans 7–23**.

1. Re-open scans 7–23 page by page.
2. Compare every current Markdown record directly against the corresponding scan.
3. Resolve provisional readings only when the visible source supports them.
4. Preserve historical spelling, punctuation, grammar, names and line/paragraph structure; do not modernize silently.
5. Leave stamp-obscured and genuinely unreadable text explicitly unresolved.
6. Cross-check scan 23's printed errata against the relevant source pages, but do **not** overwrite the archival page text silently.
7. Update each page status to `verified` only after direct audit; otherwise retain `needs-review` with a precise note.
8. Update `indexes/page-map.md`, story `README.md`, root `README.md`, and this `HANDOVER.md`.
9. Only after the Tamil source audit, create an assembled Tamil story text / documented errata layer.
10. Do **not** begin English translation until the Tamil audit gate is satisfied.
