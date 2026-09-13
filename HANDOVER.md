# HANDOVER — Kalaignar Short Stories Archive

## Repository

- repository: `pugazg/kalaignar-short-stories`
- branch: `main`
- **LIVE MAIN IS AUTHORITATIVE**

## Closed durable layers

- 1977 Tamil dual-gate: **37/37 CURRENT PASS / CLOSED**
- 1977 English E1–E5 re-audit: **37/37 PASS / CLOSED**
- 1987 `கலைஞர் சொன்ன குட்டிக் கதைகள்`: **Tamil/source + English CLOSED**
- 1976 `நளாயினி` reconciliation: **CLOSED / PASS**
- 1982 `முடியாத தொடர்கதை`: **Tamil/source + English CLOSED**
- 2004, 2008, 2009 and the completed supplemental English layers remain closed under their collection trackers.

## Active source — 1969 `கண்ணடக்கம்`

Controlling attached source: `TVA_BOK_0064095_கண்ணடக்கம்.pdf`.

Collection physical completeness remains **OPEN** because printed pages **31–52 (22 pages)** are absent. Do not guess those missing story identities/text.

Visible routing:

1. `கண்ணடக்கம்` scans 4–10 — existing canonical witness
2. `நெருப்பு` scans 11–24 — **NEW canonical — TAMIL/SOURCE CLOSED**
3. `வேணியின் காதலன்` scans 25–31 — existing canonical witness
4. `அமிர்தமதி` scans 32–41 — existing canonical witness

`நெருப்பு` Tamil/source work is now closed; the comparison-only witness backlog is unblocked.

## `நெருப்பு` current state

Workspace: `stories/neruppu/`

- source intake: **PASS**
- story range: scans **11–24 / printed 10–23**
- page records: **14/14**
- Stage 1 first-pass: **14/14**
- Stage 2 visual fidelity: **14/14**
- Stage 3 historical glyph: **14/14**
- Stage 4 final check: **14/14**
- verified: **14/14**
- needs-review: **0/14**
- not-started: **0/14**
- blocked: **0**
- Tamil assembly: **PASS / CLOSED**
- reading layer: `stories/neruppu/sections/neruppu.md`
- source closure: `stories/neruppu/TAMIL_SOURCE_CLOSURE.md`

### P1 — scans 11–15 / printed 10–14

**CLOSED / VERIFIED 5/5.**

- Stage 2 ordinary fidelity corrections: **15**
- Stage 3 character-identity corrections: **0**
- Stage 4 final source-proven corrections: **6**
- interim 16-correction revalidation: **SUPERSEDED; 12 over-corrections reverted**
- final unresolved: **0**

### P2 — scans 16–20 / printed 15–19

- Stage 1 first-pass: **COMPLETE 5/5**
- Stage 2 visual fidelity: **COMPLETE / PASS 5/5**
- Stage-2 source-proven corrections: **6**
- Stage-1 source-sensitive queue resolved: **6/6**
- Stage-2 unresolved ordinary fidelity issues: **0**
- pages: **`verified` 5/5**
- Stage 3 historical glyph: **COMPLETE / PASS 5/5**
- Stage-3 character-identity corrections: **0**
- Stage-3 unresolved glyph clusters: **0**
- Stage 4: **COMPLETE / PASS 5/5**
- Stage-4 source-proven corrections: **2**
- Stage-4 final unresolved issues: **0**
- blocked: **0**

## Mandatory four-stage cadence

1. first-pass transcription → commit + sync
2. visual text-fidelity audit → commit + sync
3. historical Tamil glyph audit → commit + sync
4. final independent source check → commit + sync; only then `verified`

## Exact next activity

**`நெருப்பு` P3 Stage 1 — first-pass transcription, scans 21–24 / printed 20–23.**

Transcribe the final four story scans from the controlling source only, preserve source spellings/punctuation/spacing and page boundaries, queue genuinely uncertain readings explicitly, synchronize controls, commit, and stop before P3 Stage 2.


### P3 — scans 21–24 / printed 20–23

**CLOSED / VERIFIED 4/4.**

- Stage 1 first-pass: **COMPLETE 4/4**
- Stage 2 visual fidelity: **COMPLETE / PASS 4/4**
- Stage 3 historical glyph: **COMPLETE / PASS 4/4**
- Stage 4 final independent source check: **COMPLETE / PASS 4/4**
- Stage-2 interim changes reviewed at final gate: **14**
- Stage-2 over-corrections reverted: **6**
- Stage-2 correction refined: **1**
- additional Stage-4 source corrections: **2**
- corrective changes applied during Stage 4: **9**
- final net source-fidelity differences from P3 Stage 1: **10**
- Stage-3 character-identity corrections: **0**
- Stage-3 unresolved glyph clusters: **0**
- final unresolved issues: **0**
- scan 24 ending sentence + closing ornament: **PASS**
- blocked: **0**

All **14/14** `நெருப்பு` page records are four-gate verified.

## `நெருப்பு` Tamil/source closure

**PASS / CLOSED.**

- verified page records: **14/14**
- assembled reading layer: `stories/neruppu/sections/neruppu.md`
- page provenance markers: **14/14**
- scan sequence: **11–24 exactly once**
- printed pages: **10–23 exactly once**
- scan 20→21 continuation: **PASS**
- scan 24 ending + ornament boundary: **PASS**
- scan 25: **excluded / opens `வேணியின் காதலன்`**
- unresolved source readings: **0**

## Exact next activity — current

**1969 `கண்ணடக்கம்` comparison-only witness audit — scans 4–10 / printed pages 3–9.**

Compare the attached 1969 witness directly against the existing 1977 canonical `stories/kannadakkam/`. Use/create `stories/kannadakkam/witnesses/1969-kannadakkam/`. Record true edition variants and any strong canonical-recheck candidates, but do not import witness wording into the 1977 canonical without a separate controlling-source recheck. Do not create duplicate Tamil or English layers.
