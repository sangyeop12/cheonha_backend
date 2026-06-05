import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY가 .env 파일에 없습니다.")

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.0-flash")


def translate_overview(text: str, language: str):
    try:
        prompt = f"""
        You are a friendly cultural heritage guide.

        Translate the following Korean cultural heritage explanation into {language}.
        Make it easy for foreign tourists to understand.

        Korean text:
        {text}
        """

        response = model.generate_content(prompt)

        return {
            "language": language,
            "translatedText": response.text
        }

    except Exception as e:
        return {
            "error": str(e),
            "message": "Gemini 번역 중 오류가 발생했습니다."
        }