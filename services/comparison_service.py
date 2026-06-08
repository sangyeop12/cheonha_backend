import os
import json
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.0-flash")


def create_cultural_comparison(
    heritage_name: str,
    overview_ko: str,
    country: str,
    language: str
):
    try:
        prompt = f"""
You are an expert cultural heritage guide.

Korean heritage name:
{heritage_name}

Korean heritage description:
{overview_ko}

Visitor country:
{country}

Response language:
{language}

Task:
Find ONE real cultural heritage, traditional facility, historical building, object, or cultural concept from {country} that helps visitors understand the Korean heritage.

Rules:
- The comparison target must be real.
- Do not invent fake names.
- Choose the closest cultural or functional equivalent.
- Explain in simple tourist-friendly language.
- Write the answer in {language}.
- Return ONLY valid JSON.
- Do not include markdown.

JSON format:
{{
  "heritageName": "{heritage_name}",
  "country": "{country}",
  "language": "{language}",
  "comparisonTarget": "real comparison target name",
  "reason": "why they are similar",
  "easyExplanation": "simple explanation for tourists"
}}
"""

        response = model.generate_content(prompt)

        text = response.text.strip()

        if text.startswith("```json"):
            text = text.replace("```json", "").replace("```", "").strip()
        elif text.startswith("```"):
            text = text.replace("```", "").strip()

        return json.loads(text)

    except Exception as e:
        return {
            "heritageName": heritage_name,
            "country": country,
            "language": language,
            "comparisonTarget": None,
            "reason": None,
            "easyExplanation": None,
            "error": str(e),
            "message": "Gemini 문화 비유 생성 중 오류가 발생했습니다."
        }