# HANDOVER — Kalaignar Short Stories Archive

## Repository

- repository: `pugazg/kalaignar-short-stories`
- branch: `main`
- permanent guides: `SHORT_STORY_PROCESSING_GUIDE.md`, `COLLECTION_SOURCE_GUIDE.md`, `HISTORICAL_TAMIL_GLYPH_TRANSCRIPTION_GUIDE.md`, `ENGLISH_TRANSLATION_GUIDE.md`

## LIVE MAIN IS AUTHORITATIVE

Fetch live `main` first and preserve newer durable work. Controlling scans outrank inferred/contextual readings. No silent normalization.

## External hold

`நடுத்தெரு நாராயணி` remains **BLOCKED** while `வெள்ளிக்கிழமை` is incomplete in `pugazg/kalaignar-novels`. The user explicitly redirected current work to the attached 1976 `நளாயினி` collection; this does not authorize `நடுத்தெரு நாராயணி`.

## Closed work

The 1982 `முடியாத தொடர்கதை` anthology is **FULLY CLOSED — Tamil/source 6/6; English 6/6**. Do not reopen without genuinely new evidence or explicit maintenance authorization.

## ACTIVE collection — 1976 `நளாயினி`

Collection workspace: `collections/1976-nalayini/`.

Source `TVA_BOK_0065574_நளாயினி_1976.pdf`:

- **78 scans**, **164,748,566 bytes**;
- `நான்காம் பதிப்பு 1976`;
- image-only; source PDF not committed;
- SHA-256 remains **pending** because raw-byte checksum access was unavailable; never invent/borrow a digest.

Inventory:

1. `நளாயினி` 3–12 — existing canonical, note only;
2. `காதல் கடிதம்` 13–18 — existing canonical, note only;
3. `புரட்சிப் படம்` 19–24 — existing canonical, note only;
4. `நாட்டிய கலாராணி` 25–46 — **ACTIVE new canonical story**;
5. `விஷம் இனிது` 47–55 — existing canonical, note only;
6. `பாலைவன ரோஜா` 56–62 — existing canonical, note only;
7. `அய்யோ ராஜா!` 63–72 — existing canonical, note only;
8. `மனம்` 73–78 — new candidate, pending after Story 4.

## Active Story 4 — `நாட்டிய கலாராணி`

Workspace: `stories/naattiya-kalarani/`.

Durable state:

- deduplication recheck: **PASS — no existing canonical/alternate-title match found**;
- direct physical boundary: **PASS — scans 25–46 / printed 25–46**;
- page records: **22/22 initialized**;
- direct first-pass transcription: **0/22**;
- Historical Tamil Glyph Pass 2: **0/22**;
- verified: **0/22**;
- blocked: **0/22**;
- Tamil assembly: **not started**.

The story is intentionally not filled from OCR or another edition merely to advance counts.

## Exact next activity

Process only **scans 25–29 / printed pages 25–29**:

1. re-fetch live `main`;
2. read the five controlling scans directly;
3. transcribe all five pages source-faithfully;
4. run the separate mandatory historical-glyph second pass on the same five pages;
5. record source-odd/ambiguous forms explicitly;
6. update page records, page map, pass/glyph trackers, audit, README and handover;
7. commit the batch before scan 30.

Do not begin scan 30 in that iteration. Do not begin `மனம்` until Story 4 is fully closed.
