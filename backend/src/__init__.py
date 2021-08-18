from flask import Flask
from src.database import db, migrate
from . import config
from src.model.models import Client
from src.model.models import Coin

def create_app(env):
    app = Flask(__name__)
    app.config.from_object(config)
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.app_context().push()
    migrate.init_app(app, db)
    return app