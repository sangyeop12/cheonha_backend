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

    fake_translations = {
        "English": "Seokbinggo was a storage building used to keep ice during the Joseon Dynasty.",
        "Japanese": "石氷庫は氷を保存するための倉庫でした。",
        "Chinese": "石冰库是古代储存冰块的仓库。"
    }

    return {
        "language": language,
        "translatedText": fake_translations.get(
            language,
            f"{language} translation example"
        )
    }