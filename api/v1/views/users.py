#!/usr/bin/python3
"""Module which handles routes dedicated for users"""
from api.v1.views import app_views
from flask import abort, jsonify, request
from models.user import User
from models import storage


@app_views.route('/users', methods=["GET"], strict_slashes=False)
def get_all_users():
    users = storage.all(User).values()
    return jsonify([user.to_dict() for user in users])


@app_views.route('/users/<user_id>', methods=['GET'], strict_slashes=False)
def get_user(user_id):
    user = storage.get(User, user_id)
    if user is None:
        abort(404)
    return jsonify(user.to_dict())


@app_views.route('/users/<user_id>', methods=['DELETE'],
                 strict_slashes=False)
def del_user(user_id):
    user = storage.get(User, user_id)
    if user is None:
        abort(404)
    else:
        storage.delete(user)
        storage.save()
        return jsonify({}), 200


@app_views.route('/users/', methods=['POST'])
def post_user():
    user_data = request.get_json(silent=True)
    print("{}".format(user_data))
    if not user_data:
        abort(400)
    if 'name' not in user_data:
        abort(400)
    new_user = User(**user_data)
    storage.new(new_user)
    storage.save()

    return jsonify(new_user.to_dict()), 201


@app_views.route('/users/<user_id>', methods=['PUT'], strict_slashes=False)
def update_user(user_id):
    user_data = storage.get(User, user_id)
    if not user_data:
        abort(404)
    found_user = request.get_json(silent=True)
    if not found_user:
        abort(400)
    for key, value in found_user.items():
        setattr(user_data, key, value)
    storage.save()
    return jsonify(user_data.to_dict()), 200
