#!/usr/bin/python3
""" Task 8: script that starts a Flask web application """

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def task_8():
    """ Task 8 Function """
    all_states = storage.all(State)
    list_states = []
    for state in all_states.values():
        list_states.append(state)
    return(render_template("7-states_list.html", list_states=list_states))


@app.teardown_appcontext
def call_storage_close(exception):
    """ close the current SQLAlchemy Session """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)
