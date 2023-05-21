#!/usr/bin/python3

"""Flask app for airbnb with routes."""

from flask import Flask, render_template

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
def c_text(text: str):
    """Somewhat like a loopback."""
    return ("C {}".format(text.replace("_", " ")))


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_text(text: str = "is cool"):
    """Somewhat like a loopback."""
    return ("Python {}".format(text.replace("_", " ")))


@app.route("/number/<int:n>", strict_slashes=False)
def numb(n: int):
    """N is a number."""
    return ("{} is a number".format(n))


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n: int):
    """Returns a number template."""
    return (render_template("5-number.html", number=n))


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def even_odd(n: int):
    """Returns a template."""
    return (render_template("6-number_odd_or_even.html", num=n))


if __name__ == "__main__":
    app.run(host="0.0.0.0")