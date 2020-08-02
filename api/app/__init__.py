from flask import Flask
from flask_bcrypt import Bcrypt

from .db import db
from config.config import config_by_name

flask_bcrypt = Bcrypt()


def create_app(config_name):
    app = Flask(__name__)

    app.config.from_object(config_by_name[config_name])
    
    db.init_app(app)
    flask_bcrypt.init_app(app)

    @app.before_first_request
    def create_tables():
        db.create_all()

    return app