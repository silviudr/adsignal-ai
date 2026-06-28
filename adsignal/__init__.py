from flask import Flask, render_template
from adsignal import config


def create_app():
    app = Flask(__name__, template_folder="templates", static_folder="static")
    app.config.from_object(config)

    @app.route("/")
    def index():
        return render_template("index.html")

    return app
