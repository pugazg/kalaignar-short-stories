# NEXT CHAT PROMPT — 1977 anthology re-audit / `நுனிக்கரும்பு` dual-gate

Continue in `pugazg/kalaignar-short-stories`, branch `main`. **LIVE MAIN IS AUTHORITATIVE.**

Observed live checkpoint when this prompt was refreshed: `0a30887b7232b70b6f985d8d0bdba742f4d75cb1` — `Close சித்தார்த்தன் சிலை 2026 dual-gate`. If live `main` has advanced, preserve the newer durable state and do not roll back.

Controlling source: `TVA_BOK_0064142_கலைஞர்_கருணாநிதியின்_சிறுகதைகள்.pdf` — first edition 1977, 260 scans, 268,486,609 bytes, SHA-256 `853032661482eaccb26c083a38d7aa75c081362d33c963c63e37d088bf20acb3`. Image-only; do not commit it.

## Durable state

Collection tracker: **OPEN — 36 / 37 dual-gate complete**.

Stories **1–36 are CLOSED**. Most recent: `சித்தார்த்தன் சிலை` (TOC `சித்தார்த்தன்`), scans **250–252 / printed 241–243** — Gate A **3/3 PASS**, Gate B **3/3 PASS**, **1 repair / 0 unresolved**.

Story 36 repair:

- scan **250 / printed 241**: legacy `அந்த வானத்துச்` → source **`அந்தி வானத்துச்`**.

All other source-sensitive forms were reconfirmed, including `ஒளி!,`; the TOC/opening-title variance remains preserved; the 251→252 split is intact. English was synchronized from “a sky” to “the evening sky”. Scan **253** independently opens Story 37.

Do not reopen Stories 1–36 unless genuinely new direct source evidence appears.

## Exact next activity — `நுனிக்கரும்பு`

- workspace: `stories/nunikkarumbu/`
- scans: **253–259**
- printed pages: **244–250**
- canonical pages: **7/7**
- scan **260** is the anthology back-cover boundary witness

Before changing anything, read the project processing guide, historical-glyph guide, root handover/prompt, collection re-audit/gate/inventory/scan-map, and all Story 37 controls/page records/assembly/English review.

Gate A: compare all seven page records and assembly directly against scans 253–259 for wording, punctuation, meaningful spacing, paragraph/dialogue structure, the opening verse, physical joins and ending furniture.

Gate B: independently reopen all seven scans at native/high resolution and explicitly check `ணா / ணை / ணொ / ணோ / லை / ளை / றா / றொ / றோ / னா / னை / னொ / னோ`, plus faint marks, ligatures and `ர/ற`, `ன/ண`, `ல/ள` ambiguity.

### Source-sensitive queue

| Scan | Printed | Source-close reading / point | Review note |
|---:|---:|---|---|
| 253 | 244 | opening verse `சதிமிதிக்கும்`, `வதங்கவிலாச்சண்பகத்து`, `சாடை` | preserve source verse; no silent regularization |
| 253 | 244 | `நாறுவது நடன நிகழ்ச்சி` | unusual source wording retained |
| 254 | 245 | `அத்தனைநாள் கடந்தவம்`, `முன்னேடி` | source-close forms retained |
| 255 | 246 | `கிறு கிறுக்க`, `இன்பபுரிக்கு`, `சாபங்`, `காலக்கடன்களை` | source wording/spelling retained |
| 256 | 247 | `கேட்டாமலே`, `அமுதா இருக்குதா?`, `சேச்சே!` | colloquial/source forms retained |
| 257 | 248 | `பகல் விருந்து ரசிகுமா?`, `தணலான`, `அடுக்குளப்பக்கம்` | source-close forms retained |
| 257→258 | 248→249 | `உள்ளங்` → `களைக்` | exact physical split forms `உள்ளங்களைக்` |
| 258 | 249 | `வண்ணமொழிகேட்டு`, `பரவாயில்ல`, `இவனத் தெரியுமா?`, `நம்பப் பயலா?` | source wording retained |
| 259 | 250 | closing ornament | canonical convention `◆ ◆ ◆` |

High-value structural checks:

- preserve the opening Bharathidasan verse as a distinct three-line block;
- preserve all six physical joins with no omission/duplication;
- exact 257→258 split: `...காட்சிகளைக் காட்டி உள்ளங்` → `களைக் கெடுத்து வைத்திருக்கிறார்கள் அல்லவா?`;
- 258→259 carries the child-address sequence into the final `தாத்தா` reversal;
- scan 259 contains the story ending and closing ornament;
- use scan **260** only as the anthology back-cover boundary witness.

If settled: apply only source-proven corrections; synchronize Tamil/controls and affected English; create/update durable `RE_AUDIT_2026.md`; advance **36/37 → 37/37** only with Gate A 7/7 + Gate B 7/7 + 0 unresolved; update collection/root controls to full closure; commit and re-fetch live `main`. Do not start a separate post-anthology activity in the same iteration.
