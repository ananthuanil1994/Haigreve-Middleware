from flask import jsonify
from src import constants
from src.models.subscriptionDetails import Subscriptions


def show_subscription_plans():
    sub_details = Subscriptions.query.all()
    subscription_plans = []
    for sub in sub_details:
        subscription_plans.append({
            constants.SUB_ID: sub.id,
            constants.SUB_PLANNAME: sub.planName,
            constants.SUB_AMOUNT: sub.amount
        })
    return jsonify(subscription_plans)

