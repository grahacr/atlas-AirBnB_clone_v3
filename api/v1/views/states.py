#!/usr/bin/python3
"""Handles all default RESTFul API actions"""
from api.v1 import app
from api.v1.views import app_views
from flask import abort, jsonify, Blueprint, request
from .models import State, BaseModel

states_bp = Blueprint('states', __name__)


@app.route('/api/v1/states', methods=['GET'])
def get_all_states():
    states = State.query.all()
    return jsonify([state.to_dict() for state in states])

@app.route('/api/v1/states/<int:state_id>', methods=['GET'])
def get_state(state_id):
    state = State.query.get(state_id)
    if state is None:
        abort(404)
    return jsonify(state.to_dict())

@app.route('/api/v1/states/<int:state_id>', method=['DELETE'])
def del_state(state_id):
    if request.method == 'DELETE':
        states = State.query.all()
        for state in states:
            if state.id == state_id:
                state.delete()
                return jsonify({}), 200
        abort(404)
@app.route('/api/v1/states', method=['POST'])
def post_state():
    