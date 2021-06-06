FROM python:3.7.2-slim

RUN pip install poetry==1.1.4

ENV APP_FOLDER=$HOME/blockchain
RUN mkdir $APP_FOLDER
WORKDIR $APP_FOLDER

COPY ./poetry.lock ./pyproject.toml $APP_FOLDER/
RUN poetry install --no-dev

COPY . $APP_FOLDER/

ENV PYTHONPATH=../
ENV FLASK_APP=$APP_FOLDER/app.py
CMD poetry run flask run --host=0.0.0.0