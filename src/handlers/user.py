from flask import jsonify, request
from src.constants import *
from datetime import datetime
from src.services.insertUserDetails import add_user
from dateutil.relativedelta import relativedelta
import hashlib


def save_customer_details():
    try:
        first_name = request.json[USER_FIRST_NAME]
        last_name = request.json[USER_LAST_NAME]
        email = request.json[USER_EMAIL]
        phone_number = request.json[USER_PHONENO]
        subscription_plan = request.json[USER_SUBPLAN]
        payment_status = request.json[PAYMENT_STATUS]
        hash_value = hashlib.md5(phone_number.encode(UTF8)).hexdigest()
        subscription_date = datetime.utcnow()
        expiration_date = datetime.utcnow()
        is_subscribed = STATUS_FALSE
        is_payment_completed = STATUS_FALSE
        group_id = STATUS_FALSE
        activation_id = STATUS_FALSE
        short_token = STATUS_FALSE
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
            'is_subscribed': is_subscribed,
            'subscription_plan': subscription_plan,
            'is_payment_completed': is_payment_completed,
            'subscription_date': subscription_date,
            'expiration_date': expiration_date,
            'group_id': group_id,
            'activation_id': activation_id,
            'short_token': short_token,
            'type': DEFAULT_USER_TYPE,
        }

        db_response = add_user(data)
        context = {'id': hash_value, 'name': first_name, 'phone_number': phone_number, 'email': email,
                   'subscription_plan': subscription_plan, 'payment_status': payment_status}

        return jsonify(context)
    except Exception as e:
        print(e.__str__())
