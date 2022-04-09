from fastapi import FastAPI

from app.settings import get_settings
from app.utils import get_some_string

settings = get_settings()

app = FastAPI(
    title="plonk",
    version="0.0.1"
)


def do_the_stuff():
    return True


@app.get("/what")
async def get_what():
    w = await get_some_string()
    if do_the_stuff():
        return {
            "what": w
        }
    else:
        return {"what": None}
