# HANDOVER — Kalaignar Short Stories Archive

## Repository

- repository: `pugazg/kalaignar-short-stories`
- branch: `main`
- permanent workflows: `SHORT_STORY_PROCESSING_GUIDE.md`, `COLLECTION_SOURCE_GUIDE.md`, `HISTORICAL_TAMIL_GLYPH_TRANSCRIPTION_GUIDE.md`, `ENGLISH_TRANSLATION_GUIDE.md`

## LIVE MAIN IS AUTHORITATIVE

Always fetch live `main` first and preserve newer durable state.

## Permanent phase rules

- controlling scan first; no silent normalization;
- preserve physical page boundaries;
- historical Tamil glyphs are decoded by character identity, not visual resemblance;
- Tamil/source closes before English;
- anthology work proceeds one story at a time;
- translation proceeds only from verified canonical Tamil;
- completed Tamil/source and English layers are not reopened without genuinely stronger evidence or explicit maintenance authorization.

## Cross-project hold

`நடுத்தெரு நாராயணி` remains **BLOCKED** while `வெள்ளிக்கிழமை` is incomplete in `pugazg/kalaignar-novels`.

The user explicitly redirected archive work to the attached 1976 `நளாயினி` source while that hold remains. This does **not** authorize `நடுத்தெரு நாராயணி`.

## Closed collection — 1982 `முடியாத தொடர்கதை`

**FULLY CLOSED — Tamil/source 6/6; English 6/6.**

Do not reopen without genuinely new evidence or explicit maintenance authorization.

## ACTIVE collection — 1976 `நளாயினி`

Collection workspace: `collections/1976-nalayini/`.

Source: `TVA_BOK_0065574_நளாயினி_1976.pdf`.

- file size: **164,748,566 bytes**;
- PDF scans: **78**;
- printed title: **நளாயினி**;
- printed author: **மு. கருணாநிதி**;
- edition: **நான்காம் பதிப்பு 1976**;
- price: **விலை ரூ. 2-00**;
- image-only;
- source PDF must not be committed;
- SHA-256: **pending** because the current runtime could render the exact source but raw-byte checksum access failed. Do not invent or borrow a digest from another edition.

No separate printed contents page was found. Direct visual inspection of every opening establishes **8 stories**:

1. `நளாயினி` — scans/printed **3–12** — existing canonical — **NOTE ONLY / DO NOT RETRANSCRIBE**;
2. `காதல் கடிதம்` — **13–18** — existing canonical — **NOTE ONLY / DO NOT RETRANSCRIBE**;
3. `புரட்சிப் படம்` — **19–24** — existing canonical — **NOTE ONLY / DO NOT RETRANSCRIBE**;
4. `நாட்டிய கலாராணி` — **25–46** — **NEW canonical-story candidate / NEXT**;
5. `விஷம் இனிது` — **47–55** — existing canonical — **NOTE ONLY / DO NOT RETRANSCRIBE**;
6. `பாலைவன ரோஜா` — **56–62** — existing canonical — **NOTE ONLY / DO NOT RETRANSCRIBE**;
7. `அய்யோ ராஜா!` — **63–72** — existing canonical — **NOTE ONLY / DO NOT RETRANSCRIBE**;
8. `மனம்` — **73–78** — **NEW canonical-story candidate / pending after Story 4**.

The six duplicates were only registered as additional 1976 physical witnesses. No word-level comparison, retranscription, or alteration of their existing Tamil/English files was performed.

Controls:

- `collections/1976-nalayini/README.md`
- `collections/1976-nalayini/metadata/source.md`
- `collections/1976-nalayini/indexes/story-inventory.md`
- `collections/1976-nalayini/indexes/scan-map.md`
- `collections/1976-nalayini/DUPLICATE_WITNESSES.md`

## Exact next activity

Process only Story 4 **`நாட்டிய கலாராணி`**, scans **25–46 / printed pages 25–46**, from the attached 1976 source.

Before source-dependent writes:

1. fetch live `main`;
2. read `SHORT_STORY_PROCESSING_GUIDE.md`, `COLLECTION_SOURCE_GUIDE.md`, this handover, `NEXT_CHAT_PROMPT.md`, and the 1976 collection controls;
3. reconfirm no canonical story exists under the exact heading or a documented alternate title;
4. create the canonical Story-4 workspace only then;
5. preserve all 22 physical page boundaries and source-odd/historical glyph forms;
6. complete the story's Tamil/source workflow before advancing the collection.

Do **not** begin Story 8 `மனம்` in the same Story-4 activity. Do **not** start `நடுத்தெரு நாராயணி` while its external gate remains unsatisfied.
