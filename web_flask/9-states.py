#!/usr/bin/python3
""" Task 10: script that starts a Flask web application """

from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)


@app.route("/states", strict_slashes=False)
@app.route("/states/<id>", strict_slashes=False)
def task_10(id=None):
    """ Task 10 Function """
    list_states = storage.all(State)
    if id is None:
        return(render_template("9-states.html", list_states=list_states))
    else:
        return(render_template("9-states.html",
                               list_states=list_states, id="State." + id))


@app.teardown_appcontext
def call_storage_close(exception):
    """ close the current SQLAlchemy Session """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)
