#!/usr/bin/python3
"""
    creates a Blueprint endpoint
"""
from api.v1.views import app_views
from flask import jsonify
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.user import User
from models.state import State
from models import storage


@app_views.route("/status")
def status():
    """
        returns json
    """
    return jsonify({"status": "OK"})


@app_views.route("/stats")
def stats():
    classes = {"Amenity": Amenity, "City": City,
               "Place": Place, "Review": Review, "State": State, "User": User}

    cls_dict = {}
    for k, v in classes.items():
        total_cls_objs = storage.count(v)
        key = k.lower()
        if key[-1] == 'y':  # Make key plural if ends with 'y'
            key = key[:-1] + 'ies'
        else:  # make plural by adding 's'
            key = key + 's'

        cls_dict[key] = total_cls_objs
    return jsonify(cls_dict)
