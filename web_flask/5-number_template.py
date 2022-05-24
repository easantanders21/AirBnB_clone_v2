#!/usr/bin/python3
""" Task 5: script that starts a Flask web application """

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def task_0():
    """ Task 0 Function """
    return("Hello HBNB!")


@app.route("/hbnb", strict_slashes=False)
def task_1():
    """ Task 1 Function """
    return("HBNB")


@app.route("/c/<text>", strict_slashes=False)
def task_2(text):
    """ Task 2 Function """
    new_string = text.replace("_", " ")
    return("C %s" % new_string)


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def task_3(text="is cool"):
    """ Task 3 Function """
    new_string = text.replace("_", " ")
    return("Python %s" % new_string)


@app.route('/number/<int:n>', strict_slashes=False)
def task_4(n):
    """ Task 4 Function """
    return "%d is a number" % n


@app.route('/number_template/<int:n>', strict_slashes=False)
def task_5(n):
    """ Task 5 Function """
    return render_template("5-number.html", n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)
