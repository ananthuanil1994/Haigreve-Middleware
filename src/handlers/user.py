from flask import jsonify, request
from src.constants import *
from datetime import datetime
from src.services.insertUserDetails import add_user
from dateutil.relativedelta import relativedelta
import hashlib


def save_customer_details(first_name, last_name, phone_number, email, payment_status, subscription_plan, group_id,
                          activation_id, short_token):
    try:
        hash_value = hashlib.md5(phone_number.encode(UTF8)).hexdigest()
        subscription_date = datetime.utcnow()
        expiration_date = NONE
        is_subscribed = STATUS_FALSE
        is_payment_completed = STATUS_FALSE
        if payment_status == PAYMENT_SUCCESS:
            expiration_date = subscription_date + relativedelta(months=int(subscription_plan))
            is_subscribed = STATUS_TRUE
            is_payment_completed = STATUS_TRUE

        data = {
            'hash_value': hash_value,
            'first_name': first_name,
            'last_name': last_name,
            'phone_number': phone_number,
            'email': email,
            'subscription_plan': subscription_plan,
            'subscription_date': subscription_date,
            'expiration_date': expiration_date,
            'is_subscribed': is_subscribed,
            'is_payment_completed': is_payment_completed,
            'group_id': group_id,
            'activation_id': activation_id,
            'short_token': short_token
        }

        db_response = add_user(data)
        return db_response
    except Exception as e:
        print(e.__str__())
