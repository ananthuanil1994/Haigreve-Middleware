import os
from threading import Lock

import pandas as pd
import pysftp
import requests
from decouple import config


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


def get_activation_code():
    try:
        mutex = Lock()
        cnopts = pysftp.CnOpts()
        remote_csv_path = 'Teletalk-Consumer/Inbox/Teletalk-Consumer-Teletalk-Consumer-Test-20211123-15776-1563zw3.csv'
        local_csv_path = 'Teletalk-Consumer-Teletalk-Consumer-Test-20211123-15776-1563zw3.csv'
        cnopts.hostkeys = None
        with pysftp.Connection(host=config("SFTP_URL"), port=config("SFTP_PORT"), username=("SFTP_USER"),
                               password=config("SFTP_PASSWORD"), cnopts=cnopts) as sftp:
            mutex.acquire()
            if not sftp.exists(remote_csv_path):
                return None
            file = sftp.get(remote_csv_path, preserve_mtime=True)
            with open(local_csv_path, 'r+') as f:
                df = pd.read_csv(f)
                for index, row in df.iterrows():
                    if row['Status'] == 'unused':
                        df.loc[index, 'Status'] = 'used'
                        f.seek(index)
                        df.to_csv("Teletalk-Consumer-Teletalk-Consumer-Test-20211123-15776-1563zw3.csv", index=False)
                        sftp.put(local_csv_path, remote_csv_path, preserve_mtime=True)
                        os.remove('Teletalk-Consumer-Teletalk-Consumer-Test-20211123-15776-1563zw3.csv')
                        mutex.release()
                        return row['Code']

    except Exception as e:
        print(e.__str__())
