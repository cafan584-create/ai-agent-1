from pydantic_settings import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    # Supabase
    supabase_url: str = ""
    supabase_db_url: str = ""

    # API Keys
    fred_api_key: str = ""
    exchangerate_api_key: str = ""
    newsapi_key: str = ""

    # Telegram Bot
    telegram_bot_token: str = ""

    # Optional AI
    groq_api_key: str = ""

    # App
    app_env: str = "development"
    app_port: int = 8000

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


@lru_cache()
def get_settings() -> Settings:
    return Settings()