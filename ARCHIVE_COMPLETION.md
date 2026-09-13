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

That paragraph recorded the 1987 intake state at activation time. The 1987 collection has since reached **Tamil/source PASS / CLOSED and English 25/25 PASS / CLOSED**; its collection README is authoritative for that later closure. Current execution state is governed by `HANDOVER.md` and `NEXT_CHAT_PROMPT.md`.

## Closed QA addendum — 1977 English re-audit

The 1977 anthology remains source-complete and translation-complete in the historical trackers. The separately authorized post-Tamil English re-audit is now **CLOSED** and does not invalidate those completed phases.

Final English re-audit: **E1/E2/E3/E4/E5 CLOSED — 37/37 PASS; 49 cumulative E4 English-quality repairs; 0 E5 repairs; 0 unresolved**. E5 final page traceability: **250/250 PASS**. Tracker: `ENGLISH_REAUDIT_PROGRESS.md`.

## Post-closure addendum — 1976 `நளாயினி` exact-edition reconciliation — CLOSED

A later explicit authorization processed:

`TVA_BOK_0065574_நளாயினி_1976.pdf` — fourth edition, 1976, 78 scans.

The source contributed two new canonicals:

- `நாட்டிய கலாராணி` — Tamil + English PASS / CLOSED;
- `மானம்` — Tamil + English PASS / CLOSED.

The remaining six stories were handled as **comparison-only witnesses** against existing canonicals, with no duplicate Tamil transcription and no duplicate English translation.

Final witness state:

- stories: **6/6 COMPLETE / PASS**
- target pages: **48/48 reviewed**
- true edition variants: **17**
- canonical defects exposed by the `நளாயினி` witness and repaired only after direct controlling-source recheck: **8**
- canonical changes from witness evidence alone: **0**
- unresolved witness issues: **0**

Per user instruction, the attached PDF itself was sufficient for the 1976 witness layer; Tamil Digital Library and Wikisource mirrors were not used as substitute sources.

This 1976 reconciliation is **CLOSED under current evidence**.

## Post-closure reactivation — 1969 `கண்ணடக்கம்` — ACTIVE

The user supplied:

`TVA_BOK_0064095_கண்ணடக்கம்.pdf`

Registered source facts:

- printed title: **கண்ணடக்கம்**
- author: **மு. கருணாநிதி**
- publisher/imprint: **திராவிடப்பண்ணை**
- represented edition: **இரண்டாம் பதிப்பு — 1969**
- scans: **43**
- bytes: **50,321,052**
- source type: image-only
- source PDF committed: **No**
- SHA-256: **PENDING**; do not invent a checksum

Visible routing:

- `கண்ணடக்கம்` scans 4–10 / printed 3–9 — existing canonical, comparison witness only;
- `நெருப்பு` scans 11–24 / printed 10–23 — **new canonical TAMIL/SOURCE PASS / CLOSED**;
- `வேணியின் காதலன்` scans 25–31 / printed 24–30 — existing canonical, comparison witness only;
- `அமிர்தமதி` scans 32–41 / printed 53–62 — existing canonical, comparison witness only.

A critical physical discontinuity remains open: printed pages **31–52 (22 pages)** are absent from the supplied PDF between `வேணியின் காதலன்` and `அமிர்தமதி`. No missing story identity or text is inferred.

### Current `நெருப்பு` checkpoint

Workspace: `stories/neruppu/`.

- source range: scans **11–24 / printed 10–23**
- page records: **14/14 initialized**
- P1 scans 11–15: **all four stages COMPLETE / VERIFIED 5/5**
- P2 scans 16–20: **all four stages COMPLETE / VERIFIED 5/5**
- P2 Stage-2 source-proven corrections: **6**
- P2 Stage-3 character-identity corrections: **0**
- P2 Stage-4 final source-proven corrections: **2**
- Stages 1–4 overall: **14/14 COMPLETE / PASS**
- verified: **14/14**
- needs-review: **0/14**
- not-started: **0/14**
- blocked: **0**
- P3 Stage-2 interim changes reviewed at final gate: **14**
- P3 Stage-2 over-corrections reverted: **6**
- P3 Stage-2 correction refined: **1**
- additional P3 Stage-4 source corrections: **2**
- corrective changes applied during P3 Stage 4: **9**
- P3 final net source-fidelity differences from Stage 1: **10**
- final unresolved source issues: **0**
- Tamil assembly: **PASS / CLOSED**
- canonical reading layer: `stories/neruppu/sections/neruppu.md`
- assembly page provenance markers: **14/14**
- source closure record: `stories/neruppu/TAMIL_SOURCE_CLOSURE.md`

### 1969 comparison-only witness progress

- `கண்ணடக்கம்` scans **4–10 / printed 3–9** — **COMPLETE / PASS, 7/7 scans**
  - same narrative and eye-hospital ending;
  - no major added / omitted block;
  - canonical Tamil / English / verified status changed: **No**;
  - high-value recheck evidence: 1969 `வாளை மீனுக்கோ` and the registered 2009 witness both differ from canonical `வான மீனுக்கோ`;
  - current canonical `துணி ஏணை` and `நமனுலகு` independently supported;
  - unresolved witness issues: **0**.
- `வேணியின் காதலன்` scans **25–31 / printed 24–30** — **COMPLETE / PASS, 7/7 scans**
  - same narrative / fatal ending;
  - canonical `கூண்டுக் கிளி ஆக்குவேனென்றான்` and unusual `கந்தனு?` independently supported;
  - 1969 `யோசனைதான்!` vs canonical `யோசனை தான்!` retained as edition spacing evidence;
  - 1969 `என் வாழ்வைத் துண்டித்த` vs canonical `வாழ்க்கைத் துண்டித்த` retained as edition wording evidence;
  - canonical Tamil / English / verified status changed: **No**;
  - unresolved witness issues: **0**.
- `அமிர்தமதி` scans **32–41 / printed 53–62** — **COMPLETE / PASS, 10/10 scans**
  - same complete frame + embedded `யசோதர காவியம்` narrative;
  - all ten final 1977 historical-glyph repair identities independently supported;
  - quoted verse lexical sequence independently supported;
  - canonical Tamil / English / verified status changed: **No**;
  - scan 41 ending + scan 42 advertisement boundary: **PASS**;
  - unresolved witness issues: **0**.

### 1969 visible-source disposition

All visible story work is complete under the supplied PDF. The physical collection remains **INCOMPLETE / OPEN** because printed pages **31–52** are absent.

Current next state: **SOURCE-COMPLETENESS HOLD**.

Because the collection is being processed Tamil-first, English for the new canonical `நெருப்பு` is deferred until the collection-wide Tamil/source release gate can close. Do not infer missing story identities or use substitute editions to patch the gap without explicit authorization.
