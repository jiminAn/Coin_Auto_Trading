from flask import Flask
from src.database import db, migrate
from . import config

from src.model.models import client_information
from src.model.models import coin_information

def create_app(env):
    app = Flask(__name__)
    app.config.from_object(config)
    db.init_app(app)
    migrate.init_app(app, db)
    return app