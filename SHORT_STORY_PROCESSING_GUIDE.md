# Short Story Processing Guide

இந்த repository-யில் கலைஞர் மு. கருணாநிதியின் சிறுகதைகள் மற்றும் தனிநூலாக வெளிவந்த சிறுகதைப் பதிப்புகளை ஒரே source-first முறையில் மின்னாக்குவதற்கான நிரந்தர வழிகாட்டி.

## 1. அடிப்படை விதி

> **மூல ஸ்கேன் தான் controlling source.**

Markdown உரை மூலத்தைப் பாதுகாக்க வேண்டும்; புதிய பதிப்பை உருவாக்கக் கூடாது.

அமைதியாக செய்யக்கூடாதவை:

- எழுத்துப்பிழை என்று தோன்றுவதைத் திருத்துதல்;
- பழைய சொல்/எழுத்து வடிவங்களை நவீனப்படுத்துதல்;
- இலக்கணம், punctuation, sandhi, பெயர்கள், எண்களை standardize செய்தல்;
- வரலாற்றுப் பெயர்/தேதி/மேற்கோளை memory அல்லது இணையப் பதிப்பால் மாற்றுதல்;
- தெளிவில்லாத எழுத்தை sentence பொருளை வைத்து ஊகித்தல்;
- scan-ல் இல்லாத heading/section label-ஐ body text-க்குள் silently சேர்த்தல்.

## 2. PDF policy

Source PDF repository-க்குள் commit செய்யப்படாது.

ஒவ்வொரு source-க்கும் `metadata/source.md`-ல் குறைந்தது பின்வருவன பதிவு செய்ய வேண்டும்:

- source filename;
- SHA-256 checksum;
- file size;
- scan page count;
- title / author as printed;
- edition / publication details visible in scan;
- printed-page numbering behaviour;
- scan condition;
- handwritten notes, library stamps, accession marks, bleed-through, illustrations, advertisements போன்ற anomalies.

## 3. ஒவ்வொரு சிறுகதைக்கும் அமைப்பு

```text
stories/<story>/
  README.md
  metadata/
    source.md
  indexes/
    page-map.md
  pages/
    0001-....md
  sections/
```

பின்னர் தேவைக்கேற்ப:

```text
  audit.md
  translations/en/
  TRANSLATION_REVIEW.md
  HANDOVER.md
```

## 4. பக்கவாரி பதிவு

ஒவ்வொரு scan page-க்கும் Markdown record கட்டாயம் — cover, review, preface, body text, contents/advertisement, blank page, back cover அனைத்தும் உட்பட.

Front matter:

```yaml
---
scan_page: 1
printed_page: null
story: "kizhavan-kanavu"
section: "cover"
page_type: "cover"
status: "verified"
language: "ta"
source_filename: "...pdf"
transcription_method: "direct visual comparison with source scan"
---
```

Status:

- `not-started`
- `partial`
- `needs-review`
- `verified`
- `blocked`

`verified` என்பது scan-ஐ நேரடியாகப் பார்த்து எழுத்து, punctuation, line/paragraph structure மற்றும் non-text marks அனைத்தையும் உறுதிப்படுத்திய பின்னரே பயன்படுத்த வேண்டும்.

## 5. Printed text vs non-text marks

தனித்தனியாகப் பதிவு செய்ய வேண்டும்:

- அச்சு உரை;
- கையெழுத்து / underline / marginal mark;
- library stamp / accession mark;
- bleed-through;
- scanner artefact;
- photograph / illustration / cover artwork / advertisement.

தெளிவில்லாத handwritten text-ஐ ஊகிக்க வேண்டாம். factual visual description மட்டும் தரலாம்.

## 6. சிறுகதை உரைக்கான கூடுதல் விதிகள்

- அச்சில் உள்ள paragraph boundaries-ஐ பாதுகாக்கவும்.
- dialogue punctuation மற்றும் quotation marks-ஐ source போலவே வைத்திருக்கவும்.
- archaic / historical spelling, names, titles source-ஐத் தாண்டி standardize செய்யக்கூடாது.
- front-matter reviews, publisher notes, author notes ஆகியவை story body-யுடன் கலக்கப்படக்கூடாது; அவற்றின் source position தனியாகப் பாதுகாக்கப்பட வேண்டும்.
- story முடிந்த பின் உள்ள publisher catalogue / commercial advertisements கூட scan publication-ன் physical record ஆக page-level-ல் பதிவு செய்யப்பட வேண்டும்; அவை story body அல்ல என்பது metadata-வில் தெளிவாக இருக்க வேண்டும்.

## 7. Batch workflow

1. repository state ஆய்வு செய்து duplicate story இல்லையென உறுதி செய்.
2. PDF scan identity, checksum, file size, page count உறுதி செய்.
3. cover / edition / publication / review / preface pages ஆய்வு செய்.
4. `metadata/source.md` உருவாக்கு/புதுப்பி.
5. அனைத்து scan pages-க்கும் `indexes/page-map.md` manifest உருவாக்கு.
6. சிறிய batch-ஆக page records உருவாக்கி transcription செய்.
7. தெளிவில்லாதவை `partial` அல்லது `needs-review` ஆக வைத்திரு.
8. batch முடிந்ததும் story README மற்றும் root `HANDOVER.md` புதுப்பி.
9. direct visual comparison முடிந்த பின் மட்டும் page status `verified` ஆக மாற்று.
10. முழு தமிழ் source audit முடியும் வரை English translation தொடங்கக்கூடாது.

## 8. Source-page marker

ஒவ்வொரு page record-ன் முடிவிலும்:

```html
<!-- மூல ஸ்கேன் பக்கம்: 1; அச்சுப் பக்கம்: — -->
```

## 9. Audit மற்றும் translation gates

Tamil transcription complete என்பது translation-ready என்பதல்ல.

Translation தொடங்குவதற்கு முன்:

1. எல்லா scan pages-க்கும் record இருக்க வேண்டும்;
2. story body pages அனைத்தும் direct visual audit செய்யப்பட்டிருக்க வேண்டும்;
3. unresolved readings வெளிப்படையாகக் குறிக்கப்பட்டிருக்க வேண்டும்;
4. page-map மற்றும் story README status ஒன்றோடொன்று பொருந்த வேண்டும்;
5. source text-ஐ silently modernize/correct செய்யாதது உறுதிப்படுத்தப்பட வேண்டும்.

## 10. Git / handover நடைமுறை

- narrow, descriptive commits செய்யவும்;
- ஒவ்வொரு batch-க்கும் repository/story status புதுப்பிக்கவும்;
- `HANDOVER.md`-ல் branch, current state, source identity/checksum, completed pages, unresolved items, next exact action பதிவு செய்யவும்;
- source PDF repository-க்கு push செய்யக்கூடாது.
