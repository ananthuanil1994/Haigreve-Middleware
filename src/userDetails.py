from sqlalchemy.sql import expression
import sys


# class Users(db.Model):
#     __tablename__ = 'user_details'
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(50), nullable=False)
#     mobileNo = db.Column(db.String(20), unique=True, nullable=False)
#     email = db.Column(db.String(20), nullable=False)
#     isSubscribed = db.Column(db.Boolean, server_default=expression.false(), nullable=False)
#     subscriptionPlan = db.Column(db.String(100), nullable=True)
#     isPaymentCompleted = db.Column(db.Boolean, server_default=expression.false(), nullable=False)
#     subscriptionDate = db.Column(db.DateTime(), nullable=False)