import hashlib
import json
import requests
from flask import jsonify, request
from src import ZIMPERIUM_HOST, AUTHORIZATION, CONTENT_TYPE, APPLICATION, STATUS_FALSE, ZIMPERIUM_ACTIVATION_API, \
    ZIMPERIUM_ACTIVATION_LIMIT, NONE, UTF8, SUB_ID, MESSAGE, GRP_ID, SHORT_TOKEN, PAYMENT_SUCCESS, USER_PHONENO, \
    ERROR_RESPONSE, USER_SUBSCRIBED, USER_NOT_SUBSCRIBED, URL, CONNECTION_ERROR, TIMEOUT_ERROR, GENERAL_ERROR, \
    PROGRAM_CLOSED_ERROR
from src.handlers.subscription_handler import check_subscription_status
from src.models.user_details import Users
from src.services.updateUserSubscriptionDetails import update_details
from src.utilities.utils import get_activation_link, get_default_group_id


def activate_zimperium_user():
    try:
        group_id, access_token = get_default_group_id()
        mobile_no = request.json[USER_PHONENO]
        result = check_subscription_status(mobile_no)
        if result == USER_SUBSCRIBED:
            hash_value = hashlib.md5(mobile_no.encode(UTF8)).hexdigest()
            user_details = Users.query.get(hash_value)
            if user_details:
                first_name = user_details.first_name
                last_name = user_details.last_name
                email = user_details.email
            else:
                return jsonify({MESSAGE: USER_NOT_SUBSCRIBED})
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
            response = json.loads(response.content.decode(UTF8))

            if response.get(MESSAGE, NONE):
                url = get_activation_link(user_details.short_token)
                return jsonify({URL: url})

            user_details.group_id = response[GRP_ID]
            user_details.activation_id = response[SUB_ID]
            user_details.short_token = response[SHORT_TOKEN]
            user_details.payment_status = PAYMENT_SUCCESS
            result = update_details(user_details)
            url = ERROR_RESPONSE
            if user_details.short_token and result:
                url = get_activation_link(user_details.short_token)
            return jsonify({URL: url})
        return jsonify({URL: NONE})
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
