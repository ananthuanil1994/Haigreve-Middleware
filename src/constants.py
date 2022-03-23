# User post data

USER_NAME = "name"
USER_PHONENO = "phone_number"
USER_EMAIL = "email"
USER_SUBPLAN = "subscription_plan"
DURATION = "duration_month"
PAYMENT_STATUS ="payment_status"
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

# SMS_DEFAULT_NAME = "User"
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
SUB_TABLE_NAME = "subscription_plans"

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
SUB_CLIENT_ID = 'haigreve'
SUB_PRODUCT_ID = 'HAIGREVE_MOBILE_SECURITY_MS4'
SUB_SERVICE_ID = 'START MSW'
SUB_TYPE = 'subscription'
SUB_SERVICE_NAME = 'START MSW'
SUB_CHANNEL_NAME = 'CP'

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
