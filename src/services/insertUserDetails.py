from src.models.user_details import Users
from src import db


def add_user(data):
    user_details = Users(id=data['hash_value'], first_name=data['first_name'], last_name=data['last_name'],
                         mobile_number=data['phone_number'], email=data['email'], is_subscribed=data['is_subscribed'],
                         subscription_plan=data['subscription_plan'], is_payment_completed=data['is_payment_completed'],
                         subscription_date=data['subscription_date'], expiration_date=data['expiration_date'],
                         group_id=data['group_id'], activation_id=data['activation_id'], short_token=data['short_token'],
                         type=data['type'], provider=data['provider']
                         )
    db.session.merge(user_details)
    db.session.commit()
    db.session.close()
    return True
