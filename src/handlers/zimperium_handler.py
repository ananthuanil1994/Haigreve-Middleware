import json
import requests
from flask import jsonify
import jwt
import time
from config import ZIMPERIUM_LOGIN_PAYLOAD
from src import ZIMPERIUM_HOST, ZIMPERIUM_LOGIN_API, db, ZIMPERIUM_GROUP_API, BEARER, \
    LOGIN_HEADER, AUTHORIZATION, CONTENT_TYPE, APPLICATION, STATUS_FALSE, ZIMPERIUM_ACTIVATION_API, \
    ZIMPERIUM_ACTIVATION_LIMIT, PLAN_VALUE, DECODED_INITIAL, ACCESS_TOKEN, NONE, VERIFY_SIGNATURE, \
    TOKEN_EXPIRY, UTF8, ZIMPERIUM_ACCESS_TOKEN, ZIMPERIUM_REFRESH_TOKEN, RESP_STATUS, SUB_ID, MESSAGE, GRP_ID, \
    SHORT_TOKEN, VALUE_ZERO, PAYMENT_SUCCESS, MESSAGE_STATUS, PAYMENT_FAILED
from src.handlers.user import save_customer_details
from src.models.token_details import Tokens
from src.utilities.utils import activation_sms_message_format, send_sms_message, get_user_details


def zimperium_login():

    url = f'{ZIMPERIUM_HOST}{ZIMPERIUM_LOGIN_API}'
    obj = Tokens.query.order_by(-Tokens.id).first()
    decoded = DECODED_INITIAL
    token = getattr(obj, ACCESS_TOKEN, NONE)
    if token is not NONE:
        decoded = jwt.decode(token, options={VERIFY_SIGNATURE: STATUS_FALSE})
    else:
        decoded[TOKEN_EXPIRY] = VALUE_ZERO
    if decoded[TOKEN_EXPIRY] < time.time():
        response = requests.post(url, json=ZIMPERIUM_LOGIN_PAYLOAD, headers=LOGIN_HEADER)
        response = json.loads(response.content.decode(UTF8))

        if response:
            access_token = response[ZIMPERIUM_ACCESS_TOKEN]
            refresh_token = response[ZIMPERIUM_REFRESH_TOKEN]
            transaction = Tokens(access_token=access_token, refresh_token=refresh_token)
            db.session.add(transaction)
            db.session.commit()
        else:
            return False
        return access_token
    return token


def get_default_group_id():
    access_token = BEARER + ' ' + zimperium_login()
    url = f'{ZIMPERIUM_HOST}{ZIMPERIUM_GROUP_API}'
    headers = {
        CONTENT_TYPE: APPLICATION,
        AUTHORIZATION: access_token
    }
    response = requests.get(url, headers=headers)
    response = json.loads(response.content.decode(UTF8))
    if not response:
        return jsonify({RESP_STATUS: STATUS_FALSE})
    group_id = response[0][SUB_ID]
    return group_id, access_token


def activate_zimperium_user():
    group_id, access_token = get_default_group_id()
    first_name, last_name, email, mobile_no = get_user_details()
    payload = {
        "email": email,
        "firstName": first_name,
        "lastName": last_name,
        "phoneNumber": mobile_no,
        "sendEmailInvite": STATUS_FALSE,
        "activationLimit": ZIMPERIUM_ACTIVATION_LIMIT,
        "groupId": group_id
    }
    payload = json.dumps(payload)
    url = f'{ZIMPERIUM_HOST}{ZIMPERIUM_ACTIVATION_API}'
    headers = {
        CONTENT_TYPE: APPLICATION,
        AUTHORIZATION: access_token
    }

    response = requests.post(url, data=payload, headers=headers)
    response = json.loads(response.content.decode(UTF8))

    if response.get(MESSAGE, NONE):
        return response[MESSAGE]
    subscription_plan = PLAN_VALUE
    group_id = response[GRP_ID]
    activation_id = response[SUB_ID]
    short_token = response[SHORT_TOKEN]
    payment_status = PAYMENT_SUCCESS

    db_response = save_customer_details(first_name, last_name, mobile_no, email, payment_status, subscription_plan,
                                        group_id, activation_id, short_token)
    if db_response:
        if short_token:
            message = activation_sms_message_format(first_name, short_token)
            msg_status = send_sms_message(mobile_no, message)
    return jsonify({MESSAGE_STATUS: PAYMENT_SUCCESS})


