from sqlalchemy.sql import expression
from src import db
from src.constants import *
from sqlalchemy.dialects.mysql import BIGINT


class Users(db.Model):
    __tablename__ = TABLE_NAME
    id = db.Column(BIGINT(unsigned=STATUS_TRUE), primary_key=STATUS_TRUE)
    name = db.Column(db.String(50), nullable=STATUS_FALSE)
    mobileNo = db.Column(db.String(20), unique=STATUS_TRUE, nullable=STATUS_FALSE)
    email = db.Column(db.String(20), nullable=STATUS_FALSE)
    isSubscribed = db.Column(db.Boolean, server_default=expression.false(), nullable=STATUS_FALSE)
    subscriptionPlan = db.Column(db.String(100), nullable=STATUS_TRUE)
    isPaymentCompleted = db.Column(db.Boolean, server_default=expression.false(), nullable=STATUS_FALSE)
    subscriptionDate = db.Column(db.DateTime(), nullable=STATUS_FALSE)


db.create_all()
