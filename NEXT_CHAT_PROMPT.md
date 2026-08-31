# NEXT CHAT PROMPT — Kalaignar Short Stories Archive

Continue the **Kalaignar Short Stories archival project** directly in:

`https://github.com/pugazg/kalaignar-short-stories`

Branch: `main`

Use the GitHub connector and work directly on `main`.

Controlling anthology source:

`TVA_BOK_0064142_கலைஞர்_கருணாநிதியின்_சிறுகதைகள்.pdf`

Attach / resolve the controlling PDF before source-dependent visual checking.

## LIVE MAIN IS AUTHORITATIVE

Fetch live `main` first. If it has advanced beyond any checkpoint copied into this prompt, preserve the newer durable state and continue from it.

## MANDATORY STARTUP

Read completely before making project changes:

1. `SHORT_STORY_PROCESSING_GUIDE.md`
2. `COLLECTION_SOURCE_GUIDE.md`
3. `VISUAL_FIDELITY_CHECK_GUIDE.md`
4. `VISUAL_FIDELITY_PROGRESS.md`
5. `HANDOVER.md`
6. `NEXT_CHAT_PROMPT.md`
7. collection `README.md`
8. collection `indexes/story-inventory.md`
9. collection `indexes/scan-map.md`

Then inspect the active story's existing page records, Tamil assembly, audit and page map.

## DURABLE COMPLETED MILESTONE

The 1977 anthology Tamil source-text pass is fully complete:

- stories registered: **37 / 37**
- Tamil source processing: **37 / 37 complete**
- untranscribed stories: **0 / 37**
- story-text coverage: scans **10–259 / printed pages 1–250**
- scan **260**: verified back cover
- all 37 canonical anthology story workspaces have complete Tamil assemblies and audits
- all 37 have **0 blocked / 0 unresolved story text**
- English translation from the anthology: **0 / 37 started**

Do not redo the completed Tamil source pass unless new source-supported correction evidence appears during the visual-fidelity phase.

## USER-AUTHORIZED CURRENT PHASE — VISUAL FIDELITY CHECK

The user explicitly authorized **visual fidelity check** as the next phase.

Follow `VISUAL_FIDELITY_CHECK_GUIDE.md`.

The check covers source-significant visual structure such as:

- story headings and opening/ending roles;
- paragraph boundaries and dialogue separation;
- verse / song / display-line lineation;
- intentional display emphasis or structural lead-ins;
- opening rules, closing ornaments, illustrations and captions where source-significant;
- page joins and story boundaries;
- correct exclusion of running headers and printed page numbers from story body.

It does not require facsimile recreation of fonts, exact prose line wraps, margins, paper colour or scan defects.

If a visual check reveals a textual error, apply the permanent source rules: verify the complete source span, correct only what the scan supports, and propagate the correction through affected layers.

## VISUAL-FIDELITY PHASE STATE

See `VISUAL_FIDELITY_PROGRESS.md`.

Current durable state:

- complete: **0 / 37**
- pending: **37 / 37**
- needs recheck: **0**

## NEXT EXACT ACTIVITY — STORY 1 ONLY

Perform the visual fidelity check for Story 1 — **`புகழேந்தி`**.

Canonical workspace:

`stories/pugazhendhi/`

Source coordinates:

- printed pages **1–6**
- anthology scans **10–15**
- scan **16** is the boundary witness and opens Story 2 `நளாயினி`

Required activity when I say **“Proceed with next activity”**:

1. Fetch live `main` and preserve newer work.
2. Inspect source scans **10–15** directly.
3. Compare every page with the committed page record and Tamil assembly.
4. Check opening heading/rule, paragraph structure, dialogue/display lines, source-significant emphasis, page-role metadata, non-text marks, all physical joins, and the ending ornament.
5. Inspect scan **16** only as the next-story boundary witness.
6. Correct any source-significant structural mismatch found. If wording itself is wrong, use the full-span source-verification rules before correction.
7. Create `stories/pugazhendhi/visual-fidelity.md` with findings and result.
8. Update `VISUAL_FIDELITY_PROGRESS.md`.
9. Update `HANDOVER.md` and `NEXT_CHAT_PROMPT.md` to Story 2 only after Story 1 visual fidelity is fully closed.
10. Re-fetch live `main` and changed controls before declaring closure.
11. **Do not start Story 2 in the same activity.**

Expected result: **1 / 37 visual-fidelity complete, 36 remaining**.

## PHASE GUARD

Do not begin English translation, modernization, republication or another downstream phase during visual-fidelity work unless separately authorized by the user or mandated by newer live repository state.

## CONTROLLING-SOURCE RULES

The supplied scan remains the controlling textual authority. Do not silently modernize spelling, punctuation, grammar, sandhi, names, paragraphs, title forms or source anomalies. Do not guess unclear Tamil from context, OCR, memory or another edition. Older Tamil glyph shapes must be checked against the source typeface and full surrounding span. Do not commit the PDF or generated renders/crops.
