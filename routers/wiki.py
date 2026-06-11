from fastapi import APIRouter
from services.wikipedia_service import fetch_wikipedia_summary

router = APIRouter()


@router.get("/summary")
def wiki_summary(title: str, language: str = "ENGLISH"):
    return fetch_wikipedia_summary(
        title=title,
        language=language
    )