# Retrospective Historical-Glyph Re-audit — 2026-09-07

Controlling source: `TVA_BOK_0065566_கலைஞர்_சொன்ன_குட்டிக்_கதைகள்_1987.pdf`

This re-audit was opened after verified records were found to preserve modern visual look-alikes of historical Tamil type instead of decoding the underlying character identity required by `HISTORICAL_TAMIL_GLYPH_TRANSCRIPTION_GUIDE.md`.

## Controlling rule

Historical type is decoded to its correct modern Unicode identity. Source spelling, grammar, punctuation, compounds and spacing otherwise remain unchanged.

Minimum independent families:

`ணா / ணை / ணொ / ணோ / லை / ளை / றா / றொ / றோ / னா / னை / னொ / னோ`

## Confirmed corrections / decisions

| Scan | Story | Earlier/apparent reading | Source-supported Unicode reading | Class |
|---:|---|---|---|---|
| 19 | Story 9 | `சொன்னுராம்` | `சொன்னாராம்` | historical `னா` |
| 22 | Story 10 `இரு நிழல்கள்` | `பேசினர்கள்` | `பேசினார்கள்` | historical `னா` |
| 25 | Story 12 | `நிலமையை` | `நிலைமையை` | historical `லை` |
| 25 | Story 13 | `பேசினன்` | `பேசினான்` | historical `னா` |
| 26 | Story 13 | `பின்னல்` | `பின்னால்` | historical `னா` |
| 26 | Story 13 | `வினவினன்` | `வினவினான்` | historical `னா` |
| 27 | Story 13 | `சகோதரார்கள்` | `சகோதரர்கள்` | ordinary source-text correction |
| 27 | Story 14 | `இல்லறவிழவிலே` | `இல்வாழ்விலே` | ordinary source-text correction |
| 28 | Story 14 | earlier quote reading | `மல்லிகையின் வெண் சங்கு வண்டூத` | ordinary source-text correction |
| 29 | Story 15 | historical-lookalike ambiguity | `அவனா!` | historical `னா` confirmed |
| 29 | Story 15 | `அவன் தவறிவிடுவானே` | `அவன்தவறிவிடுவானே` | source spacing |
| 32 | Story 16 | modern-lookalike forms | `விளங்கினான்`, `வாலிபனான`, `திரும்பினான்` | historical `னா` |
| 33 | Story 17 | apparent `இட்டானும்` | `இட்டானாம்` | historical `னா` |
| 34 | Story 18 | `பின்னலிருந்து` | `பின்னாலிருந்து` | historical `னா`, two occurrences |

`அந்நிலை` on scan 26 was separately rechecked and remains **`அந்நிலை`**.

Story 9 scan 19 punctuation/spacing was also resynchronized from the physical source. Story 10's direct banner was separately reread as **`இரு நிழல்கள்`**, replacing the earlier incorrect heading `இரு நிகழ்வுகள்`.

No global replacement was authorized or performed. Grammar and another edition were not used as proof.

## Closure

The retrospective gate is **CLOSED through scan 34**.

- L1 scans 5–19: reopened where necessary and reconciled
- L2 scans 20–34: all 15 physical scans independently checked
- unresolved retrospective glyph locations through scan 34: **0**

The same two-pass rule remains mandatory for L3 and all future historical-Tamil source work.
