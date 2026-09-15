# NEXT CHAT PROMPT — சீரழித்த சிரிப்பு! / Stage 4 final source check

Continue in `pugazg/kalaignar-short-stories`, branch `main`. **LIVE MAIN IS AUTHORITATIVE.**

## Active canonical

`stories/seerazhitha-sirippu/`

Controlling source:

`TVA_PRL_0033125_காஞ்சி_பொங்கல்_மலர்_1966.pdf`

- publication: **காஞ்சி — பொங்கல் மலர்**
- year: **1966**
- story scans: **101–102 / printed 91–92**
- scan 103: separate `அடிமைகள்`
- source pixels control; no OCR/web/Wikisource/alternate-source authority

## Durable state

- source intake: **COMPLETE**
- Stage 1: **COMPLETE 2/2**
- Stage 2 ordinary visual fidelity: **COMPLETE / PASS — 27 authoritative corrections**
  - scan 101: **15**
  - scan 102: **12**
- former Stage-2 30-correction count: **SUPERSEDED**
- Stage-2 historical-glyph regressions retracted: **3**
- Stage-2 unresolved ordinary-fidelity readings: **0**
- Stage 3 historical Tamil glyph corrective re-audit: **COMPLETE / PASS 2/2**
- Stage-3 character-identity corrections: **4**
  - scan 101: **2**
  - scan 102: **2**
- Stage-3 unresolved glyph clusters: **0**
- both page records: **needs-review**
- verified pages: **0/2**

Corrective Stage-3 readings that must not regress:

- `கடன்காரனாம்` — historical `னா`
- `ஆடைகளை அணிவிக்கட்டுமா?` — historical `ளை`
- `நடத்தினாள்` — historical `னா`
- final `அவளை வாழவிடாமல் செய்த...` — historical `ளை`

Durable records:
- `stories/seerazhitha-sirippu/STAGE2_BATCH_001.md`
- `stories/seerazhitha-sirippu/HISTORICAL_GLYPH_GATE.md`

The boxed scan-102 `முகப்பில்:` poem remains excluded as non-story matter. The scan 101→102 `வேதனைச் / சிலையானாள்` continuation remains PASS.

## Exact next activity

Perform **Stage 4 final independent source check** for scans **101–102 / printed 91–92**.

1. fetch live `main`;
2. reopen both source scans directly and reread the complete story independently;
3. verify wording, omission/duplication, punctuation, source spacing, quotation and paragraph boundaries;
4. explicitly recheck the four corrective historical-glyph readings above against the pixels; do not revert them by modern visual resemblance;
5. verify scan-101 illustrated-title / multi-column reading order;
6. verify scan 101→102 `வேதனைச் / சிலையானாள்` continuation;
7. confirm scan-102 boxed `முகப்பில்:` material is excluded;
8. confirm closing ornament and scan-103 `அடிமைகள்` forward boundary;
9. apply only source-proven final corrections; if the final gate passes, promote both pages to `verified` and synchronize all controls;
10. create/update the Stage-4 final-source-check record, commit, and stop.

Do not begin English translation or `மதுரைச் செலவு` in the same activity.

The 1958 `தேனலைகள்` source remains **DEFERRED**.
