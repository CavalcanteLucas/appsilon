import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    DB_PASS = os.environ.get("DB_PASS")
    DB_USER = os.environ.get("DB_USER")
    DB_HOST = os.environ.get("DB_HOST")
    DB_PORT = os.environ.get("DB_PORT")
    DB_NAME = os.environ.get("DB_NAME")
    SQLALCHEMY_DATABASE_URI = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    TITLE = "Appsilon"
    EXTENSIONS = [
        "appsilon.ext.database:init_app",
        "appsilon.ext.commands:init_app",
        "appsilon.blueprints.views:init_app",
    ]
    TEMPLATES_AUTO_RELOAD = True
