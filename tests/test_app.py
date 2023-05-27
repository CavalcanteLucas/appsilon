from appsilon.ext.database import db


def test_app_is_created(app):
    assert app.name == "appsilon.app"


def test_config_is_loaded(config):
    assert config["DEBUG"] is False
