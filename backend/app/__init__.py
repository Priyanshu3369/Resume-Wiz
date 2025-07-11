from flask import Flask
from flask_jwt_extended import JWTManager
from flask_pymongo import PyMongo
from flask_cors import CORS
from .config import Config

mongo = PyMongo()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    CORS(app)
    mongo.init_app(app)
    jwt.init_app(app)

    from .auth.routes import auth_bp
    app.register_blueprint(auth_bp, url_prefix='/api/auth')

    return app
