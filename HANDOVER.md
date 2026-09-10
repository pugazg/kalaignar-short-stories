# HANDOVER — Kalaignar Short Stories Archive

## Repository

- repository: `pugazg/kalaignar-short-stories`
- branch: `main`
- live `main` is authoritative
- permanent source-first guides remain in force

## Highest-priority active work — 1977 anthology full re-audit

Collection: `collections/1977-kalaignar-karunanidhiyin-sirukathaigal/`.

Controlling source supplied again by user:

`TVA_BOK_0064142_கலைஞர்_கருணாநிதியின்_சிறுகதைகள்.pdf`

Raw-file identity is an exact match to the registered source:

- first edition: **1977**
- physical scans: **260**
- bytes: **268,486,609**
- SHA-256: `853032661482eaccb26c083a38d7aa75c081362d33c963c63e37d088bf20acb3`
- PDF must not be committed

### Why all 37 stories are reopened

A definite repository transcription defect has been confirmed from the controlling 1977 source in `நளாயினி`, scan **17 / printed page 8**:

- repository: `தாசிநாதீனத்தொழு!`
- source: `காசிநாதனைத்தொழு!`

Therefore the earlier 37/37 `verified` / `audit PASS` state is now legacy history only. The user explicitly authorized a full source-vs-repository re-audit of all 37 stories.

**No retranscription.** Existing repository Tamil is the comparison baseline.

Tracker: `collections/1977-kalaignar-karunanidhiyin-sirukathaigal/RE_AUDIT_2026.md`.

Current state: **OPEN — 0 / 37 stories dual-gate complete**.

### Mandatory dual gates

Every story must independently pass both:

1. **Gate A — source-fidelity comparison**
   - compare every existing page record / assembly span directly to the 1977 source;
   - correct source-proven word, punctuation, spacing, paragraph, boundary and source-mark mismatches;
   - no normalization, no full retranscription.

2. **Gate B — Old Tamil Glyph verification**
   - separate high/native-resolution re-open of every physical page;
   - explicitly check `ணா / ணை / ணொ / ணோ / லை / ளை / றா / றொ / றோ / னா / னை / னொ / னோ`;
   - follow `collections/1977-kalaignar-karunanidhiyin-sirukathaigal/OLD_TAMIL_GLYPH_REAUDIT_GATE.md`;
   - no global replacement; no spelling modernization.

A story is current PASS only after both gates close, all corrections are applied, assembled Tamil / audits / possible-error records are synchronized, and any affected existing English is corrected.

## Active target — `நளாயினி`

Canonical workspace: `stories/nalayini/`.

1977 source range: scans **16–23 / printed pages 7–14**.

Incident-priority state:

- earlier legacy status: 8/8 verified / audit PASS;
- current Gate A: **REOPENED / not yet complete**;
- current Gate B: **REOPENED / not yet complete**;
- one confirmed canonical defect already proven: `தாசிநாதீனத்தொழு!` → source `காசிநாதனைத்தொழு!`;
- other high-value candidates exposed by the 1976 witness must be checked against this 1977 source before they are called edition variants: `வலி மிகுந்த`, `அவன்/அவள்`, `கண்ஜாடை/கண்ணாடை`, `அணைத்தெடுத்து/அண்டெடுத்து`.

## Exact next activity

Complete the **full `நளாயினி` 1977 re-audit in one story-bounded activity**:

1. fetch live `main`;
2. read `SHORT_STORY_PROCESSING_GUIDE.md`, `HISTORICAL_TAMIL_GLYPH_TRANSCRIPTION_GUIDE.md`, collection `RE_AUDIT_2026.md`, `OLD_TAMIL_GLYPH_REAUDIT_GATE.md`, this handover, `NEXT_CHAT_PROMPT.md`, and `stories/nalayini/` controls;
3. Gate A — compare scans 16–23 directly against the existing 8 canonical page records and assembled Tamil; record/correct every source-proven mismatch;
4. Gate B — independently reopen scans 16–23 at high/native resolution and complete the mandatory old-glyph audit;
5. synchronize page records, assembled Tamil, story audit / possible-error queue, and any affected English;
6. update `stories/nalayini/witnesses/1976-nalayini/VARIANT_COMPARISON.md` so supposed 1976 variants that are actually canonical transcription defects are reclassified;
7. mark both re-audit gates PASS only if 8/8 pages close with zero unresolved source/glyph issues;
8. update collection tracker and root controls;
9. commit and stop/report.

Do not begin `புகழேந்தி` in the same activity. After `நளாயினி` closes, the re-audit order is `புகழேந்தி`, then Stories 3–37 in anthology order.

## 1976 `நளாயினி` comparison extension — PAUSED behind 1977 canonical re-audit

Controlling source: `TVA_BOK_0065574_நளாயினி_1976.pdf` — 78 scans, 164,748,566 bytes, fourth edition 1976, SHA-256 `7297006fca435b07f8a4f0f564c254cf54c23892c63f5c870e79edac1cf1dd06`.

Closed new-canonical stories remain closed:

- `நாட்டிய கலாராணி` — Tamil + English PASS;
- `மானம்` — Tamil + English PASS.

For duplicate stories the user's comparison-only directive still applies: **no additional full transcription and no duplicate English**.

`நளாயினி` P1 1976 scans 3–7 had 13 apparent differences, but their classification is now provisional until the controlling 1977 canonical source is re-audited. At least one (`காசிநாதனைத் தொழு!`) has already proved to be a repository transcription defect rather than an edition variant.

Do not resume 1976 scans 8–12 comparison until the 1977 `நளாயினி` dual-gate re-audit closes.

## Independent external hold

`நடுத்தெரு நாராயணி` remains controlled by the separate `வெள்ளிக்கிழமை` completion gate.
