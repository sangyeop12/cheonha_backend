import os
import json
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.0-flash")


def create_cultural_comparison(heritage_name: str, overview_ko: str, country: str, language: str):

    prompt = f"""
You are a cultural heritage guide AI.

Korean heritage name:
{heritage_name}

Korean description:
{overview_ko}

Visitor country:
{country}

Response language:
{language}

Task:
Find a REAL cultural heritage, traditional facility, historical object, or cultural concept from the visitor's country that can help them understand this Korean heritage.

Rules:
- Do not invent fake heritage.
- Use a real and culturally meaningful comparison.
- Explain why they are similar.
- Use the requested response language.
- Return only JSON.

JSON format:
{{
  "heritageName": "{heritage_name}",
  "country": "{country}",
  "comparisonTarget": "real foreign comparison target",
  "reason": "why they are similar",
  "easyExplanation": "easy explanation for tourists"
}}
"""

    response = model.generate_content(prompt)

    try:
        return json.loads(response.text)
    except Exception:
        return {
            "heritageName": heritage_name,
            "country": country,
            "comparisonTarget": "",
            "reason": "",
            "easyExplanation": response.text
        }