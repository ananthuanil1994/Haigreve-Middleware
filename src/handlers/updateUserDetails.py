from flask import jsonify, request
from datetime import datetime
from src.services.updateUserSubscriptionDetails import update_details
from src.constants import *
from src.models.user_details import Users
from src import db

import hashlib

from src.utilities.utils import activation_sms_message_format


def update_customer_details():
    phone_no = request.json[USER_PHONENO]
    hash_value = hashlib.md5(phone_no.encode('utf-8')).hexdigest()
    userdetails = Users.query.get(hash_value)

    if userdetails:
        result = update_details(userdetails)
    else:
        return jsonify({
            "update_status": False,
            "message_status": False
        })

    if result:
        # Do FTP and get code
        activation_code = "abc123"
        message_text = activation_sms_message_format(userdetails.name, activation_code)
        # message_status = send_SMS_message(phone_no, message_text)
        # if message_status == "data is updated":
        return jsonify({
            "status": True,
            "message_status": True
        })
    else:
        return jsonify({
            "update_status": False,
            "message_status": False
        })