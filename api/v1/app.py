#!/usr/bin/python3
"""New module for application"""

from api.v1.views import app_views
from flask import Flask
from models import storage
from os import getenv
from flask import jsonify


app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown(exception):
    storage.close()


@app.errorhandler(404)
def page_not_found(error):
    return jsonify({"error": "Not found"}), 404


if __name__ == '__main__':
    host = getenv('HBNB_API_HOST', default='0.0.0.0')
    port = getenv('HBNB_API_PORT', default=5000)
    app.run(host=host, port=port, threaded=True)
