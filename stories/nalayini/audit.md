# தமிழ் மூலத் தணிக்கை — நளாயினி

## Current audit status

**PASS — 2026 dual-gate re-audit complete.**

- controlling source: `TVA_BOK_0064142_கலைஞர்_கருணாநிதியின்_சிறுகதைகள்.pdf`
- edition: **முதல் பதிப்பு: 1977**
- source scans: **16–23**
- printed pages: **7–14**
- exact source SHA-256: `853032661482eaccb26c083a38d7aa75c081362d33c963c63e37d088bf20acb3`
- Gate A source-fidelity comparison: **PASS — 8/8**
- Gate B independent Old Tamil Glyph verification: **PASS — 8/8**
- source-proven canonical repairs: **15**
- unresolved source readings: **0**
- unresolved historical-glyph readings: **0**

This 2026 audit supersedes the earlier source PASS for current release confidence. The work was a direct source-vs-existing-repository comparison, **not a retranscription**.

## Source-proven repairs

| Scan | Earlier repository reading | Correct 1977 source reading |
|---:|---|---|
| 16 | `கையில் ஒரு கூடையுடன்` | `தலையிலே ஒரு கூடையுடன்` |
| 17 | `என்னே ஏன்` | `என்னை ஏன்` |
| 17 | `கூடவிட்டு` | `கூடுவிட்டு` |
| 17 | `போடமாட்டேன்` | `போட்டமாட்டேன்` |
| 17 | `வில மதிக்க` | `விலை மதிக்க` |
| 17 | `கோமானத் தாமரையெனும்` | `கோமளத் தாமரையெனும்` |
| 17 | `தாசிநாதீனத்தொழு!` | `காசிநாதனைத்தொழு!` |
| 17 | `கண்ணிகையின்` | `கணிகையின்` |
| 18 | `வலிக்குந்த உடம்பை` | `வலிமிகுந்த உடம்பை` |
| 18 | `கேட்டும் ஓவியம்` | `கேட்கும் ஓவியம்` |
| 18 | `கூவினார்` | `கூவினர்` |
| 19 | `கண்ணாடை காட்டினாள்` | `கண்ஜாடை காட்டினாள்` |
| 19 | `அண்டெடுத்து` | `அணைத்தெடுத்து` |
| 22 | `குறைத்துக்கொண்டிருக்கட்டும்` | `குரைத்துக்கொண்டிருக்கட்டும்` |
| 22 | `உற்சாகமில்லை` | `உற்சாக மில்லை` |

No source-fidelity correction was required on scans **20, 21, or 23**.

## Gate B — Old Tamil Glyph re-audit

Every physical page was independently reopened at high/native-resolution and the mandatory families were explicitly considered:

`ணா / ணை / ணொ / ணோ / லை / ளை / றா / றொ / றோ / னா / னை / னொ / னோ`

Gate-B character-identity repairs included:

1. scan 17 `வில` → `விலை` — `லை` family;
2. scan 19 `அண்டெடுத்து` → `அணைத்தெடுத்து` — `ணை` family;
3. scan 17 `கோமானத்` → `கோமளத்` — additional faint/old character distinction;
4. scan 22 `குறைத்துக்கொண்டிருக்கட்டும்` → `குரைத்துக்கொண்டிருக்கட்டும்` — `ற` / `ர` distinction.

**Gate B PASS — 0 unresolved.**

## Rechecked source-odd readings retained

The controlling 1977 scan directly supports, among others:

- `வரவிழைந்த`, `சோபிதம்`, `விசாரத்தைக்`;
- scan 17 `மெளத் கல்யர்`, `தவம் புரியவு மல்ல`, `நயனவல்லித்ததை`;
- scan 18 joined `மெளத்கல்யர்`, `வண்ணேயாளர்`, `எடெமுது வோர்`, `சுருதிவிட்ட`, `காமக்கிறுக்கு`;
- `அம்சதூளிகா`, `கற்புக் கரசியின்`;
- `க்ஷமித்துவிடு`, `புண்ய வதியையும்`, `எண்ணுதெல்லாம்`;
- `தணலிற் புழுவாய்த்`, `வீணகானம்`, `விரகதாபத்தை`, plus source variation `பதி பக்தி` / `பதிபக்தி`;
- `அலட்சியப் படுத்தினேன்`, `அந்த வார்த்தின் காரணமாக`, `குட்டம் பிடித்தவன்`, `பதிவிரதை`, `திரெளபதியாகப்`;
- final `புனர் ஜென்மம்`, `பூரிப்புடன்`, `இன்பகீதம்`, and note `திரெளபதையாகப்`.

These are retained because source pixels support them; they are not modernized from lexical expectation.

## Cross-page and structure gate

**PASS.** The five physical continuations were checked on both sides:

1. 16→17: `கால்` + `பாகத்துக்குமேல்...`
2. 18→19: `தனக்குத்` + `தானே ஆச்சரியப்பட்டுக் கொண்டாள்.`
3. 19→20: unfinished Ulaga quotation + `க்ஷமித்துவிடு நளாயினி!...`
4. 20→21: `காணப்படு` + `கிறார்கள்.`
5. 22→23: `“இதயா! இது உண்மையா?”` + `“பொய் இல்லை!...”`

The opening rule, scan-20 enlarged paragraph initial, scan-23 separator, separate printed `குறிப்பு :—`, and closing ornament remain represented. Story 3 `சபலம்` is excluded.

## Assembly and English synchronization

- canonical Tamil assembly: **synchronized after all 15 repairs**;
- possible-error queue: **reconciled / 0 pending source candidates**;
- existing English: **synchronized where repaired Tamil changed meaning**;
- 1976 comparison candidates: **adjudicated against the controlling 1977 source**.

## Final result

**PASS — `நளாயினி` is current-source complete under the 2026 dual-gate standard: Gate A 8/8 PASS, Gate B 8/8 PASS, 15 canonical repairs, 0 unresolved source/glyph readings.**
