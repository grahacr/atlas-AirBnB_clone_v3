#!/usr/bin/python3
"""module for checking status of route"""
from flask import jsonify
from api.v1.views import app_views
from models import storage


@app_views.route('/status', strict_slashes=False)
def index():
    """return status"""
    response = {"status": "OK"}
    return response

@app_views.route('/stats', strict_slashes=False)
def stats():
    objects_count = {}
    objects_count['amenities'] = storage.count('Amenity')
    objects_count['cities'] = storage.count('City')
    objects_count['places'] = storage.count('Place')
    objects_count['reviews'] = storage.count('Review')
    objects_count['states'] = storage.count('State')
    objects_count['users'] = storage.count('User')
    return objects_count