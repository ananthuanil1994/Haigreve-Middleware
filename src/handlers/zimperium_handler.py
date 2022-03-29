import hashlib
import json
from datetime import datetime
import requests
from dateutil.relativedelta import relativedelta
from flask import jsonify
import jwt, time
from src import ZIMPERIUM_HOST, ZIMPERIUM_LOGIN_API, ZIMPERIUM_LOGIN_PAYLOAD, db, ZIMPERIUM_GROUP_API, BEARER, \
    LOGIN_HEADER, AUTHORIZATION, CONTENT_TYPE, APPLICATION, STATUS_FALSE, ZIMPERIUM_ACTIVATION_API, \
    ZIMPERIUM_ACTIVATION_LIMIT, STATUS_TRUE, PLAN_VALUE
from src.models.token_details import Tokens
from src.services.insertUserDetails import add_user
from src.utilities.utils import get_zimperium_code, activation_sms_message_format, send_sms_message, get_user_details


def zimperium_login():

    url = f'{ZIMPERIUM_HOST}{ZIMPERIUM_LOGIN_API}'
    obj = Tokens.query.order_by(-Tokens.id).first()
    token = obj.access_token
    decoded = jwt.decode(token, options={"verify_signature": STATUS_FALSE})

    if decoded['exp'] < time.time():
        response = requests.post(url, json=ZIMPERIUM_LOGIN_PAYLOAD, headers=LOGIN_HEADER)
        response = json.loads(response.content.decode("utf-8"))

        if response:
            access_token = response['accessToken']
            refresh_token = response['refreshToken']
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
    response = json.loads(response.content.decode("utf-8"))
    if not response:
        return jsonify({"group_id_status": STATUS_FALSE})
    group_id = response[0]['id']
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
    response = json.loads(response.content.decode("utf-8"))
    if response.get('message', None):
        return response['message']
    subscription_plan = PLAN_VALUE
    hash_value = hashlib.md5(mobile_no.encode('utf-8')).hexdigest()
    subscription_date = datetime.utcnow()
    expiration_date = subscription_date + relativedelta(months=int(subscription_plan))
    is_subscribed = STATUS_TRUE
    is_payment_completed = STATUS_TRUE
    group_id = response['groupId']
    activation_id = response['id']
    short_token = response['shortToken']

    data = {
        'hash_value': hash_value,
        'first_name': first_name,
        'last_name': last_name,
        'phone_number': mobile_no,
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
    context = {'id': hash_value, 'first_name': first_name, 'last_name': last_name, 'phone_number': mobile_no,
               'email': email, 'subscription_plan': subscription_plan, 'payment_status': is_payment_completed}
    if db_response and is_payment_completed:
        code = get_zimperium_code(hash_value)
        if code:
            message = activation_sms_message_format(first_name, code)
            msg_status = send_sms_message(mobile_no, message)
    return jsonify(context)


