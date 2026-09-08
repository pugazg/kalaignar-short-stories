# முடியாத தொடர்கதை — 1982 collection source

Collection workspace for **`முடியாத தொடர்கதை`**, a five-short-story anthology by கலைஞர் மு. கருணாநிதி.

## Source snapshot

- source PDF: `TVA_BOK_0065572_முடியாத_தொடர்கதை.pdf`
- file size: **194,350,272 bytes**
- PDF scans: **95**
- SHA-256: **`d69034c5374c6c1604ddeb6d8e034c4410ae0d58201f2dd1608edd0e6d8cfd41`**
- printed title: **முடியாத தொடர்கதை**
- printed author: **கலைஞர் மு. கருணாநிதி**
- publisher: **தமிழோசை பதிப்பகம்**, 84, அபிபுல்லா சாலை, தியாகராயநகர், சென்னை-600017
- represented edition: **முதற்பதிப்பு — செப்டம்பர் 1982**
- printed price: **ரூ. 5-00**
- source PDF committed to GitHub: **No**
- source type: **image-only scan**

The scan is controlling. Do not silently normalize wording, punctuation, spacing, historical glyphs or source-title variants.

## Physical map

- scan 1: front cover
- scan 2: blank
- scan 3: title page
- scan 4: publication / bibliographical data
- scans 5–6: `பதிப்புரை`, printed pages 3–4
- scans 7–93: five story-bearing ranges, printed pages 5–91
- scan 94: advertisement / next-publication page, non-story
- scan 95: back cover

No separate printed contents page was found. The five-story inventory was therefore established by visually confirming every story-opening heading and every ending/next-story boundary.

## Story inventory — 5 / 5 registered

| # | Opening heading | PDF scans | Printed pages | Repository state |
|---:|---|---:|---:|---|
| 1 | `பெற்ற பிள்ளையை விற்ற தாய்` | 7–28 | 5–26 | new canonical candidate; not yet transcribed |
| 2 | `காசா லேசா` | 29–40 | 27–38 | new canonical candidate; not yet transcribed |
| 3 | `சீமான் வீட்டு சீக்காளி` | 41–49 | 39–47 | new canonical candidate; not yet transcribed |
| 4 | `நந்தியூர் நரியப்பன்` | 50–58 | 48–56 | new canonical candidate; not yet transcribed |
| 5 | `முடியாத தொடர்கதை` | 59–93 | 57–91 | new canonical candidate; not yet transcribed |

`காசா லேசா` and `சீமான் வீட்டு சீக்காளி` appear without a visible terminal exclamation mark in their stylized opening headings, while subsequent running headers use `காசா லேசா!` and `சீமான் வீட்டு சீக்காளி!`. Keep those source-layer forms distinct rather than silently normalizing them.

The collection title and Story 5 have the same wording, `முடியாத தொடர்கதை`. The physical anthology remains under `collections/`; Story 5 will receive its own canonical `stories/` workspace only when it becomes active.

## Duplicate / canonical-identity intake

Repository searches on live `main` for all five exact headings, plus distinctive title fragments, returned no existing canonical match. See `DUPLICATE_AUDIT.md`.

Do not pre-create five empty story folders. Under `COLLECTION_SOURCE_GUIDE.md`, create each story workspace only when that story becomes the active processing target and recheck live `main` immediately before creation.

## Processing state

- collection source registration: **PASS**
- physical scan map: **95 / 95 structurally mapped**
- story inventory: **5 / 5 COMPLETE**
- duplicate/canonical preflight: **5 / 5 — no existing repository match found**
- Tamil story transcription: **0 / 5**
- historical-glyph final verification: **0 / 5**
- English: **not started**

Historical Tamil typeforms are present. Every activated story must follow the mandatory two-pass historical-glyph workflow in `HISTORICAL_TAMIL_GLYPH_TRANSCRIPTION_GUIDE.md`.

## Exact next activity

Process **Story 1 — `பெற்ற பிள்ளையை விற்ற தாய்`**, scans **7–28 / printed pages 5–26**.

Before creating its canonical story workspace:

1. fetch live `main`;
2. rerun duplicate/canonical-identity search;
3. visually confirm scan 7 opening and scan 28 ending against scan 29, which opens Story 2 `காசா லேசா`;
4. create page records for exactly scans 7–28;
5. perform Pass 1 transcription and the separate native/high-resolution historical-glyph Pass 2;
6. process **only this one anthology story** in the activity unless the user explicitly changes the rule.

`நடுத்தெரு நாராயணி` remains blocked while `வெள்ளிக்கிழமை` is incomplete; this 1982 anthology is the user-authorized interim source.
