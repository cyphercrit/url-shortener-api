from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from urllib.parse import quote
import os
import logging # for azure logstream

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    # loads environment variables
    load_dotenv()

    db_password = quote(os.getenv("DB_PASSWORD")) # used for db passwords with special characters
    
    # configures the app
    app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{os.getenv("DB_USER")}:{db_password}@{os.getenv("DB_HOST")}:{os.getenv("DB_PORT")}/{os.getenv("DB_NAME")}?connect_timeout=10'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # initializes the database
    db.init_app(app)
    
    # registers blueprints
    from app.routes import URLRoutes
    app.register_blueprint(URLRoutes().routes)

    # configures logging for azure logstream
    if not app.debug:
        logging.basicConfig(level=logging.INFO)
        logger = logging.getLogger()
        handler = logging.StreamHandler()
        handler.setLevel(logging.INFO)
        logger.addHandler(handler)
    
    return app