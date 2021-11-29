from flask import jsonify, request
from src.constants import *
from datetime import datetime
from src.services.insertUserDetails import add_user
from dateutil.relativedelta import relativedelta

import hashlib

from src.utilities.utils import activation_sms_message_format, send_sms_message


def save_customer_details():
    try:
        name = request.json[USER_NAME]
        phone_number = request.json[USER_PHONENO]
        email = request.json[USER_EMAIL]
        duration = request.json[DURATION]
        payment_status = request.json[PAYMENT_STATUS]
        subscription_plan = request.json[USER_SUBPLAN]
        hash_value = hashlib.md5(phone_number.encode('utf-8')).hexdigest()
        subscription_date = datetime.utcnow()
        expiration_date = None
        is_subscribed = False
        is_payment_completed = False
        if payment_status == PAYMENT_SUCCESS:
            expiration_date = subscription_date + relativedelta(months=int(duration))
            is_subscribed = True
            is_payment_completed = True
        data = {
            'hash_value': hash_value,
            'name': name,
            'phone_number': phone_number,
            'email': email,
            'subscription_plan': subscription_plan,
            'subscription_date': subscription_date,
            'expiration_date': expiration_date,
            'is_subscribed': is_subscribed,
            'is_payment_completed': is_payment_completed
        }


        db_response = add_user(data)
        context = {'id': hash_value, 'name': name, 'phone_number': phone_number, 'email': email,
                   'subscription_plan': subscription_plan, 'payment_status': payment_status}
        # if db_response and is_payment_completed:
        #     code = None  # need too write a function read and update csv file containing activation code.
        #     message = activation_sms_message_format(name, code)
        #     msg_status = send_sms_message(phone_number, message)
        #     pass

        return jsonify(context)
    except Exception as e:
        print(e.__str__())
