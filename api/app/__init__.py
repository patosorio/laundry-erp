from flask import Flask
from app.routes.routes import main
from config.config import Config

def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    # Register blueprints (routes)
    app.register_blueprint(main)

    return app