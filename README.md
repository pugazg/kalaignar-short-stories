# கலைஞர் சிறுகதைகள் — மின்னாக்கக் களஞ்சியம்

கலைஞர் மு. கருணாநிதியின் சிறுகதைகள் மற்றும் தனிநூலாக வெளிவந்த சிறுகதைப் பதிப்புகளை மூல ஸ்கேன்களின் பக்க வரிசையைக் காக்கும் வகையில் Markdown வடிவில் பாதுகாக்கும் களஞ்சியம்.

## மூலக் கொள்கை

> **மூல ஸ்கேன் தான் controlling source. Markdown ஒரு பாதுகாப்பு அடுக்கு; திருத்தப்பட்ட புதிய பதிப்பு அல்ல.**

மூலத்தில் இருப்பதை அமைதியாகச் சீர்திருத்தவோ, நவீனப்படுத்தவோ, ஊகித்து நிரப்பவோ கூடாது. தெளிவில்லாத வாசிப்புகள் வெளிப்படையாக `needs-review`, `partial`, அல்லது `blocked` எனக் குறிக்கப்பட வேண்டும்.

**மூல PDF கோப்புகள் இந்த repository-யில் commit செய்யப்படாது.** அவற்றின் filename, checksum, edition identity, scan condition மற்றும் page mapping மட்டும் metadata-வில் பதிவு செய்யப்படும்.

## தற்போதைய சிறுகதை

| சிறுகதை | ஆசிரியர் | scan-ல் தெரியும் பதிப்பு | நிலை |
|---|---|---|---|
| கிழவன் கனவு | மு. கருணாநிதி | இரண்டாம் பதிப்பு | **Tamil source finalized; assembly PASS; English Batches 1–3 source-reviewed** |

### தற்போதைய page status

- `verified`: **20**
- `blocked`: **4**
- `needs-review`: **2** — front matter scans 3–4 only
- `not-started`: **0**

The complete physical publication—from cover through story, printed errata, advertisements and back cover—has page-level archival records.

The story-body scans **7–22** have all completed direct visual audit. Final story disposition is **12 verified / 4 source-blocked / 0 needs-review**. Scans **15, 17, 21 and 22** are formally `blocked` because the supplied physical copy does not expose enough information to recover specific words/phrases safely. Those gaps remain explicit `blocked-by-source` markers.

Scan **23**'s printed **`பிழை திருத்தம்.`** remains a separate correction layer and has not been silently merged into the archival page text or assembled story.

## Final Tamil story layer

Current control/derived artifacts:

- `stories/kizhavan-kanavu/audit.md`
- `stories/kizhavan-kanavu/sections/kizhavan-kanavu.md`
- `stories/kizhavan-kanavu/sections/kizhavan-kanavu-errata.md`
- `stories/kizhavan-kanavu/ASSEMBLY_REVIEW.md` — **PASS**

The synchronized assembled Tamil story represents **all 16 story scans exactly once**, incorporates the final high-resolution readings, and preserves every source-blocked location explicitly.

## English translation stage

The controlled English story-translation gate is **OPEN**.

Translation workspace:

- `stories/kizhavan-kanavu/translations/en/README.md`
- `stories/kizhavan-kanavu/translations/en/TRANSLATION_PLAN.md`
- `stories/kizhavan-kanavu/translations/en/SOURCE_MAP.md`

Batch progress:

1. **scans 7–10 — source-reviewed**
2. **scans 11–14 — source-reviewed**
3. **scans 15–18 — source-reviewed**
4. scans 19–22 — not-started

Completed English batches:

- `stories/kizhavan-kanavu/translations/en/batches/01-scans-07-10.md`
- `stories/kizhavan-kanavu/translations/en/batches/02-scans-11-14.md`
- `stories/kizhavan-kanavu/translations/en/batches/03-scans-15-18.md`

English source-reviewed coverage is now **12 / 16 story scans**. Batch 3 preserves all **three** terminal source gaps in its range separately—two on scan 15 and one on scan 17—and does not reconstruct them from context or outside knowledge.

Batch 4 must preserve four distinct source-blocked readings on scan 21 and the stamp-obscured final-story phrase on scan 22. Publisher/printer footer material on scan 22 remains outside the English story scope.

## களஞ்சிய அமைப்பு

```text
README.md
SHORT_STORY_PROCESSING_GUIDE.md
HANDOVER.md
stories/
  kizhavan-kanavu/
    README.md
    metadata/
      source.md
    indexes/
      page-map.md
    pages/
    sections/
      kizhavan-kanavu.md
      kizhavan-kanavu-errata.md
    audit.md
    ASSEMBLY_REVIEW.md
    translations/
      en/
        README.md
        TRANSLATION_PLAN.md
        SOURCE_MAP.md
        batches/
          01-scans-07-10.md
          02-scans-11-14.md
          03-scans-15-18.md
```

ஒவ்வொரு சிறுகதையும் தனித்த `stories/<story-slug>/` அடைவில் பதிவாகும். பக்கவாரி records முதன்மை archival layer; assembled text, errata, audit, translation போன்றவை derived layers ஆக மட்டுமே சேர்க்கப்படும்.

விரிவான workflow: [`SHORT_STORY_PROCESSING_GUIDE.md`](SHORT_STORY_PROCESSING_GUIDE.md).  
தற்போதைய சிறுகதை: [`stories/kizhavan-kanavu/README.md`](stories/kizhavan-kanavu/README.md).

## அடுத்த activity

Begin **கிழவன் கனவு — English Translation Batch 4, scans 19–22 only**. Complete the scan-18/19 continuation, preserve all scan-21 and scan-22 source gaps explicitly, retain source-page markers, exclude the scan-22 footer/imprint from story prose, and complete direct Tamil-to-English source review before assembling the full English story.