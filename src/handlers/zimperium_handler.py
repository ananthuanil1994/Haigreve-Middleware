import hashlib
import json
import requests
from flask import jsonify, request
import jwt
import time
from config import ZIMPERIUM_LOGIN_PAYLOAD
from src import ZIMPERIUM_HOST, ZIMPERIUM_LOGIN_API, db, ZIMPERIUM_GROUP_API, BEARER, \
    LOGIN_HEADER, AUTHORIZATION, CONTENT_TYPE, APPLICATION, STATUS_FALSE, ZIMPERIUM_ACTIVATION_API, \
    ZIMPERIUM_ACTIVATION_LIMIT, DECODED_INITIAL, ACCESS_TOKEN, NONE, VERIFY_SIGNATURE, \
    TOKEN_EXPIRY, UTF8, ZIMPERIUM_ACCESS_TOKEN, ZIMPERIUM_REFRESH_TOKEN, RESP_STATUS, SUB_ID, MESSAGE, GRP_ID, \
    SHORT_TOKEN, VALUE_ZERO, PAYMENT_SUCCESS, USER_PHONENO, ERROR_RESPONSE, USER_SUBSCRIBED, USER_NOT_SUBSCRIBED, URL
from src.handlers.subscription_handler import check_subscription_status
from src.models.token_details import Tokens
from src.models.user_details import Users
from src.services.updateUserSubscriptionDetails import update_details
from src.utilities.utils import get_activation_link


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
    mobile_no = request.json[USER_PHONENO]
    result = check_subscription_status(mobile_no)
    if result == USER_SUBSCRIBED:
        hash_value = hashlib.md5(mobile_no.encode(UTF8)).hexdigest()
        user_details = Users.query.get(hash_value)
        if user_details:
            first_name = user_details.first_name
            last_name = user_details.last_name
            email = user_details.email
        else:
            return jsonify({MESSAGE: USER_NOT_SUBSCRIBED})
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
            url = get_activation_link(user_details.short_token)
            return jsonify({URL: url})

        user_details.group_id = response[GRP_ID]
        user_details.activation_id = response[SUB_ID]
        user_details.short_token = response[SHORT_TOKEN]
        user_details.payment_status = PAYMENT_SUCCESS
        result = update_details(user_details)
        url = ERROR_RESPONSE
        if user_details.short_token and result:
            url = get_activation_link(user_details.short_token)
        return jsonify({URL: url})
    return jsonify({URL: NONE})
