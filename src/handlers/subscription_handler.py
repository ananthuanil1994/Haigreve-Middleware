import hashlib
import uuid
from datetime import datetime
import requests
from flask import jsonify, request, make_response
from src import db
from src.models.transaction_details import Transactions
from src.constants import SUB_CLIENT_ID, SUB_PRODUCT_ID, SUB_SERVICE_ID, SUB_TYPE, SUB_SERVICE_NAME, \
    SUB_CHANNEL_NAME, SUB_PAGE_URL, CLIENT_ID, TRANSACTION_ID, SUB_MOBILE_NUMBER, PRODUCT_ID, SERVICE_ID, \
    CHANNEL_NAME, SERVICE_NAME, TYPE, CHECK_SUB_URL, UTF8, PROGRAM_CLOSED_ERROR, GENERAL_ERROR, TIMEOUT_ERROR, \
    CONNECTION_ERROR, STATUS_TRUE, STATUS_FALSE, MESSAGE, MSISDN, SHORT_CODE, TEXT, STATUS_UPDATED, MNO_CODE,\
    ZIMPERIUM_DEACTIVATION_RESPONSE_CODE_NOT_FOUND, RESP_STATUS, TRANSACTION_SERVICE_ID, TIME, TRANSACTIONID, SUB,\
    DEFAULT_USER_TYPE, TRANSACTION_ERROR, COM, PLUS, RENEW
from src.models.user_details import Users
from src.services.insertUserDetails import add_user
from src.utilities.utils import get_user_details


def get_confirm_subscription_url():
    try:
        first_name, last_name, email, mobile_no = get_user_details()
        transaction_id = uuid.uuid1()
        transaction_date = datetime.utcnow()
        transaction = Transactions(transaction_id=transaction_id, mobile_number=mobile_no,
                                   transaction_date=transaction_date)
        db.session.add(transaction)
        db.session.commit()
        url = f'{SUB_PAGE_URL}?{CLIENT_ID}={SUB_CLIENT_ID}&{TRANSACTION_ID}={transaction_id}&{SUB_MOBILE_NUMBER}' \
              f'={mobile_no}&{PRODUCT_ID}={SUB_PRODUCT_ID}&{SERVICE_ID}={SUB_SERVICE_ID}&{TYPE}={SUB_TYPE}&' \
              f'{SERVICE_NAME}={SUB_SERVICE_NAME}'
        return jsonify({'confirmation_link': url})
    except Exception as e:
        print(e.__str__())


def check_subscription_status(mobile_no):
    try:
        url = f'{CHECK_SUB_URL}?{CLIENT_ID}={SUB_CLIENT_ID}&{SERVICE_ID}={SUB_SERVICE_ID}&{SUB_MOBILE_NUMBER}=' \
              f'{mobile_no}&{CHANNEL_NAME}={SUB_CHANNEL_NAME}'
        result = requests.get(url).content.decode(UTF8)
        return result
    except requests.ConnectionError as e:
        print(CONNECTION_ERROR)
        print(str(e))
        pass
    except requests.Timeout as e:
        print(TIMEOUT_ERROR)
        print(str(e))
        pass
    except requests.RequestException as e:
        print(GENERAL_ERROR)
        print(str(e))
        pass
    except KeyboardInterrupt:
        print(PROGRAM_CLOSED_ERROR)


def check_sms_subscription_status(mobile_number):
    hash_value = hashlib.md5(mobile_number.encode('utf-8')).hexdigest()
    user_details = Users.query.get(hash_value)

    if user_details:
        if user_details.is_subscribed is STATUS_TRUE:
            return user_details
        else:
            return STATUS_FALSE
    return STATUS_FALSE


def update_user_subscription_status():
    mobile_number = request.json[MSISDN]
    short_code = request.json[SHORT_CODE]
    text = request.json[TEXT]
    mnocode = request.json[MNO_CODE]
    status = request.json[RESP_STATUS]
    time = request.json[TIME]
    subscription_status = request.json[TYPE]
    service_id = request.json[TRANSACTION_SERVICE_ID]
    transaction_id = request.json[TRANSACTIONID]
    transaction_details = Transactions.query.get(transaction_id)
    hash_value = hashlib.md5(mobile_number.encode(UTF8)).hexdigest()
    user_details = Users.query.get(hash_value)
    number = mobile_number.strip(PLUS)
    email = f'{number}@{number}{COM}'
    if subscription_status == SUB or RENEW:
        is_subscribed = STATUS_TRUE
        payment_completed = STATUS_TRUE
    else:
        is_subscribed = STATUS_FALSE
        payment_completed = STATUS_FALSE

    if not transaction_details:
        transaction = Transactions(transaction_id=transaction_id, mobile_number=mobile_number, short_code=short_code,
                                   text=text, mnocode=mnocode, status=status, time=time, type=subscription_status,
                                   service_id=service_id)
        db.session.add(transaction)
        db.session.commit()
        if not user_details:
            data = {
                'hash_value': hash_value,
                'first_name': mobile_number,
                'last_name': mobile_number,
                'phone_number': mobile_number,
                'email': email,
                'is_subscribed': is_subscribed,
                'subscription_plan': STATUS_FALSE,
                'is_payment_completed': payment_completed,
                'subscription_date': datetime.utcnow(),
                'expiration_date': datetime.utcnow(),
                'group_id': STATUS_FALSE,
                'activation_id': STATUS_FALSE,
                'short_token': STATUS_FALSE,
                'type': DEFAULT_USER_TYPE,
                'provider': mobile_number
            }
            status = add_user(data)
        elif user_details:
            user_details.is_subscribed = is_subscribed
            user_details.is_payment_completed = payment_completed
            db.session.commit()
        return jsonify({MESSAGE: STATUS_UPDATED})
    return make_response(jsonify({MESSAGE: TRANSACTION_ERROR}), ZIMPERIUM_DEACTIVATION_RESPONSE_CODE_NOT_FOUND)
