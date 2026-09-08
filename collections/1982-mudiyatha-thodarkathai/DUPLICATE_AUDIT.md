# Duplicate / Canonical Identity Audit — `முடியாத தொடர்கதை` (1982)

Date: **2026-09-08**  
Repository checked: `pugazg/kalaignar-short-stories`  
Branch authority: live `main`

## Purpose

Prevent creation of duplicate canonical story folders while processing the five-story anthology `முடியாத தொடர்கதை`.

## Intake result

| # | 1982 opening heading | Existing canonical match found at intake? | Intake routing |
|---:|---|---|---|
| 1 | `பெற்ற பிள்ளையை விற்ற தாய்` | **No** | new canonical candidate |
| 2 | `காசா லேசா` | **No** | new canonical candidate |
| 3 | `சீமான் வீட்டு சீக்காளி` | **No** | new canonical candidate |
| 4 | `நந்தியூர் நரியப்பன்` | **No** | new canonical candidate |
| 5 | `முடியாத தொடர்கதை` | **No** | new canonical candidate |

**Intake duplicate gate: PASS — no existing repository match was found for any of the five headings.**

Additional intake fragment searches included `பிள்ளையை விற்ற` and `சீக்காளி`.

## Story 1 activation recheck — PASS

Immediately before creating Story 1, live `main` was fetched at commit `92207d2e2cecdeabe258cfc49cb633d2a017c61e` and the exact heading **`பெற்ற பிள்ளையை விற்ற தாய்`** was searched again. No existing canonical repository match was returned.

Routing therefore remained:

- new canonical workspace: `stories/petra-pillaiyai-vitra-thaai/`
- controlling source: 1982 `முடியாத தொடர்கதை`, scans **7–28 / printed 5–26**.

This activation result does not pre-authorize Stories 2–5. Each must be re-searched against whatever live `main` exists when it becomes active.

## Important identity note — collection versus Story 5

`முடியாத தொடர்கதை` is both the physical collection title and Story 5 heading. These remain separate archival entities. The whole book stays under `collections/1982-mudiyatha-thodarkathai/`; only Story 5's exact range may later receive a canonical story workspace.

## Routing rule on future activation

For each remaining story:

1. fetch live `main`;
2. search the exact opening heading plus source-documented variants;
3. if no canonical story exists, create a new canonical story workspace using this 1982 range as its controlling source;
4. if a canonical story has appeared, register the 1982 text as an edition/source witness instead of duplicating it;
5. never use title similarity alone to overwrite another canonical work.

## Current next step

Story 1 is already activated and first-pass transcribed. Its dedicated post-transcription historical-glyph gate is next. Story 2 duplicate recheck waits until Story 1 source closure.
