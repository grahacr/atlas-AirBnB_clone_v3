#!/usr/bin/python3
"""Handles all default RESTFul API actions"""
from api.v1.views import app_views
from flask import abort, jsonify, request
from models.amenity import Amenity
from models import storage


@app_views.route('/amenities', methods=['GET'], strict_slashes=False)
def get_all_amens():
    amens = storage.all(Amenity).values()
    return jsonify([amenity.to_dict() for amenity in amens])


@app_views.route('/amenities/<amenity_id>', methods=['GET'],
                 strict_slashes=False)
def get_amenity(amenity_id):
    amenity = storage.get(Amenity, amenity_id)
    if amenity is None:
        abort(404)
    return jsonify(amenity.to_dict())


@app_views.route('/amenities/<amenity_id>', methods=['DELETE'],
                 strict_slashes=False)
def del_amenity(amenity_id):
    amenity = storage.get(Amenity, amenity_id)
    if amenity is None:
        abort(404)
    else:
        storage.delete(amenity)
        storage.save()
        return jsonify({}), 200


@app_views.route('/amenities/', methods=['POST'])
def post_amenity():
    data = request.get_json(silent=True)
    if not data:
        abort(400)
    if 'name' not in data:
        abort(400)
    new_amenity = Amenity(**data)
    storage.new(new_amenity)
    storage.save()

    return jsonify(new_amenity.to_dict()), 201


@app_views.route('/amenities/<amenity_id>', methods=['PUT'],
                 strict_slashes=False)
def update_amenity(amenity_id):
    amenity_data = storage.get(Amenity, amenity_id)
    if not amenity_data:
        abort(404)
    found_amenity = request.get_json(silent=True)
    if not found_amenity:
        abort(400)
    for key, value in found_amenity.items():
        setattr(amenity_data, key, value)
    storage.save()
    return jsonify(amenity_data.to_dict()), 200
