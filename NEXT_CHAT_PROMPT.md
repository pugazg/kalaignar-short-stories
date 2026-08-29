# NEXT CHAT PROMPT — Kalaignar Short Stories Archive

Copy the prompt below into a new chat window. **Attach the controlling anthology PDF again in that chat** before asking it to perform source-dependent transcription or visual verification.

---

Continue the **Kalaignar Short Stories archival project** directly in:

`https://github.com/pugazg/kalaignar-short-stories`

Branch: `main`

Use the GitHub connector and work directly on `main`.

The controlling anthology source is:

`TVA_BOK_0064142_கலைஞர்_கருணாநிதியின்_சிறுகதைகள்.pdf`

I am attaching / making that exact PDF available in this new chat. Do **not** commit the source PDF to GitHub.

## AUTHORITATIVE STATE

Treat **live GitHub `main` as authoritative**. Fetch the live HEAD before doing anything else. If `main` has advanced beyond the state described here, use the newer live state and do not revert completed work.

Durable state when this handoff was prepared:

- anthology: **கலைஞர் கருணாநிதியின் சிறுகதைகள்**, first edition 1977;
- 37 stories registered;
- Tamil source processing complete: **6 / 37**;
- completed anthology stories:
  1. `புகழேந்தி` — scans 10–15 / printed 1–6 — 6/6 verified;
  2. `நளாயினி` — scans 16–23 / printed 7–14 — 8/8 verified;
  3. `சபலம்` — scans 24–30 / printed 15–21 — 7/7 verified;
  4. `ஆட்டக்காவடி` — scans 31–38 / printed 22–29 — 8/8 verified;
  5. `குப்பைத்தொட்டி` — scans 39–46 / printed 30–37 — 8/8 verified;
  6. `சந்தனக்கிண்ணம்` — scans 47–56 / printed 38–47 — 10/10 verified;
- all six completed anthology stories have **0 blocked / 0 unresolved story text** and persistent `POSSIBLE_ERRORS_FOR_REVIEW.md` queues;
- English translation has not been started for these anthology stories;
- independent story `கிழவன் கனவு` remains complete.

## MANDATORY STARTUP — READ COMPLETELY BEFORE WRITES

After fetching live `main`, read completely:

1. `SHORT_STORY_PROCESSING_GUIDE.md`
2. `COLLECTION_SOURCE_GUIDE.md`
3. `HANDOVER.md`
4. `NEXT_CHAT_PROMPT.md`
5. `collections/1977-kalaignar-karunanidhiyin-sirukathaigal/README.md`
6. `collections/1977-kalaignar-karunanidhiyin-sirukathaigal/indexes/story-inventory.md`
7. `collections/1977-kalaignar-karunanidhiyin-sirukathaigal/indexes/scan-map.md`

Then inspect the latest completed story as the immediate structural reference:

8. `stories/santhana-kinnam/README.md`
9. `stories/santhana-kinnam/metadata/source.md`
10. `stories/santhana-kinnam/indexes/page-map.md`
11. `stories/santhana-kinnam/audit.md`
12. `stories/santhana-kinnam/POSSIBLE_ERRORS_FOR_REVIEW.md`

Use Story 6 only as a structural/audit reference; do not copy its wording into Story 7.

## PERMANENT SOURCE RULES

- **The supplied scan is the controlling textual authority.**
- Do not silently modernize spelling, punctuation, grammar, sandhi, names, dates, numbers, paragraph structure or source anomalies.
- Do not guess unclear Tamil from context, memory, OCR, another edition or general knowledge.
- OCR/extracted text may assist navigation only.
- **No stones should be left unturned.** Before leaving story text unresolved, use native/high-resolution inspection, enlarged crops, alternate resampling/contrast/sharpening variants, character comparison and page-boundary checks as required.
- A plausible isolated crop is not enough for `verified`; verify the complete phrase/clause/sentence source span.
- `POSSIBLE_ERRORS_FOR_REVIEW.md` is a human-review queue, not a list of confirmed errors.
- Do not use `blocked` as a shortcut. Recover defensible readings without fabrication.
- Do not commit generated render/crop images or the controlling PDF.
- Use narrow, descriptive commits.

## NEXT EXACT ACTIVITY — STORY 7 ONLY

Process anthology Story **7 — `சங்கிலிச்சாமி`** only.

Exact range:

- printed pages: **48–59**
- anthology PDF scans: **57–68**

Required boundary checks:

- visually confirm scan **57** opens `சங்கிலிச்சாமி`;
- visually confirm scan **68** contains the end of Story 7;
- visually inspect scan **69** and confirm it begins Story 8 **`கங்கையின் காதல்`**;
- do not include any scan-69 Story 8 text in the Story 7 workspace.

### Required actions

1. Fetch live `main` and confirm there is no existing canonical `சங்கிலிச்சாமி` workspace under another slug/title. If one exists, attach this anthology as an additional witness instead of creating a duplicate.
2. Verify the scan 57 / 68 / 69 boundaries from the controlling PDF.
3. If no canonical workspace exists, create a stable Story 7 workspace only after source identity check.
4. Register the 1977 anthology and exact source coordinates in `metadata/source.md`.
5. Create **12 page records** for scans **57–68**, printed pages **48–59**.
6. Transcribe directly from the source scan page by page.
7. Run direct visual/full-span source-fidelity review on every page before marking it `verified`.
8. Exhaustively investigate difficult readings; do not stop at a first plausible crop.
9. Create and maintain `POSSIBLE_ERRORS_FOR_REVIEW.md` for unusual/easily misread but legible source readings.
10. Create/update story README, source metadata, page map, all 12 page records, assembled Tamil, audit and human-review queue.
11. Verify every physical page-boundary continuation across scans 57–68.
12. Before closing Story 7, confirm there are no omitted/duplicated pages and no unresolved markers that have not gone through the exhaustive protocol.
13. Synchronize after Story 7: collection story inventory, collection README, root README, scan map, `HANDOVER.md`, and `NEXT_CHAT_PROMPT.md`.
14. **Do not start Story 8 — `கங்கையின் காதல்` — in the same activity.**

## EXPECTED PROGRESS AFTER SUCCESSFUL STORY 7 CLOSURE

If Story 7 completes cleanly:

- Tamil source processing complete: **7 / 37**;
- not yet transcribed: **30 / 37**;
- next exact story: Story 8 `கங்கையின் காதல்`, printed pages **60–63**, scans **69–72**;
- advance to that activity only after Story 7 is fully synchronized and closed.

## USER COMMAND BEHAVIOUR

When I say **“Proceed with next activity”**, execute the exact next activity recorded in live `HANDOVER.md` / `NEXT_CHAT_PROMPT.md` directly. Do not ask me to choose a routine next step.

If the controlling PDF is not actually available in the new chat/tool context, stop source transcription rather than fabricating text from this prompt.

---

End of durable restart prompt.
