from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from urllib.parse import quote
import os
import logging

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    # loads environment variables
    load_dotenv()

    db_password = quote(os.getenv("DB_PASSWORD")) # used for db passwords with special characters
    
    # configures the app
    app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{os.getenv("DB_USER")}:{db_password}@{os.getenv("DB_HOST")}:{os.getenv("DB_PORT")}/{os.getenv("DB_NAME")}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # initializes the database
    db.init_app(app)
    
    # registers blueprints
    from app.routes import URLRoutes
    app.register_blueprint(URLRoutes().routes)

    # configures Flask logging
    handler = logging.StreamHandler()
    handler.setLevel(logging.INFO)
    app.logger.addHandler(handler)

    @app.before_request
    def log_request_info():
        app.logger.info('Headers: %s', request.headers)
        app.logger.info('Body: %s', request.get_data())
    
    return app