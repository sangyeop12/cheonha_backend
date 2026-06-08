def create_cultural_comparison(heritage_name: str, country: str, language: str):
    country_upper = country.upper()

    comparison_map = {
        "JAPAN": {
            "comparisonTarget": "Japanese traditional ice storage facilities",
            "reason": "Both were used to preserve ice before modern refrigerators existed."
        },
        "CHINA": {
            "comparisonTarget": "ancient Chinese imperial ice storage systems",
            "reason": "Both show how premodern societies stored ice and managed seasonal resources."
        },
        "USA": {
            "comparisonTarget": "early American ice houses",
            "reason": "Both were built to store ice before electric refrigeration became common."
        }
    }

    result = comparison_map.get(country_upper, {
        "comparisonTarget": "traditional ice storage buildings",
        "reason": "They show how people preserved ice before modern technology."
    })

    return {
        "heritageName": heritage_name,
        "country": country,
        "language": language,
        "comparisonTarget": result["comparisonTarget"],
        "reason": result["reason"]
    }