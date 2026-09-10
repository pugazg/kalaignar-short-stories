# HANDOVER — Kalaignar Short Stories Archive

## Repository

- repository: `pugazg/kalaignar-short-stories`
- branch: `main`
- **LIVE MAIN IS AUTHORITATIVE**
- permanent source-first guides remain in force

## Highest-priority active work — 1977 anthology full re-audit

Collection: `collections/1977-kalaignar-karunanidhiyin-sirukathaigal/`.

Controlling source: `TVA_BOK_0064142_கலைஞர்_கருணாநிதியின்_சிறுகதைகள்.pdf`

- first edition: **1977**
- physical scans: **260**
- bytes: **268,486,609**
- SHA-256: `853032661482eaccb26c083a38d7aa75c081362d33c963c63e37d088bf20acb3`
- exact match to registered repository source
- image-only controlling source
- do not commit the PDF

### User directive

This 37-story exercise is **comparison repair, not retranscription**. Existing repository Tamil is the baseline. Compare directly against source pixels; correct only source-proven mismatches. Preserve source spelling, punctuation, meaningful spacing, paragraphing, page boundaries and source marks. No duplicate full transcription, no global replacement, and no modernization from lexical expectation.

### Mandatory dual gates

Every story must independently pass:

1. **Gate A — source-fidelity comparison** of every physical story page;
2. **Gate B — Old Tamil Glyph verification**, independently reopening every physical page at high/native resolution and explicitly considering `ணா / ணை / ணொ / ணோ / லை / ளை / றா / றொ / றோ / னா / னை / னொ / னோ` plus other suspicious historical forms.

Current tracker state: **OPEN — 7 / 37 dual-gate complete**.

## Closed under the 2026 standard

- `புகழேந்தி` — scans **10–15** — Gate A/B PASS; **9 repairs / 0 unresolved**.
- `நளாயினி` — scans **16–23** — Gate A/B PASS; **15 repairs / 0 unresolved**.
- `சபலம்` — scans **24–30** — Gate A/B PASS; **6 repairs / 0 unresolved**.
- `ஆட்டக்காவடி` — scans **31–38** — Gate A/B PASS; **7 repairs / 0 unresolved**; `கருவிழியானை` retained source-close.
- `குப்பைத்தொட்டி` — scans **39–46** — Gate A/B PASS; **4 repairs / 0 unresolved**. Story-7-triggered regression: scan 40 apparent `போதுதானு` → `போதுதானா` (historical `னா`). Existing English required no additional rewrite.
- `சந்தனக்கிண்ணம்` — scans **47–56** — Gate A/B PASS; **3 repairs / 0 unresolved**; one meaning-sensitive English sentence synchronized.
- `சங்கிலிச்சாமி` — scans **57–68** — Gate A **12/12 PASS**, Gate B **12/12 PASS**, **6 repairs / 0 unresolved**. Repairs: `என்னு`→`என்னா`; `தவறுக`→`தவறாக`; `தானு?`→`தானா?`; `கூறினன்`→`கூறினான்`; `கொலைகாரனுக்கிவிட்டாயே`→`கொலைகாரனாக்கிவிட்டாயே`; `காட்டினன்`→`காட்டினான்`. Genuine `செவேன்னு` retained. English already conveyed the corrected meanings; prose rewrite **0**.

Do not reopen these seven stories from stale prompts unless genuinely new direct source evidence appears.

## Exact next activity — Story 8 `கங்கையின் காதல்`

Workspace: `stories/gangaiyin-kadhal/`.

Source range:

- physical scans: **69–72**
- printed pages: **60–63**
- legacy canonical page records: **4 / 4**
- scan **73** is the boundary witness opening Story 9 `தாய்மை`

Complete both gates in one story-bounded activity:

1. fetch live `main` and preserve newer durable work;
2. read source-processing / historical-glyph guides, collection controls, and all Story 8 controls/page records/assembly/audit/possible-error files;
3. Gate A — compare all 4 canonical records and assembled Tamil directly against scans 69–72;
4. Gate B — independently reopen all 4 physical pages at high/native resolution and check all mandatory historical families;
5. correct only source-proven mismatches individually; no retranscription, global replacement or modernization;
6. synchronize assembly, audit / possible-error / historical-glyph records and existing English only where meaning changes;
7. mark PASS only with Gate A 4/4 + Gate B 4/4 + 0 unresolved;
8. if PASS, advance tracker **7/37 → 8/37**, synchronize collection/root controls, commit, re-fetch live `main`, and stop/report.

Do **not** begin Story 9 `தாய்மை` in the same activity.

## 1976 `நளாயினி` exact-edition witness work — READY / DEFERRED

Source: `TVA_BOK_0065574_நளாயினி_1976.pdf`, fourth edition 1976, 78 scans, 164,748,566 bytes, SHA-256 `7297006fca435b07f8a4f0f564c254cf54c23892c63f5c870e79edac1cf1dd06`.

For duplicate stories: comparison-only; no new full transcription / no duplicate English. P2 scans **8–12** remains deferred while the 1977 37-story re-audit is the active priority.

Closed new-canonical 1976 stories remain closed: `நாட்டிய கலாராணி` and `மானம்` — Tamil + English PASS.

## Independent external hold

`நடுத்தெரு நாராயணி` remains controlled by the separate `வெள்ளிக்கிழமை` completion gate.
