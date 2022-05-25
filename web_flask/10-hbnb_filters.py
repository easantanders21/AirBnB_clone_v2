#!/usr/bin/python3
""" Task 11: script that starts a Flask web application """

from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity

app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def task_11(id=None):
    """ Task 11 Function """
    list_states = storage.all(State)
    list_amenities = storage.all(Amenity)
    return(render_template("10-hbnb_filters.html",
                           list_states=list_states,
                           list_amenities=list_amenities))


@app.teardown_appcontext
def call_storage_close(exception):
    """ close the current SQLAlchemy Session """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)
