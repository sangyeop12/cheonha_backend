def create_cultural_comparison(
    heritage_name: str,
    overview_ko: str,
    country: str,
    language: str
):
    try:
        return {
            "heritageName": heritage_name,
            "country": country,
            "language": language,
            "comparisonTarget": f"{country} cultural heritage with a similar role",
            "reason": f"{heritage_name} can be compared with a familiar cultural concept from {country}.",
            "easyExplanation": f"For visitors from {country}, {heritage_name} can be understood through a similar traditional facility or cultural heritage from their own country."
        }

    except Exception as e:
        return {
            "error": str(e),
            "message": "문화 비유 생성 중 오류가 발생했습니다."
        }