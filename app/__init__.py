from flask import Flask
from flask_restx import Api
from .routes import ns


def create_app():
    app = Flask(__name__)
    api = Api(app, title="Sentiment Analysis API", description="Simple sentiment analysis API")

    api.add_namespace(ns)

    return app
