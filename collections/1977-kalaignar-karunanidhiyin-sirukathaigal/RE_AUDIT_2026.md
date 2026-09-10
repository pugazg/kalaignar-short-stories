# 1977 anthology source re-audit — 2026

## Status

**OPEN — 0 / 37 stories have passed the new dual-gate re-audit.**

The earlier `verified` / `audit PASS` state is retained as historical provenance only. It is **not sufficient for current release confidence** after a source-comparison defect was confirmed in `நளாயினி`.

## Controlling source identity

Exact attached source used for this re-audit:

- file: `TVA_BOK_0064142_கலைஞர்_கருணாநிதியின்_சிறுகதைகள்.pdf`
- printed edition: **முதல் பதிப்பு: 1977**
- physical scans: **260**
- bytes: **268,486,609**
- SHA-256: `853032661482eaccb26c083a38d7aa75c081362d33c963c63e37d088bf20acb3`
- source PDF must not be committed

The attached file exactly matches the source identity already registered in this repository.

## User directive

This is a **comparison re-audit, not a retranscription project**.

For every story:

- use the existing canonical/page-record Tamil as the comparison target;
- compare it directly against the 1977 source pixels;
- correct only source-proven mismatches;
- never create another full transcription merely to perform the audit;
- preserve source spelling, punctuation, paragraphing, page boundaries, source-odd forms and non-text marks;
- no normalization from later editions or from lexical expectation;
- no global replacements.

## Mandatory dual gates

A story is not re-closed until **both gates independently PASS**.

### Gate A — source-fidelity comparison

Compare all existing story text and relevant source marks against every physical 1977 story page.

Gate A must check:

- words and word forms;
- omitted / duplicated / substituted text;
- punctuation and meaningful spacing;
- paragraph and page-boundary continuations;
- headings, separators, ornaments and note layers where applicable;
- suspicious readings previously left in possible-error queues.

Gate A is **not** a fresh transcription. It is a direct source-vs-repository audit.

### Gate B — Historical Tamil Glyph re-audit

This is a **separate independent gate after / alongside Gate A, but it may not be inferred from Gate A**.

Every physical page must be reopened at high/native resolution and explicitly checked for the mandatory historical families:

`ணா / ணை / ணொ / ணோ / லை / ளை / றா / றொ / றோ / னா / னை / னொ / னோ`

Follow `HISTORICAL_TAMIL_GLYPH_TRANSCRIPTION_GUIDE.md` plus `OLD_TAMIL_GLYPH_REAUDIT_GATE.md` in this collection.

A glyph correction changes character identity only; it does not authorize spelling modernization.

## Closure / synchronization rule

After both gates PASS for a story:

1. correct affected canonical page records;
2. synchronize assembled Tamil;
3. update story audit / possible-error records;
4. update any existing English translation affected by a proven Tamil correction;
5. record all corrections in the story's re-audit record;
6. update this collection tracker;
7. only then restore current `PASS` status for that story.

## Triggering defect

`நளாயினி`, source scan **17 / printed page 8**:

- repository currently: `தாசிநாதீனத்தொழு!`
- attached 1977 source: `காசிநாதனைத்தொழு!`

This is a confirmed repository transcription defect, not a 1976↔1977 edition variant. The canonical correction will be made during the complete `நளாயினி` re-audit so the whole story is repaired and synchronized in one controlled activity.

## Progress

| # | Story | 1977 scans | Gate A source fidelity | Gate B old glyph | Current state |
|---:|---|---:|---|---|---|
| 1 | `புகழேந்தி` | 10–15 | pending | pending | REOPENED |
| 2 | `நளாயினி` | 16–23 | **ACTIVE** | pending | REOPENED — confirmed defect present |
| 3 | `சபலம்` | 24–30 | pending | pending | REOPENED |
| 4 | `ஆட்டக்காவடி` | 31–38 | pending | pending | REOPENED |
| 5 | `குப்பைத்தொட்டி` | 39–46 | pending | pending | REOPENED |
| 6 | `சந்தனக்கிண்ணம்` | 47–56 | pending | pending | REOPENED |
| 7 | `சங்கிலிச்சாமி` | 57–68 | pending | pending | REOPENED |
| 8 | `கங்கையின் காதல்` | 69–72 | pending | pending | REOPENED |
| 9 | `தாய்மை` | 73–83 | pending | pending | REOPENED |
| 10 | `தப்பிவிட்டார்கள்` | 84–91 | pending | pending | REOPENED |
| 11 | `தப்பவில்லை` | 92–101 | pending | pending | REOPENED |
| 12 | `ஆதரிக்கிறார்` | 102–107 | pending | pending | REOPENED |
| 13 | `இரகசியம்!` | 108–111 | pending | pending | REOPENED |
| 14 | `முந்நூறு ரூபாய்` | 112–114 | pending | pending | REOPENED |
| 15 | `ஏழை` | 115–118 | pending | pending | REOPENED |
| 16 | `ஒரிஜினலில் உள்ளபடி` | 119–125 | pending | pending | REOPENED |
| 17 | `பனங்குலை` | 126–130 | pending | pending | REOPENED |
| 18 | `செத்தவள் கதை` | 131–139 | pending | pending | REOPENED |
| 19 | `பிரேத விசாரணை` | 140–145 | pending | pending | REOPENED |
| 20 | `கண்டதும் காதல் ஒழிக!` | 146–150 | pending | pending | REOPENED |
| 21 | `ஆலமரத்துப் புறாக்கள்` | 151–155 | pending | pending | REOPENED |
| 22 | `தொத்துக்கிளி` | 156–160 | pending | pending | REOPENED |
| 23 | `காதல் கடிதம்` | 161–165 | pending | pending | REOPENED |
| 24 | `கண்ணடக்கம்` | 166–172 | pending | pending | REOPENED |
| 25 | `வாழ முடியாதவர்கள்` | 173–180 | pending | pending | REOPENED |
| 26 | `அபாக்ய சிந்தாமணி` | 181–188 | pending | pending | REOPENED |
| 27 | `பாலைவன ரோஜா` | 189–193 | pending | pending | REOPENED |
| 28 | `புரட்சிப் படம்` | 194–198 | pending | pending | REOPENED |
| 29 | `திடுக்கிடும் கதை` | 199–204 | pending | pending | REOPENED |
| 30 | `கடைசிக் கட்டம்` | 205–210 | pending | pending | REOPENED |
| 31 | `அய்யோ ராஜா!` | 211–217 | pending | pending | REOPENED |
| 32 | `விஷம் இனிது` | 218–224 | pending | pending | REOPENED |
| 33 | `வேணியின் காதலன்` | 225–230 | pending | pending | REOPENED |
| 34 | `அமிர்தமதி` | 231–238 | pending | pending | REOPENED |
| 35 | `சுமந்தவள்` | 239–249 | pending | pending | REOPENED |
| 36 | `சித்தார்த்தன் சிலை` | 250–252 | pending | pending | REOPENED |
| 37 | `நுனிக்கரும்பு` | 253–259 | pending | pending | REOPENED |

## Processing order

Incident priority: complete `நளாயினி` first because a definite canonical error has already been proved.

After `நளாயினி` closes under both gates, audit `புகழேந்தி`, then continue Story 3 through Story 37 in anthology order.

## Exact next activity

Re-audit `நளாயினி`, scans **16–23 / printed 7–14**, against its existing repository records and assembly:

- Gate A: complete source-fidelity comparison for all 8 pages;
- Gate B: independently perform the old-Tamil-glyph re-audit on all 8 pages;
- repair every source-proven canonical mismatch;
- synchronize assembled Tamil, audits / possible-error queue and any affected English;
- update the 1976 witness comparison classifications where a supposed variant is actually a canonical transcription defect;
- commit and stop/report.

Do not begin `புகழேந்தி` in the same activity.
