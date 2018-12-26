from flask import Flask
from application.config import Config

# from flask_sqlalchemy import SQLAlchemy


def create_app(config_class=Config):
    app = Flask(__name__)

    # import config parameters to flask app
    app.config.from_object(Config)

    # initilize extensions

    # import blueprints and register
    from application.auth.routes import auth as auth_bleprint
    app.register_blueprint(auth_bleprint)
    from application.errors.handlers import errors as errors_bleprint
    app.register_blueprint(errors_bleprint)
    from application.main.routes import main as main_bleprint
    app.register_blueprint(main_bleprint)

    return app
