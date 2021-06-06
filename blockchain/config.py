from flask import Flask


class Config:
    APP_NAME = "blockchain-poc"
    APP_HOST = "localhost"
    ENVIRONMENT = "localhost"
    TESTING = False
    FLASK_ENV = "development"


config = Config()


def init_app(app: Flask) -> None:
    app.config.from_object(config)