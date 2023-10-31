#!/usr/bin/python3
"""
    creates flask server
"""


from flask import Flask, jsonify, make_response
from models import storage
from api.v1.views import app_views
from os import getenv
app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown_appocontext(exc):
    """
        calls storage.close
    """
    storage.close()


@app.errorhandler(404)
def page_not_found(error):
    return make_response(jsonify({"error": "Not found"}), 404)


if __name__ == "__main__":
    if getenv("HBNB_API_HOST") and getenv("HBNB_API_PORT"):
        app.run(host=getenv("HBNB_API_HOST"),
                port=int(getenv("HBNB_API_PORT")))
    else:
        app.run(host="0.0.0.0", port=5000, threaded=True)
