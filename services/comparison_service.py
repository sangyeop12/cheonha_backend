def create_cultural_comparison(heritage_name: str, overview_ko: str, country: str, language: str):
    return {
        "heritageName": heritage_name,
        "country": country,
        "language": language,
        "comparisonTarget": f"{country} cultural heritage with a similar role",
        "reason": f"{heritage_name} is explained using the visitor's cultural background. Based on the Korean description, this heritage is compared with a similar concept from {country}.",
        "easyExplanation": f"For visitors from {country}, {heritage_name} can be understood by comparing it with a familiar cultural heritage or traditional facility from their own country."
    }