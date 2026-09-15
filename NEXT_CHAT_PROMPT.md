# NEXT CHAT PROMPT — சீரழித்த சிரிப்பு! / Stage 1 scans 101–102

Continue in `pugazg/kalaignar-short-stories`, branch `main`. **LIVE MAIN IS AUTHORITATIVE.**

## Newly onboarded periodical sources

Four user-supplied magazine sources are now durably registered.

### பனங்குலை — 1977 முரசொலி பொங்கல் மலர்

- existing canonical: `stories/panangulai/`
- witness scans: **6–7**
- comparison: **CLOSED / PASS 2/2**
- material variants: **10**
- canonical changes: **0**
- do not reopen automatically

### சீரழித்த சிரிப்பு! — ACTIVE

Canonical workspace:

`stories/seerazhitha-sirippu/`

Controlling source:

`TVA_PRL_0033125_காஞ்சி_பொங்கல்_மலர்_1966.pdf`

- full PDF: **116 scans**
- source bytes: **135,439,066**
- SHA-256: `82061a8a5d76c401cf5c804f757f2fb80873171b25388830cb129c71fd476047`
- story scans: **101–102**
- printed folios: **91–92**
- scan 103 opens `அடிமைகள்`
- source intake: **COMPLETE**
- dedup: **new canonical**
- initialized page records: **2/2**
- Stage 1: **NOT STARTED**
- Markdown baseline: `seerazhitha_sirippu.md` — **locator only; not authority**

### மதுரைச் செலவு — queued after current story

- canonical: `stories/madurai-selavu/`
- source: 1960 முரசொலி பொங்கல் மலர்
- physical scans **21–26 / printed 17–22**
- story text scans **21–24 + 26**
- scan 25 is a verified non-story interleaf and must be excluded
- source intake complete; Stage 1 not started

### கொன்று வருக! — queued after மதுரைச் செலவு

- canonical: `stories/kondru-varuga/`
- source: 1952 முரசொலி பொங்கல் மலர்
- scans **8–13 / printed 32–37**
- scan 14 opens `திராவிட இலக்கியம்`
- source intake complete; Stage 1 not started

## Exact next activity

Perform **Stage 1 first-pass transcription** for `சீரழித்த சிரிப்பு!`, scans **101–102 / printed 91–92**.

Rules:

1. fetch live `main` first;
2. read the story README, source metadata, source-intake record and page map;
3. source pixels are controlling — **no OCR/web/Wikisource/alternate edition authority**;
4. the user-supplied `seerazhitha_sirippu.md` may be used only as a locator/draft;
5. reconstruct physical multi-column reading order from the scan itself;
6. preserve source wording, punctuation, dialogue/paragraph boundaries, names and historical forms;
7. if a span is genuinely uncertain, record it for review rather than guessing;
8. set both page records to `needs-review`;
9. update Stage-1 progress / story controls / `HANDOVER.md` / `NEXT_CHAT_PROMPT.md`;
10. commit Stage 1 and stop before Stage 2.

Do not begin `மதுரைச் செலவு` in the same activity.

The 1958 `தேனலைகள்` source remains **DEFERRED**.
