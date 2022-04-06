import hashlib

from flask import request, jsonify

from src import USER_PHONENO, REDIRECTION_URL, UTF8, RESP_STATUS, ERROR_RESPONSE
from src.models.user_details import Users
from src.utilities.utils import redirection_sms_message_format, send_sms_message


def get_redirection_url():
    phone_no = request.json[USER_PHONENO]
    hash_value = hashlib.md5(phone_no.encode(UTF8)).hexdigest()
    user_details = Users.query.get(hash_value)
    if user_details:
        name = user_details.first_name + ' ' + user_details.last_name
        url = f'{REDIRECTION_URL}{phone_no}'
        message = redirection_sms_message_format(name, url)
        result = send_sms_message(phone_no, message)
    else:
        result = ERROR_RESPONSE
    return jsonify({RESP_STATUS: result})
