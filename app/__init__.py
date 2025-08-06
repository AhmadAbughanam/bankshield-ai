import os
from flask import Flask


def create_app():
    app = Flask(__name__)
    app.secret_key = "bankshield-secret"
    app.config["UPLOAD_FOLDER"] = os.path.join(os.getcwd(), "data")

    from .routes import main

    app.register_blueprint(main)

    return app
