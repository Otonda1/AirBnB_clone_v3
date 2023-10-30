#!/usr/bin/python3
"""
    creates flask server
"""


from flask import Flask
from models import storage
from api.v1.views import app_views
from os import getenv
app = Flask(__name__)
app.register_blueprint("app_views")


@app.teardown_appcontext
def teardown_appocontext():
    """
        calls storage.close
    """
    storage.close()


if __name__ == "__main__":
    if getenv("HBNB_API_HOST") and getenv("HBNB_API_PORT"):
        app.run(host=getenv("HBNB_API_HOST"),
                port=int(getenv("HBNB_API_PORT")))
    else:
        app.run(host="0.0.0.0", port=5000)
