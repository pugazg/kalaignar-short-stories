# Stage 3 — Batch 1 historical Tamil glyph audit

Work: **தெருக்கூத்து**  
Controlling source: `TVA_BOK_0064193_நாடும்_நாடகமும்.pdf`  
Batch: scans **25–36 / printed 17–28**

## Method

- live `main` was re-fetched before the audit;
- all 12 Stage-2 page records were treated as the working transcription;
- all 12 controlling scans were reopened and checked directly;
- the audit followed `HISTORICAL_TAMIL_GLYPH_TRANSCRIPTION_GUIDE.md`;
- all 13 mandatory families were explicitly checked:
  `ணா / ணை / ணொ / ணோ / லை / ளை / றா / றொ / றோ / னா / னை / னொ / னோ`;
- character identity was judged from complete source words/phrases and repeated same-edition forms, not isolated strokes;
- no OCR, web copy, Wikisource, catalogue text, alternate edition, or contextual reconstruction was used;
- no modernization of spelling or grammar was permitted.

## Result

- scans audited: **12/12**
- mandatory families audited: **13/13**
- family disposition: **9 present / 4 absent**
- character-identity corrections: **0**
- unresolved historical-glyph clusters: **0**
- guessed readings: **0**
- page status after Stage 3: **needs-review 12/12**
- Stage 4 final independent source check: **NEXT**

## Batch-wide family disposition

| Family | Disposition | Representative direct-scan examples |
|---|---|---|
| `ணா` | **absent** | — |
| `ணை` | **present** | scan 25 `கண்ணை`; 26 `அணைக்க`; 33 `அணைத்தபடி`; 35 `ஆணையிட்டுள்ளான்` |
| `ணொ` | **absent** | — |
| `ணோ` | **absent** | — |
| `லை` | **present** | scan 25 `சோலைகள்`; 28 `மணிமேகலை`; 30 `நிலைமை`; 36 `தேயிலைத்` |
| `ளை` | **present** | scan 27 `மேனியளை`; 29 `வாளை`; 31 `வளைகிறீர்கள்`; 32 `வாளை` |
| `றா` | **present** | scan 26 `சென்றான்`; 28 `அமர்ந்திருக்கிறார்கள்`; 34 `சிரிக்கிறார்` |
| `றொ` | **present** | scan 32 `மென்றொரு`; 33 `என்றொரு` |
| `றோ` | **present** | scan 31 `சொல்லன்றோ` |
| `னா` | **present** | scan 26 `பாடினாள்`; 31 `ஆனால்`; 35 `தென்னாப்பிரிக்கா` |
| `னை` | **present** | scan 26 `புள்ளிமானை`; 35 `அன்னை`; 36 `பூனைக்குட்டி` |
| `னொ` | **absent** | — |
| `னோ` | **present** | scan 35 `போனோமே` |

## Page-level disposition

| Scan | Printed | Present mandatory families | Character-identity corrections | Unresolved clusters |
|---:|---:|---|---:|---:|
| 25 | 17 | `ணை / லை / ளை` | 0 | 0 |
| 26 | 18 | `ணை / ளை / றா / னா / னை` | 0 | 0 |
| 27 | 19 | `ணை / லை / ளை / னா / னை` | 0 | 0 |
| 28 | 20 | `ணை / லை / ளை / றா / னா` | 0 | 0 |
| 29 | 21 | `ளை / றா` | 0 | 0 |
| 30 | 22 | `லை / றா / னா / னை` | 0 | 0 |
| 31 | 23 | `ளை / றா / றோ / னா / னை` | 0 | 0 |
| 32 | 24 | `லை / ளை / றா / றொ` | 0 | 0 |
| 33 | 25 | `ணை / ளை / றா / றொ` | 0 | 0 |
| 34 | 26 | `லை / றா` | 0 | 0 |
| 35 | 27 | `ணை / லை / றா / னா / னை / னோ` | 0 | 0 |
| 36 | 28 | `லை / றா / னை` | 0 | 0 |

## Notable direct checks

- scan 29 `வாளை வீசியபடி` — the historical `ளை` identity in `வாளை` is directly supported;
- scan 32 `வீரனே வாளை எடு!` — the same `ளை` identity is independently repeated in the edition;
- scan 31 `சொல்லன்றோ` confirms the `றோ` family;
- scans 32–33 `மென்றொரு / என்றொரு` confirm `றொ`;
- scan 35 `போனோமே` confirms `னோ`.

No modern-lookalike misdecoding was found in the committed Stage-2 text.

## Stage-3 disposition

**COMPLETE / PASS — 12/12 pages; 13/13 mandatory families audited; 0 character-identity corrections; 0 unresolved glyph clusters.**

All page records remain `needs-review` until Stage 4.

## Exact next activity

Run **Stage 4 final independent source check** for scans **25–36 / printed 17–28**.

Reopen the complete batch fresh from the Stage-3 committed text and compare end to end against the controlling scan. Confirm:

- no omissions or duplications;
- all Stage-2 corrections remain correct;
- all Stage-3 family dispositions remain correct;
- punctuation, dialogue, song layout, scene headings and paragraphing are source-faithful;
- all physical joins and the scan-36 work ending are correct;
- no unresolved source-text or historical-glyph issue remains.

Promote pages to `verified` only if the final source check passes. Synchronize all controls, commit Stage 4, re-fetch live `main`, then stop before `சந்தனக்கிண்ணம்`.
