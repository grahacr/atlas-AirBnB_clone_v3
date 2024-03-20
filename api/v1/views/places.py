#!/usr/bin/python3
"""This module handles api actions for Place objects"""
from api.v1.views import app_views
from flask import abort, jsonify, request
from models.places import Place
from models.city import City
from models import storage


@app_views('/cities/<city_id>/places', method="GET")
def get_all_places(city_id):
    data = storage.get(City, city_id)
    if data is None:
        abort(404)
    place = storage.all(Place)
    if not place:
        s
    return jsonify([place.to_dict() for place in places])


@app_views.route('/cities/<city_id>/places/<place_id>', methods=['GET'], strict_slashes=False)
def find_place(place_id):
    place = storage.get(Place, place_id)
    if place is None:
        abort(404)
    return jsonify(place.to_dict())


@app_views.route('/cities/<city_id>/places/<place_id>', methods=['DELETE'],
                 strict_slashes=False)
def del_user(place_id):
    place = storage.get(Place, place_id)
    if place is None:
        abort(404)
    else:
        storage.delete(place)
        storage.save()
        return jsonify({}), 200


