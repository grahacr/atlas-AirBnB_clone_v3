#!/usr/bin/python3
"""Handles all default RESTFul API actions"""
from api.v1.views import app_views
from flask import abort, jsonify, request
from models.state import State, City
from models import storage


@app_views.route('/states/<state_id>/cities', methods=['GET'], strict_slashes=False)
def get_cities(state_id):
    state = storage.get(State, state_id)
    if not state:
        abort(404)
    else:
        cities = state.cities
        return jsonify([city.to_dict() for city in cities])
