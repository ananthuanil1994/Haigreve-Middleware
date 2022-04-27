import hashlib
import json
import requests
from flask import jsonify, request, make_response
from src import ZIMPERIUM_HOST, AUTHORIZATION, CONTENT_TYPE, APPLICATION, STATUS_FALSE, ZIMPERIUM_ACTIVATION_API, \
    ZIMPERIUM_ACTIVATION_LIMIT, NONE, UTF8, SUB_ID, MESSAGE, GRP_ID, SHORT_TOKEN, USER_PHONENO, \
    ERROR_RESPONSE, USER_NOT_REGISTERED, URL, CONNECTION_ERROR, TIMEOUT_ERROR, GENERAL_ERROR, \
    PROGRAM_CLOSED_ERROR, SLASH, USER_DEACTIVATED, USER_NOT_DEACTIVATED, \
    ZIMPERIUM_DEACTIVATION_RESPONSE_CODE_SUCCESS, ZIMPERIUM_DEACTIVATION_RESPONSE_CODE_NOT_FOUND, \
    USER_ALREADY_DEACTIVATED, NO_USER_TO_DEACTIVATE, USER_NOT_SUBSCRIBED, USER_SUBSCRIBED
from src.handlers.subscription_handler import check_sms_subscription_status, check_subscription_status
from src.models.user_details import Users
from src.services.getRenewalUsersList import get_users_for_deactivating
from src.services.updateUserSubscriptionDetails import update_details
from src.utilities.utils import get_activation_link, get_default_group_id
from src import db


def activate_zimperium_user():
    try:
        group_id, access_token = get_default_group_id()
        mobile_no = request.json[USER_PHONENO]
        user_details = check_sms_subscription_status(mobile_no)
        if user_details:
            if user_details.is_subscribed:
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
                url = NONE
                return make_response(jsonify({URL: url}), 404)

            user_details.group_id = response[GRP_ID]
            user_details.activation_id = response[SUB_ID]
            user_details.short_token = response[SHORT_TOKEN]
            result = update_details(user_details)
            url = ERROR_RESPONSE
            short_token = user_details.short_token
            if short_token and result:
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


def deactivate_zimperium_users():
    user_data = get_users_for_deactivating()
    if user_data:
        for user in user_data:
            mobile_no = user.mobile_number
            group_id, access_token = get_default_group_id()
            hash_value = hashlib.md5(mobile_no.encode(UTF8)).hexdigest()
            user_details = Users.query.get(hash_value)
            if user_details:
                activation_id = user_details.activation_id
            else:
                return jsonify({MESSAGE: USER_NOT_REGISTERED})
            url = f'{ZIMPERIUM_HOST}{ZIMPERIUM_ACTIVATION_API}{SLASH}{activation_id}'
            headers = {
                CONTENT_TYPE: APPLICATION,
                AUTHORIZATION: access_token
            }

            response = requests.delete(url, headers=headers)
            response_code = response.status_code
            if response_code == ZIMPERIUM_DEACTIVATION_RESPONSE_CODE_SUCCESS:
                user_details.group_id = NONE
                user_details.activation_id = NONE
                user_details.short_token = NONE
                user_details.is_subscribed = STATUS_FALSE
                user_details.is_payment_completed = STATUS_FALSE
                db.session.commit()
                print(USER_DEACTIVATED)
                return True
            elif response_code == ZIMPERIUM_DEACTIVATION_RESPONSE_CODE_NOT_FOUND:
                print(USER_ALREADY_DEACTIVATED)
                return True
            print(USER_NOT_DEACTIVATED)
            return True
    print(NO_USER_TO_DEACTIVATE)
    return True
