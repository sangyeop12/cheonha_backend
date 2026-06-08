from deep_translator import GoogleTranslator


def translate_overview(text: str, language: str):

    proper_nouns = {
        "석빙고": "Seokbinggo",
        "첨성대": "Cheomseongdae",
        "불국사": "Bulguksa",
        "경복궁": "Gyeongbokgung"
    }

    for kor, eng in proper_nouns.items():
        text = text.replace(kor, eng)

    lang = language.upper()

    target_map = {
        "ENGLISH": "en",
        "JAPANESE": "ja",
        "CHINESE": "zh-CN",
        "KOREAN": "ko"
    }

    target_lang = target_map.get(lang, "en")

    translated = GoogleTranslator(
        source="ko",
        target=target_lang
    ).translate(text)

    return {
        "language": language,
        "translatedText": translated
    }