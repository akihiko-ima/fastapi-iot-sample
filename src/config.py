from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache


class Settings(BaseSettings):
    secret_key: str
    sqlalchemy_database_url: str

    model_config = SettingsConfigDict(env_file=".env")


@lru_cache()
def get_settings():
    """settingのキャッシュ化"""
    return Settings()
