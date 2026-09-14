# NEXT CHAT PROMPT — 1953 `தப்பிவிட்டார்கள்` / `முந்நூறு ரூபாய்` witness

Continue in `pugazg/kalaignar-short-stories`, branch `main`. **LIVE MAIN IS AUTHORITATIVE.**

## Controlling anthology source

Use only the attached:

`TVA_BOK_0064098_தப்பிவிட்டார்கள்.pdf`

Source identity:

- edition: **நான்காம் பதிப்பு — ஆகஸ்ட் '53**
- physical scans: **34**
- source type: **image-only**
- source authority: **direct scan pixels**
- pagination relation for story pages: **scan = printed page + 2**

Do not use OCR, web text or another edition as authority for the 1953 witness wording.

## Collection durable state

Workspace:

`collections/1953-thappivittargal/`

1. `தப்பிவிட்டார்கள்` — witness **CLOSED / PASS 9/9**
2. `சபலம்` — witness **CLOSED / PASS 8/8**
3. `விலையால் வாங்கலையோ` — canonical **TAMIL/SOURCE CLOSED / PASS 8/8**
4. `முந்நூறு ரூபாய்` — witness **NOT STARTED / CURRENT**

Story 3 closure:

- reading layer: `stories/vilaiyal-vangalaiyo/sections/vilaiyal-vangalaiyo.md`
- closure: `stories/vilaiyal-vangalaiyo/TAMIL_SOURCE_CLOSURE.md`
- verified pages: **8/8**
- unresolved: **0**
- English: **deferred by collection-wide Tamil-first gate**

## Current target — Story 4 `முந்நூறு ரூபாய்`

1953 witness:

- scans **32–34**
- printed pages **30–32**
- total physical pages: **3**
- scan **34** is the final physical scan in the supplied anthology

Canonical route:

`stories/munnuru-rupai/`

1977 canonical authority:

- source: `TVA_BOK_0064142_கலைஞர்_கருணாநிதியின்_சிறுகதைகள்.pdf`
- canonical scans **112–114**
- printed pages **103–105**
- Tamil: **CURRENT PASS / CLOSED 3/3**
- English: **PASS / CLOSED**
- canonical unresolved source / glyph readings: **0 / 0**

Use the closed canonical page records / Tamil reading layer as the normal comparison authority. Reopen the exact 1977 controlling scan only if the 1953 witness exposes a genuine provenance/fidelity conflict that merits a canonical-recheck candidate.

## Exact next activity

Process the **entire 3-page 1953 witness** in this activity:

1. Fetch live `main`.
2. Read `SHORT_STORY_PROCESSING_GUIDE.md`, `COLLECTION_SOURCE_GUIDE.md`, root `HANDOVER.md`, this prompt, and the 1953 collection README/inventory.
3. Read the closed canonical `stories/munnuru-rupai/` README, canonical Tamil page records / section, and current audit status.
4. Inspect 1953 scans **32–34** directly at native / enlarged resolution.
5. Confirm scan 32 opening heading `முந்நூறு ரூபாய்`, scan 34 story ending, and that scan 34 is the anthology terminal page.
6. Create witness workspace:
   - `stories/munnuru-rupai/witnesses/1953-thappivittargal/README.md`
   - `stories/munnuru-rupai/witnesses/1953-thappivittargal/VARIANT_COMPARISON.md`
7. Compare the 1953 witness end-to-end with the 1977 canonical story.
8. Record wording, spelling, punctuation, layout and ending variants as edition evidence.
9. Do **not** change canonical Tamil or English merely because the 1953 reading differs.
10. Open a canonical-recheck candidate only if the current 1977 canonical reading itself becomes genuinely suspect.
11. Update `stories/munnuru-rupai/README.md`, the 1953 collection README/inventory, root `HANDOVER.md`, and this prompt.
12. If the witness closes with no source-dependent backlog, mark the 1953 collection's **Tamil/source phase CLOSED**.
13. Commit / synchronize.
14. **Stop after the witness / collection-wide Tamil-source closure. Do not begin English in the same activity.**

After collection-wide Tamil/source closure, the automatic next phase is English translation for the new canonical Story 3 `விலையால் வாங்கலையோ`, unless the user explicitly redirects.
