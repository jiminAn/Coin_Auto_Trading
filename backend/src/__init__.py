from flask import Flask
from . import config
from .database import db, migrate


def create_app(env):
    app = Flask(__name__)
    app.config.from_object(config)
    db.app = app
    db.init_app(app)
    migrate.init_app(app, db)
    app.app_context().push()


    from .views import coin_views, main_views
    app.register_blueprint(main_views.bp)
    app.register_blueprint(coin_views.bp)
    return app
