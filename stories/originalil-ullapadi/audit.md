# தமிழ் மூலத் தணிக்கை — ஒரிஜினலில் உள்ளபடி

## Audit scope

- Controlling source: `TVA_BOK_0064142_கலைஞர்_கருணாநிதியின்_சிறுகதைகள்.pdf`
- Collection: **கலைஞர் கருணாநிதியின் சிறுகதைகள்**, முதல் பதிப்பு 1977
- Story range: scans **119–125** / printed pages **110–116**
- Page records: **7 / 7**
- Source PDF stored in GitHub: **No**

## Source-review method

All seven story scans were directly reviewed from the supplied controlling PDF. Native embedded page images at **3146×4826** were inspected, with enlarged full-span crops for source-sensitive Tamil, punctuation, dialogue, deliberate wordplay and physical joins. No contextual modernization or inferred correction was substituted for visible source text.

## Page disposition

| Printed page | Scan | Status | Boundary / key note |
|---:|---:|---|---|
| 110 | 119 | verified | story opening `ஒரிஜினலில் உள்ளபடி`; press-manager dialogue; source forms `போட்டாமல்`, `ஜாஸ்தியாச்சே` retained |
| 111 | 120 | verified | Kandasami reads the notice; old-form `திரெளபதி`, `எளனம்`, `அலக் கழியும்`; ends at `அலட்சியம்` |
| 112 | 121 | verified | completes `அலட்சியம் நிறைந்த வெறுப்பு`; Kandasami's accusation/plan; ends at `செட்டியாரின் தோளில்` |
| 113 | 122 | verified | completes `தோளில் போட்டுவிட்டான்`; notice order and printing; source `நாறு`; ends at `செட்டியார் உத்தரவுப்` |
| 114 | 123 | verified | completes `உத்தரவுப்படி`; public reaction; `‘லக்னம்’ தவறக்கூடாது`; Swami arrives |
| 115 | 124 | verified | altered notice exposed; `விபசாரம்` / `விபச்சாரம்` and `உடன் யாசிப்பார்கள்` wordplay preserved |
| 116 | 125 | verified | final confrontation and explanation; source forms `சித்தரிக்கப்பட்டிருக்கிறள்`, `காமக் காண்டா மிருகம்`, `பொறும்`; closing ornament |

Totals: **7/7 verified; 0 needs-review status pages; 0 blocked; 0 unresolved story text.**

## Cross-page audit

**PASS**

Explicit split continuations:

1. printed 111→112 / scans 120→121: `...“மகாகும்பாபிஷேகம்..........ம்......மட உலகம்......” அலட்சியம்` → `நிறைந்த வெறுப்பு அவன் முகத்தில் கோடுகளைக் கிழித்தது.`
2. printed 112→113 / scans 121→122: `...செட்டியாரின் தோளில்` → `போட்டுவிட்டான்.`
3. printed 113→114 / scans 122→123: `...செட்டியார் உத்தரவுப்` → `படி ‘பத்தாயிரம் நோட்டீசை’யும் ஊரெங்கும்...`

The 119→120, 123→124 and 124→125 boundaries were also visually checked and do not split a sentence/word. No page is omitted or duplicated.

## Story-boundary audit

- scan 119 / printed 110 opens `ஒரிஜினலில் உள்ளபடி`.
- scan 125 / printed 116 contains the final exchange, story ending and ornamental closing rule.
- scan 126 visibly opens **`பனங்குலை`**.
- Story 17 text included: **No**.

## Difficult-reading / human-review layer

Unusual but legible readings are retained in `POSSIBLE_ERRORS_FOR_REVIEW.md`; queue status is not proof of error. The final source-span recheck confirmed scan 123 `படி ‘பத்தாயிரம் நோட்டீசை’யும் ஊரெங்கும்...`. A source-faithfulness correction was also made before commit on scans 120 and 124: the scan prints old-form `திரெளபதி`, so the provisional normalized `திரௌபதி` was replaced everywhere in this workspace. Other enlarged checks include scan 120 `எளனம்` / `அலக் கழியும்`, scan 121 `வெங்கடாசலபதி கீர்த்தின்...`, scan 122 `நாறு`, scan 123 `‘லக்னம்’` and `உபன்யாசத்திற்காகச்`, scan 124 the deliberate `விபசாரம்` / `விபச்சாரம்` contrast, and scan 125 `சித்தரிக்கப்பட்டிருக்கிறள்` / `பொறும்`.

## Assembly gate

- scans represented: **7 / 7**
- scan order: **119 → 125**
- printed order: **110 → 116**
- duplicated pages: **none**
- omitted pages: **none**
- Story 17 included: **No**
- unresolved story markers: **0**

## Audit result

**PASS — ஒரிஜினலில் உள்ளபடி source range is fully transcribed and structurally source-complete for the current reading: 7/7 verified, 0 blocked, 0 unresolved story text, with a persistent human possible-error queue.**
