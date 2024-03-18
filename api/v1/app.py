#/usr/bin/python3
"""New module for application"""
from flask import Flask, Blueprint
from models import storage
from api.v1.views app_views


app = Flask(__name__)
app.register_blueprint(app_views

@app.teardown_appcontext
