import uuid
from datetime import datetime
import requests
from flask import jsonify, request
from src import db
from src.models.transaction_details import Transactions
from src.constants import USER_PHONENO, SUB_CLIENT_ID, SUB_PRODUCT_ID, SUB_SERVICE_ID, SUB_TYPE, SUB_SERVICE_NAME, \
    SUB_CHANNEL_NAME, SUB_PAGE_URL, CLIENT_ID, TRANSACTION_ID, SUB_MOBILE_NUMBER, PRODUCT_ID, SERVICE_ID, CHANNEL_NAME, \
    SERVICE_NAME, TYPE, CHECK_SUB_URL, USER_EMAIL, USER_FIRST_NAME, USER_LAST_NAME


def get_confirm_subscription_url():
    try:
        first_name = request.json[USER_FIRST_NAME]
        last_name = request.json[USER_LAST_NAME]
        email = request.json[USER_EMAIL]
        mobile_no = request.json[USER_PHONENO]
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


def check_subscription_status():
    try:
        mobile_no = request.json[USER_PHONENO]
        url = f'{CHECK_SUB_URL}?{CLIENT_ID}={SUB_CLIENT_ID}&{SERVICE_ID}={SUB_SERVICE_ID}&{SUB_MOBILE_NUMBER}=' \
              f'{mobile_no}&{CHANNEL_NAME}={SUB_CHANNEL_NAME}'
        result = (str(requests.get(url).content).split('b', 1)[1]).replace("'", '')
        return jsonify({"subscription_status": result})
    except Exception as e:
        print(e.__str__())
