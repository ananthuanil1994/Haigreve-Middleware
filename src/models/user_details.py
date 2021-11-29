from sqlalchemy.sql import expression
from src import db
from src.constants import *
from sqlalchemy.dialects.mysql import BIGINT


class Users(db.Model):
    __tablename__ = TABLE_NAME
    id = db.Column(db.String(50), primary_key=STATUS_TRUE)
    name = db.Column(db.String(50), nullable=STATUS_FALSE)
    mobile_number = db.Column(db.String(20), unique=STATUS_TRUE, nullable=STATUS_FALSE)
    email = db.Column(db.String(20), nullable=STATUS_FALSE)
    is_subscribed = db.Column(db.Boolean, server_default=expression.false(), nullable=STATUS_FALSE)
    subscription_plan = db.Column(db.Integer, nullable=STATUS_TRUE)
    is_payment_completed = db.Column(db.Boolean, server_default=expression.false(), nullable=STATUS_FALSE)
    subscription_date = db.Column(db.DateTime(), nullable=STATUS_FALSE)
    expiration_date = db.Column(db.DateTime(), nullable=STATUS_TRUE)
    # subscription_plan = db.Column(db.Integer, db.ForeignKey('subscriptions.id'))

db.create_all()
