from flask import jsonify, request
from src.constants import *
from datetime import datetime
from src.models.user_details import Users
from src.services.insertUserDetails import add_user
import hashlib


def save_customer_details():
    try:
        first_name = request.json[USER_FIRST_NAME]
        last_name = request.json[USER_LAST_NAME]
        phone_number = request.json[USER_PHONENO]
        provider = request.json[NETWORK_PROVIDER]
        subscription_plan = request.json[USER_SUBPLAN]
        hash_value = hashlib.md5(phone_number.encode(UTF8)).hexdigest()
        user_details = Users.query.get(hash_value)

        if not user_details:
            subscription_date = datetime.utcnow()
            expiration_date = datetime.utcnow()
            is_subscribed = STATUS_FALSE
            is_payment_completed = STATUS_FALSE
            group_id = STATUS_FALSE
            activation_id = STATUS_FALSE
            short_token = STATUS_FALSE
            number = phone_number.strip('+')
            email = f'{number}@{provider}.com'
        else:
            return jsonify({MESSAGE: ALREADY_REGISTERED})

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
            'provider': provider
        }

        db_response = add_user(data)
        return jsonify({MESSAGE: USER_REGISTERED})
    except Exception as e:
        print(e.__str__())
