from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv, dotenv_values

class Config:
    def __init__(self):
        load_dotenv()
        self.env = dotenv_values('.env')
    
    def init_app(self):
        app = Flask(__name__)

        app.config['SQLALCHEMY_DATABASE_URI'] = f'''
            postgresql://
            {self.env["DB_USER"]}:
            {self.env["DB_PASSWORD"]}@
            {self.env["DB_HOST"]}:
            {self.env["DB_PORT"]}/
            {self.env["DB_NAME"]}''' # database information
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        return app

class Database:
    def __init__(self, app):
        self.db = SQLAlchemy(app)
    
    def get_db(self):
        return self.db