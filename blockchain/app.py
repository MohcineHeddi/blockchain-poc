from flask import Flask

from blockchain import config, api


def create_app() -> Flask:
    app = Flask(__name__)

    config.init_app(app)
    api.init_app(app)

    return app