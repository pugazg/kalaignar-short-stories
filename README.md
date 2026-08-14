# கலைஞர் சிறுகதைகள் — மின்னாக்கக் களஞ்சியம்

கலைஞர் மு. கருணாநிதியின் சிறுகதைகள் மற்றும் தனிநூலாக வெளிவந்த சிறுகதைப் பதிப்புகளை மூல ஸ்கேன்களின் பக்க வரிசையைக் காக்கும் வகையில் Markdown வடிவில் பாதுகாக்கும் களஞ்சியம்.

## மூலக் கொள்கை

> **மூல ஸ்கேன் தான் controlling source. Markdown ஒரு பாதுகாப்பு அடுக்கு; திருத்தப்பட்ட புதிய பதிப்பு அல்ல.**

மூலத்தில் இருப்பதை அமைதியாகச் சீர்திருத்தவோ, நவீனப்படுத்தவோ, ஊகித்து நிரப்பவோ கூடாது. தெளிவில்லாத வாசிப்புகள் வெளிப்படையாக `needs-review`, `partial`, அல்லது `blocked` எனக் குறிக்கப்பட வேண்டும்.

**மூல PDF கோப்புகள் இந்த repository-யில் commit செய்யப்படாது.** அவற்றின் filename, checksum, edition identity, scan condition மற்றும் page mapping மட்டும் metadata-வில் பதிவு செய்யப்படும்.

## தற்போதைய சிறுகதை

| சிறுகதை | ஆசிரியர் | scan-ல் தெரியும் பதிப்பு | நிலை |
|---|---|---|---|
| கிழவன் கனவு | மு. கருணாநிதி | இரண்டாம் பதிப்பு | **26/26 page records; story source audit complete; 12/16 story scans verified; 4/16 source-blocked** |

### தற்போதைய page status

- `verified`: **20**
- `blocked`: **4**
- `needs-review`: **2** — front matter scans 3–4
- `not-started`: **0**

The complete physical publication—from cover through story, printed errata, advertisements and back cover—has page-level archival records.

The story-body scans **7–22** have all completed direct visual audit. The final high-resolution pass resolved scans **8, 14 and 18**; scans **15, 17, 21 and 22** are now formally `blocked` because the supplied physical source itself does not expose enough information to recover specific words/phrases safely. Those gaps are marked `blocked-by-source`, not guessed.

Scan **23**'s printed **`பிழை திருத்தம்.`** remains a separate correction layer and has not been silently merged into the archival page text.

Current derived artifacts:

- `stories/kizhavan-kanavu/sections/kizhavan-kanavu.md`
- `stories/kizhavan-kanavu/sections/kizhavan-kanavu-errata.md`
- `stories/kizhavan-kanavu/ASSEMBLY_REVIEW.md`
- `stories/kizhavan-kanavu/audit.md`

The page records are the finalized Tamil source layer. The assembled Tamil story still requires one synchronization pass to reflect the newly resolved readings and final `blocked-by-source` markers before the English translation workflow is opened.

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
```

ஒவ்வொரு சிறுகதையும் தனித்த `stories/<story-slug>/` அடைவில் பதிவாகும். பக்கவாரி records முதன்மை archival layer; assembled text, errata, audit, translation போன்றவை derived layers ஆக மட்டுமே சேர்க்கப்படும்.

விரிவான workflow: [`SHORT_STORY_PROCESSING_GUIDE.md`](SHORT_STORY_PROCESSING_GUIDE.md).  
தற்போதைய சிறுகதை: [`stories/kizhavan-kanavu/README.md`](stories/kizhavan-kanavu/README.md).

## அடுத்த activity

Synchronize `stories/kizhavan-kanavu/sections/kizhavan-kanavu.md` and `ASSEMBLY_REVIEW.md` with the finalized page records. After that consistency check passes, create the English translation workflow/plan while preserving every source-blocked gap explicitly.
