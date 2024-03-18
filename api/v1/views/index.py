#!/usr/bin/python3
"""module for checking status of route"""
from flask import jsonify
from api.v1.views import app_views


@app_views.route('/status', strict_slashes=False)
def index():
    """return status"""
    response = {"status": "OK"}
    return response
