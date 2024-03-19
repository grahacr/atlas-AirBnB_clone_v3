#!/usr/bin/python3
"""package module for app views"""


from flask import Blueprint


app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

from api.v1.views.index import *