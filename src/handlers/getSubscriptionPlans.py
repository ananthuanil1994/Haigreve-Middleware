from flask import jsonify
from src import constants


def show_subscription_plans():
    subscription_plans = constants.subscriptionPlans
    return jsonify(subscription_plans)

