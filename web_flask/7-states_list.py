#!/usr/bin/python3

"""Flask app for airbnb with routes."""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    """Return the list of states in database."""
    d = storage.all(State)
    datas = d.values()
    return (render_template("7-states_list.html", datas=datas))


@app.teardown_appcontext
def close_session(exception):
    """Closes database session."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
