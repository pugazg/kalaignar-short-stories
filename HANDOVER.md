# HANDOVER — Kalaignar Short Stories Archive

## Repository

- repository: `pugazg/kalaignar-short-stories`
- branch: `main`
- permanent guides: `SHORT_STORY_PROCESSING_GUIDE.md`, `COLLECTION_SOURCE_GUIDE.md`, `HISTORICAL_TAMIL_GLYPH_TRANSCRIPTION_GUIDE.md`, `BATCH_TRANSCRIPTION_VERIFICATION_WORKFLOW.md`, `ENGLISH_TRANSLATION_GUIDE.md`

## LIVE MAIN IS AUTHORITATIVE

Fetch live `main` first. Controlling scans outrank contextual readings; no silent normalization.

## External hold

`நடுத்தெரு நாராயணி` remains **BLOCKED** while `வெள்ளிக்கிழமை` is incomplete.

## ACTIVE collection — 1976 `நளாயினி`

Controlling source: attached `TVA_BOK_0065574_நளாயினி_1976.pdf` — **78 scans**, **164,748,566 bytes**, fourth edition 1976, image-only, not committed; SHA-256 pending. The attached PDF itself is the sole controlling source unless the user explicitly requests external comparison.

Story inventory retains Story 8 heading **`மானம்`** from scan 73; never regress to `மனம்`.

## Story 4 — `நாட்டிய கலாராணி` — TAMIL SOURCE-COMPLETE

Workspace: `stories/naattiya-kalarani/`; physical range **scans 25–46 / printed 25–46**.

Durable state:

- source boundary / dedup: **PASS / PASS**;
- page records: **22/22 verified**;
- direct transcription: **22/22 COMPLETE**;
- independent historical-glyph/source Stage B: **22/22 PASS / COMPLETE**;
- total source corrections: **19**;
- unresolved / blocked: **0 / 0**;
- canonical Tamil assembly: `stories/naattiya-kalarani/sections/naattiya-kalarani.md` — **COMPLETE**;
- assembly review: `stories/naattiya-kalarani/ASSEMBLY_REVIEW.md` — **PASS — 22/22 coverage, 0 omission, 0 duplication**;
- final signature block and closing ornaments: **preserved**;
- Tamil/source state: **SOURCE-COMPLETE**.

Do not reopen Story 4 without new direct-source evidence or explicit comparison authorization.

## Exact next activity — Story 8 `மானம்` activation ONLY

Physical range: **scans 73–78 / printed pages 73–78**. Scan 73 directly shows heading `மானம்`.

1. re-fetch live `main` and preserve newer work;
2. use only the attached controlling PDF for source-dependent evidence;
3. confirm scan 73 opening and scan 78 ending/boundary from source;
4. run a canonical duplicate/alternate-title check in the repository for `மானம்`; never use the stale erroneous heading `மனம்` as authority;
5. if no canonical duplicate exists, create `stories/maanam/` source-intake workspace, `README.md`, `SOURCE_INTAKE.md`, `metadata/source.md`, `indexes/page-map.md`, and six page records for scans 73–78 initialized as `not-started`;
6. synchronize collection/root handover controls;
7. commit and stop/report.

**Do not transcribe Story 8 in the same activation activity.** After a durable activation commit, its first Stage-A transcription batch becomes the next activity.
