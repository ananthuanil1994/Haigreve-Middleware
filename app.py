from flask import Flask, jsonify, request
from apscheduler.schedulers.background import BackgroundScheduler
from src.handlers import getSubscriptionPlans, saveUserDetails

# Instantiating a flask app
app = Flask(__name__)


app.add_url_rule('/subscriptionPlans',
                 view_func=getSubscriptionPlans.show_subscription_plans,
                 methods=['GET'])

app.add_url_rule('/saveCustomerDetails',
                 view_func=saveUserDetails.save_customer_details,
                 methods=['POST'])


@app.route('/updateSubscriptionStatus', methods=['GET', 'POST'])
def update_subscription_status():
    # TODO : API which gets hit on payment success / failure
    return {"success": "Status updated, SMS sent"}


def sent_renewal_notification():
    # TODO : Scheduler function which tracks subscription dates and sent renewal SMS
    time_now = datetime.now()
    print(f"Scheduler is alive : {time_now}")


def start_scheduler():
    scheduler = BackgroundScheduler({'apscheduler.timezone': 'Asia/Dhaka'})
    scheduler.add_job(sent_renewal_notification, 'interval', seconds=10)
    scheduler.start()


if __name__ == '__main__':
    # start_scheduler()
    # app.run(debug=True, use_reloader=False)
    app.run(debug=True)
