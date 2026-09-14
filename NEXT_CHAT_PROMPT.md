# NEXT CHAT PROMPT — `விலையால் வாங்கலையோ` / English batch scans 24–27

Continue in `pugazg/kalaignar-short-stories`, branch `main`. **LIVE MAIN IS AUTHORITATIVE.**

## Phase transition

The 1953 `தப்பிவிட்டார்கள்` collection-wide Tamil/source phase is now **CLOSED / PASS**.

All four stories are dispositioned:

1. `தப்பிவிட்டார்கள்` — witness **CLOSED / PASS 9/9**
2. `சபலம்` — witness **CLOSED / PASS 8/8**
3. `விலையால் வாங்கலையோ` — canonical Tamil/source **CLOSED / PASS 8/8**
4. `முந்நூறு ரூபாய்` — witness **CLOSED / PASS 3/3**

Collection-wide unresolved source-dependent items: **0**.

Under `COLLECTION_SOURCE_GUIDE.md` and `ENGLISH_TRANSLATION_GUIDE.md`, English translation for the new canonical Story 3 `விலையால் வாங்கலையோ` is the automatic next phase.

## Tamil authority

Canonical story:

`stories/vilaiyal-vangalaiyo/`

Verified Tamil assembly:

`stories/vilaiyal-vangalaiyo/sections/vilaiyal-vangalaiyo.md`

Source closure:

`stories/vilaiyal-vangalaiyo/TAMIL_SOURCE_CLOSURE.md`

Review queue:

`stories/vilaiyal-vangalaiyo/POSSIBLE_ERRORS_FOR_REVIEW.md` — **0 open**

Tamil/source state:

- source scans **24–31 / printed 22–29**
- verified page records: **8/8**
- unresolved Tamil readings: **0**
- Stage 4 Tamil/source closure: **PASS / CLOSED**
- Tamil must not be changed merely to improve English

## English workflow authority

Read before translating:

- `ENGLISH_TRANSLATION_GUIDE.md`
- `SHORT_STORY_PROCESSING_GUIDE.md`
- `COLLECTION_SOURCE_GUIDE.md`
- root `HANDOVER.md`
- this prompt
- 1953 collection README / inventory
- story README / Tamil assembly / source closure / review queue / page map
- verified Tamil page records for the active batch

Translation path:

`stories/vilaiyal-vangalaiyo/translations/en/vilaiyal-vangalaiyo.md`

Review path:

`stories/vilaiyal-vangalaiyo/TRANSLATION_REVIEW.md`

Collection tracker to create / initialize:

`collections/1953-thappivittargal/ENGLISH_TRANSLATION_PROGRESS.md`

## User-requested small-durable-task rule

Keep English work in small committed units so translation / traceability state is synchronized before the execution window is exhausted.

Planned English drafting sequence:

1. scans **24–27 / printed 22–25** — **CURRENT**
2. scans **28–31 / printed 26–29**
3. full-story English fidelity / terminology review
4. physical page-anchor validation / final translation closure

Do not translate scans 28–31 in the current activity.

## Exact next activity

Process **English translation only for verified Tamil scans 24–27 / printed 22–25**.

1. Fetch live `main`.
2. Read the English guide and all controlling Tamil / source controls listed above.
3. Read verified Tamil page records:
   - `pages/0024-vilaiyal-vangalaiyo-01.md`
   - `pages/0025-vilaiyal-vangalaiyo-02.md`
   - `pages/0026-vilaiyal-vangalaiyo-03.md`
   - `pages/0027-vilaiyal-vangalaiyo-04.md`
4. Initialize `translations/en/vilaiyal-vangalaiyo.md`.
5. Use a conservative title treatment; transliteration **Vilaiyal Vangalaiyo** is acceptable for the draft and must be documented in `TRANSLATION_REVIEW.md`.
6. Translate the complete verified Tamil content of scans **24–27 only**.
7. Preserve dialogue, paragraph order, rhetorical repetition and the scan-25 internal three-circle divider as meaningful structure.
8. Retain source-page provenance markers at the exact verified Tamil physical boundaries:
   - source scan 24 / printed 22
   - source scan 25 / printed 23
   - source scan 26 / printed 24
   - source scan 27 / printed 25
9. Do not translate running headers / printed page numbers / audit notes.
10. Do not import 1953 witness-vs-1977 comparison wording from other stories; this translation follows only the verified canonical Tamil for `விலையால் வாங்கலையோ`.
11. If English exposes a likely Tamil issue, stop that span and reopen the Tamil only under the source guide; do not correct Tamil from English expectation.
12. Initialize `TRANSLATION_REVIEW.md` as **IN PROGRESS**, documenting title treatment, source range, Tamil authority, difficult terms / cultural choices encountered in scans 24–27, and confirmation that Tamil was not silently changed.
13. Initialize collection `ENGLISH_TRANSLATION_PROGRESS.md`:
    - `விலையால் வாங்கலையோ` — **in progress 4/8**
    - other three 1953 stories — **not canonical English targets; their canonical English remains controlled by their existing canonical editions**
14. Update story README, collection README / inventory, root `HANDOVER.md`, and this prompt.
15. Commit / synchronize.
16. **Stop after scan 27. Do not begin scans 28–31 in the same activity.**

The next batch after this will be English scans **28–31 / printed 26–29**.
