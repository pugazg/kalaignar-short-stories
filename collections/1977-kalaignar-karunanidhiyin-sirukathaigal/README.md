# கலைஞர் கருணாநிதியின் சிறுகதைகள் — 1977 anthology source

Collection-level archival source for the 37 canonical short-story workspaces derived from **கலைஞர் கருணாநிதியின் சிறுகதைகள்**.

## Source snapshot

- printed title: **கலைஞர் கருணாநிதியின் சிறுகதைகள்**
- author: **கலைஞர் மு. கருணாநிதி**
- publisher: **தமிழ்க்கனி பதிப்பகம், சென்னை-28**
- edition: **முதல் பதிப்பு: 1977**
- file: `TVA_BOK_0064142_கலைஞர்_கருணாநிதியின்_சிறுகதைகள்.pdf`
- physical scans: **260**
- printed story pages: **1–250**
- stories: **37**
- bytes: **268,486,609**
- SHA-256: `853032661482eaccb26c083a38d7aa75c081362d33c963c63e37d088bf20acb3`
- source PDF committed: **No**

Pagination inside the story block is `scan = printed page + 9`: scan **10** = printed page **1**, scan **259** = printed page **250**, scan **260** = verified back cover.

## 2026 full source + Old Tamil Glyph re-audit

**OPEN — 10 / 37 CURRENT PASS.**

The exact 1977 source was reattached and byte identity matched the registered source. This programme is **comparison repair, not retranscription**. Existing canonical Tamil is the baseline.

Every story must independently pass:

1. **Gate A — source fidelity**, comparing every existing story page directly to controlling pixels;
2. **Gate B — Old Tamil Glyph**, independently reopening every physical page at high/native resolution and explicitly inspecting `ணா / ணை / ணொ / ணோ / லை / ளை / றா / றொ / றோ / னா / னை / னொ / னோ` plus other suspicious forms.

Rules: source-first, no global replacement, no lexical modernization, and no PASS with unresolved source/glyph candidates.

Tracker: [`RE_AUDIT_2026.md`](RE_AUDIT_2026.md).  
Gate definition: [`OLD_TAMIL_GLYPH_REAUDIT_GATE.md`](OLD_TAMIL_GLYPH_REAUDIT_GATE.md).

## Re-closed under the 2026 standard

- `புகழேந்தி` — scans **10–15** — Gate A/B PASS; **9 repairs / 0 unresolved**.
- `நளாயினி` — scans **16–23** — Gate A/B PASS; **15 repairs / 0 unresolved**.
- `சபலம்` — scans **24–30** — Gate A/B PASS; **6 repairs / 0 unresolved**.
- `ஆட்டக்காவடி` — scans **31–38** — Gate A/B PASS; **7 repairs / 0 unresolved**; `கருவிழியானை` reconfirmed source-close.
- `குப்பைத்தொட்டி` — scans **39–46** — Gate A/B PASS; **4 repairs / 0 unresolved**; Story-7-triggered historical-`னா` regression repaired `போதுதானு` → `போதுதானா`; English remains synchronized.
- `சந்தனக்கிண்ணம்` — scans **47–56** — Gate A **10/10 PASS**, Gate B **10/10 PASS**, **3 repairs / 0 unresolved**. Repairs: `கள்ளச்` → `கிள்ளச்`; `தமிழ்த்தாய்கள்` → `தமிழ்த்தாய்களை` with historical `ளை` directly resolved; `வந்து விட்டான என` → `வந்து விட்டான் என`. Meaning-sensitive English synchronized.
- `சங்கிலிச்சாமி` — scans **57–68** — Gate A **12/12 PASS**, Gate B **12/12 PASS**, **6 repairs / 0 unresolved**. Historical `றா/னா` corrections synchronized; English already conveyed the corrected meanings, so no prose rewrite was required.
- `கங்கையின் காதல்` — scans **69–72** — Gate A **4/4 PASS**, Gate B **4/4 PASS**, **2 repairs / 0 unresolved**.
- `தாய்மை` — scans **73–83** — Gate A **11/11 PASS**, Gate B **11/11 PASS**, **42 repairs / 0 unresolved**; English resynchronized.
- `தப்பிவிட்டார்கள்` — scans **84–91** — Gate A **8/8 PASS**, Gate B **8/8 PASS**, **12 repairs / 0 unresolved**; English prose rewrite 0.

Do not reopen these ten stories from stale prompts unless genuinely new direct source evidence appears.

## Exact next activity

Story 11 **`தப்பவில்லை`** — scans **92–101 / printed pages 83–92** — **NEXT**.

Complete Gate A **10/10** and independent Gate B **10/10**. Use scan **102** only as the boundary witness opening `ஆதரிக்கிறார்`. Advance to **11/37** only with zero unresolved; stop before Story 12.
## Legacy processing state

Before this re-audit, all **37 / 37** stories had canonical Tamil page records/assemblies and were recorded `verified` / audit PASS. Those artifacts remain the comparison baseline but do not by themselves satisfy current release confidence.

Complete order and scan/page mapping:

- `indexes/story-inventory.md`
- `indexes/scan-map.md`
- `RE_AUDIT_2026.md`

## Source-title distinctions

The anthology preserves these title differences and they must not be silently normalized:

1. TOC `புரட்சிப்படம்` ↔ opening `புரட்சிப் படம்`;
2. TOC `சித்தார்த்தன்` ↔ opening `சித்தார்த்தன் சிலை`.
