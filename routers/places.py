from fastapi import APIRouter
from services.tour_api_service import (
    fetch_nearby_places,
    fetch_place_detail
)

router = APIRouter()


# 주변 관광지
@router.get("/nearby")
def nearby(lat: float, lng: float):

    return fetch_nearby_places(
        lat=lat,
        lng=lng
    )


# 상세 정보
@router.get("/detail")
def detail(contentId: str):

    return fetch_place_detail(
        content_id=contentId
    )
