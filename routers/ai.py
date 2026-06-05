from fastapi import APIRouter
from services.gemini_service import translate_overview

router = APIRouter()


@router.get("/translate")
def translate(text: str, language: str):

    return translate_overview(
        text=text,
        language=language
    )
