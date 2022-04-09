import pytest
from app.main import get_some_string


@pytest.fixture()
def patch_env_vars(monkeypatch):
    pass


@pytest.mark.asyncio
async def test_get_some_string_1(patch_env_vars):
    w = await get_some_string()
    assert w == "1.0"

