import jwt
import time
from config import ZIMPERIUM_LOGIN_PAYLOAD
import requests
from flask import request, jsonify
from src import ZIMPERIUM_HOST, ACTIVATION_LINK_API, SMS_LINK, SMS_MESSAGE, USER_FIRST_NAME, USER_LAST_NAME, \
    USER_EMAIL, USER_PHONENO, UTF8, db, ZIMPERIUM_REFRESH_TOKEN, ZIMPERIUM_ACCESS_TOKEN, LOGIN_HEADER, TOKEN_EXPIRY, \
    VALUE_ZERO, VERIFY_SIGNATURE, ACCESS_TOKEN, NONE, STATUS_FALSE, DECODED_INITIAL, ZIMPERIUM_LOGIN_API, BEARER, \
    ZIMPERIUM_GROUP_API, CONTENT_TYPE, AUTHORIZATION, APPLICATION, RESP_STATUS, SUB_ID, RESP_NAME, RESP_ID
from src.models.token_details import Tokens
import json


def get_user_details():
    first_name = request.json[USER_FIRST_NAME]
    last_name = request.json[USER_LAST_NAME]
    email = request.json[USER_EMAIL]
    mobile_no = request.json[USER_PHONENO]
    return first_name, last_name, email, mobile_no


def activation_sms_message_format(name, code):
    link = get_activation_link(code)
    text_message = f"""
    Hello {name},
    Thanks for Subscribing Lookout MES.
    Please download  & activate the application from the link below:
    {link}

    Thanks,
    Team Haigreve
    """
    return text_message


def get_activation_link(code):
    url = f'{ZIMPERIUM_HOST}{ACTIVATION_LINK_API}{code}'
    return url


def renewal_sms_message_format(name, date, url):
    text_message = f"""
    Hello {name},
    Your Lookout MES subscription is expiring on {date}.
    To resubscribe please visit {url} .

    Thanks,
    Team Haigreve
    """
    return text_message


def send_sms_message(mobile_no, text_message):
    data = f'{SMS_LINK}{mobile_no}&{SMS_MESSAGE}={text_message}'
    result = requests.get(data).content.decode(UTF8)
    return result


def send_bulk_sms_message(userdata):
    for user in userdata:
        mobile_no = user.mobile_number
        text_message = renewal_sms_message_format(user.first_name, user.expiration_date, "")
        send_sms_message(mobile_no, text_message)
    return True


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


def get_group_id(group_name):
    group_id = NONE
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
    group_name = group_name.title()
    for group in response:
        if group[RESP_NAME] == group_name:
            group_id = group[RESP_ID]
    return group_id, access_token
