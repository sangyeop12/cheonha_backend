from fastapi import APIRouter
from pydantic import BaseModel
from services.gemini_service import translate_overview
from services.comparison_service import create_cultural_comparison

router = APIRouter()


class ComparisonRequest(BaseModel):
    heritageName: str
    overviewKo: str
    country: str
    language: str


@router.get("/translate")
def translate(text: str, language: str):
    return translate_overview(text=text, language=language)


@router.post("/comparison")
def comparison(request: ComparisonRequest):
    return create_cultural_comparison(
        heritage_name=request.heritageName,
        overview_ko=request.overviewKo,
        country=request.country,
        language=request.language
    )