#!/usr/bin/python3
"""
A Script to handle routes relating to index file
"""
from flask import jsonify
from api.v1.views import app_views
from models import storage


@app_views.route("/status", methods=["GET"], strict_slashes=False)
def view_status():
    """ Returns JSON """
    return jsonify(status="OK")


@app_views.route("/stats", methods=["GET"], strict_slashes=False)
def get_stats():
    """Retrieves the number of each object by type"""
    return jsonify(
        amenities=storage.count("Amenity"),
        cities=storage.count("City"),
        places=storage.count("Place"),
        reviews=storage.count("Review"),
        states=storage.count("State"),
        users=storage.count("User"),
    )
