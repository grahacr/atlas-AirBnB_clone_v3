#!/usr/bin/python3
"""Handles all default RESTFul API actions"""
from api.v1 import app
from flask import abort, jsonify, Blueprint
from .models import State

states_bp = Blueprint('states', __name__)


@states_bp.route('/api/v1/states', methods=['GET'])
def get_all_states():
    states = State.query.all()
    return jsonify([state.to_dict() for state in states])

@states_bp.route('/api/v1/states/<int:state_id>', methods=['GET'])
def get_state(state_id):
    state = State.query.get(state_id)
    if state is None:
        abort(404)
    return jsonify(state.to_dict())
