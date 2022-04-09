from app.settings import get_settings


async def get_some_string():
    settings = get_settings()
    return settings.some_string
