import pytest
import os
from flask import Flask
from config import Config
from flask_cors import CORS  # comment this on deployment
import mongoengine
from flask_mongoengine import MongoEngine
from flask_jwt_extended import JWTManager


class TestConfig:
    TESTING = True
    SECRET_KEY = os.environ.get('SECRET_KEY') or '5tay0ut!'
    MONGODB_SETTINGS = {
        "db": "simplicity-cloud",
        "host": "localhost",
        "port": 27017
    }


@pytest.fixture
def app():
    # db = MongoEngine()
    # app = Flask(__name__)
    # app.config.from_object(TestConfig)
    # # app.config['MONGODB_SETTINGS']= {
    # #     "db": "simplicity-cloud-test",
    # #     "host": "localhost",
    # #     "port": 27017
    # # }
    # # with app.app_context():
    from api import app
    from api import User, Project, Hardware
    from api import routes

    app.config["TESTING"] = True
    app.config['MONGODB_SETTINGS'] = {
        "db": "simplicity-cloud-test",
        "host": "localhost",
        "port": 27017
    }
    return app


@pytest.fixture
def client(app):
    return app.test_client()



# @pytest.fixture
# def db(app):
#     db = MongoEngine()
#     db.init(app)
#     from api import init_hardware, init_godmin
#     return db


# @pytest.fixture(autouse=True)
# def clean_db(db):
#     db.drop_collection("Users")
#     # db.drop_collection()
#     # Project.drop_collection()
