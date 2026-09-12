# HANDOVER — Kalaignar Short Stories Archive

## Repository

- repository: `pugazg/kalaignar-short-stories`
- branch: `main`
- **LIVE MAIN IS AUTHORITATIVE**
- refreshed durable closure checkpoint: `f980e80c556bc2cf76b1c08e0504e077b0b980ed` — `Close 1977 anthology dual-gate at 37 of 37`
- permanent source-first guides remain in force

## 1977 anthology — 2026 dual-gate programme

Collection: `collections/1977-kalaignar-karunanidhiyin-sirukathaigal/`.

Controlling source: `TVA_BOK_0064142_கலைஞர்_கருணாநிதியின்_சிறுகதைகள்.pdf`

- first edition: **1977**
- physical scans: **260**
- bytes: **268,486,609**
- SHA-256: `853032661482eaccb26c083a38d7aa75c081362d33c963c63e37d088bf20acb3`
- image-only controlling source
- source PDF must not be committed

### Governing method

This programme was **comparison repair, not retranscription**. Existing repository Tamil was the baseline. Every story independently required:

1. **Gate A — source-fidelity comparison** against controlling pixels;
2. **Gate B — independent Old Tamil Glyph verification** at native/high resolution, explicitly considering `ணா / ணை / ணொ / ணோ / லை / ளை / றா / றொ / றோ / னா / னை / னொ / னோ` plus other suspicious historical forms.

No global replacement, lexical modernization, or context-based silent correction was permitted.

## Durable final state

**CLOSED — 37 / 37 CURRENT PASS; 0 unresolved.**

- Stories **1–37** have Gate A PASS + Gate B PASS.
- Story scans **10–259 / printed pages 1–250** are closed under the 2026 standard.
- scan **260** is the independently verified anthology back cover.
- English layers affected by source repairs are synchronized.
- source PDF / renders / crops are not committed.
- do not reopen a closed story from a stale prompt unless genuinely new direct controlling-source evidence appears.

## Final story — `நுனிக்கரும்பு`

Workspace: `stories/nunikkarumbu/`

- scans **253–259 / printed 244–250**
- Gate A: **7/7 PASS**
- Gate B: **7/7 PASS**
- source-proven repairs: **2 punctuation repairs**
- unresolved source readings: **0**
- unresolved historical-glyph readings: **0**
- English synchronization: **2 punctuation-only changes; 0 prose/meaning changes**

Repairs:

1. scan **256 / printed 247**  
   `ஒண்ணுமில்லே!...என்ன` → **`ஒண்ணுமில்லே...என்ன`**
2. scan **258 / printed 249**  
   `டே, டே!` → **`டே டே!`**

Gate B required no canonical historical-glyph correction. Representative source-confirmed families included `புண்ணாகி` (`ணா`), `தன்னை` (`னை`), `களைப்புத்` (`ளை`), `சென்றார்` (`றா`), `சொன்னார்கள்` (`னா`), and `எண்ணை` (`ணை`).

Source-sensitive forms such as `சதிமிதிக்கும்`, `வதங்கவிலாச்சண்பகத்து`, `சாடை`, `நாறுவது நடன நிகழ்ச்சி`, `அத்தனைநாள் கடந்தவம்`, `முன்னேடி`, `கிறு கிறுக்க`, `இன்பபுரிக்கு`, `சாபங்`, `காலக்கடன்களை`, `கேட்டாமலே`, `அமுதா இருக்குதா?`, `சேச்சே!`, `பகல் விருந்து ரசிகுமா?`, `தணலான`, `அடுக்குளப்பக்கம்`, `வண்ணமொழிகேட்டு`, `பரவாயில்ல`, `இவனத் தெரியுமா?`, and `நம்பப் பயலா?` were directly reconfirmed and retained.

Structural closure:

- opening Bharathidasan verse remains a distinct three-line block;
- all six physical joins PASS;
- exact 257→258 split remains `...காட்சிகளைக் காட்டி உள்ளங்` → `களைக் கெடுத்து வைத்திருக்கிறார்கள் அல்லவா?`;
- scan 259 contains the ending and closing ornament;
- scan 260 is back cover only.

Durable story ledger: `stories/nunikkarumbu/RE_AUDIT_2026.md`.

## Next activity

**None inside the 1977 anthology dual-gate programme.**

Do not automatically begin another collection, witness, modernization, translation revision, republication, or post-anthology phase. Await explicit user direction. If a future chat resumes repository work, fetch live `main` first and preserve any newer durable state.
