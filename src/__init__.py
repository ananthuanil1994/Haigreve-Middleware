from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from src.constants import *
from decouple import config

# Instantiating a flask app
app = Flask(__name__)

# SQLAlchemy configurations
app.config[SQLALCHEMY_TRACK_MODIFICATIONS] = STATUS_FALSE
app.config[SQLALCHEMY_DATABASE_URI] = f'{DIALECTDRIVER}://{config("DB_USERNAME")}:{config("DB_PASSWORD")}@{config("DB_HOST")}/{config("DB_NAME")}'

db = SQLAlchemy(app)

