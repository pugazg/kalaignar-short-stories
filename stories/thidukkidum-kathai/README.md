# திடுக்கிடும் கதை

Canonical story workspace for **திடுக்கிடும் கதை**, processed from the 1977 anthology **கலைஞர் கருணாநிதியின் சிறுகதைகள்**.

## Source

- Author: **கலைஞர் மு. கருணாநிதி**
- Controlling source: `TVA_BOK_0064142_கலைஞர்_கருணாநிதியின்_சிறுகதைகள்.pdf`
- Collection edition: **முதல் பதிப்பு: 1977**
- Printed pages: **190–195**
- PDF scans: **199–204**
- Source PDF committed to GitHub: **No**

Full source metadata: [`metadata/source.md`](metadata/source.md).

## 2026 dual-gate status

**CURRENT PASS / CLOSED**

- Gate A: **6/6 PASS**
- Gate B: **6/6 PASS**
- source-proven repairs: **2**
  - scan 200: `காதலே` → `காதலை` (historical `லை`)
  - scan 202: `என்னுல் தான்` → `என்னால் தான்` (historical `னா`)
- unresolved source readings: **0**
- unresolved historical-glyph readings: **0**
- possible-error queue: **0 pending / 0 unresolved**
- English prose rewrite required: **0**
- 2026-09-02 English page-anchor correction: **preserved unchanged**

Durable ledger: [`RE_AUDIT_2026.md`](RE_AUDIT_2026.md).

## Tamil archival status

**PASS — 6 / 6 story pages transcribed and directly source-reviewed.**

- page records: **6 / 6**
- `verified`: **6**
- `needs-review`: **0**
- `blocked`: **0**
- explicit missing / unresolved story text: **0**
- Tamil assembly: [`sections/thidukkidum-kathai.md`](sections/thidukkidum-kathai.md)
- audit: [`audit.md`](audit.md)
- human possible-error queue: [`POSSIBLE_ERRORS_FOR_REVIEW.md`](POSSIBLE_ERRORS_FOR_REVIEW.md)

## Visual fidelity

**PASS — corrected.** See [`visual-fidelity.md`](visual-fidelity.md).

Direct source review synchronized the scan-199 opening rule/enlarged initial and standalone source-note treatment, confirmed the `காதல் கதை` and `வீரக்கதை` subsection headings, classified scan-202 printer signature `க—13` as page furniture, and synchronized scan 204 to `story-ending` with its closing ornament. The 2026 dual-gate reread additionally corrected historical `லை` / `னா` identities on scans 200 and 202. **Story wording changed: Yes — two source-proven historical-glyph repairs.**

## Story boundary

- scan **199** opens `திடுக்கிடும் கதை`;
- scan **204** contains the final staircase-key punchline and closing ornament;
- scan **205** opens Story 30 `கடைசிக் கட்டம்`;
- Story 30 text included here: **No**.

## English translation

**PASS — complete.**

- English: [`translations/en/thidukkidum-kathai.md`](translations/en/thidukkidum-kathai.md)
- review: [`TRANSLATION_REVIEW.md`](TRANSLATION_REVIEW.md)
- source-page markers: **6 / 6 represented**
- source note and `காதல் கதை` / `வீரக்கதை` subsection structure preserved: **Yes**
- canonical Tamil changed during translation: **No**

### Post-completion English provenance correction — 2026-09-02

Downstream Wave-2 ingestion exposed that the six English source-page markers were present and ordered but were **mis-anchored to content from scan 200 onward**. The English prose itself was complete.

The marker positions have now been re-anchored against the six verified Tamil page records without changing the title, note, headings, English prose, punctuation or canonical Tamil. Scan **204 / printed 195** now contains its actual translated ending instead of an empty marker section.

- pre-correction English blob: `0547de49e20f8ff96a5be5fb6a683d2b5b661d1e`
- corrected English blob: `6e321b1b333d3d1c2bbc598cc73e6f6bd6aeae1d`
- boundary manifest: [`translations/en/page-anchors.json`](translations/en/page-anchors.json)
- regression validator: [`../../scripts/validate-english-page-anchors.py`](../../scripts/validate-english-page-anchors.py)
- post-correction review result: **PASS**
- canonical Tamil changed by correction: **No**

## Completion state

**திடுக்கிடும் கதை is 2026 CURRENT PASS / CLOSED: Gate A 6/6 + Gate B 6/6, 2 source-proven historical-glyph repairs, 0 unresolved.** Tamil archival source processing, visual fidelity and English translation remain complete for scans 199–204 / printed pages 190–195. English review result: PASS.

## Next anthology English activity

Story 30 — **கடைசிக் கட்டம்**, printed pages **196–201**, anthology scans **205–210**. Scan **211** opens Story 31 `அய்யோ ராஜா!`.


## English post-Tamil re-audit

- E1 completeness / physical-page alignment: **PASS**
- page coverage: **6/6**
- E1 repairs: **2 structure-traceability annotations**
- unresolved E1 issues: **0**
- E2–E5: **PENDING**
- durable record: [`ENGLISH_REAUDIT_2026.md`](ENGLISH_REAUDIT_2026.md)
