# NEXT CHAT PROMPT — `விலையால் வாங்கலையோ` / Stage 4 Tamil assembly + controls

Continue in `pugazg/kalaignar-short-stories`, branch `main`. **LIVE MAIN IS AUTHORITATIVE.**

## Controlling source

`TVA_BOK_0064098_தப்பிவிட்டார்கள்.pdf`

- collection: **தப்பிவிட்டார்கள்**
- edition: **நான்காம் பதிப்பு — ஆகஸ்ட் '53**
- story: **விலையால் வாங்கலையோ**
- canonical route: `stories/vilaiyal-vangalaiyo/`
- story scans: **24–31 / printed 22–29**
- scan 32 / printed 30: boundary witness opening `முந்நூறு ரூபாய்`

## Durable state

- T1 first-pass: **8/8 COMPLETE**
- Stage 2 historical-glyph / difficult-reading audit: **8/8 COMPLETE / PASS**
- Stage 3 final source / visual-fidelity audit: **8/8 COMPLETE / PASS**
- page records: **VERIFIED 8/8**
- unresolved source readings: **0**
- Stage-2 cumulative repairs: **30** occurrence-level textual repairs, including **9** historical-character identity corrections / resolutions
- Stage-3 cumulative final corrections: **13**
- Stage 4 Tamil assembly / controls: **NOT STARTED**
- English: **BLOCKED until Tamil/source closure**

Stage-3 checkpoints:

- `stories/vilaiyal-vangalaiyo/STAGE3_BATCH_024_027.md`
- `stories/vilaiyal-vangalaiyo/STAGE3_BATCH_028_031.md`

Stage-3 scans 28–31 final corrections included:

- scan 28: `வெளியாயிற்று`; `கவலைப் படவே யில்லை`;
- scan 29: `கடைப் பையனிடம்`;
- scan 30: source punctuation spacing in `சப் இன்ஸ்பெக்டரும்,வைரக்கண்ணும்,வேடிக்கை` and `ஆரம்பித்தது,சப்`;
- scan 31: restored omitted `என்ன` in `அவன் மனதில் என்ன எண்ணம் தோன்றிற்று`; source comma after `லக்ஷ்மி பிணமாகக் கிடந்தாள்,`; source `திருடன்!கொலைகாரன்!`.

## Exact next activity

Process **Stage 4 Tamil assembly / controls only**.

1. Fetch live `main`.
2. Read all 8 verified page records in scan order 24→31.
3. Create / update the canonical reading layer under `stories/vilaiyal-vangalaiyo/sections/` using only the verified page text.
4. Preserve all source wording, punctuation, paragraphing, internal three-circle dividers and story-ending wording.
5. Add explicit page provenance markers for all 8 scans so scan / printed-page traceability remains durable.
6. Validate scan sequence **24–31 exactly once** and printed pages **22–29 exactly once**.
7. Validate physical continuations:
   - scan 24→25: `இனி அந்த வாட்டுப் பயல்` → `இந்த ஊர்திரும்ப மாட்டான்.`
   - scan 29→30: `சொன்` → `ணன்.`
   - scan 30→31: `சப் இன்ஸ்பெக்டர் சரியானபடி` → `ஏமாற்றப்போகிறார் என்று...`
8. Validate internal three-circle dividers and final story-ending boundary.
9. Confirm scan 32 is excluded and opens `முந்நூறு ரூபாய்`.
10. Create the Tamil/source closure control file and any audit / review control files required by the repository guide.
11. Update story README / page map, collection README / inventory, root `HANDOVER.md`, and this prompt.
12. Commit / synchronize.
13. **Stop after Tamil/source closure. Do not begin English in the same activity.**

Story 4 `முந்நூறு ரூபாய்` remains untouched.
