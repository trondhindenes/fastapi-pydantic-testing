from functools import lru_cache
from typing import List
import os

from pydantic import BaseSettings, Field

USE_CACHED_SETTINGS = os.getenv("USE_CACHED_SETTINGS", "TRUE").lower == "true"


class Settings(BaseSettings):
    some_string: str = Field("1.0")


@lru_cache()
def get_cached_settings():
    """
    bypass pydantic's class instantiation by caching the method
    """
    return Settings()


def get_settings() -> Settings:
    """
    will returned cached settings by default.
    :return:
    """
    if USE_CACHED_SETTINGS:
        return get_cached_settings()
    else:
        return Settings()
