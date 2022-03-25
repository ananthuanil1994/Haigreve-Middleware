import json
import requests
from src import ZIMPERIUM_HOST, ZIMPERIUM_LOGIN_API, ZIMPERIUM_LOGIN_PAYLOAD, db, ZIMPERIUM_GROUP_API, BEARER, \
    LOGIN_HEADER, AUTHORIZATION, CONTENT_TYPE, APPLICATION
from src.models.token_details import Tokens


def zimperium_login():
    url = f'{ZIMPERIUM_HOST}{ZIMPERIUM_LOGIN_API}'
    response = requests.post(url, json=ZIMPERIUM_LOGIN_PAYLOAD, headers=LOGIN_HEADER)
    response = json.loads(response.content.decode("utf-8"))
    access_token = response['accessToken']
    refresh_token = response['refreshToken']
    transaction = Tokens(access_token=access_token, refresh_token=refresh_token)
    db.session.add(transaction)
    db.session.commit()
    return access_token


def get_default_group_id():
    access_token = BEARER + ' ' + zimperium_login()
    print(access_token)
    url = f'{ZIMPERIUM_HOST}{ZIMPERIUM_GROUP_API}'
    headers = {
        CONTENT_TYPE: APPLICATION,
        AUTHORIZATION: access_token
    }
    response = requests.get(url, headers=headers)
    response = json.loads(response.content.decode("utf-8"))
    print(response)
    group_id = response[0]['id']
    return group_id
