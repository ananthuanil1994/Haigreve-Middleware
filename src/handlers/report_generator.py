import csv
from io import StringIO

from flask import request
from src import DATE, TIME, TYPE, CSV_MOBILE_NUMBER, CSV_SUBSCRIBED, CSV_PAYMENT_COMPLETED, TEXT_CSV, CSV_FILENAME, \
    CONTENT_DISPOSITION, CSV_ATTACHMENT, CSV_START_DATE, CSV_END_DATE, CSV_ACTIVATION_ID
from werkzeug import Response

from src.models.transaction_details import Transactions
from src.models.user_details import Users


def report_generator():
    date = request.json[DATE]
    user_data = Transactions.query.filter(Transactions.date_updated == date). \
        join(Users, Users.mobile_number == Transactions.mobile_number).with_entities(Transactions.mobile_number,
                                                                                     Transactions.type,
                                                                                     Users.is_subscribed,
                                                                                     Users.is_payment_completed,
                                                                                     Users.subscription_date,
                                                                                     Users.expiration_date,
                                                                                     Users.activation_id)

    def generate():
        data = StringIO()
        w = csv.writer(data)

        # write header
        w.writerow((CSV_MOBILE_NUMBER, TYPE, CSV_SUBSCRIBED, CSV_PAYMENT_COMPLETED, CSV_START_DATE, CSV_END_DATE,
                    CSV_ACTIVATION_ID))
        yield data.getvalue()
        data.seek(0)
        data.truncate(0)

        # write each log item
        for user in user_data:
            w.writerow((
                user.mobile_number,
                user.type,
                user.is_subscribed,
                user.is_payment_completed,
                user.subscription_date,
                user.expiration_date,
                user.activation_id
            ))
            yield data.getvalue()
            data.seek(0)
            data.truncate(0)

    # stream the response as the data is generated
    response = Response(generate(), mimetype=TEXT_CSV)
    # add a filename
    response.headers.set(CONTENT_DISPOSITION, CSV_ATTACHMENT, filename=CSV_FILENAME)
    return response

