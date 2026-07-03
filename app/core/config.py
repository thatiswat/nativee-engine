from pathlib import Path
from dotenv import load_dotenv
import os

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent.parent

UPLOAD_DIR = BASE_DIR / "uploads"
UPLOAD_DIR.mkdir(exist_ok=True)

GROQ_API_KEY = os.getenv(
    "GROQ_API_KEY",
    "",
).strip()

TRANSLATION_PROVIDER = os.getenv(
    "TRANSLATION_PROVIDER",
    "google",
).strip().lower()

ENGINE_HOST = os.getenv(
    "ENGINE_HOST",
    "0.0.0.0",
)

ENGINE_PORT = int(
    os.getenv(
        "ENGINE_PORT",
        "8001",
    )
)