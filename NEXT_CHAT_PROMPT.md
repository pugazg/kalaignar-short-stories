# NEXT CHAT PROMPT — `விலையால் வாங்கலையோ` / T1 scans 26–27

Continue in `pugazg/kalaignar-short-stories`, branch `main`. **LIVE MAIN IS AUTHORITATIVE.**

## Controlling source

Use only the attached:

`TVA_BOK_0064098_தப்பிவிட்டார்கள்.pdf`

- collection: **தப்பிவிட்டார்கள்**
- edition: **நான்காம் பதிப்பு — ஆகஸ்ட் '53**
- source type: **image-only**
- source authority: **direct scan pixels**
- story: **விலையால் வாங்கலையோ**
- story span: scans **24–31 / printed 22–29**
- canonical route: `stories/vilaiyal-vangalaiyo/`

Do not use OCR, web text or another edition as textual authority.

## Durable state

The new canonical identity check is complete: no pre-existing canonical work matched the exact title, transliterations, `வைரக்கண்ணு`, or distinctive opening dialogue.

T1 first-pass transcription:

- scans **24–25 / printed 22–23** — **COMPLETE / COMMITTED**
- scans **26–31 / printed 24–29** — not started
- cumulative T1: **2/8**
- verified pages: **0/8**
- Stage 2–4: not started
- English: blocked

Checkpoint:

`stories/vilaiyal-vangalaiyo/T1_BATCH_024_025.md`

Scan 24 contains one deliberately unresolved dialogue span. Do **not** solve it during this T1 batch; it belongs to the later Stage-2 historical-glyph / difficult-reading pass.

## User-requested small-task rule

Keep the work in small durable units so commits and synchronization happen before the execution window is exhausted.

Planned sequence:

1. T1 scans 24–25 — **DONE**
2. T1 scans 26–27 — **CURRENT**
3. T1 scans 28–29
4. T1 scans 30–31 + boundary check
5. Stage 2 scans 24–27
6. Stage 2 scans 28–31
7. Stage 3 + Stage 4 closure

## Exact next activity

Process **only scans 26–27 / printed pages 24–25**:

1. fetch live `main`;
2. read the two direct source scans at native / enlarged resolution;
3. create:
   - `pages/0026-vilaiyal-vangalaiyo-03.md`
   - `pages/0027-vilaiyal-vangalaiyo-04.md`
   - a durable `T1_BATCH_026_027.md` checkpoint;
4. use `status: partial`; do not promote T1 pages to verified;
5. preserve source wording / punctuation / paragraphing exactly;
6. if any cluster is uncertain, document it rather than guessing;
7. update `README.md`, page map, collection trackers, root `HANDOVER.md`, and this prompt;
8. commit / synchronize;
9. **stop after scan 27**. Do not begin scans 28–29 in the same activity.

Historical-glyph verification will be a separate later stage using the user-supplied `HISTORICAL_TAMIL_GLYPH_TRANSCRIPTION_GUIDE.md`.
