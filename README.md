# கலைஞர் சிறுகதைகள் — மின்னாக்கக் களஞ்சியம்

கலைஞர் மு. கருணாநிதியின் சிறுகதைகள் மற்றும் தனிநூலாக வெளிவந்த சிறுகதைப் பதிப்புகளை மூல ஸ்கேன்களின் பக்க வரிசையைக் காக்கும் வகையில் Markdown வடிவில் பாதுகாக்கும் களஞ்சியம்.

## மூலக் கொள்கை

> **மூல ஸ்கேன் தான் controlling source. Markdown ஒரு பாதுகாப்பு அடுக்கு; திருத்தப்பட்ட புதிய பதிப்பு அல்ல.**

மூலத்தில் இருப்பதை அமைதியாகச் சீர்திருத்தவோ, நவீனப்படுத்தவோ, ஊகித்து நிரப்பவோ கூடாது. தெளிவில்லாத வாசிப்புகள் வெளிப்படையாக `needs-review`, `partial`, அல்லது `blocked` எனக் குறிக்கப்பட வேண்டும்.

**மூல PDF கோப்புகள் இந்த repository-யில் commit செய்யப்படாது.** அவற்றின் filename, checksum, edition identity, scan condition மற்றும் page mapping மட்டும் metadata-வில் பதிவு செய்யப்படும்.

## தற்போதைய சிறுகதை

| சிறுகதை | ஆசிரியர் | scan-ல் தெரியும் பதிப்பு | நிலை |
|---|---|---|---|
| கிழவன் கனவு | மு. கருணாநிதி | இரண்டாம் பதிப்பு | **26-page Tamil audit CLOSED; English story-body COMPLETE / release-ready** |

### இறுதி physical-copy page status

- `verified`: **20**
- `blocked`: **6** — scans 3, 4, 15, 17, 21, 22
- `needs-review`: **0**
- `not-started`: **0**

The complete physical publication—from cover through front matter, story, printed errata, advertisements and back cover—now has **26 / 26 terminal page dispositions**.

The final front-matter pass converted scans **3–4** from generic review status to terminal `blocked`: scan 3 has two short `“குடியரசு”` review passages physically hidden by a library stamp; scan 4 has one short phrase that remains visually indistinct at maximum useful enlargement. No wording was reconstructed from context.

## Tamil story layer

Story-body scans **7–22** remain:

- **12 verified / 4 source-blocked / 0 needs-review**.

Control/derived files:

- `stories/kizhavan-kanavu/audit.md` — full 26-page audit closure;
- `stories/kizhavan-kanavu/sections/kizhavan-kanavu.md`;
- `stories/kizhavan-kanavu/sections/kizhavan-kanavu-errata.md` — **10** publisher corrections kept separately;
- `stories/kizhavan-kanavu/ASSEMBLY_REVIEW.md` — **PASS**.

## English translation stage

The **story-body English translation, scans 7–22, is COMPLETE**.

- 4 / 4 source batches reviewed;
- 16 / 16 story scans assembled;
- 8 / 8 terminal `SOURCE BLOCKED` story locations retained;
- editorial consistency review: **PASS**;
- release review: **PASS — release-ready with documented source limitations**.

Final/review files include:

- `stories/kizhavan-kanavu/translations/en/kizhavan-kanavu-en.md`
- `stories/kizhavan-kanavu/translations/en/ERRATA_NOTES.md`
- `stories/kizhavan-kanavu/translations/en/EDITORIAL_CONSISTENCY_REVIEW.md`
- `stories/kizhavan-kanavu/translations/en/RELEASE_REPORT.md`

Scan-22 publisher/printer/footer material remains outside the English story prose, and scan-23 errata is not silently substituted.

## களஞ்சிய அமைப்பு

```text
README.md
SHORT_STORY_PROCESSING_GUIDE.md
HANDOVER.md
stories/
  kizhavan-kanavu/
    README.md
    metadata/
    indexes/
    pages/
    sections/
    audit.md
    ASSEMBLY_REVIEW.md
    translations/
      en/
        README.md
        TRANSLATION_PLAN.md
        SOURCE_MAP.md
        ERRATA_NOTES.md
        kizhavan-kanavu-en.md
        EDITORIAL_CONSISTENCY_REVIEW.md
        RELEASE_REPORT.md
        batches/
```

விரிவான workflow: [`SHORT_STORY_PROCESSING_GUIDE.md`](SHORT_STORY_PROCESSING_GUIDE.md).  
முடிக்கப்பட்ட தற்போதைய சிறுகதை: [`stories/kizhavan-kanavu/README.md`](stories/kizhavan-kanavu/README.md).

## அடுத்த activity

**கிழவன் கனவு processing is closed for this supplied copy.** Do not reopen terminal blocked readings unless a genuinely clearer source is introduced. The next repository activity is to register and inspect the **next Kalaignar short-story PDF** when supplied.
