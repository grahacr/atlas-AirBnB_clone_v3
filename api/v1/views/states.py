#!/usr/bin/python3
"""Handles all default RESTFul API actions"""
from api.v1.views import app_views
from flask import abort, jsonify, request
from models.state import State
from models import storage


@app_views.route('/states', methods=['GET'], strict_slashes=False)
def get_all_states():
    states = storage.all(State).values()
    return jsonify([state.to_dict() for state in states])

@app_views.route('/states/<state_id>', methods=['GET'], strict_slashes=False)
def get_state(state_id):
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    return jsonify(state.to_dict())

@app_views.route('/states/<state_id>', methods=['DELETE'],
                 strict_slashes=False)
def del_state(state_id):
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    else:
        storage.delete(state)
        storage.save()
        return jsonify({}), 200

@app_views.route('/states/', methods=['POST'])
def post_state():
    data = request.get_json(silent=True)
    if not data:
        abort(400)
    if 'name' not in data:
        abort(400)
    new_state = State(**data)
    storage.new(new_state)
    storage.save()

    return jsonify(new_state.to_dict()), 201	

@app_views.route('/states/<state_id>', methods=['PUT'])
def update_state(state_id):
    state_data = storage.get(State, state_id)
    if not state_data:
        abort(404)
    found_state = request.get_json(silent=True)
    if not found_state:
        abort(400)
    for key, value in found_state.items():
        setattr(state_data, key, value)
    storage.save()
    return jsonify(state_data.to_dict()), 200
