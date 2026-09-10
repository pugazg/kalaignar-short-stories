# Old Tamil Glyph Re-audit Gate — 1977 anthology

## Purpose

This gate is mandatory for the 2026 re-audit of all 37 stories in `கலைஞர் கருணாநிதியின் சிறுகதைகள்` (1977).

It is **separate from ordinary source-fidelity comparison**. A story cannot regain current PASS status merely because its existing text was compared once against the source. The historical-glyph gate must independently close.

## Controlling source

`TVA_BOK_0064142_கலைஞர்_கருணாநிதியின்_சிறுகதைகள்.pdf`

- exact SHA-256: `853032661482eaccb26c083a38d7aa75c081362d33c963c63e37d088bf20acb3`
- 260 physical scans
- first edition 1977
- source PDF is not committed

## Mandatory families

Every physical story page must be independently checked for:

`ணா / ணை / ணொ / ணோ / லை / ளை / றா / றொ / றோ / னா / னை / னொ / னோ`

This list is the minimum, not the maximum. Remain alert for other old ligatures, faint vowel marks, touching type, broken ink, worn type and stylized display forms.

## Gate procedure

For each story:

1. Finish or establish the source-fidelity comparison baseline against the existing repository text.
2. Reopen **every physical page independently at high/native resolution**.
3. Check the 13 mandatory families explicitly; do not assume Gate A already covered them.
4. Search the repository page text for expected family occurrences, but do not rely only on that search: an earlier mistranscription may have encoded the wrong family and therefore evade a text search.
5. Compare suspicious old shapes against clearer same-page / same-edition forms where useful.
6. Read full words and neighboring phrase context from source pixels before changing a character identity.
7. Record each correction individually with scan / printed-page provenance.
8. Never global-replace.
9. Never modernize spelling, grammar, spacing or vocabulary merely because an old glyph has been decoded.
10. If a glyph remains genuinely unresolved after documented escalation, the page and story remain open.

## Independence rule

A correction noticed during Gate A may be queued, but **Gate B still requires a fresh independent visual check**.

Likewise, Gate B may discover a lexical/source mismatch not previously found by Gate A. In that case Gate A must be reopened for the affected span and the source-fidelity record synchronized.

## Evidence / recording

Each re-audited story should maintain or update a durable historical-glyph audit record that states:

- source scan coverage;
- pages checked at high/native resolution;
- mandatory family coverage;
- corrections, each as earlier repository reading → source-supported Unicode reading;
- historical family where applicable;
- unresolved count;
- final Gate B status.

## PASS condition

Gate B is PASS only when:

- every physical story page has been independently reopened;
- all 13 families have been explicitly considered across the story;
- every actual/suspicious occurrence has been source-checked;
- all source-proven corrections are applied individually;
- no unexamined candidate remains;
- unresolved historical-glyph count is **0**.

## Failure / hold condition

If any historical character identity remains uncertain, do not call the story PASS. Keep the story re-audit open and use the difficult-reading escalation in `HISTORICAL_TAMIL_GLYPH_TRANSCRIPTION_GUIDE.md`.

## Short rule

> **Source comparison proves the words; the independent old-glyph gate proves the character identities. Both must PASS.**
