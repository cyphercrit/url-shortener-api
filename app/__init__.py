from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv, dotenv_values
from urllib.parse import quote

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    # loads environment variables
    load_dotenv()
    env = dotenv_values('.env')

    db_password = quote(env["DB_PASSWORD"]) # used for db passwords with special characters
    
    # configures the app
    app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{env["DB_USER"]}:{db_password}@{env["DB_HOST"]}:{env["DB_PORT"]}/{env["DB_NAME"]}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # initializes the database
    db.init_app(app)
    
    # registers blueprints
    from app.routes import URLRoutes
    app.register_blueprint(URLRoutes().routes)
    
    return app