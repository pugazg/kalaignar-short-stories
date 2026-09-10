# HANDOVER — Kalaignar Short Stories Archive

## Repository

- repository: `pugazg/kalaignar-short-stories`
- branch: `main`
- **LIVE MAIN IS AUTHORITATIVE**
- permanent source-first guides remain in force

## Highest-priority active work — 1977 anthology full re-audit

Collection: `collections/1977-kalaignar-karunanidhiyin-sirukathaigal/`.

Controlling source:

`TVA_BOK_0064142_கலைஞர்_கருணாநிதியின்_சிறுகதைகள்.pdf`

- first edition: **1977**
- physical scans: **260**
- bytes: **268,486,609**
- SHA-256: `853032661482eaccb26c083a38d7aa75c081362d33c963c63e37d088bf20acb3`
- exact match to registered repository source
- do not commit the PDF

### User directive

This 37-story exercise is **comparison repair, not retranscription**.

Use existing repository Tamil as the baseline. Compare directly against source pixels; correct only source-proven mismatches. No duplicate full transcription, no global replacement, and no modernization from lexical expectation.

### Mandatory dual gates

Every story must independently pass:

1. **Gate A — source-fidelity comparison** of all physical story pages;
2. **Gate B — Old Tamil Glyph verification**, with each physical page independently reopened at high/native resolution and explicit consideration of `ணா / ணை / ணொ / ணோ / லை / ளை / றா / றொ / றோ / னா / னை / னொ / னோ`.

Collection gate: `collections/1977-kalaignar-karunanidhiyin-sirukathaigal/OLD_TAMIL_GLYPH_REAUDIT_GATE.md`.

A story is current PASS only after both gates pass, unresolved source/glyph count is zero, and all affected page records, assembled Tamil, audits/queues and existing English are synchronized.

Tracker: `collections/1977-kalaignar-karunanidhiyin-sirukathaigal/RE_AUDIT_2026.md`.

Current tracker state: **OPEN — 5 / 37 dual-gate complete**.

## Closed under the 2026 standard

### `நளாயினி`

- scans **16–23 / printed 7–14**
- Gate A **8/8 PASS**; Gate B **8/8 PASS**
- canonical repairs: **15**
- unresolved source / historical-glyph readings: **0 / 0**
- durable record: `stories/nalayini/RE_AUDIT_2026.md`

### `புகழேந்தி`

- scans **10–15 / printed 1–6**
- Gate A **6/6 PASS**; Gate B **6/6 PASS**
- canonical repairs: **9**
- unresolved source / historical-glyph readings: **0 / 0**
- durable record: `stories/pugazhendhi/RE_AUDIT_2026.md`

### `சபலம்`

- scans **24–30 / printed 15–21**
- Gate A **7/7 PASS**; Gate B **7/7 PASS**
- canonical repairs: **6**
- unresolved source / historical-glyph readings: **0 / 0**
- durable record: `stories/sabalam/RE_AUDIT_2026.md`

### `ஆட்டக்காவடி`

Workspace: `stories/aattakkavadi/`.

Source range: scans **31–38 / printed pages 22–29**.

Final re-audit state:

- Gate A: **PASS — 8/8**;
- Gate B: **PASS — 8/8**;
- source-proven canonical repairs: **7**;
- unresolved source readings: **0**;
- unresolved historical-glyph readings: **0**;
- scan 31: both `அவ்வளவு தான்` source-spacing forms restored;
- scan 32: `அவர்களே ஏமாற்றி விட்டால்` → `அவர்களை ஏமாற்றி விட்டால்`;
- scan 33: `பக்திக் காவடி யென்று` and exact `கனிமொழி!....நீ` restored;
- scan 36: quote punctuation restored to `கண்ணியவானு நீ?—” கனிமொழி`; high-risk `கருவிழியானை` independently reconfirmed as the controlling source reading and **not** normalized to `கருவிழியானான்`;
- scan 38: `செருகப் பட்டதுபோல்` restored;
- canonical pages, Tamil assembly, audit, closed possible-error queue, page map and English review synchronized;
- English prose rewrite required: **0**;
- durable story record: `stories/aattakkavadi/RE_AUDIT_2026.md`.

### `குப்பைத்தொட்டி`

Workspace: `stories/kuppai-thotti/`.

Source range: scans **39–46 / printed pages 30–37**.

Final re-audit state:

- Gate A: **PASS — 8/8**;
- Gate B: **PASS — 8/8**;
- source-proven canonical repairs: **3**;
- unresolved source readings: **0**;
- unresolved historical-glyph readings: **0**;
- scan 44: `அவசரியப் புத்தி` → `அலட்சியப் புத்தி`;
- scan 45: `சிக்கிரம்` → `சீக்கிரம்`;
- scan 45: `அட;` → `அட,`;
- difficult source forms including `போதுதானு`, `மனமனவென்று`, `மூன்றூறு`, `தூராற்றம்`, `வீதிப்பக்கம் வந்து உண்மைதான்`, and `போனேனோ` were independently reconfirmed rather than normalized;
- canonical pages, Tamil assembly, audit, closed possible-error queue, story re-audit record and affected English are synchronized;
- English prose rewrite required: **1** meaning-sensitive phrase (`அலட்சியப் புத்தி`);
- durable story record: `stories/kuppai-thotti/RE_AUDIT_2026.md`.

Do not reopen these closed stories from stale prompts unless genuinely new direct source evidence appears.

## Exact next activity — Story 6 `சந்தனக்கிண்ணம்` dual-gate re-audit

Workspace: `stories/santhana-kinnam/`.

Source range: scans **47–56 / printed pages 38–47**.

In one story-bounded activity:

1. fetch live `main` and preserve newer durable work;
2. read source-processing / historical-glyph guides, collection re-audit controls, and all `stories/santhana-kinnam/` controls/page records/assembly/audit/possible-error files;
3. Gate A — compare every existing `சந்தனக்கிண்ணம்` canonical page record and assembly directly against scans 47–56;
4. Gate B — independently reopen all ten physical pages at high/native resolution and check all mandatory historical families;
5. correct only source-proven mismatches individually; never global-replace or modernize;
6. synchronize assembly, audit / possible-error / historical-glyph records and existing English only where meaning changes;
7. mark PASS only with Gate A 10/10 + Gate B 10/10 + 0 unresolved;
8. if PASS, update tracker from **5/37 to 6/37**, synchronize collection/root controls, commit, re-fetch live `main`, and stop/report.

Do **not** begin Story 7 `சங்கிலிச்சாமி` in the same activity.

## 1976 `நளாயினி` exact-edition witness work — READY / DEFERRED

Source: `TVA_BOK_0065574_நளாயினி_1976.pdf`, fourth edition 1976, 78 scans, 164,748,566 bytes, SHA-256 `7297006fca435b07f8a4f0f564c254cf54c23892c63f5c870e79edac1cf1dd06`.

For duplicate stories: comparison-only; no new full transcription / no duplicate English.

`நளாயினி` P1 scans 3–7 has been adjudicated against the repaired 1977 canonical source. P2 scans **8–12** is technically ready but remains deferred while the 1977 37-story re-audit is the active priority.

Closed new-canonical 1976 stories remain closed:

- `நாட்டிய கலாராணி` — Tamil + English PASS;
- `மானம்` — Tamil + English PASS.

## Independent external hold

`நடுத்தெரு நாராயணி` remains controlled by the separate `வெள்ளிக்கிழமை` completion gate.
