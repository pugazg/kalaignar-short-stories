# Duplicate / Canonical-Identity Audit — 1987 `கலைஞர் சொன்ன குட்டிக் கதைகள்`

## Purpose

The user explicitly requires that a 1987 story **must not be onboarded as a new canonical story if it already exists anywhere in `pugazg/kalaignar-short-stories`**.

This file is therefore a gate, not a convenience list.

## Live repository inventories checked at intake

The intake pass compared the currently readable 1987 headings against the live canonical inventory represented by:

- 1977 `கலைஞர் கருணாநிதியின் சிறுகதைகள்`;
- 2008 `கலைஞர் சொன்ன கதைகள்`;
- 2004 `கலைஞரின் குட்டிக் கதைகள்`;
- the subsequently onboarded 1997/2009 canonical stories;
- the root canonical-story register.

## Exact-title result

Among the **20 currently readable 1987 headings**, one exact existing canonical title is already established:

### `குருவி ராமேஸ்வரம்`

- 1987 source: scan **23 / printed page 22**
- existing canonical workspace: `stories/kuruvi-rameswaram/`
- existing controlling source represented there: 2004 `கலைஞரின் குட்டிக் கதைகள்`
- disposition: **DO NOT CREATE A NEW STORY FOLDER**
- correct future action: compare the 1987 text as an **additional edition witness** and store any durable witness material under the existing canonical workspace.

No other exact title among the 20 readable headings currently matches a canonical story title.

## Exact-title holds

Five stylized 1987 headings are not yet safe enough for exact-title comparison:

- scan **13 / printed 12**
- scan **20 / printed 19**
- scan **31 / printed 30**
- scan **37 / printed 36**
- scan **45 / printed 44**

Do not guess these titles from the story topic. Resolve their printed heading first, then rerun this audit.

## Content-level collision holds

Exact-title checking is only the first gate. Two currently readable titles already require special narrative comparison:

### `புகழேந்திப் புலவர் கதை` — scans 27–28

The repository already contains canonical `புகழேந்தி` from the 1977 anthology. Shared name material does **not** prove identity and does **not** prove difference. Before activating the 1987 block, compare the complete anecdote/narrative against canonical `stories/pugazhendhi/`.

State: **IDENTITY UNRESOLVED — no new folder permitted yet**.

### `யசோதர காவியம்` — scans 41–43

The repository's canonical `அமிர்தமதி` explicitly records an embedded `யசோதர காவியம்` narrative. The 1987 block therefore must be compared with that embedded material before being treated as a distinct canonical story.

State: **IDENTITY UNRESOLVED — no new folder permitted yet**.

## Mandatory per-story activation test

For every other 1987 block, immediately before creating a new `stories/<slug>/` directory:

1. fetch live `main` again;
2. check exact heading against the root canonical register and all collection inventories;
3. check obvious punctuation/spacing/title variants;
4. search distinctive names, opening phrases and closing phrases in existing canonical text when tooling permits;
5. compare the narrative premise and ending against plausible existing stories;
6. if identity matches an existing canonical story, route this source as a witness;
7. only if identity is positively distinct may a new canonical workspace be created.

A GitHub text-search miss by itself is **not proof of novelty**; search indexing may be incomplete.

## Intake counts

- physical 1987 story blocks: **25**
- readable headings currently eligible for exact-title comparison: **20**
- exact existing canonical title: **1** (`குருவி ராமேஸ்வரம்`)
- explicit narrative-identity holds despite non-identical title: **2** (`புகழேந்திப் புலவர் கதை`, `யசோதர காவியம்`)
- unresolved stylized-title rows: **5**
- stories positively declared new and activated from the 1987 source: **0**

This audit must advance together with the collection inventory; it must never be bypassed merely to speed up transcription.