from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import app, db

from app.routes import routes
app.register_blueprint(routes)
