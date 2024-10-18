from flask import Flask, request, jsonify, redirect
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv, dotenv_values

app = Flask(__name__)
load_dotenv()

env = dotenv_values()

if __name__ == "__main__":
    app.run(debug=True)