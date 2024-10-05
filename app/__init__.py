from flask_jwt_extended import JWTManager
from flask import Flask

from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
bcrypt = Bcrypt()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    jwt = JWTManager(app)
    jwt.init_app(app)

    from app.api import api_bp
    app.register_blueprint(api_bp)

    return app