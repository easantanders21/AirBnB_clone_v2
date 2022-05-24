#!/usr/bin/python3
""" Task 9: script that starts a Flask web application """

from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def task_9():
    """ Task 9 Function """
    list_states = storage.all(State)
    return(render_template("8-cities_by_states.html", list_states=list_states))


@app.teardown_appcontext
def call_storage_close(exception):
    """ close the current SQLAlchemy Session """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)
