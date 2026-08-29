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

Treat **live GitHub `main` as authoritative**. Fetch the live HEAD before doing anything else. Do not rely only on this prompt or an older chat summary. If `main` has advanced beyond the state described below, use the newer live state and do not revert completed work.

The durable state when this handoff was prepared is:

- anthology: **கலைஞர் கருணாநிதியின் சிறுகதைகள்**, first edition 1977;
- 37 stories registered;
- Tamil source processing complete: **5 / 37**;
- completed anthology stories:
  1. `புகழேந்தி` — scans 10–15 / printed pages 1–6 — 6/6 verified;
  2. `நளாயினி` — scans 16–23 / printed pages 7–14 — 8/8 verified;
  3. `சபலம்` — scans 24–30 / printed pages 15–21 — 7/7 verified;
  4. `ஆட்டக்காவடி` — scans 31–38 / printed pages 22–29 — 8/8 verified;
  5. `குப்பைத்தொட்டி` — scans 39–46 / printed pages 30–37 — 8/8 verified;
- all five completed anthology stories have **0 blocked / 0 unresolved story text** and persistent `POSSIBLE_ERRORS_FOR_REVIEW.md` queues;
- English translation has **not** been started for these anthology stories;
- the independent story `கிழவன் கனவு` remains complete and should not be reopened unless new correction evidence is supplied.

## MANDATORY STARTUP — READ COMPLETELY BEFORE WRITES

After fetching live `main`, read these repository files **completely**:

1. `SHORT_STORY_PROCESSING_GUIDE.md`
2. `COLLECTION_SOURCE_GUIDE.md`
3. `HANDOVER.md`
4. `NEXT_CHAT_PROMPT.md`
5. `collections/1977-kalaignar-karunanidhiyin-sirukathaigal/README.md`
6. `collections/1977-kalaignar-karunanidhiyin-sirukathaigal/indexes/story-inventory.md`
7. `collections/1977-kalaignar-karunanidhiyin-sirukathaigal/indexes/scan-map.md`

Then inspect the latest completed story as the immediate structural reference:

8. `stories/kuppai-thotti/README.md`
9. `stories/kuppai-thotti/metadata/source.md`
10. `stories/kuppai-thotti/indexes/page-map.md`
11. `stories/kuppai-thotti/audit.md`
12. `stories/kuppai-thotti/POSSIBLE_ERRORS_FOR_REVIEW.md`

Do not copy `குப்பைத்தொட்டி` wording into the next story; use it only to understand repository structure and audit expectations.

## PERMANENT SOURCE RULES

- **The supplied scan is the controlling textual authority.**
- Do not silently modernize spelling, punctuation, grammar, sandhi, names, dates, numbers, paragraph structure or source anomalies.
- Do not guess unclear Tamil from context, memory, OCR, another edition or general knowledge.
- OCR/extracted text may assist navigation only; it is not controlling authority.
- **No stones should be left unturned.** Before leaving story text unresolved, use native/high-resolution page inspection, progressively enlarged crops, alternate resampling/contrast/sharpening variants, character comparison and page-boundary checks as required by the guide.
- A plausible isolated crop is not enough for `verified`; verify the complete phrase/clause/sentence span against the source.
- User-supplied corrections may reopen previously verified text, but must be checked against the controlling scan and propagated through all dependent files.
- `POSSIBLE_ERRORS_FOR_REVIEW.md` is a human-review queue, **not** a list of confirmed errors. Unusual but visually legible source readings can remain verified while being queued for later review.
- Do not use `blocked` as a shortcut. The objective is zero unresolved story-text blocks wherever a defensible source reading can be recovered, without fabrication.
- Do not commit generated render/crop images or the controlling PDF to GitHub.
- Use narrow, descriptive commits.

## NEXT EXACT ACTIVITY — STORY 6 ONLY

Process anthology Story **6 — `சந்தனக்கிண்ணம்`** only.

Exact range:

- printed pages: **38–47**
- anthology PDF scans: **47–56**

Required boundary checks:

- visually confirm scan **47** opens `சந்தனக்கிண்ணம்`;
- visually confirm scan **56** contains the end of Story 6;
- visually inspect scan **57** and confirm it begins Story 7 **`சங்கிலிச்சாமி`**;
- do not include any scan-57 Story 7 text in the Story 6 workspace.

### Required actions

1. Fetch live `main` and confirm there is no existing canonical `சந்தனக்கிண்ணம்` workspace under another slug/title. If one exists, attach this anthology as an additional witness instead of creating a duplicate.
2. Verify the scan 47 / 56 / 57 boundaries from the controlling PDF.
3. If no canonical workspace exists, create a stable workspace, expected slug `stories/santhana-kinnam/` unless live repository/source evidence supports another established slug.
4. Register the 1977 anthology and exact source coordinates in `metadata/source.md`.
5. Create **10 page records** for scans **47–56**, printed pages **38–47**.
6. Transcribe directly from the source scan page by page.
7. Run direct visual/full-span source-fidelity review on every page before marking it `verified`.
8. Exhaustively investigate difficult readings; do not stop at a first plausible crop.
9. Create and maintain `POSSIBLE_ERRORS_FOR_REVIEW.md` for unusual/easily misread but legible source readings.
10. Create/update:
   - story `README.md`;
   - `metadata/source.md`;
   - `indexes/page-map.md`;
   - all 10 `pages/*.md` records;
   - assembled Tamil under `sections/`;
   - `audit.md`;
   - `POSSIBLE_ERRORS_FOR_REVIEW.md`.
11. Verify every physical page-boundary continuation across scans 47–56.
12. Before closing Story 6, confirm there are no omitted/duplicated pages and no unresolved markers that have not gone through the exhaustive protocol.
13. Synchronize after Story 6:
   - `collections/1977-kalaignar-karunanidhiyin-sirukathaigal/indexes/story-inventory.md`;
   - collection `README.md`;
   - root `README.md`;
   - collection `indexes/scan-map.md`;
   - root `HANDOVER.md`;
   - root `NEXT_CHAT_PROMPT.md` so it points to the following exact activity.
14. **Do not start Story 7 — `சங்கிலிச்சாமி` — in the same activity.**

## EXPECTED PROGRESS AFTER SUCCESSFUL STORY 6 CLOSURE

If Story 6 completes cleanly, anthology progress should become:

- Tamil source processing complete: **6 / 37**;
- not yet transcribed: **31 / 37**;
- next exact story: Story 7 `சங்கிலிச்சாமி`, printed pages **48–59**, scans **57–68**;
- however, only update to that next activity after Story 6 is fully synchronized and closed.

## USER COMMAND BEHAVIOUR

When I say **“Proceed with next activity”**, execute the exact next activity recorded in live `HANDOVER.md` / `NEXT_CHAT_PROMPT.md` directly. Do not ask me to choose a routine next step.

If the controlling PDF is not actually available in the new chat/tool context, tell me it needs to be attached/resolved before source transcription; do not fabricate the missing source from this prompt.

---

End of durable restart prompt.
