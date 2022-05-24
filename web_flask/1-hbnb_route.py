#!/usr/bin/python3
""" Task 1: script that starts a Flask web application """

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def task_0():
    """ Task 0 Function """
    return("Hello HBNB!")


@app.route("/hbnb", strict_slashes=False)
def task_1():
    """ Task 0 Function """
    return("HBNB")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)
