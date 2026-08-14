# கலைஞர் சிறுகதைகள் — மின்னாக்கக் களஞ்சியம்

கலைஞர் மு. கருணாநிதியின் சிறுகதைகள் மற்றும் தனிநூலாக வெளிவந்த சிறுகதைப் பதிப்புகளை மூல ஸ்கேன்களின் பக்க வரிசையைக் காக்கும் வகையில் Markdown வடிவில் பாதுகாக்கும் களஞ்சியம்.

## மூலக் கொள்கை

> **மூல ஸ்கேன் தான் controlling source. Markdown ஒரு பாதுகாப்பு அடுக்கு; திருத்தப்பட்ட புதிய பதிப்பு அல்ல.**

மூலத்தில் இருப்பதை அமைதியாகச் சீர்திருத்தவோ, நவீனப்படுத்தவோ, ஊகித்து நிரப்பவோ கூடாது. தெளிவில்லாத வாசிப்புகள் வெளிப்படையாக `blocked` ஆகக் குறிக்கப்பட வேண்டும்.

**மூல PDF கோப்புகள் இந்த repository-யில் commit செய்யப்படாது.** அவற்றின் filename, checksum, edition identity, scan condition மற்றும் page mapping மட்டும் metadata-வில் பதிவு செய்யப்படும்.

## தற்போதைய சிறுகதை

| சிறுகதை | ஆசிரியர் | scan-ல் தெரியும் பதிப்பு | நிலை |
|---|---|---|---|
| கிழவன் கனவு | மு. கருணாநிதி | இரண்டாம் பதிப்பு | **26-page Tamil audit CLOSED; English story-body COMPLETE / release-ready** |

### இறுதி physical-copy page status

- `verified`: **21**
- `blocked`: **5** — scans 3, 4, 15, 17, 21
- `needs-review`: **0**
- `not-started`: **0**

The complete physical publication has **26 / 26 terminal page dispositions**.

## Tamil story layer

Story-body scans **7–22**:

- **13 verified / 3 source-blocked / 0 needs-review**;
- explicit blocked story-text locations: **7** — scan 15 ×2, scan 17 ×1, scan 21 ×4.

Scan **22 / printed page 18** is now verified with the corrected ending:

**`இதே கனவைத்தான் ராமசாமிப்பெரியாரும் காண்கிறார். வரப்போகும் திராவிடத்தின் அழியாத சித்திரம் ; அந்தக் கிழவன் கனவு.`**

The salesperson / advertisement / publisher-printer material below that conclusion is not part of the story and is intentionally excluded from story transcription/translation scope.

Control/derived files:

- `stories/kizhavan-kanavu/audit.md` — full 26-page audit closure;
- `stories/kizhavan-kanavu/sections/kizhavan-kanavu.md`;
- `stories/kizhavan-kanavu/sections/kizhavan-kanavu-errata.md` — **10** publisher corrections kept separately;
- `stories/kizhavan-kanavu/ASSEMBLY_REVIEW.md` — **PASS**.

## English translation stage

The **story-body English translation, scans 7–22, is COMPLETE**.

- 4 / 4 source batches reviewed;
- 16 / 16 story scans assembled;
- **7 / 7** terminal `SOURCE BLOCKED` story locations retained;
- scan 22 conclusion resolved and translated;
- editorial consistency review: **PASS**;
- release review: **PASS — release-ready with documented source limitations**.

Resolved English ending:

**“Ramasami Periyar too sees this very dream. The imperishable image of the Dravidam that is to come; that is the old man's dream.”**

Final/review files include:

- `stories/kizhavan-kanavu/translations/en/kizhavan-kanavu-en.md`
- `stories/kizhavan-kanavu/translations/en/ERRATA_NOTES.md`
- `stories/kizhavan-kanavu/translations/en/EDITORIAL_CONSISTENCY_REVIEW.md`
- `stories/kizhavan-kanavu/translations/en/RELEASE_REPORT.md`

Scan-23 errata is not silently substituted into archival Tamil or English prose.

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
