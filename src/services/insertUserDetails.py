from src.models.userDetails import Users
from src import db
from src.constants import *


def insert_details(hash_value, name, phone_no, email, subscription_plan, subscription_date):
    user_details = Users(id=hash_value, name=name, mobileNo=phone_no, email=email,
                         isSubscribed=STATUS_FALSE, subscriptionPlan=subscription_plan,
                         isPaymentCompleted=STATUS_FALSE, subscriptionDate=subscription_date)
    db.session.add(user_details)
    db.session.commit()
    return True
