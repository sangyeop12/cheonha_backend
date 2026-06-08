from fastapi import APIRouter
from services.gemini_service import translate_overview
from services.comparison_service import create_cultural_comparison

router = APIRouter()


@router.get("/translate")
def translate(text: str, language: str):

    return translate_overview(
        text=text,
        language=language
    )

@router.get("/comparison")
def comparison(heritageName: str, country: str, language: str):
    return create_cultural_comparison(
        heritage_name=heritageName,
        country=country,
        language=language
    )
