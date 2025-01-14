#!/usr/bin/python3

"""
Flask web server for our airbnb page.
white route called  states.
"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)



@app.route('/hbnb_filters', strict_slashes=False)
def hbnb():
    """Get all cities of just one."""
    data = storage.all(State).values()
    res = []
    if uid:
        for state in data:
            if state.id == uid:
                res = [state]
                break
            else:
                res = []
    else:
        res = data
    return render_template("9-states.html", datas=res)


@app.teardown_appcontext
def teardown_session(exceptions):
    """Close the session after every requests."""
    storage.close()


if __name__ == '__main__':
    """Running the file."""
    app.run("0.0.0.0", 5000)
