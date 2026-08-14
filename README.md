# கலைஞர் சிறுகதைகள் — மின்னாக்கக் களஞ்சியம்

கலைஞர் மு. கருணாநிதியின் சிறுகதைகள் மற்றும் தனிநூலாக வெளிவந்த சிறுகதைப் பதிப்புகளை மூல ஸ்கேன்களின் பக்க வரிசையைக் காக்கும் வகையில் Markdown வடிவில் பாதுகாக்கும் களஞ்சியம்.

## மூலக் கொள்கை

> **மூல ஸ்கேன் தான் controlling source. Markdown ஒரு பாதுகாப்பு அடுக்கு; திருத்தப்பட்ட புதிய பதிப்பு அல்ல.**

மூலத்தில் இருப்பதை அமைதியாகச் சீர்திருத்தவோ, நவீனப்படுத்தவோ, ஊகித்து நிரப்பவோ கூடாது. தெளிவில்லாத வாசிப்புகள் வெளிப்படையாக `needs-review`, `partial`, அல்லது `blocked` எனக் குறிக்கப்பட வேண்டும்.

**மூல PDF கோப்புகள் இந்த repository-யில் commit செய்யப்படாது.** அவற்றின் filename, checksum, edition identity, scan condition மற்றும் page mapping மட்டும் metadata-வில் பதிவு செய்யப்படும்.

## தற்போதைய சிறுகதை

| சிறுகதை | ஆசிரியர் | scan-ல் தெரியும் பதிப்பு | நிலை |
|---|---|---|---|
| கிழவன் கனவு | மு. கருணாநிதி | இரண்டாம் பதிப்பு | **26/26 page records created; full scan archived; Tamil audit pending** |

### தற்போதைய page status

- scans 1, 2, 5, 6, 24, 25, 26 — `verified`
- scans 3, 4, 7–23 — `needs-review`
- `not-started` — **0**

The complete physical publication—from cover through story, printed errata, advertisements and back cover—now has page-level archival records.

Scans **7–22** contain the **கிழவன் கனவு** story body and have been directly transcribed from the scan. They remain `needs-review` because the next stage is a dedicated Tamil source audit of worn / ambiguous type and stamp-obscured readings. No later edition or context-based reconstruction has been used to silently fill those gaps.

A significant back-matter correction was also made: scan **23** is a printed **`பிழை திருத்தம்.`** table followed by tobacco advertising, not a publisher catalogue. The errata is preserved separately and is not silently applied to the archival page text.

அடுத்த activity: **full Tamil source audit of scans 7–23**, followed by an assembled Tamil story text only after the page readings are reviewed.

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
```

ஒவ்வொரு சிறுகதையும் தனித்த `stories/<story-slug>/` அடைவில் பதிவாகும். பக்கவாரி records முதன்மை archival layer; பின்னர் தேவையான section/chapter assemblies, audit, translation மற்றும் review files சேர்க்கப்படும்.

விரிவான workflow: [`SHORT_STORY_PROCESSING_GUIDE.md`](SHORT_STORY_PROCESSING_GUIDE.md).  
தற்போதைய சிறுகதை: [`stories/kizhavan-kanavu/README.md`](stories/kizhavan-kanavu/README.md).
