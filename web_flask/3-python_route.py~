#!/usr/bin/python3

"""Flask app for airbnb with two routes."""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """Hello Route."""
    return ("Hello HBNB!")


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Returns HBNB."""
    return ("HBNB")


@app.route("/c/<text>", strict_slashes=False)
def ctext(text):
    """Somewhat like a loopback."""
    return ("C {}".format(text.replace("_", " ")))


if __name__ == "__main__":
    app.run(host="0.0.0.0")
