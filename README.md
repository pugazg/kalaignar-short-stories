# கலைஞர் சிறுகதைகள் — மின்னாக்கக் களஞ்சியம்

கலைஞர் மு. கருணாநிதியின் சிறுகதைகள் மற்றும் தனிநூலாக வெளிவந்த சிறுகதைப் பதிப்புகளை மூல ஸ்கேன்களின் பக்க வரிசையைக் காக்கும் வகையில் Markdown வடிவில் பாதுகாக்கும் களஞ்சியம்.

## மூலக் கொள்கை

> **மூல ஸ்கேன் தான் controlling source. Markdown ஒரு பாதுகாப்பு அடுக்கு; திருத்தப்பட்ட புதிய பதிப்பு அல்ல.**

மூலத்தில் இருப்பதை அமைதியாகச் சீர்திருத்தவோ, நவீனப்படுத்தவோ, ஊகித்து நிரப்பவோ கூடாது.

அதே நேரத்தில் story text-ல் ஒரு வாசிப்பு கடினமாக இருப்பதற்காக அதை விரைவாக `blocked` என்று விட்டுவிடக்கூடாது. Repository guide-ன் புதிய நிரந்தர விதி:

> **No stones should be left unturned.**

Native embedded scan, high-resolution enlargement, alternate image variants, stamp-stroke separation, neighbouring typeform comparison, page-boundary checks, user-supplied reading verification, மற்றும் provenance-உடைய secondary corroboration ஆகிய escalation-கள் தேவையான அளவு முயற்சிக்கப்பட்ட பிறகே story text `blocked` ஆக இருக்கலாம். Secondary witness source-ஐ silently overwrite செய்யக்கூடாது.

**மூல PDF கோப்புகள் repository-யில் commit செய்யப்படாது.** Filename, checksum, edition identity, scan condition மற்றும் page mapping மட்டும் metadata-வில் பதிவு செய்யப்படும்.

## தற்போதைய சிறுகதை

| சிறுகதை | ஆசிரியர் | scan-ல் தெரியும் பதிப்பு | நிலை |
|---|---|---|---|
| கிழவன் கனவு | மு. கருணாநிதி | இரண்டாம் பதிப்பு | **Story source 16/16 VERIFIED; English COMPLETE / source-complete / release-ready** |

## கிழவன் கனவு — final story status

Story-body scans **7–22**:

- `verified`: **16 / 16**
- `blocked`: **0**
- `needs-review`: **0**
- unresolved story-text locations: **0**

Formerly difficult readings on scans 15, 17, 21 and 22 were all reopened and resolved.

Key final readings include:

- scan 15: `துர் எண்ணத்தை`, `புது தழுவகம் ஒன்று`, `அநாதிப் பிள்ளையாருக்கு`, `பிள்ளை பிறக்குமென்று`;
- scan 17: `பார்வதியை அணைத்தபடி பரமன்`;
- scan 21: `இந்த நினைவு அந்த துணைவர்கள் உள்ளத்தை உருக்கிவார்த்தது.`, `ஆநிரைகோ`, `உரநெஞ்சன்`, `இந்தி எதிர்ப்பு`;
- scan 22: `இதே கனவைத்தான் ராமசாமிப்பெரியாரும் காண்கிறார். வரப்போகும் திராவிடத்தின் அழியாத சித்திரம் ; அந்தக் கிழவன் கனவு.`

The salesperson / advertisement / publisher-printer matter below the scan-22 conclusion is not part of the story and is excluded from story transcription/translation scope.

## Physical-copy page status

Across all 26 scans:

- `verified`: **24**
- `blocked`: **2** — front-matter scans 3–4 only
- `needs-review`: **0**
- `not-started`: **0**

The remaining two blocked page records are non-story front matter. If full-publication zero-block closure is required, the same exhaustive protocol must be applied to them.

## Tamil story layer

- `stories/kizhavan-kanavu/audit.md`
- `stories/kizhavan-kanavu/sections/kizhavan-kanavu.md` — **zero blocked markers**
- `stories/kizhavan-kanavu/sections/kizhavan-kanavu-errata.md` — **10** publisher corrections separately mapped
- `stories/kizhavan-kanavu/ASSEMBLY_REVIEW.md` — **PASS / 16 of 16 verified**

## English translation stage

The **story-body English translation, scans 7–22, is COMPLETE and source-complete**.

- 4 / 4 source batches reviewed;
- 16 / 16 story scans assembled;
- English `SOURCE BLOCKED` markers: **0**;
- editorial consistency review: **PASS**;
- release review: **PASS — story source complete / release-ready**.

Final English ending:

**“Periyar EV Ramasamy too sees this very dream. The imperishable image of the Dravidam that is to come; that is the old man's dream.”**

Final/review files include:

- `stories/kizhavan-kanavu/translations/en/kizhavan-kanavu-en.md`
- `stories/kizhavan-kanavu/translations/en/ERRATA_NOTES.md`
- `stories/kizhavan-kanavu/translations/en/EDITORIAL_CONSISTENCY_REVIEW.md`
- `stories/kizhavan-kanavu/translations/en/RELEASE_REPORT.md`

Scan-23 errata remains a separate textual layer and is not silently substituted into archival Tamil or English prose.

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

The **கிழவன் கனவு story body is fully resolved and closed**. Optional next cleanup for this physical publication is to apply the same exhaustive protocol to non-story front-matter scans **3–4**; otherwise the next archival activity is source registration for the next Kalaignar short-story PDF.
