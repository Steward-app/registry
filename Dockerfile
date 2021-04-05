FROM python:3.8-slim

RUN mkdir /app
WORKDIR /app
ADD . /app

RUN pip install poetry
RUN poetry config virtualenvs.create false && poetry install --no-dev --no-interaction --no-ansi

ENTRYPOINT poetry run python -m registry.${SERVICE}_server
