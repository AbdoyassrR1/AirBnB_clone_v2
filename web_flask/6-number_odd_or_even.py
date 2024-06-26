#!/usr/bin/python3
"""
starts a Flask web application:
"""
from flask import Flask, render_template
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
    return "{:d} is a number".format(n)


@app.route('/number_template/<int:n>')
def display_html(n):
    """ Display n is a HTML page only if n is an integer """
    return render_template("5-number.html", num=n)


@app.route('/number_odd_or_even/<int:n>')
def odd_or_even(n):
    """ Display n is odd or even only if n is an integer """
    odd_or_even = ""
    if (n % 2 == 0):
        odd_or_even = "even"
    else:
        odd_or_even = "odd"
    return render_template(
                            "6-number_odd_or_even.html",
                            num=n,
                            odd_or_even=odd_or_even
                            )


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
    app.url_map.strict_slashes = False
