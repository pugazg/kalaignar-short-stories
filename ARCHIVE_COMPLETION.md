# Archive Completion — Kalaignar Short Stories

**Archive-wide closure date:** 2026-09-06  
**Repository:** `pugazg/kalaignar-short-stories`  
**Branch:** `main`

## Purpose

This file records the archive-wide closure reached on 2026-09-06 for the then-authorized scope. `PROJECT_COMPLETION.md` remains the detailed historical completion record for the 1977 anthology and its later Story-29 page-anchor correction.

A later explicit authorization can reopen the archive for a new source without invalidating the completed state recorded here. See the post-closure reactivation section at the end.

## Archive-wide closed state reached on 2026-09-06

| Scope | Tamil / source | Visual | English | Status |
|---|---:|---:|---:|---|
| 1977 `கலைஞர் கருணாநிதியின் சிறுகதைகள்` | **37 / 37 PASS** | **37 / 37 PASS** | **37 / 37 PASS** | **CLOSED — 2026 dual-gate 37/37 CURRENT PASS** |
| 2008 `கலைஞர் சொன்ன கதைகள்` | **40 / 40 PASS** | **40 / 40 PASS** | **40 / 40 PASS** | **CLOSED** |
| 2004 `கலைஞரின் குட்டிக் கதைகள்` | **34 / 34 PASS** | **34 / 34 PASS** | **34 / 34 PASS** | **CLOSED** |
| 1997 new short-story onboarding | `நண்பனா?` **3 / 3 PASS** | **PASS** | **PASS** | **CLOSED** |
| 2009 new short-story onboarding | **5 / 5 PASS** | **5 / 5 PASS** | **5 / 5 PASS** | **CLOSED** |
| 2009 existing-canonical witness comparison | **11 / 11 complete** | evidence workflow | canonical English unchanged | **CLOSED** |
| Supplemental English queue | verified Tamil already closed | source-page anchoring PASS | **6 / 6 PASS** | **CLOSED** |

No item from that completed scope remains pending.

## 1997 source closure

Source: `TVA_BOK_0064315_திராவிட_இயக்க_எழுத்தாளர்_சிறுகதைகள்.pdf`

- scans: **115**
- contents: **10 works**
- short-story titles represented canonically: **9**
- newly onboarded short story: `நண்பனா?` — 3/3 verified; Tamil audit PASS; visual PASS; English PASS
- `நடுத்தெரு நாராயணி`: deliberately excluded from short-story onboarding and reserved for separate short-novel handling
- short-novel physical span recorded for handoff: scans **62–85 / printed pages 52–75**

## 2009 source closure

Source: `TVA_BOK_0065745_16_கதையினிலே.pdf`

- SHA-256: `21daed58600d2e927dec4341fd1e0eab597f12d50f8c444458de9bc4ad18a859`
- size: **384,978,955 bytes**
- scans: **183**
- stories: **16 / 16 physically present**
- story block: scans **6–182**
- scan **183**: back cover
- new stories onboarded: **5 / 5 PASS**
- existing-canonical independent-witness comparisons: **11 / 11 COMPLETE / CLOSED**
- supplemental English for the five new 2009 stories: **5 / 5 PASS**

### Corrected preview provenance

The supplied conversation upload is the full **384,978,955-byte / 183-scan** PDF. During one comparison iteration, ChatGPT's rendered-file preview/index exposed page images only through scan **150**. This was a preview/access limit, **not a truncated PDF**. Earlier documentation that called the conversation PDF or working copy “truncated after scan 150” was corrected during archive closure.

## 2009 independent-witness disposition

Final ledger:

`collections/2009-16-kathaiyinile/ADDITIONAL_WITNESS_COMPARISON.md`

- compared: **11 / 11**
- canonical 1977 Tamil changed from 2009 evidence: **No**
- canonical 1977 English changed: **No**
- canonical verified page statuses changed: **No**
- apparent corrections remain controlling-source recheck evidence until the exact 1977 scan is reopened under separate authorization.

The physical anomaly remains preserved: scan **110 / printed p105** still closes `குப்பைத் தொட்டி`; `சங்கிலிச்சாமி` begins scan **111** despite the TOC assigning p105 to it.

## Supplemental English closure

Tracker: `NEW_STORY_ENGLISH_TRANSLATION_PROGRESS.md`

1. `நண்பனா?` — PASS
2. `காந்தி தேசம்` — PASS
3. `அணில் குஞ்சு` — PASS
4. `கொள்ளைபுரம்` — PASS
5. `எழுத்தாளர் ஏகலைவன்` — PASS
6. `மலரவில்லை` — PASS

Final state: **6 / 6 PASS; 0 pending; 0 NEEDS REVIEW**. Every item has story-local translation review with physical source-page anchoring PASS. No canonical Tamil was silently changed to improve English.

## Durable closure controls

The 2026-09-06 closed checkpoint is preserved through:

- `HANDOVER.md`
- `NEXT_CHAT_PROMPT.md`
- `README.md`
- `NEW_STORY_ENGLISH_TRANSLATION_PROGRESS.md`
- completed collection workspaces and their trackers.

`PROJECT_COMPLETION.md` remains the historical 1977-specific record.

## Post-closure reactivation — 1987 source intake

After the closure above, the user explicitly authorized a new source:

**`கலைஞர் சொன்ன குட்டிக் கதைகள்` — Second Edition, 1987**

New workspace:

`collections/1987-kalaignar-sonna-kuttik-kathaigal/`

This authorization **does not reopen or invalidate any previously closed collection**. It is a new source-intake phase.

Initial registered facts:

- source PDF: `TVA_BOK_0065566_கலைஞர்_சொன்ன_குட்டிக்_கதைகள்_1987.pdf`
- byte size: **107,757,858**
- scans: **50**
- publisher: **செல்வகுமார் பதிப்பகம்**
- represented edition: **இரண்டாம் பதிப்பு — 1987**
- direct physical story blocks identified: **25 / 25**
- exact/usable headings at first intake: **20 / 25**
- title recheck holds: scans **13, 20, 31, 37, 45**
- known exact canonical duplicate: `குருவி ராமேஸ்வரம்` — additional witness only
- new canonical 1987 story workspaces created at intake: **0**
- 1987 pages marked verified at intake: **0**
- SHA-256: **PENDING** because mounted-byte hashing was unavailable in the current execution session.

The user also supplied `HISTORICAL_TAMIL_GLYPH_TRANSCRIPTION_GUIDE.md`, now adopted as the mandatory historical-glyph verification guide for this 1987 source. Duplicate checking must precede every new story activation.

Therefore the repository's **current** state is no longer “no authorized work”: the previous archive scope remains closed, while the 1987 source intake is **ACTIVE**. Current execution state is governed by `HANDOVER.md`, `NEXT_CHAT_PROMPT.md`, and the 1987 collection controls.

## Active QA addendum — 1977 English re-audit

The 1977 anthology remains source-complete and translation-complete in the historical trackers. A newly authorized post-Tamil English re-audit is **ACTIVE** and does not invalidate those completed phases.

Current English re-audit: **E1 31/37 PASS; 8 page-anchor/content-boundary repairs; 17 structure-traceability annotation repairs; 0 unresolved; E2–E5 not started**. Next: Story 32 `விஷம் இனிது`. Tracker: `ENGLISH_REAUDIT_PROGRESS.md`.
