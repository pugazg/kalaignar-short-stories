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
2. **Gate B — Old Tamil Glyph verification**, with each physical page independently reopened at high/native resolution and explicit consideration of:
   `ணா / ணை / ணொ / ணோ / லை / ளை / றா / றொ / றோ / னா / னை / னொ / னோ`.

Collection gate: `collections/1977-kalaignar-karunanidhiyin-sirukathaigal/OLD_TAMIL_GLYPH_REAUDIT_GATE.md`.

A story is current PASS only after both gates pass, unresolved source/glyph count is zero, and all affected page records, assembled Tamil, audits/queues and existing English are synchronized.

Tracker: `collections/1977-kalaignar-karunanidhiyin-sirukathaigal/RE_AUDIT_2026.md`.

Current tracker state: **OPEN — 2 / 37 dual-gate complete**.

## `நளாயினி` — 2026 RE-AUDIT CLOSED / PASS

Workspace: `stories/nalayini/`.

Source range: scans **16–23 / printed pages 7–14**.

Final re-audit state:

- Gate A: **PASS — 8/8**;
- Gate B: **PASS — 8/8**;
- source-proven canonical repairs: **15**;
- unresolved source readings: **0**;
- unresolved historical-glyph readings: **0**;
- canonical page records / Tamil assembly / possible-error queue / affected English: synchronized;
- 1976 P1 witness candidates: **8 canonical defects / 5 true edition variants / 0 unresolved**.

Do not reopen `நளாயினி` from stale prompts unless new direct source evidence appears.

## `புகழேந்தி` — 2026 RE-AUDIT CLOSED / PASS

Workspace: `stories/pugazhendhi/`.

Source range: scans **10–15 / printed pages 1–6**.

Final re-audit state:

- Gate A: **PASS — 6/6**;
- Gate B: **PASS — 6/6**;
- source-proven canonical repairs: **9**;
- unresolved source readings: **0**;
- unresolved historical-glyph readings: **0**;
- two historical-`லை` repairs: `தீவலி` → `தலைவலி`; `கால்ப் பணிவிடைகள்` → `காலைப் பணிவிடைகள்`;
- scan-14 `காதற் கண்கள்`: independently high-resolution confirmed as the controlling 1977 reading; 2009 `காதற் கணைகள்` is an edition difference;
- canonical page records, Tamil assembly, source metadata, audit, possible-error queue and affected English: synchronized;
- durable story record: `stories/pugazhendhi/RE_AUDIT_2026.md`.

Do not reopen `புகழேந்தி` from stale prompts unless new direct source evidence appears.

## Exact next activity — Story 3 `சபலம்` dual-gate re-audit

Workspace: `stories/sabalam/`.

Source range: scans **24–30 / printed pages 15–21**.

In one story-bounded activity:

1. fetch live `main` and preserve newer durable work;
2. read source-processing / historical-glyph guides, collection re-audit controls, and all `stories/sabalam/` controls/page records/assembly/audit/possible-error files;
3. Gate A — compare every existing `சபலம்` canonical page record and assembly directly against scans 24–30;
4. Gate B — independently reopen all seven physical pages at high/native resolution and check all mandatory historical families;
5. correct only source-proven mismatches individually; never global-replace or modernize;
6. synchronize assembly, audit / possible-error / historical-glyph records and existing English only where meaning changes;
7. mark PASS only with Gate A 7/7 + Gate B 7/7 + 0 unresolved;
8. if PASS, update tracker from **2/37 to 3/37**, synchronize collection/root controls, commit, re-fetch live `main`, and stop/report.

Do **not** begin Story 4 `ஆட்டக்காவடி` in the same activity.

## 1976 `நளாயினி` exact-edition witness work — READY / DEFERRED

Source: `TVA_BOK_0065574_நளாயினி_1976.pdf`, fourth edition 1976, 78 scans, 164,748,566 bytes, SHA-256 `7297006fca435b07f8a4f0f564c254cf54c23892c63f5c870e79edac1cf1dd06`.

For duplicate stories: comparison-only; no new full transcription / no duplicate English.

`நளாயினி` P1 scans 3–7 has been adjudicated against the repaired 1977 canonical source. P2 scans **8–12** is technically ready but remains deferred while the 1977 37-story re-audit is the active priority.

Closed new-canonical 1976 stories remain closed:

- `நாட்டிய கலாராணி` — Tamil + English PASS;
- `மானம்` — Tamil + English PASS.

## Independent external hold

`நடுத்தெரு நாராயணி` remains controlled by the separate `வெள்ளிக்கிழமை` completion gate.
