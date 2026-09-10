# தமிழ் மூலத் தணிக்கை — புகழேந்தி

## Audit scope

- Controlling source: `TVA_BOK_0064142_கலைஞர்_கருணாநிதியின்_சிறுகதைகள்.pdf`
- Collection: **கலைஞர் கருணாநிதியின் சிறுகதைகள்**, முதல் பதிப்பு 1977
- Story range: scans **10–15** / printed pages **1–6**
- Page records: **6 / 6**
- 2026 comparison mode: **repair existing canonical Tamil; no retranscription**
- Source PDF stored in GitHub: **No**

## 2026 dual-gate result

**PASS — Gate A 6/6 / Gate B 6/6 / 9 canonical repairs / 0 unresolved source readings / 0 unresolved historical-glyph readings.**

Full correction provenance: [`RE_AUDIT_2026.md`](RE_AUDIT_2026.md).

## Page disposition

| Printed page | Scan | Gate A | Gate B | Repairs |
|---:|---:|---|---|---:|
| 1 | 10 | PASS | PASS | 1 |
| 2 | 11 | PASS | PASS | 2 |
| 3 | 12 | PASS | PASS | 2 |
| 4 | 13 | PASS | PASS | 2 |
| 5 | 14 | PASS | PASS | 0 |
| 6 | 15 | PASS | PASS | 2 |

Totals: **6/6 pages dual-gate PASS; 9 repairs; 0 unresolved**.

## Source-proven repairs

1. scan 10: `இது போன்ற விவரங்கள்` → `இது போன்ற விவரங்களை`;
2. scan 11: `ஆகவே அவனை மேதை` → `ஆகவே அவன் மேதை`;
3. scan 11: `புகழ்தரும் தீவலி` → `புகழ்தரும் தலைவலி` — historical `லை`;
4. scan 12: `தத்தரூபமாகச்` → `தத்ரூபமாகச்`;
5. scan 12: `அவனைப் போய்க் கேட்டார்` → `அவனைப் போய்க் கேட்பர்`;
6. scan 13: `வயித்துக்கிடக்கிறது` → `லயித்துக்கிடக்கிறது`;
7. scan 13: `யாரும் தொந்தரவு கொடுக்காமல் விருப்பத்திற்காகத் தனியாக` → `யாரும் தொந்தரவு கொடுக்காமலிருப்பதற்காகத் தனியாக`;
8. scan 15: `கால்ப் பணிவிடைகள்` → `காலைப் பணிவிடைகள்` — historical `லை`;
9. scan 15: `உன் கைகளை கண்களில்` → `உன் கைகளைக் கண்களில்`.

## Independent Old Tamil Glyph gate

All six physical pages were separately reopened at high/native resolution after the source-fidelity comparison. Mandatory families explicitly considered:

`ணா / ணை / ணொ / ணோ / லை / ளை / றா / றொ / றோ / னா / னை / னொ / னோ`

Two historical-`லை` defects were repaired (`தலைவலி`, `காலைப்`). The scan-14 candidate `காதற் கண்கள்` was independently rechecked and confirmed as the 1977 reading; the later `காதற் கணைகள்` form is not imported.

Historical-glyph unresolved count: **0**.

## Cross-page audit

**PASS**

1. printed 1→2: `அவனது பெயர் கூறவே` → `மக்கள் தயங்குவர்—...`;
2. printed 3→4: `“உங்கள் இலட்சியம்` → `கைகூடும் வரையில்...`;
3. printed 5→6: `திருமணமும்` → `வேண்டார்!”`.

The assembled Tamil layer preserves a source-scan marker at each physical boundary. Story 2 text is excluded.

## Unusual readings / former review queue

Every prior story-local possible-error candidate was revisited in the 2026 comparison and glyph passes. Confirmed errors were repaired. Source-supported unusual forms were retained, including `பாராட்டுப் படித்தது`, `அவனோர் பிடேல்டோ!`, `மணக்கும் அவன் நெஞ்சம்`, `மாட்டானும்!`, `காதற் கண்கள்`, `அவளோ, என் காலில் பட்ட உன் கரங்கள் முத்தமிடுகிறாள்!`, and `ஏறெடுத்தும் பாராமல்`.

The queue is now **CLOSED — 0 pending / 0 unresolved**. See `POSSIBLE_ERRORS_FOR_REVIEW.md`.

## Additional-witness comparison — 2009 fourth edition

The earlier Fourth Edition (March 2009) `16 கதையினிலே` witness remains useful provenance but is subordinate to the 1977 controlling scan. Direct 1977 reinspection adjudicated the high-value witness candidates:

- 2009 `தலைவலி` corroborated a true canonical defect in legacy 1977 transcription;
- 2009 `லயித்துக் கிடக்கிறது` exposed a true canonical defect; 1977 joined spacing `லயித்துக்கிடக்கிறது` is retained;
- 2009 `காலைப் பணிவிடைகள்` exposed a true canonical defect;
- 1977 `காதற் கண்கள்` versus 2009 `காதற் கணைகள்` is an edition difference;
- 1977 `மணக்கும்` versus 2009 `மனக்கும்` is an edition difference;
- 1977 `அவனோர் பிடேல்டோ!` versus 2009 `அவனொரு பிடேல்டோ!` is an edition difference.

No later-edition wording was silently imported.

## Assembly / translation gate

- `sections/pugazhendhi.md`: synchronized to all 9 repairs;
- source order: scans **10 → 15** / printed **1 → 6**;
- omitted / duplicated pages: **0 / 0**;
- existing English: synchronized only where repaired Tamil materially changed the meaning or grammar;
- Story 2 included: **No**.

## Audit result

**PASS — `புகழேந்தி` is CURRENT PASS / CLOSED under the 2026 dual-gate standard: Gate A 6/6, Gate B 6/6, 9 source-proven canonical repairs, 0 unresolved source readings, 0 unresolved historical-glyph readings.**
