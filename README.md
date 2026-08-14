# கலைஞர் சிறுகதைகள் — மின்னாக்கக் களஞ்சியம்

கலைஞர் மு. கருணாநிதியின் சிறுகதைகள் மற்றும் தனிநூலாக வெளிவந்த சிறுகதைப் பதிப்புகளை மூல ஸ்கேன்களின் பக்க வரிசையைக் காக்கும் வகையில் Markdown வடிவில் பாதுகாக்கும் களஞ்சியம்.

## மூலக் கொள்கை

> **மூல ஸ்கேன் தான் controlling source. Markdown ஒரு பாதுகாப்பு அடுக்கு; திருத்தப்பட்ட புதிய பதிப்பு அல்ல.**

மூலத்தில் இருப்பதை அமைதியாகச் சீர்திருத்தவோ, நவீனப்படுத்தவோ, ஊகித்து நிரப்பவோ கூடாது. தெளிவில்லாத வாசிப்புகள் வெளிப்படையாக `needs-review`, `partial`, அல்லது `blocked` எனக் குறிக்கப்பட வேண்டும்.

**மூல PDF கோப்புகள் இந்த repository-யில் commit செய்யப்படாது.** அவற்றின் filename, checksum, edition identity, scan condition மற்றும் page mapping மட்டும் metadata-வில் பதிவு செய்யப்படும்.

## தற்போதைய சிறுகதை

| சிறுகதை | ஆசிரியர் | scan-ல் தெரியும் பதிப்பு | நிலை |
|---|---|---|---|
| கிழவன் கனவு | மு. கருணாநிதி | இரண்டாம் பதிப்பு | source registered; 26-page manifest complete; 6/26 page records created |

### தற்போதைய page status

- scan 1 — `verified`
- scans 2–6 — `partial` (உறுதிப்படுத்தப்பட்ட headings/dates/signatures மட்டும்; முழு body transcription pending)
- scans 7–26 — `not-started`

இணைக்கப்பட்ட scan-ல் சிறுகதை body-க்கு முன் மதிப்புரைகள் / வெளியீட்டாளர் குறிப்புகள் / ஆசிரியர் குறிப்பு உள்ளன; body முடிந்த பின் பிற நூல்கள் மற்றும் வணிக விளம்பரப் பக்கங்களும் உள்ளன. அவையும் scanned publication-ன் பகுதிகளாக page-level archival records-ல் பதிவு செய்யப்படும்.

அடுத்த batch: **scans 2–6 முழுமையான word-for-word visual transcription மற்றும் audit**. அதன் பின் story body scans **7–10**.

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

ஒவ்வொரு சிறுகதையும் தனித்த `stories/<story-slug>/` அடைவில் பதிவாகும். பக்கவாரி records முதன்மை archival layer; பின்னர் தேவையான assembled text, audit, translation மற்றும் review files சேர்க்கப்படும்.

விரிவான workflow: [`SHORT_STORY_PROCESSING_GUIDE.md`](SHORT_STORY_PROCESSING_GUIDE.md).  
தற்போதைய சிறுகதை: [`stories/kizhavan-kanavu/README.md`](stories/kizhavan-kanavu/README.md).
