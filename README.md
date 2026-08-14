# கலைஞர் சிறுகதைகள் — மின்னாக்கக் களஞ்சியம்

கலைஞர் மு. கருணாநிதியின் சிறுகதைகள் மற்றும் தனிநூலாக வெளிவந்த சிறுகதைப் பதிப்புகளை மூல ஸ்கேன்களின் பக்க வரிசையைக் காக்கும் வகையில் Markdown வடிவில் பாதுகாக்கும் களஞ்சியம்.

## மூலக் கொள்கை

> **மூல ஸ்கேன் தான் controlling source. Markdown ஒரு பாதுகாப்பு அடுக்கு; திருத்தப்பட்ட புதிய பதிப்பு அல்ல.**

மூலத்தில் இருப்பதை அமைதியாகச் சீர்திருத்தவோ, நவீனப்படுத்தவோ, ஊகித்து நிரப்பவோ கூடாது. தெளிவில்லாத வாசிப்புகள் வெளிப்படையாக `needs-review`, `partial`, அல்லது `blocked` எனக் குறிக்கப்பட வேண்டும்.

**மூல PDF கோப்புகள் இந்த repository-யில் commit செய்யப்படாது.** அவற்றின் filename, checksum, edition identity, scan condition மற்றும் page mapping மட்டும் metadata-வில் பதிவு செய்யப்படும்.

## தற்போதைய சிறுகதை

| சிறுகதை | ஆசிரியர் | scan-ல் தெரியும் பதிப்பு | நிலை |
|---|---|---|---|
| கிழவன் கனவு | மு. கருணாநிதி | இரண்டாம் பதிப்பு | **Tamil source finalized; assembly PASS; all 4 English source batches reviewed** |

### தற்போதைய page status

- `verified`: **20**
- `blocked`: **4**
- `needs-review`: **2** — front matter scans 3–4 only
- `not-started`: **0**

The complete physical publication—from cover through story, printed errata, advertisements and back cover—has page-level archival records.

The story-body scans **7–22** have all completed direct visual audit. Final story disposition is **12 verified / 4 source-blocked / 0 needs-review**. Scan **23**'s printed **`பிழை திருத்தம்.`** remains a separate correction layer and has not been silently merged into the archival page text, Tamil assembly, or English translation.

## Tamil story layer

- `stories/kizhavan-kanavu/audit.md`
- `stories/kizhavan-kanavu/sections/kizhavan-kanavu.md`
- `stories/kizhavan-kanavu/sections/kizhavan-kanavu-errata.md`
- `stories/kizhavan-kanavu/ASSEMBLY_REVIEW.md` — **PASS**

The synchronized Tamil story represents all **16** story scans exactly once and preserves every source-blocked location explicitly.

## English translation stage

The four controlled source batches are now all **source-reviewed**:

1. scans 7–10 — **source-reviewed**
2. scans 11–14 — **source-reviewed**
3. scans 15–18 — **source-reviewed**
4. scans 19–22 — **source-reviewed**

English source-reviewed coverage: **16 / 16 story scans**.

Batch files:

- `stories/kizhavan-kanavu/translations/en/batches/01-scans-07-10.md`
- `stories/kizhavan-kanavu/translations/en/batches/02-scans-11-14.md`
- `stories/kizhavan-kanavu/translations/en/batches/03-scans-15-18.md`
- `stories/kizhavan-kanavu/translations/en/batches/04-scans-19-22.md`

Across the English translation, **8 terminal SOURCE BLOCKED locations** remain visible at the exact source positions: scan 15 ×2, scan 17 ×1, scan 21 ×4, scan 22 ×1. None has been reconstructed from context, history, mythology, another edition, likely slogans, or web text.

The scan-22 publisher/printer/footer material remains outside the English story prose.

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
        batches/
          01-scans-07-10.md
          02-scans-11-14.md
          03-scans-15-18.md
          04-scans-19-22.md
```

விரிவான workflow: [`SHORT_STORY_PROCESSING_GUIDE.md`](SHORT_STORY_PROCESSING_GUIDE.md).  
தற்போதைய சிறுகதை: [`stories/kizhavan-kanavu/README.md`](stories/kizhavan-kanavu/README.md).

## அடுத்த activity

Assemble the four source-reviewed English batches into `stories/kizhavan-kanavu/translations/en/kizhavan-kanavu-en.md`, preserving all 16 source-page markers and all 8 SOURCE BLOCKED positions. Then perform the full cross-batch editorial/source consistency review before creating any release report.