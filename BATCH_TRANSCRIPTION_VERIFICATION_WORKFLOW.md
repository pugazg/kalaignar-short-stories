# Two-Stage Batch Transcription / Verification Workflow

This is the default execution workflow for source-page batches in `pugazg/kalaignar-short-stories` unless the user explicitly overrides it.

It complements `SHORT_STORY_PROCESSING_GUIDE.md` and `HISTORICAL_TAMIL_GLYPH_TRANSCRIPTION_GUIDE.md`. It changes **when** the two passes are executed and committed; it does **not** weaken source fidelity, historical-glyph requirements, difficult-reading escalation, or final verification gates.

## Why this workflow exists

Do not combine direct transcription, independent glyph verification, difficult-reading enhancement, control synchronization, and final closure into one oversized activity when they can be made durable in smaller stages.

The objective is:

- finish useful work sooner;
- commit completed work before a long verification pass begins;
- keep the historical-glyph second pass genuinely independent;
- avoid repeatedly reopening already-clear source text;
- use crops/enhancements only when the source actually requires them.

## Batch size

Use the story/work-specific batch size already recorded in its controls. If no special size is recorded, a small batch such as five physical scans is preferred.

Each batch has **two separate durable activities**.

---

## Stage A — direct transcription

Stage A is one bounded activity and one durable checkpoint.

1. Re-fetch live `main`; live `main` remains authoritative.
2. Resolve the controlling scan/PDF.
3. Read each requested **whole page directly from the source** and transcribe it once.
4. Preserve source punctuation, spacing, paragraphing, spelling, source-odd words, page boundaries and clearly identifiable historical character identity.
5. **Do not run the systematic 13-family Historical Tamil Glyph Pass 2 during Stage A.**
6. **Do not repeatedly reopen already-clear words or pages during Stage A.**
7. **Do not create crops/enhancements routinely.** Use a minimal enlargement only when a reading is genuinely too unclear to transcribe responsibly from the normal source view. If it still cannot be settled without a dedicated verification exercise, record the uncertainty instead of turning Stage A into Stage B.
8. An obvious historical glyph may be encoded correctly when its identity is clear during transcription; that does not count as Pass 2 closure.
9. After direct transcription, the page normally remains `needs-review`; Stage A alone must not promote a story-text page to final `verified` when the independent glyph gate applies.
10. Synchronize the page records and **Pass-1/current-state controls only**: page map, Pass-1 tracker, README/audit/handover/NEXT prompt as required by the active work.
11. Commit Stage A before beginning the independent glyph pass.
12. Stop and report the durable result. Do not continue into Stage B in the same activity unless the user explicitly asks to combine them.

A normal Stage-A report should be short: batch, number transcribed, unresolved count, commit, and the next exact activity.

---

## Stage B — independent historical-glyph / source verification

Stage B is a **separate activity after the Stage-A commit is durable**.

1. Re-fetch live `main` and start from the committed Stage-A transcription.
2. Reopen the same physical pages independently.
3. Perform the mandatory historical-glyph second pass, explicitly checking:

   `ணா / ணை / ணொ / ணோ / லை / ளை / றா / றொ / றோ / னா / னை / னொ / னோ`

4. Also inspect any locations recorded as source-sensitive or uncertain in Stage A.
5. **Do not perform a full retranscription merely because Stage B has begun.** Compare the committed text against the source and correct only where source evidence requires it.
6. Create crops, native-pixel enlargements, contrast variants or other enhancements **only for an actual unresolved/suspicious character cluster**. An unusual but clearly printed source word is not, by itself, a reason to crop or modernize it.
7. Record corrections individually; never global-replace.
8. If ambiguity remains, keep the affected page `needs-review` and follow the documented difficult-reading escalation rules.
9. Promote a page to `verified` only when direct transcription and the independent source/glyph verification both close.
10. Synchronize glyph gate, possible-error queue, page map, Pass-1/verification trackers, README/audit/handover/NEXT prompt and any other affected controls.
11. Commit Stage B and re-fetch live `main` to prove durability.
12. Stop and report the corrections/unresolved counts and next exact activity.

---

## Batch progression rule

For a normal batch sequence:

`Batch N Stage A → COMMIT → Batch N Stage B → COMMIT → Batch N+1 Stage A`

Do **not** begin the next batch merely because Stage A of the current batch is complete. The current batch's Stage B must close first unless the user explicitly changes the workflow.

## Crop / enhancement threshold

The default is **no crop**.

Use crops/enhancement only when at least one of these is true:

- character identity cannot be responsibly settled at normal/native page view;
- a historical glyph family is genuinely ambiguous;
- ink damage, bleed-through, stamp, touching type, faint vowel mark or scan damage prevents a confident reading;
- Stage B finds a concrete mismatch between transcription and source that requires closer inspection.

Do not crop merely because:

- a word is archaic or unusual;
- grammar looks odd;
- the source differs from modern spelling;
- a word contains one of the 13 historical-glyph families but is already clearly readable.

## Status semantics under this workflow

- `not-started` — no direct transcription yet;
- `needs-review` — Stage A transcription exists but independent verification is still pending, or a real ambiguity remains;
- `verified` — Stage A plus independent Stage B both closed;
- `blocked` — only after the repository's exhaustive difficult-reading escalation has genuinely failed.

## Turn / activity discipline

The working activity should prioritize producing the durable checkpoint, not narrating every inspection step.

- Perform the bounded stage.
- Synchronize required controls.
- Commit.
- Re-fetch when required by closure rules.
- Report the result concisely.

If an activity cannot finish, record exactly what is durable and make the unfinished stage—not a later stage—the next exact activity.
