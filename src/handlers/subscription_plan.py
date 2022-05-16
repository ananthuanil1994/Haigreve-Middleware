from flask import jsonify
from src import constants
from src.models.subscription_details import Subscriptions


def show_subscription_plans():
    sub_details = Subscriptions.query.all()
    subscription_plans = []
    for sub in sub_details:
        subscription_plans.append({
            constants.SUB_ID: sub.id,
            constants.SUB_PLANNAME: sub.plan_name,
            constants.SUB_AMOUNT: sub.amount,
            constants.SUB_DURATION: sub.duration_months
        })
    return jsonify(subscription_plans)

