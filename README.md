# கலைஞர் சிறுகதைகள் — மின்னாக்கக் களஞ்சியம்

கலைஞர் மு. கருணாநிதியின் சிறுகதைகள் மற்றும் தனிநூலாக வெளிவந்த சிறுகதைப் பதிப்புகளை மூல ஸ்கேன்களின் பக்க வரிசையைக் காக்கும் வகையில் Markdown வடிவில் பாதுகாக்கும் களஞ்சியம்.

## மூலக் கொள்கை

> **மூல ஸ்கேன் தான் controlling source. Markdown ஒரு பாதுகாப்பு அடுக்கு; திருத்தப்பட்ட புதிய பதிப்பு அல்ல.**

மூலத்தில் இருப்பதை அமைதியாகச் சீர்திருத்தவோ, நவீனப்படுத்தவோ, ஊகித்து நிரப்பவோ கூடாது. தெளிவில்லாத வாசிப்புகள் வெளிப்படையாக `needs-review`, `partial`, அல்லது `blocked` எனக் குறிக்கப்பட வேண்டும்.

**மூல PDF கோப்புகள் இந்த repository-யில் commit செய்யப்படாது.** அவற்றின் filename, checksum, edition identity, scan condition மற்றும் page mapping மட்டும் metadata-வில் பதிவு செய்யப்படும்.

## தற்போதைய சிறுகதை

| சிறுகதை | ஆசிரியர் | scan-ல் தெரியும் பதிப்பு | நிலை |
|---|---|---|---|
| கிழவன் கனவு | மு. கருணாநிதி | இரண்டாம் பதிப்பு | **Tamil story source finalized; assembly PASS; English translation workflow ready** |

### தற்போதைய page status

- `verified`: **20**
- `blocked`: **4**
- `needs-review`: **2** — front matter scans 3–4 only
- `not-started`: **0**

The complete physical publication—from cover through story, printed errata, advertisements and back cover—has page-level archival records.

The story-body scans **7–22** have all completed direct visual audit. Final story disposition is **12 verified / 4 source-blocked / 0 needs-review**. Scans **15, 17, 21 and 22** are formally `blocked` because the supplied physical copy does not expose enough visual information to recover specific words/phrases safely. Those gaps remain explicit `blocked-by-source` markers.

Scan **23**'s printed **`பிழை திருத்தம்.`** remains a separate correction layer and has not been silently merged into the archival page text or assembled story.

## Final Tamil story layer

Current control/derived artifacts:

- `stories/kizhavan-kanavu/audit.md`
- `stories/kizhavan-kanavu/sections/kizhavan-kanavu.md`
- `stories/kizhavan-kanavu/sections/kizhavan-kanavu-errata.md`
- `stories/kizhavan-kanavu/ASSEMBLY_REVIEW.md` — **PASS**

The synchronized assembled Tamil story represents **all 16 story scans exactly once**, incorporates the final high-resolution readings, and preserves every source-blocked location explicitly.

## English translation stage

The controlled English story-translation gate is now **OPEN**.

Translation workspace:

- `stories/kizhavan-kanavu/translations/en/README.md`
- `stories/kizhavan-kanavu/translations/en/TRANSLATION_PLAN.md`
- `stories/kizhavan-kanavu/translations/en/SOURCE_MAP.md`

No English story prose has been drafted yet.

The planned translation batches are:

1. scans 7–10
2. scans 11–14
3. scans 15–18
4. scans 19–22

A `blocked-by-source` Tamil gap must remain explicitly blocked in English. Publisher errata must remain separately documented rather than silently substituted into the archival translation.

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
```

ஒவ்வொரு சிறுகதையும் தனித்த `stories/<story-slug>/` அடைவில் பதிவாகும். பக்கவாரி records முதன்மை archival layer; assembled text, errata, audit, translation போன்றவை derived layers ஆக மட்டுமே சேர்க்கப்படும்.

விரிவான workflow: [`SHORT_STORY_PROCESSING_GUIDE.md`](SHORT_STORY_PROCESSING_GUIDE.md).  
தற்போதைய சிறுகதை: [`stories/kizhavan-kanavu/README.md`](stories/kizhavan-kanavu/README.md).

## அடுத்த activity

Begin **கிழவன் கனவு — English Translation Batch 1, scans 7–10 only**. Retain source-page markers and complete a direct Tamil-to-English source review before moving to Batch 2.
