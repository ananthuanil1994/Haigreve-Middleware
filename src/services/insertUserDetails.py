from src.models.user_details import Users
from src import db


def add_user(data):
    user_details = Users(id=data['hash_value'], name=data['name'], mobile_number=data['phone_number'], email=data['email'],
                         is_subscribed=data['is_subscribed'], subscription_plan=data['subscription_plan'],
                         is_payment_completed=data['is_payment_completed'], subscription_date=data['subscription_date'],
                         expiration_date=data['expiration_date'])
    db.session.add(user_details)
    db.session.commit()
    return True
