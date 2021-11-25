from flask import jsonify, request
from src.constants import *
from datetime import datetime
from src.services.insertUserDetails import insert_details

import hashlib


def save_customer_details():
    name = request.json[USER_NAME]
    phone_no = request.json[USER_PHONENO]
    email = request.json[USER_EMAIL]
    subscription_plan = request.json[USER_SUBPLAN]

    hash_value = hashlib.md5(phone_no.encode('utf-8')).hexdigest()
    subscription_date = datetime.utcnow()

    db_response = insert_details(hash_value, name, phone_no, email, subscription_plan, subscription_date)

    context = {RESP_ID: hash_value, RESP_NAME: name, RESP_PHONENO: phone_no, RESP_EMAIL: email,
               RESP_SUBPLAN: subscription_plan, RESP_STATUS: RESP_STATUSVALUE}

    return jsonify(context)
