#!/usr/bin/python3
"""
    creates a Blueprint endpoint
"""
from api.v1.views import app_views
from flask import jsonify


@app_views.route("/status")
def status():
    """
        returns json
    """
    return jsonify({"status": "OK"})
