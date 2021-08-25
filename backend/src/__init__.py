from flask import Flask
from src.database import db, migrate
from . import config

def create_app(env):
    app = Flask(__name__)
    app.config.from_object(config)
    db.init_app(app)
    migrate.init_app(app, db)

    from .views import coin_views, main_views
    app.register_blueprint(main_views.bp)
    app.register_blueprint(coin_views.bp)
    return app