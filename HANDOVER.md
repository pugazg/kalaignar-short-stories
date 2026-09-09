# HANDOVER — Kalaignar Short Stories Archive

## Repository

- repository: `pugazg/kalaignar-short-stories`
- branch: `main`
- permanent guides: `SHORT_STORY_PROCESSING_GUIDE.md`, `COLLECTION_SOURCE_GUIDE.md`, `HISTORICAL_TAMIL_GLYPH_TRANSCRIPTION_GUIDE.md`, `BATCH_TRANSCRIPTION_VERIFICATION_WORKFLOW.md`, `ENGLISH_TRANSLATION_GUIDE.md`

## LIVE MAIN IS AUTHORITATIVE

Fetch live `main` first and preserve newer durable work. Controlling scans outrank inferred/contextual readings. No silent normalization.

## Batch execution workflow — mandatory

Use `BATCH_TRANSCRIPTION_VERIFICATION_WORKFLOW.md` for page batches unless the user explicitly overrides it.

Each batch is split into two separate durable activities:

1. **Stage A — direct transcription → synchronize Pass-1 state → commit → stop/report**;
2. **Stage B — independent historical-glyph/source verification → synchronize verification state → commit → stop/report**.

Do not routinely crop/enhance during Stage A. Crops/enhancements belong only to genuinely unclear readings; the systematic 13-family audit belongs to Stage B. Do not begin the next batch until the current batch's Stage B is committed unless the user explicitly changes this rule.

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

### Controlling-source instruction

The user downloaded this exact PDF from the Tamil Digital Library and attached the downloaded file. **Use the attached PDF itself as the sole controlling source.** Do not query the Tamil Digital Library website again or use another external source for headings, transcription, boundaries, spelling, punctuation, metadata or glyph decisions unless the user explicitly asks for external comparison.

Inventory:

1. `நளாயினி` 3–12 — existing canonical, note only;
2. `காதல் கடிதம்` 13–18 — existing canonical, note only;
3. `புரட்சிப் படம்` 19–24 — existing canonical, note only;
4. `நாட்டிய கலாராணி` 25–46 — **ACTIVE new canonical story**;
5. `விஷம் இனிது` 47–55 — existing canonical, note only;
6. `பாலைவன ரோஜா` 56–62 — existing canonical, note only;
7. `அய்யோ ராஜா!` 63–72 — existing canonical, note only;
8. `மானம்` 73–78 — new candidate, pending after Story 4.

The Story-8 heading is `மானம்`, directly visible on attached scan 73. Earlier archive controls said `மனம்`; that was an intake transcription error and must not recur.

## Active Story 4 — `நாட்டிய கலாராணி`

Workspace: `stories/naattiya-kalarani/`.

Durable state:

- deduplication recheck: **PASS — no existing canonical/alternate-title match found**;
- direct physical boundary: **PASS — scans 25–46 / printed 25–46**;
- page records: **22/22 initialized**;
- direct first-pass transcription: **5/22 — scans 25–29 Stage A COMPLETE**;
- `needs-review`: **5/22**;
- Historical Tamil Glyph Pass 2: **0/22**;
- verified: **0/22**;
- blocked: **0/22**;
- Tamil assembly: **not started**.

P1 Stage-A physical boundary facts are preserved: scan 25 ends `நட்டுவ` and scan 26 begins `னரும்`; scan 27 ends `கவிவாணர்-` and scan 28 independently begins `கவிவாணர்-மதிவாணர்`. Source-sensitive but legible readings are recorded in `stories/naattiya-kalarani/POSSIBLE_ERRORS_FOR_REVIEW.md`. There are **0 blocking unreadable locations** in this Stage-A batch.

## Exact next activity — P1 Stage B only

Process only **scans 25–29 / printed pages 25–29** as **Stage B — independent historical-glyph/source verification**:

1. re-fetch live `main` and start from the committed Stage-A page records;
2. independently reopen the same five controlling scans;
3. compare the committed text against source pixels; do not fully retranscribe;
4. explicitly check `ணா / ணை / ணொ / ணோ / லை / ளை / றா / றொ / றோ / னா / னை / னொ / னோ` plus the source-sensitive queue;
5. create crops/enhancements only when an actual character/spacing/punctuation ambiguity remains;
6. record corrections individually; never global-replace;
7. promote only pages that fully close to `verified`; retain any unresolved page as `needs-review`;
8. synchronize page records and verification/current-state controls;
9. commit Stage B and stop/report.

Do **not** begin scan 30 in the same activity. Do not begin `மானம்` until Story 4 is fully closed.
