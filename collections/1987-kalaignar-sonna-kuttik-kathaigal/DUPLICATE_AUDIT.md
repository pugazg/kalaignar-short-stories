# Duplicate / Canonical-Identity Audit — 1987 `கலைஞர் சொன்ன குட்டிக் கதைகள்`

## Purpose

The user explicitly requires that a 1987 story **must not be onboarded as a new canonical story if it already exists anywhere in `pugazg/kalaignar-short-stories`, including under an alternate title**.

This file is an activation gate. A search-index miss alone is never proof of novelty. Canonical collection inventories and direct narrative identity control the decision.

## Canonical registers used

The 1987 rows are checked against the closed canonical registers represented by:

- 1977 `கலைஞர் கருணாநிதியின் சிறுகதைகள்` — 37 stories;
- 2008 `கலைஞர் சொன்ன கதைகள்` — 40 stories;
- 2004 `கலைஞரின் குட்டிக் கதைகள்` — 34 stories;
- subsequently onboarded 1997/2009 canonical additions;
- story-local content where a plausible alternate-title collision exists.

## Direct-heading audit — 25 / 25 exact

The five intake title holds were resolved from source pixels:

- scan 13 — `சொர்க்கத்திற்குச் சென்றுவந்த அழகி!`
- scan 20 — `இரு நிகழ்வுகள்`
- scan 31 — `குறிக்கோள்`
- scan 37 — `தெனாலிராமன் கதை`
- scan 45 — `அகத்திணை அன்பு!`

Story 1's intake title was separately corrected from `மன்னனும் குறவியும்.` to **`மன்னனும் குருவியும்!`**.

## Established canonical identities before Batch 01

### Story 1 — `மன்னனும் குருவியும்!`

**POSITIVELY DISTINCT / NEW CANONICAL IDENTITY** at `stories/mannanum-kuruviyum/`.

Its source closure remains open because the narrative continues into upper scan 6.

### Story 2 — `அரசாபிமானக் கதை` → canonical `ஜாடி குட்டி போடுமா?`

Direct comparison establishes positive identity with canonical `stories/jaadi-kutti-poduma/`.

Disposition: **EXISTING CANONICAL STORY — never create `stories/arasabimana-kathai/`.**

1987 witness path:

`stories/jaadi-kutti-poduma/witnesses/1987-kalaignar-sonna-kuttik-kathaigal/`

Canonical 2008 Tamil/English remain unchanged.

### Story 11 — `குருவி ராமேஸ்வரம்`

- 1987 scan **23 / printed 22**
- existing workspace: `stories/kuruvi-rameswaram/`
- disposition: **EXISTING CANONICAL — additional witness only**

## Batch 01 identity audit — scans 6–20

Durable source/structure record: `BATCH_0001_SCANS_0006_0020.md`.

### Story 3 — `தென்னை மரத்தில் புல்`

Direct source identity: coconut-tree / grass-excuse anecdote.

No canonical 1977, 2004, 2008 or later-addition inventory represents this narrative under the same or a plausible alternate title.

**Disposition: PASS — positively distinct identity.**

### Story 4 — `நாராயணு! நாராயணு!`

Direct source identity: Narada/devotion-test anecdote represented across scans 8–upper 10.

No represented canonical story has this narrative identity.

**Disposition: PASS — positively distinct identity.**

### Story 5 — `துறவியும் சீடர்களும்`

Direct source identity: the monk/disciples lesson occupying lower scan 10 through upper scan 12.

No represented canonical story has this narrative identity.

**Disposition: PASS — positively distinct identity.**

### Story 6 — `முல்லை முத்துக்குமரன்`

The complete physical story span lower scan 12 → upper scan 13 was reviewed as one narrative and compared against the canonical inventories. No represented canonical story or plausible alternate-title identity was found.

**Disposition: PASS — positively distinct identity.**

### Story 7 — `சொர்க்கத்திற்குச் சென்றுவந்த அழகி!`

A title/theme collision with 2004 canonical `சொர்க்கத்திற்கு வந்தது எப்படி?` was explicitly tested.

They are **different narratives**:

- 2004 `சொர்க்கத்திற்கு வந்தது எப்படி?` is the Nayanmar / heaven-arrival testimony sequence;
- 1987 scans lower 13 → upper 15 form a separate domestic/ascetic narrative centred on a woman.

**Disposition: PASS — positively distinct identity. Do not route to `stories/sorgaththirku-vandhathu-eppadi/`.**

### Story 8 — `புத்தர் உணர்த்திய உண்மை`

A Buddhist-content collision with 1977 canonical `சித்தார்த்தன் சிலை` was explicitly tested.

They are **different narratives**:

- the 1987 story is the bereavement lesson in which a grieving woman is asked to obtain grain from a household untouched by death;
- `சித்தார்த்தன் சிலை` is the literary story of a deserted woman appealing before a Buddha statue.

**Disposition: PASS — positively distinct identity. Do not route to `stories/siddharthan-silai/`.**

### Story 9 — `கஜினி முகமதுவும் கவிஞர் பார்டோசியும்`

The named historical Ghazni/Firdawsi anecdote represented lower scan 18 → upper scan 20 has no matching canonical narrative in the current registers.

**Disposition: PASS — positively distinct identity.**

### Story 10 — `இரு நிகழ்வுகள்`

Only its opening in lower scan 20 falls inside Batch 01. The story continues through scans 21–22.

**Disposition: IDENTITY OPEN — do not create a canonical workspace until Batch 02 reviews the complete story.**

## Existing later content-level holds

### `புகழேந்திப் புலவர் கதை` — scans 27–28

Compare complete narrative with canonical `stories/pugazhendhi/` before activation.

State: **IDENTITY UNRESOLVED — no new folder permitted**.

### `யசோதர காவியம்` — scans 41–43

Canonical `அமிர்தமதி` contains an embedded `யசோதர காவியம்` narrative.

State: **IDENTITY UNRESOLVED — no new folder permitted**.

### `தெனாலிராமன் கதை` and `தெனாலிராமன் பூனை`

Separate physical headings, but both require independent content comparison against current canon and against each other when activated.

## Identity versus text verification

Identity PASS does **not** mean that the 1987 lexical layer is verified.

For Batch 01, the currently available rendered source supports physical-boundary and narrative-identity decisions, but does not support certification of every small historical Tamil glyph. Therefore Stories 3–9 are not yet populated with low-confidence canonical text merely because their identities are now distinct.

## Mandatory per-story activation test

Before every remaining row:

1. fetch live `main`;
2. establish exact intra-page start/end boundaries;
3. check exact and plausible alternate titles against canonical registers;
4. compare distinctive opening/ending content and named anecdote identity;
5. route matching material as an additional witness;
6. create a new canonical workspace only when positively distinct;
7. keep textual/glyph verification separate from identity determination.

## Current counts

- physical 1987 headings: **25 / 25 exact**
- distinct 1987 identities established: **8** — Story 1 and Stories 3–9
- 1987 rows positively matched to existing canon: **2** — Story 2 → `ஜாடி குட்டி போடுமா?`; Story 11 → `குருவி ராமேஸ்வரம்`
- Batch-01 partial identity row: **1** — Story 10 `இரு நிகழ்வுகள்`
- explicit later identity holds: **2** — Story 14 `புகழேந்திப் புலவர் கதை`, Story 21 `யசோதர காவியம்`

Next identity work begins by completing Story 10 in Batch 02, scans 21–22.
