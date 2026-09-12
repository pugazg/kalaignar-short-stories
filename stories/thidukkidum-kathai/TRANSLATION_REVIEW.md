# English Translation Review — திடுக்கிடும் கதை

## Scope

- Story: **திடுக்கிடும் கதை**
- English title treatment: **Thidukkidum Kathai** (transliteration retained; the closing phrase is rendered by immediate sense inside the story)
- Controlling source: `TVA_BOK_0064142_கலைஞர்_கருணாநிதியின்_சிறுகதைகள்.pdf`
- Printed pages: **190–195**
- Anthology scans: **199–204**
- Canonical Tamil assembly: `sections/thidukkidum-kathai.md`
- English translation: `translations/en/thidukkidum-kathai.md`
- Boundary witness: scan **205**, opening Story 30 `கடைசிக் கட்டம்`

## Translation gate

The story entered translation after the repository recorded:

- Tamil page records: **6 / 6 verified**;
- Tamil audit: **PASS**;
- unresolved / blocked story text: **0**;
- canonical Tamil assembly: complete;
- visual fidelity: **PASS — corrected**;
- possible-error queue read before translation.

The canonical Tamil was not modified during the English activity.

## Completeness review

**PASS**

- all six verified source pages are represented in English;
- source-page comments for scans **199–204** are retained once and in order;
- the physical joins **199→200**, **200→201**, **201→202**, **202→203** (`...பிணமாகச்` → `சாய்ந்து கிடந்தார்கள்.`), and **203→204** (`...மிரட்டலைக்` → `கண்ட கிளர்ச்சித் தலைவர்...`) remain traceable;
- the standalone source note, `காதல் கதை` and `வீரக்கதை` subsection structure, and final parenthetical punchline are represented;
- the New York/lift frame, Pyramus–Thisbe love story, Antony’s political/caste allegory, and Charles’s key revelation remain complete and in source order;
- printer signature `க—13` remains excluded as page furniture;
- scan **205 / Story 30** text is not included.

## Title, names and key-term treatment

- `திடுக்கிடும் கதை` is retained as **Thidukkidum Kathai**.
- `ரோமியோ`, `ஆண்டனி`, and `சார்லஸ்` are rendered **Romeo, Antony**, and **Charles**.
- `ஓவிட்`, `திஸ்பே`, and `பைரமஸ்` are rendered **Ovid, Thisbe**, and **Pyramus**.
- the source’s `மல்பெரி` / `மல்பரி` variation is reflected as **malberi** / **malbari** rather than used to rewrite the canonical Tamil.
- `நிசின் சமாதி` is retained source-close as **Nisin’s tomb** rather than replaced through an outside classical-source identification.
- the story-within-story labels are translated as **Love Story** and **Heroic Story**, preserving their separate heading role.

## Possible-error queue handling

`POSSIBLE_ERRORS_FOR_REVIEW.md` was read in full. No source-sensitive form was silently normalized.

Notable conservative choices include:

- `திரும்பினர்கள்`, `அவள் வர்ணித்தபடி`, `இன்பக்கடலாடினர்கள்`, `இரண்டு ஜோடிக் கிளிகளைக் பிரித்து`, `தேக்கிய இன்ப வெள்ளத்திற்குப்`, `காதற் சொற்களின்`, and `வேற்றார் சென்று` remain source-governed; the later 2026 source audit corrected historical-`லை` `காதலே மூடி மறைக்க` → `காதலை மூடி மறைக்க`, whose English meaning was already rendered correctly;
- `கிழட்டுச் சிங்கம்` is rendered as the old lioness described by the scene;
- the later 2026 glyph audit corrected historical-`னா` `என்னுல் தான்` → `என்னால் தான்`; the existing English “because of me alone” already matches the corrected source meaning;
- `கண்காணச் சீமை` is rendered minimally as a far-off land rather than asserted as a specific place;
- `கெளவிக்கொண்டிருந்தது` is represented as the sword being lodged/gripping the heart in context;
- `சாக்காடென்னும் பூக்காட்டிற்கு`, `கர்ச்சனை`, `பரிபாலித்துவந்தான்`, visibly spaced `துரத்து வதாகவோ`, `இதுதானப்பா`, and `பாக்கியிருந்தது` remain source-governed in Tamil.

## Structural and rhetorical review

- the New York staircase frame remains the governing comic structure;
- Romeo’s first story preserves the tragic lover sequence before the trio resume climbing;
- Antony’s second story remains an intentionally unnamed political/caste parable without any outside identification of its actors or setting;
- Charles’s third “story” consists solely of the practical revelation that the room key was left downstairs;
- the final parenthetical sentence remains the narrator’s closing comic confirmation.

## Source issues reopened during translation

**None.**

Translation exposed no issue strong enough to justify reopening or changing the verified Tamil transcription.

## Result

**PASS — English translation complete for Story 29.**

The English file is complete and traceable to the verified Tamil assembly. Canonical Tamil remains authoritative.

## Post-completion provenance-anchor correction — 2026-09-02

A downstream Digital Library Bulk Onboarding Wave-2 ingestion check exposed a defect that the original translation review did not detect. The English prose was complete, and the source-page markers **199–204** were present once and in order, but marker presence/order was mistakenly treated as sufficient evidence of page traceability.

### Defect confirmed

Against the six verified Tamil page records:

- scan **199 / printed 190** ends at `அதாவது;` / English `Namely:`;
- scan **200 / printed 191** begins `“அன்புள்ள நண்பர்களே!...` / English `“Dear friends! Today you will have to walk to your room...`;
- scan **201 / printed 192** begins `யாரின் கண்களைவிடக்...` / English `Whose eyes could be sharper than the eyes of lovers?...`;
- scan **202 / printed 193** begins `புள்ளிமானைக்...` / English `A lioness that had killed a spotted deer...`;
- scan **203 / printed 194** begins the physical continuation `சாய்ந்து கிடந்தார்கள்.` / English `—together.`;
- scan **204 / printed 195** begins the physical continuation `கண்ட கிளர்ச்சித் தலைவர்...` / English `—the leader of the uprising immediately cried...` and contains the complete translated ending.

In the pre-correction English blob `0547de49e20f8ff96a5be5fb6a683d2b5b661d1e`, the translation of scan 200 was still under marker 199; markers 200–203 each lagged the corresponding translated source page by one boundary; marker 204 was followed by no story prose.

The original review sentence saying the joins were traceable was therefore **too strong with respect to English marker anchoring**. It accurately described prose completeness and source order, but did not prove physical-page attribution.

### Correction performed

Only the English source-page marker positions were changed. The corrected English blob is `6e321b1b333d3d1c2bbc598cc73e6f6bd6aeae1d`.

- title: unchanged;
- source note: unchanged;
- headings: unchanged;
- English prose and punctuation: unchanged;
- canonical Tamil: unchanged;
- scan/printed-page marker labels: unchanged;
- marker positions: re-anchored to the actual six physical Tamil page boundaries.

All five cross-page joins now remain traceable at the correct physical transition, including the split continuations 202→203 and 203→204.

### Regression guard / re-verification

`translations/en/page-anchors.json` records human-adjudicated start/end boundary evidence for all six scans, and the repository-level `scripts/validate-english-page-anchors.py` validator checks marker sequence, printed-page agreement, non-empty English sections for source pages containing story text, and the human-reviewed boundary anchors without relying on Tamil/English paragraph-count equality.

Regression application:

1. corrected mapping → **PASS**;
2. pre-correction shifted mapping → **FAIL**, including a scan-200 start-anchor mismatch and an empty scan-204 translated section;
3. corrected mapping restored → **PASS**.

### Current result

**PASS — Story 29 English translation remains complete and is re-verified for physical source-page provenance after the marker-only correction.**

No Tamil source issue was reopened and no English prose was retranscribed or retranslated.


## 2026 source re-audit synchronization

- canonical Tamil: **CURRENT PASS / CLOSED**
- Gate A: **6/6 PASS**
- Gate B: **6/6 PASS**
- source-proven Tamil repairs: **2**
  - scan 200 `காதலே` → `காதலை` (`லை`)
  - scan 202 `என்னுல் தான்` → `என்னால் தான்` (`னா`)
- English prose rewrite required: **0**
- 2026-09-02 page-anchor correction and `page-anchors.json`: **preserved unchanged**
- unresolved source / historical-glyph readings: **0 / 0**


## English re-audit 2026 — E1

**PASS — completeness and physical-page alignment.**

- physical pages: **6/6 PASS**
- omissions / duplications / unsupported additions: **0 / 0 / 0**
- E1 repairs: **2 structure-traceability annotations**
- Tamil/source reopened: **No**
- unresolved E1 issues: **0**

The existing human-adjudicated page anchoring remains PASS for all six scans. The prior downstream correction and `page-anchors.json` evidence were respected; no marker was moved in this E1 pass. The opening rule and enlarged-initial provenance annotations were restored; the standalone source note and `Love Story` / `Heroic Story` subsection structure remain represented.

Full record: [`ENGLISH_REAUDIT_2026.md`](ENGLISH_REAUDIT_2026.md). E2–E5 remain pending.


## English re-audit 2026 — E2

**PASS — meaning fidelity.**

The complete English was rechecked sentence-by-sentence against the final canonical Tamil, including both 2026 glyph repairs and the pre-existing human-adjudicated page-anchor correction. No E2 prose repair was required. The lift/stair framing, Romeo–Thisbe/Pyramus love story, Antony's heroic story, Charles's final startling-story turn and subsection boundaries preserve source meaning and narrative order. Source-close classical names and opaque forms remain conservative for E3; no English meaning defect was proven.

English repairs: **0**. Tamil/source reopened: **No**. Unresolved E2 issues: **0**.


## English re-audit 2026 — E3

**PASS — terminology / names / cultural consistency.**

Classical/literary names and story labels are consistent: **Romeo, Antony, Charles, Ovid, Thisbe, Pyramus**, with source-close **Nisin's tomb** retained because outside classical-source identification would exceed the source. The unnamed political/caste allegory remains deliberately unnamed. No E3 repair was required.

English repairs: **0**. Tamil/source reopened: **No**. Unresolved E3 issues: **0**.

## English re-audit 2026 — E4

**PASS — English quality.**

No English prose repair was required. The classical/source-close forms and the source’s `malberi` / `malbari` variation remain deliberately preserved.

English-quality repairs: **0**. Tamil changed: **No**. E2/E3 decisions altered: **No**. Source reopened: **No**. Unresolved E4 issues: **0**.
