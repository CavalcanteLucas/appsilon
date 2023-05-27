from flask import Flask

from appsilon.config import Config
from appsilon.ext import configuration


def create_app(config_class=Config):
    app = Flask(__name__)

    configuration.init_app(app, config_class)
    configuration.load_extensions(app)

    return app

app = create_app()
