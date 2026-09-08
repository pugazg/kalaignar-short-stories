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

No separate printed contents page was found. The five-story inventory was established by visually confirming every story-opening heading and every ending/next-story boundary.

## Story inventory — 5 / 5 registered

| # | Opening heading | PDF scans | Printed pages | Repository state |
|---:|---|---:|---:|---|
| 1 | `பெற்ற பிள்ளையை விற்ற தாய்` | 7–28 | 5–26 | **first-pass 22/22 COMPLETE; historical-glyph gate PENDING; not source-closed** |
| 2 | `காசா லேசா` | 29–40 | 27–38 | new canonical candidate; waiting |
| 3 | `சீமான் வீட்டு சீக்காளி` | 41–49 | 39–47 | new canonical candidate; waiting |
| 4 | `நந்தியூர் நரியப்பன்` | 50–58 | 48–56 | new canonical candidate; waiting |
| 5 | `முடியாத தொடர்கதை` | 59–93 | 57–91 | new canonical candidate; waiting |

`காசா லேசா` and `சீமான் வீட்டு சீக்காளி` appear without a visible terminal exclamation mark in their stylized opening headings, while subsequent running headers use `காசா லேசா!` and `சீமான் வீட்டு சீக்காளி!`. Keep those source-layer forms distinct rather than silently normalizing them.

The collection title and Story 5 have the same wording, `முடியாத தொடர்கதை`. The physical anthology remains under `collections/`; Story 5 receives its own canonical `stories/` workspace only when it becomes active.

## 1982 old-glyph phase rule — user directed

This source has a high density of old Tamil typeforms. For **each story in this 1982 anthology**:

1. complete the full first-pass transcription for the story;
2. keep the page records `needs-review`;
3. run **one dedicated post-transcription Historical Tamil Glyph Gate** across every page of that story;
4. explicitly check all 13 minimum families `ணா / ணை / ணொ / ணோ / லை / ளை / றா / றொ / றோ / னா / னை / னொ / னோ` and any other suspicious old forms;
5. record corrections individually from source pixels — never global-replace or modernize;
6. do not declare final Tamil/source verification and do not start the following anthology story until the active story's glyph/source gates close.

The separate gate is intentionally **after transcription**; seeing old forms while transcribing does not count as gate closure.

## Duplicate / canonical-identity intake

Repository searches on live `main` for all five headings returned no existing canonical match at collection intake. Story 1 was searched again immediately before activation and still had no existing match, so `stories/petra-pillaiyai-vitra-thaai/` was created as a new canonical workspace controlled by this 1982 source. See `DUPLICATE_AUDIT.md`.

Do not pre-create the remaining four story folders. Recheck live `main` immediately before activating each story.

## Processing state

- collection source registration: **PASS**
- physical scan map: **95 / 95 structurally mapped**
- story inventory: **5 / 5 COMPLETE**
- Story 1 first-pass transcription: **22 / 22 COMPLETE**
- Story 1 historical-glyph gate: **PENDING**
- Story 1 final verified pages: **0 / 22**
- Tamil/source stories closed: **0 / 5**
- English: **not started**

## Exact next activity

Run the dedicated **Story 1 Historical Tamil Glyph Gate** for `பெற்ற பிள்ளையை விற்ற தாய்`, scans **7–28 / printed pages 5–26**.

Gate controls:

- `stories/petra-pillaiyai-vitra-thaai/HISTORICAL_GLYPH_GATE.md`
- `stories/petra-pillaiyai-vitra-thaai/POSSIBLE_ERRORS_FOR_REVIEW.md`
- all 22 page records and the assembled first-pass Tamil.

Do **not** begin Story 2 `காசா லேசா` until Story 1's post-transcription glyph gate and source closure have PASSed.

`நடுத்தெரு நாராயணி` remains blocked while `வெள்ளிக்கிழமை` is incomplete; this 1982 anthology remains the user-authorized interim source.
