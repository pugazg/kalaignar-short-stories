# NEXT CHAT PROMPT — `விலையால் வாங்கலையோ` / final English page-anchor closure

Continue in `pugazg/kalaignar-short-stories`, branch `main`. **LIVE MAIN IS AUTHORITATIVE.**

## Durable state

The 1953 `தப்பிவிட்டார்கள்` Tamil/source phase is **CLOSED / PASS**.

`விலையால் வாங்கலையோ`:

- source scans: **24–31 / printed 22–29**
- verified Tamil pages: **8/8**
- Tamil assembly: `stories/vilaiyal-vangalaiyo/sections/vilaiyal-vangalaiyo.md`
- Tamil source closure: `stories/vilaiyal-vangalaiyo/TAMIL_SOURCE_CLOSURE.md`
- English path: `stories/vilaiyal-vangalaiyo/translations/en/vilaiyal-vangalaiyo.md`
- English review: `stories/vilaiyal-vangalaiyo/TRANSLATION_REVIEW.md`
- English tracker: `collections/1953-thappivittargal/ENGLISH_TRANSLATION_PROGRESS.md`
- English draft: **8/8 COMPLETE**
- full-story fidelity review: **PASS**
- terminology review: **PASS**
- reviewed English title: **Bought for a Price?**
- reviewed final refrain: **Was the bangle bought for a price?**
- English refinements in full-story review: **30**
- unresolved fidelity / terminology issues: **0**
- Tamil reopened during English: **No**
- current English phase: **IN PROGRESS only because final physical page-anchor validation is pending**

## Final-anchor authority

Read before work:

- `ENGLISH_TRANSLATION_GUIDE.md`, especially §8.1;
- `scripts/validate-english-page-anchors.py`;
- root `HANDOVER.md`;
- this prompt;
- `TRANSLATION_REVIEW.md`;
- all 8 verified Tamil `pages/*.md` records;
- complete reviewed English translation.

Do not use paragraph-count arithmetic as provenance evidence.

## Human-adjudicated boundary witnesses

Use the verified Tamil page records to reconfirm these English boundaries before writing the manifest:

| Scan | Printed | Expected English section start | Expected English section end |
|---:|---:|---|---|
| 24 | 22 | `“Why are you just sitting there with a newspaper in your hand?` | `That wretched fellow` |
| 25 | 23 | `won't come back to this town.` | `He read its closing passages twice.` |
| 26 | 24 | `“Society!......Fine society......rotten` | `The silence did not last long.` |
| 27 | 25 | `“You only wrote the letter yesterday.` | `He was thoroughly fooled.”` |
| 28 | 26 | `“Aththan.........from today, our life begins.”` | `seem no more than mounds of earth.` |
| 29 | 27 | `How many hardships had she endured for his love!` | `he sa` |
| 30 | 28 | `id something in Hindustani to his shop boy.` | `going to be thoroughly` |
| 31 | 29 | `fooled.` | `“Was the bangle bought for a price?”` |

The scan 29→30 English `sa` → `id` split is deliberate because the verified Tamil physical page boundary splits `சொன்` → `ணன்.`.

## Exact next activity

Process **final physical page-anchor validation and English closure only**.

1. Fetch live `main`.
2. Re-read the 8 verified Tamil page records and the reviewed English file.
3. Reconfirm every boundary witness above against the current live files. If the reviewed English changed since this prompt, derive fresh anchors from live main rather than forcing stale strings.
4. Create:
   `stories/vilaiyal-vangalaiyo/translations/en/page-anchors.json`
   with:
   - `story`: `vilaiyal-vangalaiyo`
   - eight anchors in scan order 24→31,
   - `printed_page` 22→29,
   - `english_starts_with`,
   - `english_ends_with`.
5. Run the repository validator on the corrected state:
   `python3 scripts/validate-english-page-anchors.py stories/vilaiyal-vangalaiyo`
   Expected: **PASS with human-reviewed boundary anchors**.
6. Run the validator self-test if needed to confirm validator behavior:
   `python3 scripts/validate-english-page-anchors.py --self-test`.
7. Perform the mandatory regression proof required by the guide:
   - corrected state → **PASS**;
   - introduce a temporary shifted-marker / anchor-defect fixture equivalent to the prior class of error → **FAIL specifically because of page anchoring**;
   - restore corrected state → **PASS**.
   Do not commit the defective fixture.
8. Confirm all 8 English marker sections contain substantive translated content and scan 31 is non-empty.
9. Confirm marker scan sequence **24–31 exactly once** and printed pages **22–29 exactly once**.
10. Confirm all three three-open-circle dividers remain present.
11. Update `TRANSLATION_REVIEW.md` with final anchor results, validator outputs / regression result, and set overall translation result to **PASS** only if all checks succeed.
12. Update `ENGLISH_TRANSLATION_PROGRESS.md`: Story 3 → **PASS**; collection English phase → **CLOSED / PASS**.
13. Update story README, page map, collection README / inventory, root `HANDOVER.md`, and this prompt.
14. Commit / synchronize.
15. Re-fetch live `main` and changed controls; verify no `pending`, `in progress`, or `NEEDS REVIEW` English target remains in the 1953 collection.
16. **Stop after 1953 English closure. Do not begin another anthology in the same activity.**

If the validator or human anchor check fails, leave English **IN PROGRESS**, record the exact defect, repair it, and rerun the corrected → defect → restored proof before closure.
