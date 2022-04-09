import pytest



@pytest.fixture()
def patch_env_vars_2(monkeypatch):
    monkeypatch.setenv("some_string".upper(), "2.0")


@pytest.mark.asyncio
async def test_get_some_string_2():
    from app.main import get_some_string
    from app.main import get_what
    w = await get_some_string()
    assert w == "1.0"


def mocked_do_the_stuff():
    return False


"""
It's now very hard to "reset" settings since they're cached
even if we update the corresponding envvar by monkeypatching it it has no effect
This means that test results may vary depending on if you run them one by one or all together
Try:

pipenv run pytest tests/test_some_string_2.py::test_get_some_string_4
vs
pipenv run pytest
..and notice how they differ
"""


@pytest.mark.asyncio
async def test_get_some_string_3(patch_env_vars_2, mocker):
    from app.main import get_some_string
    from app.main import get_what
    mocker.patch("app.main.do_the_stuff", mocked_do_the_stuff)
    w = await get_what()
    assert w["what"] is None


@pytest.mark.asyncio
async def test_get_some_string_4(patch_env_vars_2):
    from app.main import get_some_string
    from app.main import get_what
    w = await get_what()
    assert w["what"] == "2.0"
