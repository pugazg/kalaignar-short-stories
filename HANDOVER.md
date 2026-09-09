# HANDOVER — Kalaignar Short Stories Archive

## Repository

- repository: `pugazg/kalaignar-short-stories`
- branch: `main`
- permanent guides: `SHORT_STORY_PROCESSING_GUIDE.md`, `COLLECTION_SOURCE_GUIDE.md`, `HISTORICAL_TAMIL_GLYPH_TRANSCRIPTION_GUIDE.md`, `BATCH_TRANSCRIPTION_VERIFICATION_WORKFLOW.md`, `ENGLISH_TRANSLATION_GUIDE.md`

## LIVE MAIN IS AUTHORITATIVE

Fetch live `main` first and preserve newer durable work. Controlling scans outrank inferred/contextual readings. No silent normalization.

## Batch execution workflow — mandatory

Each physical batch is two durable activities:

1. **Stage A — direct transcription → synchronize Pass-1 state → commit → stop/report**;
2. **Stage B — independent historical-glyph/source verification → synchronize verification state → commit → stop/report**.

Do not routinely crop/enhance clear text. Do not begin the next batch until the current batch's Stage B is committed unless the user explicitly changes this rule.

## External hold

`நடுத்தெரு நாராயணி` remains **BLOCKED** while `வெள்ளிக்கிழமை` is incomplete in `pugazg/kalaignar-novels`.

## Closed work

The 1982 `முடியாத தொடர்கதை` anthology is **FULLY CLOSED — Tamil/source 6/6; English 6/6**.

## ACTIVE collection — 1976 `நளாயினி`

Collection workspace: `collections/1976-nalayini/`.

Source `TVA_BOK_0065574_நளாயினி_1976.pdf`:

- **78 scans**, **164,748,566 bytes**;
- `நான்காம் பதிப்பு 1976`;
- image-only; source PDF not committed;
- SHA-256 remains **pending** because raw-byte checksum access was unavailable; never invent/borrow a digest;
- the attached PDF itself is the sole controlling source unless the user explicitly requests external comparison.

Inventory:

1. `நளாயினி` 3–12 — existing canonical, note only;
2. `காதல் கடிதம்` 13–18 — existing canonical, note only;
3. `புரட்சிப் படம்` 19–24 — existing canonical, note only;
4. `நாட்டிய கலாராணி` 25–46 — **ACTIVE new canonical story**;
5. `விஷம் இனிது` 47–55 — existing canonical, note only;
6. `பாலைவன ரோஜா` 56–62 — existing canonical, note only;
7. `அய்யோ ராஜா!` 63–72 — existing canonical, note only;
8. `மானம்` 73–78 — new candidate, pending after Story 4.

Story 8 heading is **`மானம்`** from attached scan 73; do not regress to `மனம்`.

## Active Story 4 — `நாட்டிய கலாராணி`

Workspace: `stories/naattiya-kalarani/`.

Durable state:

- source boundary / dedup: **PASS / PASS**;
- page records: **22/22**;
- direct first-pass transcription: **5/22**;
- independent historical-glyph/source Stage B: **5/22**;
- verified: **5/22 — scans 25–29**;
- `needs-review`: **0**;
- blocked / unresolved: **0 / 0**;
- Tamil assembly: **not started**.

P1 scans 25–29 are **FULLY CLOSED**. Stage-B corrections:

1. scan 26 `இன்பபுரிக்கு` → `இன்ப புரிக்கு`;
2. scan 28 `துடிக்கிட்ட` → `திடுக்கிட்ட`;
3. scan 29 `ராஜ்ய விஷயங்களைக்` → `ராஜ்ய விஷயங்களை`.

The physical splits `நட்டுவ` / `னரும்` and `கவிவாணர்-` / `கவிவாணர்-மதிவாணர்` are confirmed and retained. Source-odd readings `தீயிலேகிடக்க`, `அங்கேன்`, `யாருக்குக் அளித்தது`, `நங்கள்`, and `மார்பிலேபுரண்ட` are confirmed, not normalized.

## Exact next activity — P2 Stage A only

Process **scans 30–34 / printed pages 30–34** only:

1. re-fetch live `main`;
2. read each whole page directly from the attached controlling source and transcribe once;
3. preserve source wording, punctuation, spacing, paragraphing, page boundaries and clearly readable historical character identity;
4. do **not** run the systematic 13-family Stage B in this activity;
5. do not routinely create crops/enhancements or repeatedly reopen clear words; use closer inspection only if a reading genuinely cannot be transcribed responsibly;
6. keep scans 30–34 `needs-review` after Stage A;
7. synchronize Pass-1/current-state controls;
8. commit Stage A;
9. stop and report.

After that durable commit, P2 Stage B on scans 30–34 becomes the next exact activity. Do not begin Story 8 `மானம்`.
