# NEXT CHAT PROMPT — 1977 anthology re-audit / `சுமந்தவள்` dual-gate

Continue in `pugazg/kalaignar-short-stories`, branch `main`. **LIVE MAIN IS AUTHORITATIVE.**

Observed live checkpoint when this prompt was refreshed: `0902ed35296436a2e005513d090e6618c4294e46` — `Advance anthology tracker through அமிர்தமதி`. If live `main` has advanced, preserve the newer durable state and do not roll back.

Controlling source: `TVA_BOK_0064142_கலைஞர்_கருணாநிதியின்_சிறுகதைகள்.pdf` — first edition 1977, 260 scans, 268,486,609 bytes, SHA-256 `853032661482eaccb26c083a38d7aa75c081362d33c963c63e37d088bf20acb3`. Image-only; do not commit it.

## Durable state

Collection tracker: **OPEN — 34 / 37 dual-gate complete**.

Stories **1–34 are CLOSED**. Most recent: `அமிர்தமதி`, scans **231–238 / printed 222–229** — Gate A **8/8 PASS**, Gate B **8/8 PASS**, **10 historical-glyph repairs / 0 unresolved**.

Key `அமிர்தமதி` corrections included `போகிறாயா`, `சொன்னாய்`, `பார்த்திருக்கிறாயா`, `வேறாகப்`, `பலவாறாக`, `அவனை அணைத்து`, `நன்றாயிருக்கிறது`, and `சொன்னாயே`. English required one sentence sync for explicit `அணைத்து`.

Do not reopen Stories 1–34 unless genuinely new direct source evidence appears.

## Exact next activity — `சுமந்தவள்`

- workspace: `stories/sumanthaval/`
- controlling 1977 scans: **239–249**
- printed pages: **230–240**
- canonical pages: **11/11**
- scan **250** is boundary witness opening Story 36 **`சித்தார்த்தன் சிலை`**
- Story 36 TOC title: **`சித்தார்த்தன்`**

### Critical edition rule

A 2009 fourth-edition witness has already been fully compared. It contains many editorial variants and a substantial epilogue absent from this 1977 edition. It is **not controlling**. Use it only to identify spans worth reopening; canonical changes require direct proof from the 1977 scans.

### Highest-priority controlling-source rechecks

1. scan **246 / printed 237** — 1977 canonical `சன சுரத்தை`; 2009 witness `ஈன குரத்தை`;
2. scan **240 / printed 231** — 1977 canonical `அவள் உள்ளத்தில்`; 2009 witness `அவா, உள்ளத்தில்`;
3. scan **245 / printed 236** — 1977 canonical `முழுங்கால்`; 2009 witness `முழங்கால்`;
4. scan **239 / printed 230** — 1977 canonical `திரு திருவென்று`; 2009 witness `துருதுருவென்று`.

Also reopen all remaining entries in `stories/sumanthaval/POSSIBLE_ERRORS_FOR_REVIEW.md`, including `அடுக்களை`, `அண்ணு`, `குழறல்`, `கர்ப்பவதி`, `கனிமரமென`, `மூனையளவு`, `மண்ணுக்கி`, `பெட்காபி`, `யெளவனத்தின்`, `அலறினள்`, and `எமை விட்டு எச்சில் இலையே!`.

Gate A: compare every scan 239–249 for wording, punctuation, meaningful spacing, paragraph/dialogue structure, page boundaries, closing ornament and exact joins.

Gate B: independently reopen all eleven pages and explicitly check `ணா / ணை / ணொ / ணோ / லை / ளை / றா / றொ / றோ / னா / னை / னொ / னோ`, plus faint vowel marks, ligatures and `ர/ற`, `ன/ண`, `ல/ள`.

Known physical joins include:
- 243→244: `செளந்தரியோ அந்த வீட்டு` → `மகராணிபோல...`;
- 244→245: `...அந்தக் குழந்தை அளித்த வேதனையால்` → `ஏற்கனவே...`;
- 247→248: `“ஆராரோ” பாடுவதும்` → `பிணிக்கு மருந்து தருவதும்...`.

Preserve the controlling 1977 ending on scan **249**. Do **not** import the 2009 epilogue.

If settled: apply only source-proven 1977 corrections; synchronize affected English and all controls; create/update the durable dual-gate record; advance **34/37 → 35/37** only with Gate A 11/11 + Gate B 11/11 + 0 unresolved; commit and re-fetch live `main`.

Do **not** begin Story 36 in the same activity.
