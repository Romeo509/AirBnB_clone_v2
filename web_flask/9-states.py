#!/usr/bin/python3
"""
Script that starts a Flask web application
"""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def handle_teardown(self):
    """
    Method to handle teardown of the application context
    """
    storage.close()


@app.route('/states', strict_slashes=False)
def states_list():
    """
    Method to render a list of states
    """
    states = sorted(list(storage.all("State").values()), key=lambda x: x.name)
    return render_template("9-states.html", states=states)


@app.route('/states/<state_id>', strict_slashes=False)
def state_cities(state_id):
    """
    Method to render a list of cities for a given state
    """
    state = storage.get("State", state_id)
    if state:
        cities = sorted(state.cities, key=lambda x: x.name)
        return render_template("9-states.html", state=state, cities=cities)
    else:
        return render_template("9-states.html", state=None)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
