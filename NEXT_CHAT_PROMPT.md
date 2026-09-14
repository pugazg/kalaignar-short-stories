# NEXT CHAT PROMPT — `விலையால் வாங்கலையோ` / T1 scans 30–31 + boundary

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

T1 first-pass transcription:

- scans **24–25 / printed 22–23** — **COMPLETE / COMMITTED**
- scans **26–27 / printed 24–25** — **COMPLETE / COMMITTED**
- scans **28–29 / printed 26–27** — **COMPLETE / COMMITTED**
- scans **30–31 / printed 28–29** — not started
- cumulative T1: **6/8**
- verified pages: **0/8**
- Stage 2–4: not started
- English: blocked

Durable checkpoints:

- `stories/vilaiyal-vangalaiyo/T1_BATCH_024_025.md`
- `stories/vilaiyal-vangalaiyo/T1_BATCH_026_027.md`
- `stories/vilaiyal-vangalaiyo/T1_BATCH_028_029.md`

Known T1 review points remain provisional. Do not solve or normalize them during the final T1 batch; they belong to Stage 2 under the user-supplied `HISTORICAL_TAMIL_GLYPH_TRANSCRIPTION_GUIDE.md`.

## Small-task rule

Keep every unit small enough to commit and synchronize:

1. T1 scans 24–25 — **DONE**
2. T1 scans 26–27 — **DONE**
3. T1 scans 28–29 — **DONE**
4. T1 scans 30–31 + scan-32 boundary witness — **CURRENT**
5. Stage 2 scans 24–27
6. Stage 2 scans 28–31
7. Stage 3 + Stage 4 closure

## Exact next activity

Process only **scans 30–31 / printed pages 28–29**, then inspect **scan 32** only to confirm that `முந்நூறு ரூபாய்` begins there.

1. fetch live `main`;
2. read scans 30–31 at native / enlarged resolution;
3. create:
   - `pages/0030-vilaiyal-vangalaiyo-07.md`
   - `pages/0031-vilaiyal-vangalaiyo-08.md`
   - `T1_BATCH_030_031.md`;
4. keep `status: partial`; T1 does not promote pages to verified;
5. preserve source wording / punctuation / paragraphing / old forms;
6. record uncertain clusters instead of guessing;
7. inspect scan 32 only for the next-story heading / boundary; do **not** transcribe Story 4 body;
8. update story README / page map, collection README / inventory, root `HANDOVER.md`, and this prompt;
9. commit / synchronize;
10. stop with **T1 = 8/8 COMPLETE**. Do not start Stage 2 in the same activity.

After this checkpoint, the next activity becomes **Stage 2 historical-glyph / difficult-reading audit scans 24–27**.
