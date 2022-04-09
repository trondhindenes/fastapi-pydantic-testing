# Fastapi-pydantic-testing

### See corresponding blog post at https://hindenes.com/testing-fastapi-basesettings

## Setup
You need pipenv installed. I use pyenv to manage my python versions, so I normally set up and app like this using:
```shell
PYENV_VERSION=3.10.2 python3 -m venv .venv
PIPENV_VENV_IN_PROJECT=1 pipenv install -d
```
this way I have full control of which python version to use.

## Run tests
```shell
pipenv run pytest
```

## Run the app
There's not much there, but if you want do:
```shell
PYTHONPATH=. pipenv run python app/runserver.py
```