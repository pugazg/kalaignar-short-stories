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

### `blocked` என்பது கடைசி அவசர நிலை — story text-க்கு உடனடி முடிவு அல்ல

**No stones should be left unturned.** ஒரு story reading முதலில் தெளிவில்லாமல் தெரிகிறது என்பதற்காக அதை `blocked` என்று முடித்து workflow-ஐ மூடக்கூடாது.

Story text-ல் ஒரு வாசிப்பை `blocked` என விடுவதற்கு முன் கீழ்கண்ட escalation அனைத்தும் documented ஆக முயற்சிக்கப்பட வேண்டும்:

1. சாதாரண PDF render மட்டும் அல்லாமல் PDF-இன் **native embedded scan image** இருப்பின் அதை நேரடியாக ஆய்வு செய்;
2. progressively enlarged crops உருவாக்கி original/native pixels-ஐ ஒப்பிடு;
3. nearest-neighbour மற்றும் high-quality resampling ஆகிய இரண்டிலும் எழுத்துருவை ஒப்பிடு;
4. contrast, gamma, sharpening, grayscale/channel separation, threshold போன்ற non-destructive visual variants-ஐ முயற்சி செய்;
5. library stamp அல்லது seal story letters-ஐ கடக்கும்போது, thick stamp strokes மற்றும் thin print strokes-ஐ வேறுபடுத்த morphological / edge-based separation போன்ற image-processing முறைகளை முயற்சி செய்;
6. அதே பக்கத்திலும் அடுத்தடுத்த பக்கங்களிலும் வரும் ஒரே எழுத்துரு வடிவங்களுடன் character-by-character ஒப்பிடு;
7. page-boundary continuation / split word / repeated phrase இருக்கிறதா என்று முன்னும் பின்னும் உள்ள scan pages-ஐ மீண்டும் பார்க்கவும்;
8. user வழங்கும் தெளிவான reading இருந்தால் அதை native source image-க்கு எதிராக எழுத்துருவாரியாக verify செய்;
9. source image இன்னும் ambiguity விட்டால், **அதே work-ன் independent secondary witness** (வேறு scan, edition, author-ன் later quotation போன்றது) provenance-உடன் corroboration-ஆகப் பார்க்கலாம்;
10. secondary witness-ன் wording-ஐ controlling scan-க்கு silently import செய்யக்கூடாது. Source image ஆதரிக்கும் missing reading-ஐத் தீர்க்க மட்டுமே பயன்படுத்த வேண்டும்; witness வேறுபாடுகள் audit note-ல் வெளிப்படையாகப் பதிவு செய்ய வேண்டும்.

Story release/translation closure-க்கு முன் எல்லா பழைய `blocked` story locations-மும் இந்த exhaustive protocol-ன் கீழ் மீண்டும் திறந்து பரிசோதிக்கப்பட வேண்டும். **Processing objective: zero unresolved story-text blocks wherever a defensible reading can be recovered.**

ஒரு physical source உண்மையிலேயே எழுத்தை இழந்துவிட்டதும், exhaustive image work மற்றும் provenance-உடைய secondary witnesses எதுவும் தீர்வு தராததும் documented ஆக நிரூபிக்கப்பட்ட பின்னரே `blocked` terminal ஆக இருக்கலாம். Missing text-ஐ fabrication மூலம் zero blocks ஆக்குவது இந்த விதியின் நோக்கம் அல்ல.

### Difficult-reading verification sanity check

Image enhancement ஒரு plausible word அல்லது short fragment-ஐ காட்டுகிறது என்பதற்காக மட்டும் அந்த reading-ஐ `verified` ஆக promote செய்யக்கூடாது. குறிப்பாக stamp, bleed-through, worn type அல்லது touching glyphs இருக்கும் இடங்களில் **isolated character reconstruction can be confidently wrong**.

`verified` செய்வதற்கு முன்:

1. குறைந்தது முழு **phrase / clause / sentence span**-ஐ original/native scan-ல் மீண்டும் படி;
2. enhanced crop-ல் கண்ட fragment, left/right neighbouring words மற்றும் line continuation-க்கு எழுத்துருவாரியாக பொருந்துகிறதா பார்க்கவும்;
3. crop processing உருவாக்கிய artificial joins/splits உள்ளதா original pixels-ோடு ஒப்பிடு;
4. user ஒரு நீளமான exact reading கொடுத்தால், அதில் உள்ள ஒவ்வொரு recoverable word-ஐ source span-க்கு எதிராகச் சரிபார்; முன்பு `verified` செய்யப்பட்ட reading-ஐயும் தேவையானால் reopen செய்;
5. ஒரு short fragment-ஐ தீர்த்ததால் முழு sentence தீர்ந்துவிட்டதாகக் கருதக்கூடாது—stamp/mark கடக்கும் **முழு sentence path** ஆய்வு செய்யப்பட வேண்டும்;
6. ஒரு later correction பழைய `verified` reading தவறு என நிரூபித்தால், page record மட்டும் அல்லாமல் Tamil assembly, English translation, source map, audit, review/report files அனைத்தையும் resynchronize செய்;
7. audit note-ல் **what was previously read, what replaced it, and why the earlier verification failed** என்பதைக் குறிப்பிடு.

**Principle:** confidence in a processed crop is not the same as confidence in the source. Verification belongs to the complete source span.

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
- story text-க்கு `blocked` marker வந்தவுடன் அடுத்த batch-க்கு இயந்திரமாக நகராமல், மேலுள்ள exhaustive resolution protocol-ஐ முதலில் இயக்க வேண்டும்.

## 7. Batch workflow

1. repository state ஆய்வு செய்து duplicate story இல்லையென உறுதி செய்.
2. PDF scan identity, checksum, file size, page count உறுதி செய்.
3. cover / edition / publication / review / preface pages ஆய்வு செய்.
4. `metadata/source.md` உருவாக்கு/புதுப்பி.
5. அனைத்து scan pages-க்கும் `indexes/page-map.md` manifest உருவாக்கு.
6. சிறிய batch-ஆக page records உருவாக்கி transcription செய்.
7. தெளிவில்லாதவை முதலில் `partial` அல்லது `needs-review` ஆக வைத்திருந்து exhaustive resolution protocol-க்கு அனுப்பு; story text-ல் `blocked` status-ஐ shortcut ஆகப் பயன்படுத்தக்கூடாது.
8. batch முடிந்ததும் story README மற்றும் root `HANDOVER.md` புதுப்பி.
9. direct visual comparison + தேவையான exhaustive escalation + full-span sanity check முடிந்த பின் மட்டும் page status `verified` ஆக மாற்று.
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
3. ஒவ்வொரு முன்னாள் unresolved / blocked story reading-க்கும் exhaustive-resolution disposition பதிவு செய்யப்பட்டிருக்க வேண்டும்;
4. page-map மற்றும் story README status ஒன்றோடொன்று பொருந்த வேண்டும்;
5. source text-ஐ silently modernize/correct செய்யாதது உறுதிப்படுத்தப்பட வேண்டும்;
6. secondary witness பயன்படுத்தப்பட்ட இடமெல்லாம் provenance மற்றும் source-vs-witness distinction audit note-ல் இருக்க வேண்டும்;
7. difficult readings-க்கு isolated-fragment confidence அல்ல, complete phrase/clause/sentence source-span confidence உறுதி செய்யப்பட்டிருக்க வேண்டும்.

## 10. Git / handover நடைமுறை

- narrow, descriptive commits செய்யவும்;
- ஒவ்வொரு batch-க்கும் repository/story status புதுப்பிக்கவும்;
- `HANDOVER.md`-ல் branch, current state, source identity/checksum, completed pages, unresolved items, next exact action பதிவு செய்யவும்;
- source PDF repository-க்கு push செய்யக்கூடாது.

## 11. Cross-chat continuation protocol

இந்த archive நீண்டகாலமாக பல chat windows-ல் தொடரப்படுவதால் root `NEXT_CHAT_PROMPT.md` ஒரு **durable resume contract** ஆக பராமரிக்கப்பட வேண்டும்.

ஒவ்வொரு chat/window முடிவதற்கு முன் அல்லது user வேறு chat-ல் தொடர விரும்பும்போது:

1. முதலில் live GitHub `main`-ஐ fetch செய்து அதையே authoritative state ஆகக் கொள்ளவும்;
2. `HANDOVER.md`-ஐ current durable boundary, completed work, unresolved review queues, மற்றும் **next exact activity** உடன் புதுப்பிக்கவும்;
3. `NEXT_CHAT_PROMPT.md`-ஐ புதிய chat நேரடியாக paste செய்து தொடரக்கூடிய வகையில் புதுப்பிக்கவும்;
4. anthology project என்றால் `COLLECTION_SOURCE_GUIDE.md`, collection inventory/scan-map மற்றும் progress counts ஆகியவை handover/prompt-க்கு ஒத்திருக்க வேண்டும்;
5. user புதிய chat-ல் `Proceed with next activity` என்றால், `HANDOVER.md` / `NEXT_CHAT_PROMPT.md`-ல் பதிவு செய்யப்பட்ட next exact activity-ஐ routine clarification இல்லாமல் execute செய்ய வேண்டும்;
6. புதிய chat முன்பே completed/verified pages-ஐ காரணமின்றி redo செய்யக்கூடாது. User correction, stronger scan evidence, அல்லது live GitHub state inconsistency இருந்தால் மட்டும் reopen செய்யவும்;
7. புதிய chat தொடங்கும்போது குறைந்தது `SHORT_STORY_PROCESSING_GUIDE.md`, anthology என்றால் `COLLECTION_SOURCE_GUIDE.md`, `HANDOVER.md`, மற்றும் `NEXT_CHAT_PROMPT.md`-ஐ முழுமையாகப் படிக்க வேண்டும்;
8. prompt-ல் உள்ள checkpoint-ஐவிட live `main` முன்னேறியிருந்தால் **live `main` wins**. Prompt/chat summary-ஐ வைத்து newer repository work-ஐ overwrite/revert செய்யக்கூடாது;
9. controlling source scan புதிய chat-ல் கிடைக்கவில்லை என்றால் story transcription/verification-ஐ guess செய்து தொடரக்கூடாது. Source-ஐ மீண்டும் attach/resolve செய்த பிறகே source-dependent work செய்யவும்;
10. ஒவ்வொரு completed story/activity-க்கும் downstream control files-ஐ synchronize செய்த பின் `NEXT_CHAT_PROMPT.md`-ஐ அடுத்த exact activity-க்கு advance செய்யவும்.

**Cross-chat invariant:** repository files—not memory of an earlier chat—are the durable project state.