from flask import Flask
from config import config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


login_manager = LoginManager()
db = SQLAlchemy()
login_manager.login_view = "auth.login"


def create_app(config_name):
    app = Flask(__name__)

    # import config parameters to flask app
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    # initilize extensions
    db.init_app(app)
    login_manager.init_app(app)

    # import blueprints and register
    from application.auth.routes import auth
    app.register_blueprint(auth)
    from application.dashboard.routes import dashboard
    app.register_blueprint(dashboard)
    from application.errors.handlers import errors
    app.register_blueprint(errors)
    from application.main.routes import main
    app.register_blueprint(main)

    return app
