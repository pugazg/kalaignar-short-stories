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

## Active source — 1969 `கண்ணடக்கம்`

Controlling attached source: `TVA_BOK_0064095_கண்ணடக்கம்.pdf`.

Collection physical completeness remains **OPEN** because printed pages **31–52 (22 pages)** are absent. Do not guess those missing story identities/text.

Visible routing:

1. `கண்ணடக்கம்` 4–10 — existing canonical witness
2. `நெருப்பு` 11–24 — **NEW canonical ACTIVE**
3. `வேணியின் காதலன்` 25–31 — existing canonical witness
4. `அமிர்தமதி` 32–41 — existing canonical witness

## `நெருப்பு` current state

Workspace: `stories/neruppu/`

- source intake: **PASS**
- story range: scans **11–24 / printed 10–23**
- page records: **14/14**
- P1 Stage 1 first-pass scans 11–15: **COMPLETE 5/5**
- Stage 1 total: **5/14**
- Stage 2 visual fidelity: **5/14**
- Stage 3 historical glyph: **5/14**
- Stage 4 final check: **5/14**
- verified: **5/14**
- needs-review: **0/14**
- not-started: **9/14**
- blocked: **0**
- P1 Stage-2 ordinary fidelity corrections: **15**
- P1 Stage-2 unresolved ordinary fidelity issues: **0**

Stage 2 is now durable. The scan-14 opening continuation was resolved from enlarged source pixels as `விதந்தன்னை`; all seven Stage-1 queued ordinary-fidelity readings have dispositions.

## Mandatory four-stage cadence

1. first-pass transcription → commit + sync
2. visual text-fidelity audit → commit + sync
3. historical Tamil glyph audit → commit + sync
4. final independent source check → commit + sync; only then `verified`

## P1 durable closure

- Stage 3 historical-glyph audit: **COMPLETE / PASS 5/5**
- Stage-3 character-identity corrections: **0**
- Stage-3 unresolved glyph clusters: **0**
- Stage 4 final independent source check: **COMPLETE / PASS 5/5**
- Stage-4 final source-proven corrections: **6**
  - scan 13 — `பிடிக்கவில்லை யென்றாலும்`; `“உலகப் பேரழகி கிளியோ”`
  - scan 14 — `இந்திரனா?`; `கேட்டுக் கேட்டுச்`
  - scan 15 — `வேறுபாடுகளும்-இதுவரையில்`; `சுக்ரீவன்.... அவன்தான்`
- interim 16-correction revalidation: **SUPERSEDED; 12 over-corrections reverted**
- omission / duplication / punctuation / paragraph / page-boundary unresolved issues after final revalidation: **0**
- Stage-3 historical-glyph changes at Stage 4: **0**
- final unresolved issues: **0**
- P1 pages: **`verified` 5/5**

## Exact next activity

**`நெருப்பு` P2 Stage 1 — first-pass transcription, scans 16–20 / printed 15–19.**

Transcribe only the five P2 scans from the controlling source, preserve source spellings/punctuation/spacing, queue genuinely uncertain readings as `needs-review`, synchronize controls, commit, and stop before Stage 2.