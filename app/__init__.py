from flask import Flask
from .extensions import api, db

def create_app():
    app = Flask(__name__)
    
    app.config["SQLALCHEMY_DATABASE_URI"]

    api.init_app(app)
    db.init_app(app)

    return app