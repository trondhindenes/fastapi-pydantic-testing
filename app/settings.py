from functools import lru_cache

from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    some_string: str = Field("1.0")


@lru_cache()
def get_settings() -> Settings:
    return Settings()
