from flask_sqlalchemy import SQLAlchemy
from app import app

# SQLAlchemy configurations
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:admin123@localhost/trialMydb'

# Instantiating SQLAlchemy object
db = SQLAlchemy(app)

