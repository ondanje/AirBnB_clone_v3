#!/usr/bin/python3
"""
Module that provides setup for flask application. Creates an instance on localhost port 5500.
Also contains an app teardown context that will close the database 
"""
from flask import Flask, render_template, jsonify
from models import storage
from api.v1.views import app_views
from os import getenv

app = Flask(__name__)
"""Flask application instance
"""
app.register_blueprint(app_views, url_prefix="/api/v1")


def teardown_appcontext(exception):
    """
    Method to close storage
    """
    storage.close()


@app.errorhandler(404)
def return_404(error):
    """Handles the HTTP 404 error
    """
    return jsonify({"error": "Not found"}), 404


if __name__ == "__main__":
    host = getenv("HBNB_API_HOST", "0.0.0.0")
    port = int(getenv("HBNB_API_PORT", 5000))
    app.run(host=host, port=port, threaded=True)
