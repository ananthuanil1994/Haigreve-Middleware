# User post data

USER_NAME = "name"
USER_PHONENO = "phoneNo"
USER_EMAIL = "email"
USER_SUBPLAN = "subscriptionPlan"

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
HASH_WORD = "TeleTalk"

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
