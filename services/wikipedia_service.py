import requests


def fetch_wikipedia_summary(title: str, language: str = "ENGLISH"):
    try:
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
            "exintro": "1",
            "explaintext": "1",
            "redirects": "1",
            "pithumbsize": "600"
        }

        response = requests.get(
            url,
            params=params,
            headers={"User-Agent": "CheonhaYujeok/1.0"}
        )
        response.raise_for_status()

        data = response.json()
        pages = data.get("query", {}).get("pages", {})

        for _, page in pages.items():
            if page.get("missing") == "":
                return {
                    "title": title,
                    "summary": "",
                    "imageUrl": "",
                    "message": "Wikipedia 문서를 찾을 수 없습니다."
                }

            return {
                "title": page.get("title", title),
                "summary": page.get("extract", ""),
                "imageUrl": page.get("thumbnail", {}).get("source", "")
            }

        return {
            "title": title,
            "summary": "",
            "imageUrl": "",
            "message": "검색 결과가 없습니다."
        }

    except Exception as e:
        return {
            "title": title,
            "summary": "",
            "imageUrl": "",
            "error": str(e),
            "message": "Wikipedia API 호출 중 오류가 발생했습니다."
        }