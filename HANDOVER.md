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
- each 1982 story: **first pass → dedicated historical-glyph gate → separate final source/visual closure → next story**.

## Cross-project hold

`நடுத்தெரு நாராயணி` remains **BLOCKED** while `வெள்ளிக்கிழமை` is incomplete in `pugazg/kalaignar-novels`.

## ACTIVE — 1982 `முடியாத தொடர்கதை`

Source: `TVA_BOK_0065572_முடியாத_தொடர்கதை.pdf` — **95 scans**, **194,350,272 bytes**, SHA-256 `d69034c5374c6c1604ddeb6d8e034c4410ae0d58201f2dd1608edd0e6d8cfd41`, first edition September 1982, image-only; do not commit PDF.

Stories 1–5 are **PASS / CLOSED**. Story 6 `முடியாத தொடர்கதை` occupies scans **59–93 / printed 57–91**.

### Story 6 durable state

- first-pass transcription: **35/35 COMPLETE**;
- page status: **35/35 `needs-review`**;
- Historical Tamil Glyph Gate: **PASS — 35/35; 11 total corrections / 0 unresolved**;
- `ஸ்பரிசிக்கப்பட்டு` is retained as printed Tamil; later English sense: **touched / was touched**;
- final source/visual closure: **IN PROGRESS — F1–F6 PASS, 6/7 batches complete**;
- F1 scans **59–63 / pp.57–61**: **PASS — 3 corrections / 0 unresolved**;
- F2 scans **64–68 / pp.62–66**: **PASS — 8 corrections / 0 unresolved**;
- F3 scans **69–73 / pp.67–71**: **PASS — 30 corrections / 0 unresolved**;
- F4 scans **74–78 / pp.72–76**: **PASS — 18 corrections / 0 unresolved**;
- F5 scans **79–83 / pp.77–81**: **PASS — 19 corrections / 0 unresolved**;
- F6 scans **84–88 / pp.82–86**: **PASS — 12 new corrections / 0 unresolved**;
- F7 scans **89–93 / pp.87–91**: **NEXT**;
- F6 key recoveries include scan 87 `பேசினான்`, `அவளது, குரல்வளையை`, `நெரித்து விடலாமா`, source quote/hyphen punctuation; scan 88 `அமுதமாக` (2 occurrences), `எங்களை வெறுப்போடு`, and the page-end join piece `நோக்`;
- the already-established scan-88 historical reading `பேசினாள்` is now synchronized in the assembled derivative;
- F6 joins 83→84, 85→86, 86→87, 87→88 passed; touching 88→89 `நோக் / கினான்` → `நோக்கினான்` passed using scan 89 only as the forward witness;
- assembled Tamil is synchronized through F6; previously established corrective readings on scans 89–92 remain to be synchronized when F7 reaches them;
- English: **not started**.

Final-closure ledger: `stories/mudiyatha-thodarkathai/FINAL_SOURCE_VISUAL_PROGRESS.md`.
Latest batch record: `stories/mudiyatha-thodarkathai/FINAL_SOURCE_VISUAL_BATCH_F6_084_088.md`.

## Five-scan final-closure rule

Process and commit **exactly 5 physical scans per iteration**:

1. F1 59–63 — **PASS**
2. F2 64–68 — **PASS**
3. F3 69–73 — **PASS**
4. F4 74–78 — **PASS**
5. F5 79–83 — **PASS**
6. F6 84–88 — **PASS**
7. F7 89–93 — **NEXT**

For each batch: native/high-resolution reread → ordinary wording/punctuation/spacing/page-boundary corrections → synchronize affected derivative text → update progress ledger + handover + next-chat prompt → **commit before starting the next batch**.

Keep all pages `needs-review` during partial batches. After F7 passes with zero ordinary source issues, perform the story-wide final closure and promote all 35 pages to `verified` together.

## Exact next activity — F7 only

Process **scans 89–93 / printed 87–91 only**. Recheck every word, punctuation/spacing choice and all physical joins in/touching the range. Reconfirm 88→89 from the F7 side; close 89→90 `சாமி / யார்` and 92→93 `ஆண்டுகளா / யிற்று`; verify scan 93 terminal star and use scan 94 only as the excluded forward-boundary witness. Apply only source-supported corrections, preserve source-odd forms, synchronize the assembled derivative including already-established scan-89–92 corrective readings when reached, update controls, and **commit F7 before story-wide promotion**.

Do not start `நடுத்தெரு நாராயணி`; its `வெள்ளிக்கிழமை` gate remains unsatisfied.
