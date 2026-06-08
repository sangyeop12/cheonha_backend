from deep_translator import GoogleTranslator


def translate_overview(text: str, language: str):
    lang = language.upper()

    target_map = {
        "ENGLISH": "en",
        "JAPANESE": "ja",
        "CHINESE": "zh-CN",
        "KOREAN": "ko"
    }

    target_lang = target_map.get(lang, "en")

    try:
        translated = GoogleTranslator(
            source="ko",
            target=target_lang
        ).translate(text)

        return {
            "language": language,
            "translatedText": translated
        }

    except Exception as e:
        return {
            "language": language,
            "error": str(e),
            "message": "번역 중 오류가 발생했습니다."
        }