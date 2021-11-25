import requests
from src.services.smsMessageFormat import renewal_sms_message_format


def send_SMS_message(mobile_no, text_message):
    data = f'http://202.74.240.169/sending_sms_win/Default.aspx?login_name=haigreve&mobileno={mobile_no}&msg={text_message}'
    result = requests.get(data).content
    return result


def send_bulk_SMS_message(userdata):
    for user in userdata:
        mobile_no = user.mobileNo
        text_message = renewal_sms_message_format(user.name, "")
        data = f'http://202.74.240.169/sending_sms_win/Default.aspx?login_name=haigreve&mobileno={mobile_no}&msg={text_message}'
        result = requests.get(data).content
    return True
