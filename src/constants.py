# User post data

USER_NAME = "name"
USER_FIRST_NAME = 'first_name'
USER_LAST_NAME = 'last_name'
USER_PHONENO = "phone_number"
USER_EMAIL = "email"
USER_SUBPLAN = "subscription_plan"
DURATION = "duration_month"
PAYMENT_STATUS = "payment_status"
# User post response

RESP_ID = "id"
RESP_NAME = "name"
RESP_PHONENO = "phoneNo"
RESP_EMAIL = "email"
RESP_SUBPLAN = "subscriptionPlan"
RESP_STATUS = "status"
RESP_STATUSVALUE = "SUCCESS"

# Status

STATUS_TRUE = True
STATUS_FALSE = False

# Routes

ROUTES_NAME = "teletalk_routes"
URL_SUBSCRIPTION_PLANS = "/subscriptionPlans"
URL_SAVE_CUSTOMER_DETAILS = "/saveCustomerDetails"
URL_UPDATE_CUSTOMER_DETAILS = "/updateCustomerDetails"
URL_CONFIRM_SUBSCRIPTION = '/confirmSubscription'
URL_CHECK_SUBSCRIPTION_STATUS = '/checkSubscriptionStatus'
URL_ACTIVATE_USER_SUBSCRIPTION = '/activateSubscription'

SMS_LINK = "http://202.74.240.169/sending_sms_win/Default.aspx?login_name=haigreve&mobileno="
SMS_MESSAGE = 'msg'
# SMS_DEFAULT_CODE = ""
#
# SMS_FORMAT = f"""
# Hello {SMS_DEFAULT_NAME},
# Thanks for Subscribing Lookout MES.
# Please download  & activate the application from the link below:
# https://get.lookout.com/web-code?code={SMS_DEFAULT_CODE}
#
# Thanks,
# Team Haigreve
# """
#
# REMINDER_SMS_FORMAT = f"""
# Hello [Name],
# Your Lookout MES subscription is expiring on DD/MM/YY.
# To resubscribe please visit [Page Address] .
#
# Thanks,
# Team Haigreve
# """

# Request methods

GET_METHOD = "GET"
POST_METHOD = "POST"

# Model

TABLE_NAME = "user_details"
USER_FOREIGN_KEY = 'user_details.mobile_number'
TXN_MODEL_NAME = 'Transactions'
SUB_TABLE_NAME = "subscription_plans"
TXN_TABLE_NAME = "transaction_details"
TXN_ID = 'transaction_id'
MOBILE_NUMBER = 'mobile_number'

# SQL alchemy configurations

SQLALCHEMY_TRACK_MODIFICATIONS = "SQLALCHEMY_TRACK_MODIFICATIONS"
SQLALCHEMY_DATABASE_URI = "SQLALCHEMY_DATABASE_URI"
DIALECTDRIVER = "mysql+pymysql"

# DB Fields

DB_ID = "id"
DB_NAME = "name"
DB_MOBILENO = "mobileNo"
DB_EMAIL = "email"
DB_ISSUBSCRIBED = "isSubscribed"
DB_SUBSCRIPTIONPLAN = "subscriptionPlan"
DB_ISPAYMENTCOMPLETED = "isPaymentCompleted"
DB_SUBSCRIPTIONDATE = "subscriptionDate"

SUB_ID = "id"
SUB_PLANNAME = "planName"
SUB_AMOUNT = "amount"
SUB_DURATION = "duration_months"
HASH_WORD = "TeleTalk"
CLIENT_ID = 'client_id'
TRANSACTION_ID = 'transaction_id'
SUB_MOBILE_NUMBER = 'mobileno'
PRODUCT_ID = 'product_id'
SERVICE_ID = 'service_id'
TYPE = 'type'
SERVICE_NAME = 'service_name'
CHANNEL_NAME = 'channel_name'
SUB_CLIENT_ID = 'haigreve'
SUB_PRODUCT_ID = 'HAIGREVE_MOBILE_SECURITY_MS4'
SUB_SERVICE_ID = 'START MSW'
SUB_TYPE = 'subscription'
SUB_SERVICE_NAME = 'START MSW'
SUB_CHANNEL_NAME = 'CP'
SUB_PAGE_URL = 'http://202.74.240.171:8086/teletalk_sdp_sub_activete.aspx'
CHECK_SUB_URL = 'http://202.74.240.169:8064/sub_status.aspx'
PLAN_VALUE = 1

subscriptionPlans = [
    {
        "id": 1,
        "planName": "1 Month License",
        "amount": 80
    },
    {
        "id": 2,
        "planName": "3 Month License",
        "amount": 240
    },
    {
        "id": 3,
        "planName": "6 Month License",
        "amount": 480
    },
    {
        "id": 4,
        "planName": "1 Year License",
        "amount": 960
    }
]

# PAYMENT STATUS
PAYMENT_SUCCESS = 'success'
PAYMENT_FAILED = 'failed'

# ZIMPERIUM
ZIMPERIUM_HOST = 'https://ziap.zimperium.com'
LOGIN_HEADER = {"Content-Type": "application/json"}
BEARER = 'Bearer'
AUTHORIZATION = 'Authorization'
CONTENT_TYPE = "Content-Type"
APPLICATION = "application/json"
ZIMPERIUM_LOGIN_API = "/api/auth/v1/api_keys/login"
ZIMPERIUM_GROUP_API = '/api/mtd-policy/public/v1/groups/'
ZIMPERIUM_ACTIVATION_API = "/api/zapp/public/v1/user-activations"
TOKEN_TABLE_NAME = 'zimperium_tokens'
ZIMPERIUM_ACTIVATION_LIMIT = 2
ACTIVATION_LINK_API = '/api/acceptor/v1/user-activation/activation?stoken='

DECODED_INITIAL = {}
ACCESS_TOKEN = 'access_token'
NONE = None
VERIFY_SIGNATURE = 'verify_signature'
TOKEN_EXPIRY = 'exp'
UTF8 = 'utf-8'
ZIMPERIUM_ACCESS_TOKEN = 'accessToken'
ZIMPERIUM_REFRESH_TOKEN = 'refreshToken'
MESSAGE = 'message'
GRP_ID = 'groupId'
SHORT_TOKEN = 'shortToken'
VALUE_ZERO = 0
MESSAGE_STATUS = 'message_status'
