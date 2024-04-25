#!/usr/bin/python3
"""
starts a Flask web application:
"""
from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello_bnb():
    """hello bnb"""
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    """hello bnb"""
    return "HBNB"


@app.route("/c/<text>")
def c_is_fun(text):
    """print C {msg}"""
    msg = text.replace('_', ' ')
    return f"C {msg}"


@app.route("/python/")
@app.route("/python/<text>")
def python_is_cool(text="is cool"):
    """print C {msg}"""
    msg = text.replace('_', ' ')
    return f"Python {msg}"


@app.route('/number/<int:n>')
def display_integer(n):
    """ Display n is a number only if n is an integer """
    return "{} is an Integer.".format(n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
    app.url_map.strict_slashes = False
