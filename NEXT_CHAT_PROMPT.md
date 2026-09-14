# NEXT CHAT PROMPT — `விலையால் வாங்கலையோ` / Stage 2 scans 28–31

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

For historical-glyph decoding use the user-supplied:

`HISTORICAL_TAMIL_GLYPH_TRANSCRIPTION_GUIDE.md`

Do not use OCR, web text or another edition as textual authority.

## Durable state

- T1: **8/8 COMPLETE**
- Stage 2: **4/8 COMPLETE / PASS — scans 24–27**
- scans 24–27 page status: **needs-review 4/4**
- scans 28–31 page status: **partial 4/4**
- verified pages: **0/8**
- Stage 3–4: not started
- English: blocked

Stage-2 checkpoint:

`stories/vilaiyal-vangalaiyo/STAGE2_BATCH_024_027.md`

Stage-2 scans 24–27 result:

- **14 occurrence-level textual repairs**;
- **1 historical-character correction**: apparent `நன்றுக` → source-supported `நன்றாக` (`றா` family);
- unresolved Stage-2 glyph clusters: **0**;
- previously unresolved text on scans 24, 26 and 27 was resolved only from direct pixels.

## Small-task rule

Keep every unit small enough to commit and synchronize:

1. T1 scans 24–31 + boundary — **DONE**
2. Stage 2 scans 24–27 — **DONE / PASS**
3. Stage 2 scans 28–31 — **CURRENT**
4. Stage 3 final source / visual-fidelity audit
5. Stage 4 assembly / controls

## Exact next activity

Process **Stage 2 only for scans 28–31 / printed 26–29**.

1. Fetch live `main`.
2. Read the four existing page records for scans 28–31 and their T1 checkpoints.
3. Read the user-supplied historical-glyph guide.
4. Reopen scans 28–31 at native / enlarged resolution.
5. Check all 13 known historical glyph families on every page.
6. Resolve T1 review points only when the source pixels support the full cluster / phrase.
7. Record every correction separately; distinguish historical-character corrections from ordinary source-fidelity corrections.
8. Leave genuinely uncertain readings explicit rather than guessing.
9. Create `STAGE2_BATCH_028_031.md`.
10. Update page statuses to `needs-review` only when their Stage-2 audit is complete.
11. Update story / collection / root trackers and this prompt.
12. Commit / synchronize.
13. **Stop after scan 31. Do not start Stage 3 in the same activity.**

Known T1 review points in this batch include:

- scan 28 — unresolved short dialogue after `“இல்...லை.”`; `வளையல்களைக்` / `வளையல்களையும்`; source spacing around `செல்லவேண்டு மென்ற`; `புதுஒளி`;
- scan 29 — unresolved short clause before `குயிலிசை கிளம்பிற்று.`; `நாட்டு சோக்காளி`; `நூறு ரூபாய்கூடப் பெறுமானமில்லை`; historical `ளை` clusters; page-ending `சொன்` continuing to scan 30;
- scan 30 — `நாழிகை`; `குற்றஞ் சாட்டப்பட்டான்`; `புறப்படும்`; lower-dialogue physical circular losses; historical-family sweep;
- scan 31 — `பதிலவரவில்லை`; `எழுப்பினன்`; `அலறினன்`; `ஆடினன்`; `சண்டமாருத`; `கூறினர்களிப்படி`; the long explanatory sentence; closing phrase `விலையால் வாங்கலையோ வளையல்`; circular physical losses.

Story 4 `முந்நூறு ரூபாய்` remains untouched.
