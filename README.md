# கலைஞர் சிறுகதைகள் — மின்னாக்கக் களஞ்சியம்

கலைஞர் மு. கருணாநிதியின் சிறுகதைகள் மற்றும் தனிநூலாக வெளிவந்த சிறுகதைப் பதிப்புகளை மூல ஸ்கேன்களின் பக்க வரிசையைக் காக்கும் வகையில் Markdown வடிவில் பாதுகாக்கும் களஞ்சியம்.

## மூலக் கொள்கை

> **மூல ஸ்கேன் தான் controlling source. Markdown ஒரு பாதுகாப்பு அடுக்கு; திருத்தப்பட்ட புதிய பதிப்பு அல்ல.**

மூலத்தில் இருப்பதை அமைதியாகச் சீர்திருத்தவோ, நவீனப்படுத்தவோ, ஊகித்து நிரப்பவோ கூடாது. தெளிவில்லாத வாசிப்புகள் வெளிப்படையாக `needs-review`, `partial`, அல்லது `blocked` எனக் குறிக்கப்பட வேண்டும்.

**மூல PDF கோப்புகள் இந்த repository-யில் commit செய்யப்படாது.** அவற்றின் filename, checksum, edition identity, scan condition மற்றும் page mapping மட்டும் metadata-வில் பதிவு செய்யப்படும்.

## தற்போதைய சிறுகதை

| சிறுகதை | ஆசிரியர் | scan-ல் தெரியும் பதிப்பு | நிலை |
|---|---|---|---|
| கிழவன் கனவு | மு. கருணாநிதி | இரண்டாம் பதிப்பு | **26/26 page records; scan 7–23 Tamil audit completed; Tamil assembly next** |

### தற்போதைய page status

- `verified` — **16** pages
- `needs-review` — **10** pages
- `not-started` — **0**

The complete physical publication—from cover through story, printed errata, advertisements and back cover—has page-level archival records.

The dedicated Tamil source audit for scans **7–23** is now complete. Scans **7, 9, 10, 11, 12, 16, 19, 20 and 23** were promoted to `verified`; scans **8, 13, 14, 15, 17, 18, 21 and 22** retain narrowly documented source-condition/reconciliation issues. Scans **3–4** retain their earlier front-matter uncertainties.

Scan **23** is a printed **`பிழை திருத்தம்.`** table followed by tobacco advertising. The errata table is now fully audited, but remains a separate source layer and is not silently applied to the archival page text.

Audit report: [`stories/kizhavan-kanavu/audit.md`](stories/kizhavan-kanavu/audit.md).

அடுத்த activity: create the assembled Tamil reading text in `stories/kizhavan-kanavu/sections/`, retaining explicit unresolved readings and documenting the printed errata separately. A consistency review must follow before English translation begins.

## களஞ்சிய அமைப்பு

```text
README.md
SHORT_STORY_PROCESSING_GUIDE.md
HANDOVER.md
stories/
  kizhavan-kanavu/
    README.md
    audit.md
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
