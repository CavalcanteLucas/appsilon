import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SQLALCHEMY_DATABASE_URI = "postgresql://appsilon_user:dale@localhost:5432/appsilon_db"
    TITLE = "Appsilon"
    EXTENSIONS = [
        "appsilon.ext.database:init_app",
        "appsilon.ext.commands:init_app",
        "appsilon.blueprints.views:init_app",
    ]
    DEBUG = True
    TESTING = False
