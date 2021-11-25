from src import db
from src.constants import *


class Subscriptions(db.Model):
    __tablename__ = SUB_TABLE_NAME
    id = db.Column(db.Integer, primary_key=STATUS_TRUE)
    planName = db.Column(db.String(100), nullable=STATUS_FALSE)
    amount = db.Column(db.Integer, nullable=STATUS_FALSE)


db.create_all()
