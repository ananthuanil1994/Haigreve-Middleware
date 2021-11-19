from flask import jsonify
from .. import constants


def show_subscription_plans():
    subscriptionPlans = constants.subscriptionPlans
    return jsonify(subscriptionPlans)


