# பக்க வரைபடம் — கிழவன் கனவு

Source: `TVA_BOK_0014165_கிழவன்_கனவு.pdf`

| Scan | Printed page | Page type / section | Status | File |
|---:|:---:|---|---|---|
| 1 | — | cover — title / author / second-edition statement / imprint | verified | `pages/0001-cover.md` |
| 2 | — | `மதிப்புரை.` — A. P. ஜனார்த்தனம் | verified | `pages/0002-mathippurai.md` |
| 3 | — | reviews — `“குடியரசு”` / `“தொழிலாளர்”` | needs-review | `pages/0003-reviews.md` |
| 4 | — | `என் வெளியிட்டேன் ?...` — சு. இராமநாதன் | needs-review | `pages/0004-en-veliyitten.md` |
| 5 | — | `வணக்கம் பல!...` — சு. இராமநாதன் | verified | `pages/0005-vanakkam-pala.md` |
| 6 | — | `எழுதியது; ஏன்?` — மு. கருணாநிதி | verified | `pages/0006-ezhuthiyathu-yen.md` |
| 7 | — | `கிழவன் கனவு` — story opening | verified | `pages/0007-kizhavan-kanavu-01.md` |
| 8 | 4 | `கிழவன் கனவு` | verified | `pages/0008-kizhavan-kanavu-02.md` |
| 9 | 5 | `கிழவன் கனவு` | verified | `pages/0009-kizhavan-kanavu-03.md` |
| 10 | 6 | `கிழவன் கனவு` | verified | `pages/0010-kizhavan-kanavu-04.md` |
| 11 | 7 | `கிழவன் கனவு` | verified | `pages/0011-kizhavan-kanavu-05.md` |
| 12 | 8 | `கிழவன் கனவு` | verified | `pages/0012-kizhavan-kanavu-06.md` |
| 13 | 9 | `கிழவன் கனவு` | verified | `pages/0013-kizhavan-kanavu-07.md` |
| 14 | 10 | `கிழவன் கனவு` | verified | `pages/0014-kizhavan-kanavu-08.md` |
| 15 | 11 | `கிழவன் கனவு` | blocked | `pages/0015-kizhavan-kanavu-09.md` |
| 16 | 12 | `கிழவன் கனவு` | verified | `pages/0016-kizhavan-kanavu-10.md` |
| 17 | 13 | `கிழவன் கனவு` | blocked | `pages/0017-kizhavan-kanavu-11.md` |
| 18 | 14 | `கிழவன் கனவு` | verified | `pages/0018-kizhavan-kanavu-12.md` |
| 19 | 15 | `கிழவன் கனவு` | verified | `pages/0019-kizhavan-kanavu-13.md` |
| 20 | 16 | `கிழவன் கனவு` | verified | `pages/0020-kizhavan-kanavu-14.md` |
| 21 | 17 | `கிழவன் கனவு` | blocked | `pages/0021-kizhavan-kanavu-15.md` |
| 22 | 18 | `கிழவன் கனவு` — conclusion / publisher-printer material at foot | blocked | `pages/0022-kizhavan-kanavu-16.md` |
| 23 | — | `பிழை திருத்தம்.` / tobacco advertisement | verified | `pages/0023-errata-advertisement.md` |
| 24 | — | `ராஜேந்திரா நைஸ் புகையிலை` advertisement | verified | `pages/0024-advertisement.md` |
| 25 | — | `தியாகராஜ விலாஸ்` advertisement | verified | `pages/0025-thiyagaraja-vilas-ad.md` |
| 26 | — | back cover / small child illustration | verified | `pages/0026-back-cover.md` |

## கணக்கு

- Source scan pages: **26**
- Page records created: **26 / 26**
- `verified`: **20**
- `blocked`: **4**
- `needs-review`: **2**
- `not-started`: **0**
- PDF stored in repository: **No**

## Numbering note

Scan page 8 visibly carries printed page **(4)** and the printed sequence continues through scan page 22 as **(18)**. Scan page 7 is the immediately preceding story-opening page, but no printed number is clearly visible in the supplied scan image; therefore the manifest deliberately records `—` rather than inferring `3`.

## Final high-resolution unresolved-reading pass

The final source-only pass on story scans **8, 14, 15, 17, 18, 21 and 22** is complete.

### Resolved and promoted to `verified`

- scan **8 / printed 4** — `பூகோள பூரணர்த்திக` resolved from high-resolution source view;
- scan **14 / printed 10** — remaining dream-passage readings resolved, including `என் நெற்றியை?`, `திராட்சையைச் சாப்பிடேன்`, and `மந்த காசத்தினிடையே`;
- scan **18 / printed 14** — remaining opening phrase resolved as `விட்டிருந்து`.

### Formally `blocked` by the supplied source

- scan **15 / printed 11** — one worn/indistinct word plus temple-history text physically covered by a circular library stamp;
- scan **17 / printed 13** — one short phrase after `பார்வதியை` remains visually indistinct even at high resolution;
- scan **21 / printed 17** — four short readings in the political/historical catalogue remain visually indistinct;
- scan **22 / printed 18** — a library stamp physically obscures part of the final story phrase and footer/imprint material.

These four pages are no longer open-ended `needs-review` items. Their unresolved text is explicitly marked `blocked-by-source`; no context, historical memory, web source or later edition has been used to reconstruct hidden wording.

Scans **3–4** remain `needs-review` for their earlier front-matter source-condition uncertainties; they are outside the story-body translation layer.

## Assembled Tamil layer

Created:

- [`../sections/kizhavan-kanavu.md`](../sections/kizhavan-kanavu.md) — story-body assembly for scans 7–22;
- [`../sections/kizhavan-kanavu-errata.md`](../sections/kizhavan-kanavu-errata.md) — explicit mapping of all 10 printed errata entries;
- [`../ASSEMBLY_REVIEW.md`](../ASSEMBLY_REVIEW.md) — consistency review across assembly, page records, page map and errata layer.

The assembled Tamil file must preserve the same three newly resolved readings and all four `blocked-by-source` locations; it must not silently apply scan 23's errata.

## Translation gate

The **story-body Tamil source audit is complete to the limit of the supplied physical source**. Every story scan now has a final disposition: `verified` or `blocked` with explicit source gaps.

English translation may therefore be opened as a controlled workflow **only if every source-blocked location remains explicitly marked and untranslated rather than guessed**. Front-matter scans 3–4 remain outside this story-body translation gate.

## அடுத்த activity

Synchronize the assembled Tamil file and consistency-review documents with these final dispositions, then prepare the English-translation workflow/plan without beginning translation until that synchronization check passes.
