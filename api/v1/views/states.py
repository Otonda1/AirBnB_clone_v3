#!/usr/bin/python3
"""Defines RESTFUL API actions for states route"""

from api.v1.views import app_views
from models.state import State
from models import storage
from flask import jsonify, abort, request

all_objs = storage.all(State)
storage.close()


@app_views.route("/states", strict_slashes=False, methods=['GET'])
def states():
    list_objs = []
    for v in all_objs.values():  # Iterate through the values(state objs)
        state_dict = v.to_dict()
        list_objs.append(state_dict)

    return jsonify(list_objs)


@app_views.route("/states/<state_id>", methods=['GET'])
def state_by_id(state_id):
    """Retrives a state by id"""
    for v in all_objs.values():
        id = v.id
        if state_id == id:
            return jsonify(v.to_dict())
    abort(404)


@app_views.route("/states/<state_id>", methods=['DELETE'])
def delete_object(state_id):
    """Delete object based  on id

    Args:
        state_id (str): Id of object to delete

    Returns:
        An empty dictonary with the status cose 200
    """
    for v in all_objs.values():
        id = v.id
        if state_id == id:
            storage.delete(v)
            storage.save()
            storage.close()
            return jsonify({}), 200
    abort(404)


@app_views.route("/states", strict_slashes=False, methods=['POST'])
def post_state():
    """Adds a new state object to the database"""
    data = request.get_json()
    if data is None:
        return jsonify({'error': 'Not a JSON'}), 404
    if 'name' not in data:
        return jsonify({'error': 'Misisng name'}), 404

    new_state = State(**data)
    storage.new(new_state)
    storage.save()
    storage.close()
    return jsonify(new_state.to_dict()), 201


@app_views.route("/states/<state_id>", methods=['PUT'])
def update_state(state_id):
    """Updates a State object"""
    data = request.get_json()
    if data is None:
        return jsonify({'error': 'Not a JSON'}), 404
    name = data['name']

    for v in all_objs.values():
        id = v.id
        if state_id == id:
            v.name = name
            storage.new(v)
            storage.save()
            storage.close()
            return jsonify(v.to_dict()), 200
    abort(404)
