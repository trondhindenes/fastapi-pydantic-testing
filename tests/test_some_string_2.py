import pytest
from app.main import get_some_string
from app.main import get_what


@pytest.fixture()
def patch_env_vars_2(monkeypatch):
    monkeypatch.setenv("some_string".upper(), "2.0")


@pytest.mark.asyncio
async def test_get_some_string_2():
    w = await get_some_string()
    assert w == "1.0"


def mocked_do_the_stuff():
    return False


# Notice how we can manipulate settings in the middle of a test file,
# even tho all methods (including get_settings) are loaded at this point

@pytest.mark.asyncio
async def test_get_some_string_3(patch_env_vars_2, mocker):
    mocker.patch("app.main.do_the_stuff", mocked_do_the_stuff)
    w = await get_what()
    assert w["what"] is None


@pytest.mark.asyncio
async def test_get_some_string_4(patch_env_vars_2):
    w = await get_what()
    assert w["what"] == "2.0"
