# Duplicate / Canonical Identity Audit — `முடியாத தொடர்கதை` (1982)

Date: **2026-09-08**  
Repository checked: `pugazg/kalaignar-short-stories`  
Branch authority: live `main`

## Purpose

Prevent creation of duplicate canonical story folders while registering the five-story anthology `முடியாத தொடர்கதை`.

## Search scope

The repository was searched on live `main` for each visually confirmed story-opening heading:

1. `பெற்ற பிள்ளையை விற்ற தாய்`
2. `காசா லேசா`
3. `சீமான் வீட்டு சீக்காளி`
4. `நந்தியூர் நரியப்பன்`
5. `முடியாத தொடர்கதை`

Additional distinctive-fragment searches included `பிள்ளையை விற்ற` and `சீக்காளி`.

## Result

| # | 1982 opening heading | Existing canonical match found at intake? | Intake routing |
|---:|---|---|---|
| 1 | `பெற்ற பிள்ளையை விற்ற தாய்` | **No** | new canonical candidate |
| 2 | `காசா லேசா` | **No** | new canonical candidate |
| 3 | `சீமான் வீட்டு சீக்காளி` | **No** | new canonical candidate |
| 4 | `நந்தியூர் நரியப்பன்` | **No** | new canonical candidate |
| 5 | `முடியாத தொடர்கதை` | **No** | new canonical candidate |

**Intake duplicate gate: PASS — no existing repository match was found for any of the five headings.**

This is a preflight result, not permission to create five empty canonical folders. Re-run the search immediately before each story is activated because live `main` may advance independently.

## Important identity note — collection versus Story 5

`முடியாத தொடர்கதை` is both:

- the title of the 1982 physical collection; and
- the heading of Story 5, scans 59–93 / printed pages 57–91.

These are different archival entities. The whole physical book stays under `collections/1982-mudiyatha-thodarkathai/`. Only Story 5's exact story range may later live under a canonical `stories/` workspace.

## Routing rule on activation

For each story:

1. fetch live `main`;
2. search exact heading plus any source-documented heading variant;
3. if no canonical story exists, create a new canonical story workspace using this 1982 range as its controlling source;
4. if a canonical story has appeared, do not duplicate it — register the 1982 text as an edition/source witness and compare explicitly;
5. never use title similarity alone to overwrite another canonical work.

## Next activation

Story 1: **`பெற்ற பிள்ளையை விற்ற தாய்`**  
Scans: **7–28**  
Printed pages: **5–26**  
Forward boundary witness: **scan 29 — `காசா லேசா`**
