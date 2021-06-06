from flask import Flask

from blockchain.api.status import bp as status_bp


def init_app(app: Flask) -> None:
    app.register_blueprint(status_bp)
