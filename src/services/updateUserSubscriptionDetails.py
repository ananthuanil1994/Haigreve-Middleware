from src import db, STATUS_TRUE
from datetime import datetime
from dateutil.relativedelta import relativedelta


def update_details(user_details):
    try:

        user_details.is_subscribed = STATUS_TRUE
        user_details.is_payment_completed = STATUS_TRUE
        user_details.subscription_date = datetime.utcnow()
        if user_details.subscription_plan == 1:
            user_details.expiration_date = datetime.utcnow() + relativedelta(days=+1)
        elif user_details.subscription_plan == 2:
            user_details.expiration_date = datetime.utcnow() + relativedelta(months=+3)
        elif user_details.subscription_plan == 3:
            user_details.expiration_date = datetime.utcnow() + relativedelta(months=+6)
        elif user_details.subscription_plan == 4:
            user_details.expiration_date = datetime.utcnow() + relativedelta(years=+1)
        else:
            user_details.expiration_date = datetime.utcnow()
        db.session.commit()
        status = True
    except Exception as e:
        status = False
    finally:
        return status
