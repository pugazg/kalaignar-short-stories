# Four-Stage Batch Transcription / Verification Workflow

This is the default execution workflow for source-page batches in `pugazg/kalaignar-short-stories` unless the user explicitly overrides it.

It complements `SHORT_STORY_PROCESSING_GUIDE.md` and `HISTORICAL_TAMIL_GLYPH_TRANSCRIPTION_GUIDE.md`.

## Core cadence

Every physical-page batch is processed as **four separate durable activities**, each followed by control synchronization and a commit:

`Stage 1 first-pass transcription → COMMIT/SYNC → Stage 2 visual text-fidelity audit → COMMIT/SYNC → Stage 3 historical-glyph audit → COMMIT/SYNC → Stage 4 final independent check → COMMIT/SYNC`

Only after Stage 4 closes may the batch be treated as fully `verified`.

## Why the stages are separate

The purpose is to avoid mixing fast capture, detailed fidelity checking, historical-glyph decoding and final approval into one oversized activity.

- Stage 1 captures the source text without waiting for perfect visual adjudication.
- Stage 2 checks ordinary textual fidelity independently.
- Stage 3 isolates historical Tamil glyph risk.
- Stage 4 performs one fresh end-to-end source check before final verification.

A rendering/enlargement problem in a later verification stage must **not** delay a responsible Stage-1 transcription checkpoint.

## Batch size

Use the story/work-specific batch size already recorded in its controls. If none is recorded, five physical scans is the default.

---

## Stage 1 — first-pass transcription

This is the initial source-faithful capture.

1. Re-fetch live `main`.
2. Open the controlling source pages.
3. Transcribe each whole page once from the source.
4. Preserve source wording, paragraphing, dialogue structure, punctuation, spacing, spelling and page boundaries as read.
5. Clearly readable historical characters may be encoded correctly, but do **not** run the systematic historical-glyph audit here.
6. Do **not** require high-resolution/crop work for every doubtful character before committing Stage 1.
7. If a reading is genuinely uncertain, preserve an explicit review marker/note rather than guessing.
8. Set transcribed pages to `needs-review`.
9. Synchronize page records, page map, progress tracker, README/audit, `HANDOVER.md` and `NEXT_CHAT_PROMPT.md`.
10. Commit Stage 1 and stop.

**Stage 1 objective:** get a complete first-pass transcription durably committed. Do not hold the whole batch waiting for later fidelity/glyph work.

---

## Stage 2 — visual text-fidelity audit

This is a separate source-vs-transcription comparison after Stage 1 is committed.

1. Re-fetch live `main`.
2. Reopen the same pages.
3. Compare the committed transcription against the source **line by line / phrase by phrase**.
4. Check ordinary textual fidelity:
   - omissions or duplicated text;
   - wrong words/letters;
   - punctuation;
   - paragraph/dialogue boundaries;
   - page-boundary continuations;
   - headings, separators and source marks;
   - accidental modernization/normalization.
5. Use enlargement/crops or non-destructive image processing only where the normal view is insufficient.
6. Correct only what source evidence supports.
7. Record unresolved source-sensitive locations explicitly.
8. Keep pages `needs-review`; Stage 2 does **not** close the historical-glyph gate.
9. Synchronize all relevant controls.
10. Commit Stage 2 and stop.

---

## Stage 3 — historical Tamil glyph audit

This is the independent glyph-focused pass.

1. Re-fetch live `main`.
2. Reopen the same pages independently.
3. Explicitly audit:
   `ணா / ணை / ணொ / ணோ / லை / ளை / றா / றொ / றோ / னா / னை / னொ / னோ`.
4. Compare whole words/phrases and same-edition forms when needed; never infer from a single isolated stroke if the cluster is ambiguous.
5. Correct character identity only where source evidence supports it; do not modernize spelling or grammar.
6. Never global-replace.
7. Use crops/native enlargement only for actual glyph ambiguity.
8. Keep pages `needs-review` until Stage 4.
9. Synchronize the glyph gate, possible-error queue and all affected controls.
10. Commit Stage 3 and stop.

---

## Stage 4 — final independent source check

This is the final approval pass.

1. Re-fetch live `main`.
2. Reopen the complete batch fresh, starting from the Stage-3 committed text.
3. Perform one final end-to-end comparison against the controlling source.
4. Confirm:
   - no omissions or duplications;
   - all page boundaries and continuations are correct;
   - text, punctuation and paragraphing remain source-faithful;
   - all Stage-2 and Stage-3 corrections are reflected;
   - all recorded uncertainties have a disposition;
   - no historical-glyph candidate remains unaudited;
   - source marks/separators/ending ornaments are handled correctly.
5. If a real issue is found, correct it and document it.
6. Promote pages to `verified` only when the final check closes with no unresolved source-text issue.
7. Synchronize page map, trackers, README/audit, handover and next prompt.
8. Commit Stage 4 and re-fetch live `main` to prove durability.
9. Only then advance to the next batch.

---

## Batch progression rule

Normal sequence:

`Batch N Stage 1 → COMMIT → Stage 2 → COMMIT → Stage 3 → COMMIT → Stage 4 → COMMIT → Batch N+1 Stage 1`

Do not skip directly from first-pass transcription to historical-glyph closure. Do not begin the next batch until the current batch's Stage 4 closes unless the user explicitly changes the workflow.

## Status semantics

- `not-started` — no Stage-1 transcription.
- `partial` — Stage-1 transcription incomplete.
- `needs-review` — Stage 1 is present but one or more of Stages 2–4 remain, or a genuine ambiguity remains.
- `verified` — all four stages completed and final source check passed.
- `blocked` — only after exhaustive source-resolution escalation genuinely fails.

## Crop / enhancement threshold

The default first-pass transcription does **not** require image enhancement.

Use enlargement/crops primarily in Stages 2–4 when:

- ordinary visual comparison cannot settle a character/word;
- faint ink, bleed-through, stamps, touching type or scan damage obstructs reading;
- a historical glyph is genuinely ambiguous;
- the final check identifies a concrete suspicious span.

## Commit / sync rule

Every stage must end in:

1. affected page records updated;
2. progress/gate files synchronized;
3. story/collection status synchronized where relevant;
4. root `HANDOVER.md` and `NEXT_CHAT_PROMPT.md` updated;
5. one focused commit;
6. stop/report before the next stage unless the user explicitly authorizes combined execution.

The working activity should produce the durable checkpoint first and narrate only the concise result.
