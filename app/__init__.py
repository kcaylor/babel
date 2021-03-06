from flask import Flask
from flask.ext.pymongo import PyMongo
from config import config
from app.models import db

def create_app(config_name):

    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app)


    from main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app

