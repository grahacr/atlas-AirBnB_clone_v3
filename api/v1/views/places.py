#!/usr/bin/python3
"""This module handles api actions for Place objects"""
from api.v1.views import app_views
from flask import abort, jsonify, request
from models.places import Place
from models.city import City
from models import storage


@app_views.route('/cities/<city_id>/places', method="GET")
def get_all_places(city_id):
    data = storage.get(City, city_id)
    if data is None:
        abort(404)
    places = storage.all(Place)
    return jsonify([place.to_dict() for place in places])


@app_views.route('/places/<place_id>', methods=['GET'], strict_slashes=False)
def find_place(place_id):
    place = storage.get(Place, place_id)
    if place is None:
        abort(404)
    return jsonify(place.to_dict())


@app_views.route('/places/<place_id>', methods=['DELETE'],
                 strict_slashes=False)
def del_place(place_id):
    place = storage.get(Place, place_id)
    if place is None:
        abort(404)
    else:
        storage.delete(place)
        storage.save()
        return jsonify({}), 200


@app_views.route('/cities/<city_id>/places/', methods=['POST'])
def input_place(city_id, place_id, user_id):
    data = storage.get(City, city_id)
    if data is None:
        abort(404)
    place_data = request.get_json(silent=True)
    if not place_data:
        abort(400)
    if 'name' not in place_data:
        abort(400)
    if 'user_id' not in place_data:
        abort(400)
    if user_id is None:
        abort(0)
    place = storage.get(Place, place_id)
    if place is None:
        abort(404)
    new_place = Place(**place_data)
    storage.new(new_place)
    storage.save()

    return jsonify(new_place.to_dict()), 201


@app_views.route('/places/<place_id>', methods=['PUT'], strict_slashes=False)
def update_place(place_id):
    place_data = storage.get(Place, place_id)
    if not place_data:
        abort(404)
    found_place = request.get_json(silent=True)
    if not found_place:
        abort(400)
    for key, value in found_place.items():
        setattr(place_data, key, value)
    storage.save()
    return jsonify(place_data.to_dict()), 200

