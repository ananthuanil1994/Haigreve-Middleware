import uuid
import requests
from flask import jsonify, request
from src.constants import USER_PHONENO, SUB_CLIENT_ID, SUB_PRODUCT_ID, SUB_SERVICE_ID, SUB_TYPE, SUB_SERVICE_NAME, \
    SUB_CHANNEL_NAME


def confirm_subscription():
    try:
        mobile_no = request.json[USER_PHONENO]
        unique_id = uuid.uuid1()
        url = f'http://202.74.240.171:8086/teletalk_sdp_sub_activete.aspx?client_id={SUB_CLIENT_ID}&\
        transaction_id={unique_id}&mobileno={mobile_no}&product_id={SUB_PRODUCT_ID}&\
        service_id={SUB_SERVICE_ID}&type={SUB_TYPE}&service_name={SUB_SERVICE_NAME}'
        result = requests.get(url).content
        if result:
            return jsonify({'status': True})
    except Exception as e:
        print(e.__str__())


def check_subscription_status():
    try:
        mobile_no = request.json[USER_PHONENO]
        url = f'http://202.74.240.169:8064/sub_status.aspx?client_id={SUB_CLIENT_ID}&service_id={SUB_SERVICE_ID}&\
        mobileno={mobile_no}&channel_name={SUB_CHANNEL_NAME}'
        result = requests.get(url).content
        return jsonify({'status': result})
    except Exception as e:
        print(e.__str__())
