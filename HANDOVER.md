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
- image-only controlling source
- do not commit the PDF

### User directive

This 37-story exercise is **comparison repair, not retranscription**.

Use existing repository Tamil as the baseline. Compare directly against source pixels; correct only source-proven mismatches. Preserve source spelling, punctuation, meaningful spacing, paragraphs, page boundaries and source marks. No duplicate full transcription, no global replacement, and no modernization from lexical expectation.

### Mandatory dual gates

Every story must independently pass:

1. **Gate A — source-fidelity comparison** of every physical story page;
2. **Gate B — Old Tamil Glyph verification**, independently reopening every physical page at high/native resolution and explicitly considering `ணா / ணை / ணொ / ணோ / லை / ளை / றா / றொ / றோ / னா / னை / னொ / னோ` plus other suspicious historical forms.

A story is current PASS only after both gates pass, unresolved source/glyph count is zero, and all affected page records, assembled Tamil, audits/queues and existing English are synchronized.

Tracker: `collections/1977-kalaignar-karunanidhiyin-sirukathaigal/RE_AUDIT_2026.md`.

Current tracker state: **OPEN — 6 / 37 dual-gate complete**.

## Closed under the 2026 standard

| Story | Scans / printed | Gate A | Gate B | Repairs | Unresolved |
|---|---|---:|---:|---:|---:|
| `புகழேந்தி` | 10–15 / 1–6 | 6/6 PASS | 6/6 PASS | 9 | 0 |
| `நளாயினி` | 16–23 / 7–14 | 8/8 PASS | 8/8 PASS | 15 | 0 |
| `சபலம்` | 24–30 / 15–21 | 7/7 PASS | 7/7 PASS | 6 | 0 |
| `ஆட்டக்காவடி` | 31–38 / 22–29 | 8/8 PASS | 8/8 PASS | 7 | 0 |
| `குப்பைத்தொட்டி` | 39–46 / 30–37 | 8/8 PASS | 8/8 PASS | 3 | 0 |
| `சந்தனக்கிண்ணம்` | 47–56 / 38–47 | 10/10 PASS | 10/10 PASS | 3 | 0 |

### Latest closure — `சந்தனக்கிண்ணம்`

Workspace: `stories/santhana-kinnam/`.

Final 2026 state:

- Gate A: **PASS — 10/10**;
- Gate B: **PASS — 10/10**;
- source-proven canonical repairs: **3**;
- unresolved source readings: **0**;
- unresolved historical-glyph readings: **0**;
- scan 52 / printed 43: `கள்ளச்` → `கிள்ளச்`;
- scan 53 / printed 44: `தமிழ்த்தாய்கள்` → `தமிழ்த்தாய்களை`, with historical `ளை` directly resolved at high/native resolution;
- scan 53 / printed 44: `வந்து விட்டான என` → `வந்து விட்டான் என`;
- Tamil page records and assembly synchronized;
- possible-error queue fully closed;
- English synchronized: “keep speaking secret words to Kamala” → **“keep telling Kamala to pinch it.”**;
- durable story record: `stories/santhana-kinnam/RE_AUDIT_2026.md`.

Do not reopen any of the six closed stories from stale prompts unless genuinely new direct source evidence appears.

## Exact next activity — Story 7 `சங்கிலிச்சாமி`

Workspace: `stories/sangilichami/`.

Source range:

- physical scans: **57–68**
- printed pages: **48–59**
- existing legacy canonical page records: **12 / 12**

Complete both gates in one story-bounded activity:

1. fetch live `main` and preserve newer durable work;
2. read source-processing / historical-glyph guides, collection controls, and all `stories/sangilichami/` controls/page records/assembly/audit/possible-error files;
3. Gate A — compare all 12 existing page records and assembled Tamil directly against scans 57–68;
4. Gate B — independently reopen all 12 physical pages at high/native resolution and check all mandatory historical families;
5. correct only source-proven mismatches individually; no retranscription, global replacement or modernization;
6. synchronize assembly, audit / possible-error / historical-glyph records and existing English only where meaning changes;
7. mark PASS only with Gate A 12/12 + Gate B 12/12 + 0 unresolved;
8. if PASS, advance tracker **6/37 → 7/37**, synchronize collection/root controls, commit, re-fetch live `main`, and stop/report.

Do **not** begin Story 8 `கங்கையின் காதல்` in the same activity.

## 1976 `நளாயினி` exact-edition witness work — READY / DEFERRED

Source: `TVA_BOK_0065574_நளாயினி_1976.pdf`, fourth edition 1976, 78 scans, 164,748,566 bytes, SHA-256 `7297006fca435b07f8a4f0f564c254cf54c23892c63f5c870e79edac1cf1dd06`.

For duplicate stories: comparison-only; no new full transcription / no duplicate English.

`நளாயினி` P1 scans 3–7 has been adjudicated against the repaired 1977 canonical source. P2 scans **8–12** is technically ready but remains deferred while the 1977 37-story re-audit is the active priority.

Closed new-canonical 1976 stories remain closed:

- `நாட்டிய கலாராணி` — Tamil + English PASS;
- `மானம்` — Tamil + English PASS.

## Independent external hold

`நடுத்தெரு நாராயணி` remains controlled by the separate `வெள்ளிக்கிழமை` completion gate.
