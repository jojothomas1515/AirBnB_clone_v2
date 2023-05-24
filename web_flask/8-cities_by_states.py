#!/usr/bin/python3

"""
Flask web server for our airbnb page.
white route called cities by states.
"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_list_by_states():
    """Send all the cities associated with a state."""
    data = storage.all(State).values()
    return render_template("8-cities_by_states.html", datas=data)


@app.teardown_appcontext
def teardown_session(exceptions):
    """Close the session after every requests."""
    storage.close()


if __name__ == '__main__':
    """Running the file."""
    app.run("0.0.0.0", 5000)
