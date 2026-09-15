# NEXT CHAT PROMPT — 1953 `நாடும் நாடகமும்` / final source batch scans 67–80

Continue in `pugazg/kalaignar-short-stories`, branch `main`. **LIVE MAIN IS AUTHORITATIVE.**

## Controlling source

Use only the user-supplied:

`TVA_BOK_0064193_நாடும்_நாடகமும்.pdf`

- edition: **முதல் பதிப்பு — 1953**
- physical scans: **80**
- direct scan pixels control
- no OCR, web copies, Wikisource, catalogue text, alternate editions, or contextual reconstruction as witness authority

## Closed prior work

- `நாடும் நாடகமும் (ஆசிரியர் பேசுகிறார்)` — **CLOSED / VERIFIED 20/20**
- `தெருக்கூத்து` — **CLOSED / VERIFIED 12/12**
- `சந்தனக்கிண்ணம்` 1953 witness — **CLOSED / PASS 15/15**
- `ஆலமரத்துப் புறாக்கள்` 1953 witness — **CLOSED / PASS FOR SOURCE-VISIBLE MATERIAL**
  - corrected span: scans **52–58 / printed 44–50**
  - scans 57–58 have large physical paper loss
  - 1953 missing wording was not reconstructed
  - highest-value variant: `"வந்தே மாத்ரம்"` ↔ canonical `"வந்தேன் எமாத்தினேன்"`
  - canonical Tamil / English unchanged

## Critical routing correction

The old downstream inventory is **RETRACTED**.

Direct source inspection proved:

- `ஆலமரத்துப் புறாக்கள்` ends by scan **58**
- scan **59 / printed 51** opens **`ஆதரிக்கிறார்`**
- `ஆதரிக்கிறார்` continues through at least scan **66**

Do not assume:

- old `ஆலமரத்துப் புறாக்கள் = 52–68`
- old `பெண்கள் = 69–75`
- old `இரகசியம்! = 76–80`

Direct headings/endings must control.

## Active witness — `ஆதரிக்கிறார்`

Canonical:
`stories/aatharikkirar/`

Witness workspace:
`stories/aatharikkirar/witnesses/1953-naadum-naadagamum/`

Processed:

- scans **59–66 / printed 51–58**
- material variant groups: **5**
- canonical recheck candidates: **0**
- unresolved: **0**
- canonical Tamil / English changed: **No / No**

Notable 1953 differences:

- extra paragraph ending `பார்ப்பனச்சேரி`;
- redistributed `நகரசபைக்காக` wording;
- `வேஷ்டியை` ↔ canonical `வேட்டியை`;
- extra award sentence `பொதுத் தொண்டுச் சிங்கம் புண்யகோடி என்ற விருதுகள் வழங்கப்பட்டன.`

## Batch size

User requested **15 physical pages per iteration**.

Only **14 scans remain**, so the next iteration is the final partial batch:

**scans 67–80 / printed 59–72 — 14 physical pages**

## Exact next activity

1. fetch live `main`;
2. render/reopen scans **67–80** directly;
3. continue `ஆதரிக்கிறார்` from scan 67 until its actual ending;
4. when a new heading appears, close the current witness and identify the new story from the source heading/content;
5. route each new story to its already-existing canonical workspace — **do not create new canonical folders**;
6. compare each source span against its canonical text and record material edition variants / canonical confirmations;
7. if witness evidence suggests a canonical error, reopen the exact canonical controlling scan before any repair;
8. preserve physical source limitations; never fill lost text from another edition;
9. create/update witness records under the relevant canonical story folders;
10. synchronize collection README, scan map, story inventory, `HANDOVER.md`, and this prompt;
11. commit and re-fetch live `main`;
12. finish through scan **80**.
