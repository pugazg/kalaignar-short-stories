# தமிழ் மூலத் தணிக்கை — சபலம்

## Audit scope

- Controlling source: `TVA_BOK_0064142_கலைஞர்_கருணாநிதியின்_சிறுகதைகள்.pdf`
- Collection: **கலைஞர் கருணாநிதியின் சிறுகதைகள்**, முதல் பதிப்பு 1977
- Story range: scans **24–30** / printed pages **15–21**
- Page records: **7 / 7**
- Source PDF stored in GitHub: **No**
- 2026 re-audit record: [`RE_AUDIT_2026.md`](RE_AUDIT_2026.md)

## 2026 source-review method

This story was reopened as **comparison repair, not retranscription**. All seven existing canonical page records and the assembled Tamil were compared directly with the exact controlling source. Native **3146 × 4826** page images were used for difficult spans.

A separate independent Old Tamil Glyph pass then reopened every physical page and explicitly considered `ணா / ணை / ணொ / ணோ / லை / ளை / றா / றொ / றோ / னா / னை / னொ / னோ`, plus other old ligatures, faint marks and `ர/ற`, `ன/ண`, `ல/ள` confusions.

No outside edition or lexical expectation was allowed to overwrite the controlling pixels. No global replacement was used.

## Gate A — source fidelity

**PASS — 7 / 7 pages.**

Source-proven canonical repairs: **6**.

| Scan | Printed page | Repair |
|---:|---:|---|
| 25 | 16 | `அவ்வப்போது பற்றிய அக்கறைகள்` → `அலுப்பைப் பற்றிய அக்கறைகள்` |
| 28 | 19 | `துவண்டிருப்பவன்போல` → `துவண்டிருப்பவனைப்போல` |
| 28 | 19 | `பார்க்கவில்லை` → `பார்க்க வில்லை` |
| 28 | 19 | `அழுதிடும்` → `அழுதிடுங்` |
| 28 | 19 | `பார்த்திருந்தாலும்` → `பார்த்திருந்தாலுங்` |
| 30 | 21 | `மூட்டை முடிச்சுகளைக் தூக்கிக்கொண்டு` → `மூட்டை முடிச்சுகளைத் தூக்கிக்கொண்டு` |

Scans **24, 26, 27, 29** required no canonical wording correction.

## Gate B — independent historical-glyph audit

**PASS — 7 / 7 pages independently reopened at native/high resolution.**

- historical-family corrections: **1**
- scan 28 / printed 19: `துவண்டிருப்பவன்போல` → `துவண்டிருப்பவனைப்போல` — historical `னை`
- unexamined historical-family candidates: **0**
- unresolved historical-glyph readings: **0**

Representative verified family occurrences are recorded in `RE_AUDIT_2026.md`.

## Page disposition

| Printed page | Scan | Gate A | Gate B | Final status |
|---:|---:|---|---|---|
| 15 | 24 | PASS | PASS | verified |
| 16 | 25 | PASS — 1 repair | PASS | verified |
| 17 | 26 | PASS | PASS | verified |
| 18 | 27 | PASS | PASS | verified |
| 19 | 28 | PASS — 4 repairs | PASS — 1 historical repair | verified |
| 20 | 29 | PASS | PASS | verified |
| 21 | 30 | PASS — 1 repair | PASS | verified |

Totals:

- `verified`: **7 / 7**
- `needs-review`: **0**
- `blocked`: **0**
- unresolved source readings: **0**
- unresolved historical-glyph readings: **0**

## Cross-page audit

**PASS**

Verified physical continuations:

1. printed 15→16: `கழுத்தில் நிற்கச் சக்தி` → `யிழந்து தொங்கும் தலையை...`
2. printed 16→17: `“மூர்த்தி” என்று கணீரென்று உச்சரித்தது` → `குழந்தை.`
3. printed 17→18: `அந்தப் பெட்டியில்` → `இருந்தவர்கள் தூக்க மயக்கத்தில்...`
4. printed 18→19: scan 27 closes its paragraph; scan 28 opens the new `வண்டி...` paragraph.
5. printed 19→20: `ஜன்னல்` → `வழியே வீசியெறிந்தான்.`
6. printed 20→21: the station/child exchange continues directly to the concluding page.

Scan **31 / printed page 22** remains boundary witness beginning Story 4 `ஆட்டக்காவடி`; no Story 4 text is included.

## Visual / structural fidelity

Existing visual-fidelity PASS remains valid. The 2026 re-audit reconfirmed:

- scan 24 opening heading + long horizontal rule;
- scan 28 enlarged initial `வ`;
- scan 30 closing ornament;
- exclusion of running titles/page numbers and scan-26 gathering signature from story text.

## Possible-error queue

`POSSIBLE_ERRORS_FOR_REVIEW.md` has now been fully adjudicated and is **CLOSED — 0 pending / 0 unresolved**. Source-supported oddities such as `கணீரென்று`, `நடசத்திரத்துக்குக்`, `கையுங்களவுமாகப்`, `ஊற்றுவதாகயிருந்தது`, `அந்தப் பசலை`, `கன்னக் கதுப்பை`, and `நாலா புறமிருந்தும்` were retained rather than normalized.

## Assembly / translation synchronization

- `sections/sabalam.md`: synchronized to all six repairs;
- existing English: synchronized where a corrected Tamil reading changed meaning;
- `TRANSLATION_REVIEW.md`: synchronized;
- no duplicate/retranscribed Tamil or English layer created.

## Audit result

**PASS — சபலம் is CURRENT PASS / CLOSED under the 2026 dual-gate standard: Gate A 7/7 PASS, Gate B 7/7 PASS, 6 source-proven canonical repairs, 0 unresolved source readings, 0 unresolved historical-glyph readings.**
