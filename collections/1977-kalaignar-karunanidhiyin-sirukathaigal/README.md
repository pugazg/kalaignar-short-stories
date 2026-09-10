# கலைஞர் கருணாநிதியின் சிறுகதைகள் — 1977 anthology source

Collection-level archival source for the 37 canonical short-story workspaces derived from **கலைஞர் கருணாநிதியின் சிறுகதைகள்**.

## Source snapshot

- printed title: **கலைஞர் கருணாநிதியின் சிறுகதைகள்**
- author: **கலைஞர் மு. கருணாநிதி**
- publisher: **தமிழ்க்கனி பதிப்பகம், சென்னை-28**
- edition: **முதல் பதிப்பு: 1977**
- file: `TVA_BOK_0064142_கலைஞர்_கருணாநிதியின்_சிறுகதைகள்.pdf`
- physical scans: **260**
- printed story pages: **1–250**
- stories in contents: **37**
- bytes: **268,486,609**
- SHA-256: `853032661482eaccb26c083a38d7aa75c081362d33c963c63e37d088bf20acb3`
- source PDF committed: **No**

Pagination inside the story block is `scan = printed page + 9`: scan **10** = printed page **1**, scan **259** = printed page **250**, and scan **260** is the verified back cover.

## 2026 full source + old-glyph re-audit — OPEN

The exact 1977 PDF was reattached on 2026-09-10 and byte identity matched the registered source. A definite canonical transcription error in `நளாயினி` proved that the earlier 37/37 `verified` state could not be relied upon as the final source-fidelity gate.

Therefore all 37 stories are being re-audited **without retranscription** under two independent gates:

1. **Gate A — source fidelity:** compare existing canonical/page-record Tamil directly with every controlling source page;
2. **Gate B — Old Tamil Glyph:** independently reopen every physical page at high/native resolution and explicitly inspect `ணா / ணை / ணொ / ணோ / லை / ளை / றா / றொ / றோ / னா / னை / னொ / னோ`, plus other suspicious old forms.

Rules: source-first, no global replacement, no lexical modernization, and no PASS while a source or historical-glyph candidate remains unresolved.

Tracker: [`RE_AUDIT_2026.md`](RE_AUDIT_2026.md). Gate definition: [`OLD_TAMIL_GLYPH_REAUDIT_GATE.md`](OLD_TAMIL_GLYPH_REAUDIT_GATE.md).

Current state: **OPEN — 1 / 37 dual-gate complete**.

### Re-closed under the 2026 standard

- `நளாயினி` — scans **16–23 / printed 7–14** — **Gate A PASS / Gate B PASS / 15 canonical repairs / 0 unresolved**. Tamil assembly and affected English are synchronized.

### Next

- `புகழேந்தி` — scans **10–15 / printed 1–6** — **NEXT**.
- after that: Story 3 `சபலம்` through Story 37 `நுனிக்கரும்பு` in anthology order.

## Legacy processing state

Before the 2026 re-audit, all **37/37** stories had canonical Tamil page records/assemblies and were recorded `verified` / audit PASS. Those artifacts are retained as the comparison baseline; **they must not be retranscribed from scratch**.

The complete canonical order and scan/page mapping remain in:

- `indexes/story-inventory.md`
- `indexes/scan-map.md`
- `RE_AUDIT_2026.md` (current gate status for all 37 stories)

## Source-title distinctions

The anthology itself preserves these title differences:

1. TOC `புரட்சிப்படம்` ↔ opening `புரட்சிப் படம்`;
2. TOC `சித்தார்த்தன்` ↔ opening `சித்தார்த்தன் சிலை`.

Both source forms remain provenance; do not normalize them away.

## Current closure rule

The old 37/37 Tamil source-pass is **legacy-complete but superseded for current release confidence**. A story is current PASS only after its 2026 Gate A and Gate B both close and all proven corrections have been synchronized.
