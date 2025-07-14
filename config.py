# config.py
from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    APP_NAME = os.getenv("APP_NAME")
    APP_ENV = os.getenv("APP_ENV")
    PORT = int(os.getenv("PORT", 8000))

    DATABASE_URL = os.getenv("DATABASE_URL")
    SECRET_KEY = os.getenv("SECRET_KEY")
    CLAUDE_API_KEY = os.getenv("CLAUDE_API_KEY")
    N8N_API_URL = os.getenv("N8N_API_URL")

settings = Settings()

