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
- Tamil/source closes before English; once closed, English is automatically next unless the user redirects;
- completed collection phases stay frozen unless genuinely stronger source evidence appears or the user explicitly requests maintenance;
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

1987 final English release audit: `collections/1987-kalaignar-sonna-kuttik-kathaigal/FINAL_ENGLISH_RELEASE_AUDIT_2026-09-08.md`.

## Cross-project hold — preserve

`நடுத்தெரு நாராயணி` remains **BLOCKED from starting** while `வெள்ளிக்கிழமை` is incomplete in `pugazg/kalaignar-novels`. The user explicitly confirmed that external gate is still unsatisfied.

## ACTIVE — 1982 `முடியாத தொடர்கதை`

Collection workspace: `collections/1982-mudiyatha-thodarkathai/`

Controlling source: `TVA_BOK_0065572_முடியாத_தொடர்கதை.pdf`

- **95 scans**
- **194,350,272 bytes**
- SHA-256 **`d69034c5374c6c1604ddeb6d8e034c4410ae0d58201f2dd1608edd0e6d8cfd41`**
- title: **முடியாத தொடர்கதை**
- author: **கலைஞர் மு. கருணாநிதி**
- publisher: **தமிழோசை பதிப்பகம்**
- edition: **முதற்பதிப்பு — செப்டம்பர் 1982**
- image-only; do not commit PDF

Collection state:

- source registration: **PASS**
- scan map: **95/95 mapped**
- story inventory: **5/5 COMPLETE**
- Tamil/source stories closed: **1/5**
- English: **not started**

Story ranges:

1. `பெற்ற பிள்ளையை விற்ற தாய்` — scans **7–28**, printed **5–26** — **PASS / CLOSED**
2. `காசா லேசா` — scans **29–40**, printed **27–38** — **ACTIVE: glyph gate PASS; final source/visual closure NEXT**
3. `சீமான் வீட்டு சீக்காளி` — scans **41–49**, printed **39–47** — waiting
4. `நந்தியூர் நரியப்பன்` — scans **50–58**, printed **48–56** — waiting
5. `முடியாத தொடர்கதை` — scans **59–93**, printed **57–91** — waiting

## User-directed 1982 phase rule

For every story:

**complete first-pass transcription → dedicated post-transcription Historical Tamil Glyph Gate at native/high resolution → separate final source/visual closure → next story**.

Minimum old-form set on every page:

`ணா / ணை / ணொ / ணோ / லை / ளை / றா / றொ / றோ / னா / னை / னொ / னோ`.

No global replacement, silent modernization or context-only correction.

## Story 1 — `பெற்ற பிள்ளையை விற்ற தாய்` — CLOSED

Workspace: `stories/petra-pillaiyai-vitra-thaai/`. Scans **7–28 / printed 5–26**. First pass 22/22, historical-glyph gate PASS, final source/visual closure PASS, 22/22 verified, 0 unresolved source/glyph items. Final audit: `stories/petra-pillaiyai-vitra-thaai/FINAL_SOURCE_VISUAL_AUDIT_2026-09-08.md`. Do not reopen without stronger evidence or explicit maintenance request.

## Story 2 — `காசா லேசா` — CURRENT DURABLE CHECKPOINT

Workspace: `stories/kaasa-lesa/`

Physical range:

- scans **29–40 / printed 27–38**;
- scan 29 opening display: `காசா லேசா`;
- later running header: `காசா லேசா!`;
- scan 40: terminal paragraph + star;
- scan 41: forward boundary opens `சீமான் வீட்டு சீக்காளி` and is excluded.

Activation / transcription state:

- fresh duplicate/canonical recheck before activation: **PASS — no existing canonical match**;
- route: **new canonical** controlled by this 1982 source range;
- first-pass transcription: **12/12 COMPLETE**;
- first-pass durable commit: `cd953e2e2d1ecd28fb242a1abf654ff2a4842c26`;
- page status: **12/12 `needs-review`**.

Historical-glyph gate:

- native/high-resolution reread: **12/12 COMPLETE**;
- gate: **PASS**;
- unresolved historical-glyph candidates: **0**;
- corrections synchronized from source pixels:
  - scan 30 `காலண காசு` → `காலணா காசு` (`ணா`);
  - scan 31 `வாரே` → `வாறே` (`றே` source identity);
  - scan 32 `ஊழில் ஒழிக்கவே` → `ஊழலை ஒழிக்கவே` (`லை`);
- source-odd scan 32 `ஒன்றுயின்` retained because pixels support it;
- scan 39 wordplay `காசாலேசா! காசாலே; நீ; சா!` retained at this gate;
- gate record: `stories/kaasa-lesa/HISTORICAL_GLYPH_GATE.md`.

**Important:** historical-glyph PASS does not make pages `verified`. The separate final source/visual closure has **not yet run**.

## Exact next activity — Story 2 final source/visual closure

1. fetch live `main` and preserve newer durable work;
2. read permanent guides, this handover, `NEXT_CHAT_PROMPT.md`, Story-2 README, metadata, page map, glyph gate, review queue and all 12 page records;
3. resolve the controlling PDF before source-pixel work;
4. directly reread scans **29–40** at native/high resolution for full phrase/clause/sentence fidelity, punctuation and spacing — not only historical glyphs;
5. verify all cross-page continuations and that no text is omitted or duplicated;
6. recheck scan 29 opening title distinction, scan 40 ending/star and scan 41 forward-boundary exclusion;
7. reconcile page records with `sections/kaasa-lesa.md`;
8. record any ordinary source/visual corrections separately from the already-closed historical-glyph gate;
9. only if all 12 pages close with zero unresolved source-text items, promote 12/12 to `verified`, create `FINAL_SOURCE_VISUAL_AUDIT_2026-09-08.md`, synchronize story/collection/root controls, and close Story 2;
10. **do not start Story 3 in the same activity**.

Do not start `நடுத்தெரு நாராயணி`; its `வெள்ளிக்கிழமை` gate remains unsatisfied.
