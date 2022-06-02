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
URL_REDIRECTION_LINK = '/redirectionLink'
URL_DEACTIVATE_USER_SUBSCRIPTION = '/deactivateSubscription'
URL_UPDATE_USER_SUBSCRIPTION_STATUS = '/updateSubscriptionStatus'
URL_REPORT_GENERATOR = '/reportGenerator'
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
PUT_METHOD = "PUT"
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
        "planName": "1 Day License",
        "amount": 2
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
ZIMPERIUM_HOST = 'https://zapac.zimperium.com'
LOGIN_HEADER = {"Content-Type": "application/json"}
BEARER = 'Bearer'
AUTHORIZATION = 'Authorization'
CONTENT_TYPE = "Content-Type"
APPLICATION = "application/json"
ZIMPERIUM_LOGIN_API = "/api/auth/v1/api_keys/login"
ZIMPERIUM_GROUP_API = '/api/mtd-policy/public/v1/groups/'
ZIMPERIUM_ACTIVATION_API = "/api/zapp/public/v1/user-activations"
TOKEN_TABLE_NAME = 'zimperium_tokens'
ZIMPERIUM_ACTIVATION_LIMIT = 1
ACTIVATION_LINK_API = '/api/acceptor/v1/user-activation/activation?stoken='
ZIMPERIUM_DEACTIVATION_RESPONSE_CODE_SUCCESS = 204
ZIMPERIUM_DEACTIVATION_RESPONSE_CODE_NOT_FOUND = 404
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
DEFAULT_USER_TYPE = "WEB"
ERROR_RESPONSE = 'database or API error'
USER_NOT_REGISTERED = 'The user is not registered'
USER_REGISTERED = 'The user is registered'
ALREADY_REGISTERED = 'user is already registered'
USER_NOT_SUBSCRIBED = 'The user is not subscribed'
USER_SUBSCRIBED = 'subscribed'
URL = 'url'
REDIRECTION_URL = 'bd.haigreve.com/activation?phone='
CONNECTION_ERROR = "OOPS!! Connection Error. Make sure you are connected to Internet. Technical Details given below."
TIMEOUT_ERROR = "OOPS!! Timeout Error"
GENERAL_ERROR = "OOPS!! General Error"
PROGRAM_CLOSED_ERROR = "Someone closed the program"
SLASH = '/'
USER_DEACTIVATED = 'Deactivated'
USER_ALREADY_DEACTIVATED = 'User already deactivated'
USER_NOT_DEACTIVATED = 'Deactivation failed due to API error'
NO_USER_TO_DEACTIVATE = "No user to deactivate"
NETWORK_PROVIDER = 'provider'
SMS_SUBSCRIPTION_STATUS = 'subscription_status'
STATUS_UPDATED = 'user status updated'
MSISDN = 'msisdn'
SHORT_CODE = 'shortcode'
TEXT = 'text'
MNO_CODE = 'mnocode'
TIME = 'time'
TRANSACTION_SERVICE_ID = 'serviceid'
TRANSACTIONID = 'transid'
SUB = 'sub'
TRANSACTION_ERROR = 'Transaction id already exist'
COM = '.com'
ERROR = 'error'
PLUS = '+'
NO_CONTENT_RESPONSE_CODE = 204
RENEW = 'renew'
START_DATE = 'startDate'
END_DATE = 'endDate'
CSV_MOBILE_NUMBER = 'mobile number'
CSV_SUBSCRIBED = 'subscription status'
CSV_PAYMENT_COMPLETED = 'payment status'
TEXT_CSV = 'text/csv'
CSV_FILENAME = 'Report.csv'
CSV_ATTACHMENT = 'attachment'
CONTENT_DISPOSITION = "Content-Disposition"
THRESHOLD_VALUE = 15
CSV_START_DATE = 'start date'
CSV_END_DATE = 'end date'
CSV_ACTIVATION_ID = 'activation id'
