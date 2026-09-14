# NEXT CHAT PROMPT — `விலையால் வாங்கலையோ` / T1 scans 28–29

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

The canonical identity / duplicate check is closed: no pre-existing canonical work matched the exact title, transliterations, `வைரக்கண்ணு`, or distinctive opening dialogue.

T1 first-pass transcription:

- scans **24–25 / printed 22–23** — **COMPLETE / COMMITTED**
- scans **26–27 / printed 24–25** — **COMPLETE / COMMITTED**
- scans **28–31 / printed 26–29** — not started
- cumulative T1: **4/8**
- verified pages: **0/8**
- Stage 2–4: not started
- English: blocked

Durable checkpoints:

- `stories/vilaiyal-vangalaiyo/T1_BATCH_024_025.md`
- `stories/vilaiyal-vangalaiyo/T1_BATCH_026_027.md`

Known T1 review points are intentionally unresolved / provisional and must wait for Stage 2. In particular, do not normalize scan-27 apparent `நன்றுக`; the historical-`றா` family must be checked against the user-supplied `HISTORICAL_TAMIL_GLYPH_TRANSCRIPTION_GUIDE.md`.

## Small-task rule

Keep every unit small enough to commit and synchronize before continuing:

1. T1 scans 24–25 — **DONE**
2. T1 scans 26–27 — **DONE**
3. T1 scans 28–29 — **CURRENT**
4. T1 scans 30–31 + boundary check
5. Stage 2 scans 24–27
6. Stage 2 scans 28–31
7. Stage 3 + Stage 4 closure

## Exact next activity

Process **only scans 28–29 / printed pages 26–27**:

1. fetch live `main`;
2. read the two direct source scans at native / enlarged resolution;
3. create:
   - `pages/0028-vilaiyal-vangalaiyo-05.md`
   - `pages/0029-vilaiyal-vangalaiyo-06.md`
   - `T1_BATCH_028_029.md`;
4. use `status: partial`; do not promote T1 pages to verified;
5. preserve source wording, punctuation, paragraphing and old forms;
6. record uncertain clusters instead of guessing;
7. update story README / page map, collection README / inventory, root `HANDOVER.md`, and this prompt;
8. commit / synchronize;
9. **stop after scan 29**. Do not begin scans 30–31 in the same activity.

Historical-glyph verification remains a later independent stage using the user-supplied guide.
