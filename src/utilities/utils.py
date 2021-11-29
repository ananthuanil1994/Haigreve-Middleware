import requests

def activation_sms_message_format(name, code):
    text_message = f"""
    Hello {name},
    Thanks for Subscribing Lookout MES.
    Please download  & activate the application from the link below:
    https://get.lookout.com/web-code?code={code}

    Thanks,
    Team Haigreve
    """
    return text_message


def renewal_sms_message_format(name, url):
    text_message = f"""
    Hello {name},
    Your Lookout MES subscription is expiring on DD/MM/YY.
    To resubscribe please visit {url} .

    Thanks,
    Team Haigreve
    """
    return text_message


def send_sms_message(mobile_no, text_message):
    data = f'http://202.74.240.169/sending_sms_win/Default.aspx?login_name=haigreve&mobileno={mobile_no}&msg={text_message}'
    result = requests.get(data).content
    return result


def send_bulk_sms_message(userdata):
    for user in userdata:
        mobile_no = user.mobileNo
        text_message = renewal_sms_message_format(user.name, "")
        data = f'http://202.74.240.169/sending_sms_win/Default.aspx?login_name=haigreve&mobileno={mobile_no}&msg={text_message}'
        result = requests.get(data).content
    return True
