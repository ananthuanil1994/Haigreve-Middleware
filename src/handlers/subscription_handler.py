import uuid
from datetime import datetime
import requests
from flask import jsonify
from src import db
from src.models.transaction_details import Transactions
from src.constants import SUB_CLIENT_ID, SUB_PRODUCT_ID, SUB_SERVICE_ID, SUB_TYPE, SUB_SERVICE_NAME, \
    SUB_CHANNEL_NAME, SUB_PAGE_URL, CLIENT_ID, TRANSACTION_ID, SUB_MOBILE_NUMBER, PRODUCT_ID, SERVICE_ID, \
    CHANNEL_NAME, SERVICE_NAME, TYPE, CHECK_SUB_URL, UTF8, PROGRAM_CLOSED_ERROR, GENERAL_ERROR, TIMEOUT_ERROR, \
    CONNECTION_ERROR
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
