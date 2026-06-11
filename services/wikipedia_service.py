import requests


def fetch_wikipedia_summary(title: str, language: str = "ENGLISH"):
    lang_map = {
        "ENGLISH": "en",
        "JAPANESE": "ja",
        "CHINESE": "zh",
        "KOREAN": "ko"
    }

    wiki_lang = lang_map.get(language.upper(), "en")

    url = f"https://{wiki_lang}.wikipedia.org/w/api.php"

    params = {
        "action": "query",
        "format": "json",
        "prop": "extracts|pageimages",
        "titles": title,
        "exintro": True,
        "explaintext": True,
        "redirects": 1,
        "pithumbsize": 600
    }

    response = requests.get(url, params=params)
    response.raise_for_status()

    data = response.json()
    pages = data.get("query", {}).get("pages", {})

    for _, page in pages.items():
        return {
            "title": page.get("title"),
            "summary": page.get("extract", ""),
            "imageUrl": page.get("thumbnail", {}).get("source", "")
        }

    return {
        "title": title,
        "summary": "",
        "imageUrl": ""
    }