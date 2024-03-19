#!/usr/bin/python3
"""Handles all default RESTFul API actions"""
from ast import Delete
from api.v1 import app
from flask import abort, jsonify, Blueprint
from models import amenity, state, city

amenities_bp = Blueprint('amenities', __name__)


@amenities_bp.route('/amenities', methods=['GET'])
def get_all_amens():
    amenities = amenity.query.all()
    return jsonify([amenity.to_dict() for amenity in amenities])

@amenities_bp.route('/amenities/<int:amenity_id>', methods=['GET'])
def get_amenity(amenity_id):
    amenity = amenity.query.get(amenity_id)
    if amenity is None:
        abort(404)
    return jsonify(amenity.to_dict())

@amenities_bp.route('/amenities/<int:amenity_id>', methods=['DELETE'])