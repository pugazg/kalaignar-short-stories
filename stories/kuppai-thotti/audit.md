# தமிழ் மூலத் தணிக்கை — குப்பைத்தொட்டி

## Final audit result

**CURRENT PASS — Gate A 8/8 + Gate B 8/8; 3 canonical repairs; 0 unresolved.**

- Controlling source: `TVA_BOK_0064142_கலைஞர்_கருணாநிதியின்_சிறுகதைகள்.pdf`
- Collection: **கலைஞர் கருணாநிதியின் சிறுகதைகள்**, முதல் பதிப்பு 1977
- Story range: scans **39–46** / printed pages **30–37**
- Page records: **8 / 8**
- Source PDF stored in GitHub: **No**
- Scan 47: boundary witness only; opens `சந்தனக்கிண்ணம்` and is excluded from this story.

## Source identity

The supplied controlling PDF was independently hashed during the re-audit:

- bytes: **268,486,609**
- SHA-256: `853032661482eaccb26c083a38d7aa75c081362d33c963c63e37d088bf20acb3`

The hash matches the registered collection source identity.

## Gate A — source fidelity

**PASS — 8/8.**

All existing canonical page records and the assembled Tamil were compared directly against the controlling 1977 pixels. The review covered wording, punctuation, meaningful spacing, paragraphing, omissions/duplications, physical page continuations, headings, separators, ornaments, note layers, and all entries in the possible-error queue.

### Source-proven repairs

1. scan 44 / printed 35: `அவசரியப் புத்தி` → **`அலட்சியப் புத்தி`**;
2. scan 45 / printed 36: `சிக்கிரம்` → **`சீக்கிரம்`**;
3. scan 45 / printed 36: `அட;` → **`அட,`**.

No other suspicious queue item met the source-proof threshold for correction. Unusual source forms including `போதுதானு`, `மனமனவென்று`, `உணர்ச்சி என்னை வளர்த்துக்கொண்டது`, `சபரகூட மஞ்சமாகி`, `குப்பைத்தொட்டி எங்கேயிருந்தால் என்ன வென்று!`, `மூன்றூறு`, `தூராற்றம்`, `வீதிப்பக்கம் வந்து உண்மைதான்`, `போனேனோ`, `சந்தித்தாகிவிட்டது`, and `வயிறாச் சோறின்றி` were independently confirmed and retained.

## Gate B — independent Old Tamil Glyph verification

**PASS — 8/8; unresolved historical-glyph readings: 0.**

Every physical story page was independently reopened at native/high resolution. The mandatory families were explicitly considered:

`ணா / ணை / ணொ / ணோ / லை / ளை / றா / றொ / றோ / னா / னை / னொ / னோ`

The independent pass also checked likely `ர/ற`, `ன/ண`, `ல/ள` confusions, faint vowel marks, touching/broken type, and other old printed forms. The scan-44 difficult word was independently enlarged and resolved as `அலட்சியப் புத்தி`; scan-45 native/enlarged review resolved `சீக்கிரம்` and the comma in `அட, பறக்காதே;`.

No unresolved character identity remained. No global replacement or modernization was used.

## Page disposition

| Printed page | Scan | Gate A | Gate B | Key disposition |
|---:|---:|---|---|---|
| 30 | 39 | PASS | PASS | Story opening; `மேனகை,` continuation |
| 31 | 40 | PASS | PASS | `போதுதானு`, `மனமனவென்று` retained |
| 32 | 41 | PASS | PASS | `எங்கிக் கிடந்த`, `காரணகரமான`, `வளர்த்துக்கொண்டது` retained |
| 33 | 42 | PASS | PASS | `சபரகூட மஞ்சமாகி`; four-line verse preserved |
| 34 | 43 | PASS | PASS | unusual `...என்ன வென்று!` retained |
| 35 | 44 | PASS | PASS | `மூன்றூறு`, `அலட்சியப் புத்தி`, `தூராற்றம்`, `பல்லைக்காட்டி` |
| 36 | 45 | PASS | PASS | `சீக்கிரம்`, `அட,`; `வந்து உண்மைதான்` retained |
| 37 | 46 | PASS | PASS | `போனேனோ`; ending + ornament |

## Cross-page audit

**PASS**

Verified physical continuations:

1. printed 30→31: `அதில் குறிப்பிடத்தக்க நட்சத்திரங்கள் மேனகை,` → `ரம்பை, ஊர்வசி, திலோத்தமை ஆகியோர்.`
2. printed 32→33: `அதிலிருந்து நேரம்` → `இரவாகத்தானிருக்குமென முடிவுகட்டி விடலாம்.`
3. printed 33→34: `எனக்குப் பக்கத்திலே ஒரு பெண் குப்பைத் தொட்டிவந்து சேரக்` → `கூடாதா?`
4. printed 34→35: `...இதற்குக் கைமாறாக முன்` → `கூட்டியே மூன்றூறு ரூபாய்...`
5. printed 35→36: `நான் தூங்குவதுபோல்` → `நடித்து நடப்பவைகளைக் கவனித்துக்கொண்டிருந்தேன்.`
6. printed 36→37: `இந்நாட்டு மன்னர்களிலே ஒருவனல்லவா,` → `எந்தக் குப்பைத்தொட்டி மறைவுக்குப் போனேனோ; தெரிய வில்லை!...`

No page is omitted or duplicated.

## Assembly gate

`sections/kuppai-thotti.md` is synchronized with the eight source pages.

- source scans represented: **8 / 8**
- scan order: **39 → 46**
- printed order: **30 → 37**
- duplicated pages: **none**
- omitted pages: **none**
- Story 6 text included: **No**
- unresolved story markers: **0**

## Translation gate

The existing English translation was checked after the Tamil repair. The scan-44 correction materially changes the meaning of the phrase and was propagated: `அலட்சியப் புத்தி` is translated as **careless in their thinking**, replacing the earlier **hasty minds**. The scan-45 spelling and punctuation repairs do not require further English prose change.

`TRANSLATION_REVIEW.md` records the synchronized result.

## Closure

- Gate A: **PASS — 8/8**
- Gate B: **PASS — 8/8**
- canonical repairs: **3**
- unresolved source readings: **0**
- unresolved historical-glyph readings: **0**
- story status: **CURRENT PASS / CLOSED**

Durable re-audit record: `RE_AUDIT_2026.md`.
