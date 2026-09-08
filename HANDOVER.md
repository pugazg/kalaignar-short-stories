# HANDOVER — Kalaignar Short Stories Archive

## Repository

- repository: `pugazg/kalaignar-short-stories`
- branch: `main`
- permanent workflows: `SHORT_STORY_PROCESSING_GUIDE.md`, `COLLECTION_SOURCE_GUIDE.md`, `HISTORICAL_TAMIL_GLYPH_TRANSCRIPTION_GUIDE.md`, `ENGLISH_TRANSLATION_GUIDE.md`

## LIVE MAIN IS AUTHORITATIVE

Always fetch live `main` first and preserve newer durable state.

## Permanent phase rules

- controlling scan first; no silent normalization;
- preserve shared physical page boundaries;
- additional witnesses never overwrite controlling canonical editions;
- decode historical Tamil type by character identity, never visual resemblance alone;
- Tamil/source closes before English;
- completed collection phases stay frozen unless stronger source evidence appears or the user explicitly requests maintenance;
- for anthology work, process **one story at a time** unless the user explicitly changes that rule.

## Closed phases — preserve

- 1977 — Tamil/visual/English **37/37 PASS**
- 2008 — Tamil/visual/English **40/40 PASS**
- 2004 — Tamil/visual/English **34/34 PASS**
- 2009 new-story onboarding — **5/5 CLOSED**
- 2009 existing-canonical witness comparison — **11/11 CLOSED**
- supplemental English — **6/6 PASS / CLOSED**
- 1987 `கலைஞர் சொன்ன குட்டிக் கதைகள்` Tamil/source — **PASS / CLOSED**
- 1987 `கலைஞர் சொன்ன குட்டிக் கதைகள்` English — **25/25 PASS / CLOSED**

## Cross-project hold — preserve

`நடுத்தெரு நாராயணி` remains **BLOCKED from starting** while `வெள்ளிக்கிழமை` is incomplete in `pugazg/kalaignar-novels`.

## ACTIVE — 1982 `முடியாத தொடர்கதை`

Collection workspace: `collections/1982-mudiyatha-thodarkathai/`

Controlling source: `TVA_BOK_0065572_முடியாத_தொடர்கதை.pdf`

- **95 scans**
- **194,350,272 bytes**
- SHA-256 **`d69034c5374c6c1604ddeb6d8e034c4410ae0d58201f2dd1608edd0e6d8cfd41`**
- publisher: **தமிழோசை பதிப்பகம்**
- edition: **முதற்பதிப்பு — செப்டம்பர் 1982**
- image-only; do not commit PDF

Collection state:

- source registration: **PASS**
- scan map: **95/95 mapped**
- story inventory: **5/5 COMPLETE**
- Tamil/source stories closed: **2/5**
- English: **not started**

Story ranges:

1. `பெற்ற பிள்ளையை விற்ற தாய்` — scans **7–28**, printed **5–26** — **PASS / CLOSED — 22/22 verified**
2. `காசா லேசா` — scans **29–40**, printed **27–38** — **PASS / CLOSED — 12/12 verified**
3. `சீமான் வீட்டு சீக்காளி` — scans **41–49**, printed **39–47** — **GLYPH GATE PASS 9/9; FINAL SOURCE/VISUAL CLOSURE NEXT**
4. `நந்தியூர் நரியப்பன்` — scans **50–58**, printed **48–56** — waiting
5. `முடியாத தொடர்கதை` — scans **59–93**, printed **57–91** — waiting

## User-directed 1982 phase rule

For every story:

**complete first-pass transcription → dedicated post-transcription Historical Tamil Glyph Gate at native/high resolution → separate final source/visual closure → next story**.

Minimum old-form set on every page:

`ணா / ணை / ணொ / ணோ / லை / ளை / றா / றொ / றோ / னா / னை / னொ / னோ`.

No global replacement, silent modernization or context-only correction.

## Stories 1–2 — CLOSED

- Story 1 `பெற்ற பிள்ளையை விற்ற தாய்`: PASS / CLOSED, 22/22 verified.
- Story 2 `காசா லேசா`: PASS / CLOSED, 12/12 verified, final audit `stories/kaasa-lesa/FINAL_SOURCE_VISUAL_AUDIT_2026-09-08.md`.

Do not reopen without stronger evidence or explicit maintenance request.

## Story 3 — `சீமான் வீட்டு சீக்காளி` — CURRENT DURABLE CHECKPOINT

Workspace: `stories/seemaan-veettu-seekkaali/`

Physical range:

- scans **41–49 / printed 39–47**;
- scan 41 opening display: `சீமான் வீட்டு சீக்காளி`;
- later running header: `சீமான் வீட்டுச் சீக்காளி!`;
- scan 49: terminal star;
- scan 50: forward boundary opens `நந்தியூர் நரியப்பன்` and is excluded.

Activation / transcription / glyph state:

- fresh duplicate/canonical recheck against live `main` before activation: **PASS — new canonical**;
- first-pass transcription: **9/9 COMPLETE**;
- first-pass assembled Tamil: **COMPLETE**;
- dedicated native/high-resolution Historical Tamil Glyph Gate: **PASS 9/9**;
- unresolved historical-glyph candidates: **0**;
- source-pixel glyph corrections: **2**:
  - scan 45 `திலவிரிகோலமாக!` → `தலைவிரிகோலமாக!` (`லை`);
  - physical scan 46 `உடலக்` → `உடலைக்` (`லை`);
- gate record: `stories/seemaan-veettu-seekkaali/HISTORICAL_GLYPH_GATE.md`;
- page status: **9/9 `needs-review`**;
- final source/visual closure: **NOT STARTED / NEXT**;
- English: **not started**.

Source-supported difficult forms retained at the glyph gate include scan 43 `முடியும்ணு`, `செதாஸ் கோப்`, source-odd `தங்கியிருக்க வேண்;`, scan 46 `பாரத்தைப் போட்டு`, and scan 47 `எதிர் கொண்டழைத்தாள்`.

Known separate final-closure issue: the first-pass reading order is intact, but text beginning `சீமான் உதவியை நாடி வந்த...` is currently carried inside the scan-45 page record although the physical continuation runs into scan 46. The final source/visual closure must restore exact physical provenance.

## Exact next activity — Story 3 final source/visual closure

1. fetch live `main` and preserve newer durable work;
2. read permanent guides, this handover, `NEXT_CHAT_PROMPT.md`, Story-3 README, metadata, page map, historical-glyph gate, review queue, all nine page records, and assembled Tamil;
3. resolve the controlling PDF before source-pixel work;
4. directly reread scans **41–49** at native/high resolution for full phrase/clause/sentence fidelity, punctuation, spacing, source-odd spellings and cross-page continuations;
5. keep the already-PASSed historical-glyph gate closed; ordinary corrections must be recorded separately;
6. explicitly resolve the scan **45→46** physical page-provenance issue and synchronize page records/assembled Tamil;
7. recheck scan 41 opening/title layer, scan 49 ending/star, and scan 50 forward-boundary exclusion;
8. only if zero unresolved ordinary source-text items remain, promote 9/9 page records to `verified`, create `FINAL_SOURCE_VISUAL_AUDIT_2026-09-08.md`, and close Story 3;
9. **hard stop: do not start Story 4 in the same activity.**

Do not start `நடுத்தெரு நாராயணி`; its `வெள்ளிக்கிழமை` gate remains unsatisfied.
