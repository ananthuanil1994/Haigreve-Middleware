from src.models.user_details import Users
from src import db
from src.constants import *
from datetime import datetime
from dateutil.relativedelta import relativedelta
from flask import jsonify


def update_details(userdetails):
    try:
        userdetails.isSubscribed = True
        userdetails.isPaymentCompleted = True
        userdetails.subscriptionDate = datetime.utcnow()
        if userdetails.subscriptionPlan == 1:
            userdetails.expirationDate = datetime.utcnow() + relativedelta(months=+1)
        elif userdetails.subscriptionPlan == 2:
            userdetails.expirationDate = datetime.utcnow() + relativedelta(months=+3)
        elif userdetails.subscriptionPlan == 3:
            userdetails.expirationDate = datetime.utcnow() + relativedelta(months=+6)
        elif userdetails.subscriptionPlan == 4:
            userdetails.expirationDate = datetime.utcnow() + relativedelta(years=+1)
        else:
            userdetails.expirationDate = datetime.utcnow()
        db.session.commit()
        status = True
    except Exception as e:
        status = False
    finally:
        return status
