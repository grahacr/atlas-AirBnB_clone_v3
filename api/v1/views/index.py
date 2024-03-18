#!/usr/bin/python3

from api.v1 import app_views

@app_views.route('/status', strict_slashes=False)
def index():
    """"""
    response = {"status": "OK"}
    return response