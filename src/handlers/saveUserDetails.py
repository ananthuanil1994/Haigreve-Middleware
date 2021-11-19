from flask import jsonify, request


def save_customer_details():
    # TODO : Fix import problem
    name = request.json['name']
    phone_no = request.json['phoneNo']
    email = request.json['email']
    subscription_plan = request.json['subscriptionPlan']
    hashword = f"{str(phone_no)}{name}"
    hash_value = abs(hash(hashword))
    context = {'id': hash_value, 'name': name, 'phoneNo': phone_no, 'email': email,
               'subscriptionPlan': subscription_plan, 'status': 'success'}
    return jsonify(context)