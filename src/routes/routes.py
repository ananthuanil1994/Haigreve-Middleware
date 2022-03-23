from src.handlers.user import save_customer_details
from src.handlers.subscription_plan import show_subscription_plans
from src.handlers.updateUserDetails import update_customer_details
from src.handlers.subscription_handler import confirm_subscription, check_subscription_status
from src import app
from flask import Blueprint
from src.constants import *

teletalk_routes = Blueprint(ROUTES_NAME, __name__)

app.add_url_rule(URL_SUBSCRIPTION_PLANS,
                 view_func=show_subscription_plans,
                 methods=[GET_METHOD])

app.add_url_rule(URL_SAVE_CUSTOMER_DETAILS,
                 view_func=save_customer_details,
                 methods=[POST_METHOD])

app.add_url_rule(URL_UPDATE_CUSTOMER_DETAILS,
                 view_func=update_customer_details,
                 methods=[POST_METHOD])

app.add_url_rule(URL_CONFIRM_SUBSCRIPTION,
                 view_func=confirm_subscription,
                 methods=[GET_METHOD])

app.add_url_rule(URL_CHECK_SUBSCRIPTION_STATUS,
                 view_func=check_subscription_status,
                 methods=[GET_METHOD])
