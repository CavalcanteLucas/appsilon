import pytest

from appsilon.app import create_app
from appsilon.ext.database import db
from appsilon.config import Config


class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///test.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


@pytest.fixture(scope="module")
def app():
    """Instance of main Flask app"""
    app = create_app(TestConfig)
    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()


@pytest.fixture(scope="module")
def client(app):
    """Instance of Flask test client"""
    return app.test_client()


@pytest.fixture(scope="module")
def config(app):
    """Instance of Flask config"""
    return app.config
