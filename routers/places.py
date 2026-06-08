from fastapi import APIRouter
from services.tour_api_service import fetch_nearby_places, fetch_place_detail
from services.gemini_service import translate_overview

router = APIRouter()


@router.get("/nearby")
def nearby(lat: float, lng: float):
    return fetch_nearby_places(lat=lat, lng=lng)


@router.get("/detail")
def detail(contentId: str):
    return fetch_place_detail(content_id=contentId)


@router.get("/detail-translated")
def detail_translated(contentId: str, language: str):
    detail_data = fetch_place_detail(content_id=contentId)

    overview_ko = detail_data.get("overview", "")

    translated = translate_overview(
        text=overview_ko,
        language=language
    )

    return {
        "contentId": detail_data.get("contentId"),
        "title": detail_data.get("title"),
        "address": detail_data.get("address"),
        "imageUrl": detail_data.get("imageUrl"),
        "mapX": detail_data.get("mapX"),
        "mapY": detail_data.get("mapY"),
        "overviewKo": overview_ko,
        "language": language,
        "overviewTranslated": translated.get("translatedText")
    }