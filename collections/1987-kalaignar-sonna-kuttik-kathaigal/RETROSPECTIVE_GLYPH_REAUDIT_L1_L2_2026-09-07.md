# Retrospective Historical-Glyph Re-audit — 2026-09-07

Controlling source: `TVA_BOK_0065566_கலைஞர்_சொன்ன_குட்டிக்_கதைகள்_1987.pdf`

This re-audit was opened after verified records were found to preserve modern visual look-alikes of historical Tamil type instead of decoding the underlying character identity required by `HISTORICAL_TAMIL_GLYPH_TRANSCRIPTION_GUIDE.md`.

## Controlling rule

Historical type is decoded to its correct modern Unicode identity. Source spelling, grammar, punctuation, compounds and spacing otherwise remain unchanged. The 13 minimum families are checked independently at native/high resolution:

`ணா / ணை / ணொ / ணோ / லை / ளை / றா / றொ / றோ / னா / னை / னொ / னோ`

## Confirmed corrections in this retrospective pass

| Scan | Story | Earlier transcription | Correct Unicode/source reading | Class |
|---:|---|---|---|---|
| 19 | கஜினி முகமதுவும் கவிஞர் பார்டோசியும் | `சொன்னுராம்` | `சொன்னாராம்` | historical `னா` |
| 22 | இரு நிகழ்வுகள் | `பேசினர்கள்` | `பேசினார்கள்` | historical `னா` |
| 25 | சாமியாரும் பூக்காரியும் | `நிலமையை` | `நிலைமையை` | historical `லை` |
| 25 | ஹஜ்ரத் அலியும் யூதனும் | `பேசினன்` | `பேசினான்` | historical `னா` |
| 26 | ஹஜ்ரத் அலியும் யூதனும் | `பின்னல்` | `பின்னால்` | historical `னா` |
| 26 | ஹஜ்ரத் அலியும் யூதனும் | `வினவினன்` | `வினவினான்` | historical `னா` |
| 27 | ஹஜ்ரத் அலியும் யூதனும் | `சகோதரார்கள்` | `சகோதரர்கள்` | ordinary source-text correction |
| 27 | புகழேந்திப் புலவர் கதை | `இல்லறவிழவிலே` | `இல்வாழ்விலே` | ordinary source-text correction |
| 28 | புகழேந்திப் புலவர் கதை | `மல்லிகையின் வெண் சங்கு வண்டே` | `மல்லிகையின் வெண் சங்கு வண்டூத` | ordinary source-text correction |
| 29 | மன மாற்றம் | `அவன் தவறிவிடுவானே` | `அவன்தவறிவிடுவானே` | source spacing/compound correction |

`அந்நிலை` on scan 26 was separately rechecked and remains **`அந்நிலை`**: its historical `லை` identity had already been encoded correctly.

Story 9 scan 19 also requires punctuation/spacing synchronization independently of the glyph correction: `வந்தது.—வந்தவர்கள்`, `கஜினி முகமது விடம்`, `பொற்காசுகளைத் தருவதென்று`, and source-joined `கவிஞர்பார்டோசியை`.

No global replacement is authorized. Every correction above was decided from the physical source pixels and same-edition type behaviour.
