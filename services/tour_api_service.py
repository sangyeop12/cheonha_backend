import os
import requests
from dotenv import load_dotenv

load_dotenv()

TOUR_API_KEY = os.getenv("TOUR_API_KEY")
BASE_URL = "https://apis.data.go.kr/B551011/KorService2"


def fetch_nearby_places(lat: float, lng: float):
    url = f"{BASE_URL}/locationBasedList2"

    params = {
        "serviceKey": TOUR_API_KEY,
        "MobileOS": "ETC",
        "MobileApp": "CheonhaYujeok",
        "_type": "json",
        "mapX": lng,
        "mapY": lat,
        "radius": 3000,
        "arrange": "E",
        "numOfRows": 20,
        "pageNo": 1,
    }

    response = requests.get(url, params=params)
    response.raise_for_status()

    data = response.json()
    items = data.get("response", {}).get("body", {}).get("items", {}).get("item", [])

    if isinstance(items, dict):
        items = [items]

    return [
        {
            "contentId": item.get("contentid"),
            "title": item.get("title"),
            "address": item.get("addr1"),
            "imageUrl": item.get("firstimage"),
            "distance": item.get("dist"),
            "mapX": item.get("mapx"),
            "mapY": item.get("mapy"),
        }
        for item in items
    ]


def fetch_place_detail(content_id: str):
    url = f"{BASE_URL}/detailCommon2"

    params = {
    "serviceKey": TOUR_API_KEY,
    "MobileOS": "ETC",
    "MobileApp": "CheonhaYujeok",
    "_type": "json",
    "contentId": content_id,
}

    response = requests.get(url, params=params)
    response.raise_for_status()

    data = response.json()
    items = data.get("response", {}).get("body", {}).get("items", {}).get("item", [])

    if isinstance(items, list) and len(items) > 0:
        item = items[0]
    elif isinstance(items, dict):
        item = items
    else:
        return {
            "message": "상세 데이터가 없습니다.",
            "contentId": content_id,
            "raw": data,
        }

    return {
        "contentId": item.get("contentid"),
        "title": item.get("title"),
        "address": item.get("addr1"),
        "overview": item.get("overview"),
        "imageUrl": item.get("firstimage"),
        "mapX": item.get("mapx"),
        "mapY": item.get("mapy"),
    }