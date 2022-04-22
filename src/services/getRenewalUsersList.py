from src import VALUE_ZERO
from src.models.user_details import Users
from datetime import datetime, date
from dateutil.relativedelta import relativedelta

from src.utilities.utils import send_bulk_sms_message


def get_users_for_renewal():
    current_date = datetime.utcnow()
    next_date = current_date + relativedelta(days=+3)
    user_data = Users.query.filter(current_date <= Users.expiration_date).\
        filter(Users.expiration_date <= next_date).all()
    send_bulk_sms_message(user_data)
    return True


def get_users_for_deactivating():
    user_data = Users.query.filter(Users.is_subscribed == VALUE_ZERO)
    return user_data
