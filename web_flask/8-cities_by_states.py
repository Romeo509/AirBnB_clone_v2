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


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """
    Method to render a list of states and their associated cities
    """
    states = storage.all('State').values()
    return render_template("8-cities_by_states.html", states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
