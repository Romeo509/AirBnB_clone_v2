#!/usr/bin/python3

from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def close_session(exception):
    """Closes the SQLAlchemy session after each request."""
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """Retrieves all states and
       their cities, sorts them, and renders an HTML page."""
    states = storage.all('State')
    states.sort(key=lambda state: state.name)

    all_cities = {}
    for state in states:
        cities = []
        if hasattr(state, "cities"):
            cities = state.cities
        else:
            cities = storage.all('City', state_id=state.id)
        cities.sort(key=lambda city: city.name)
        all_cities[state.id] = cities

    return render_template(
        'cities_by_states.html',
        states=states,
        all_cities=all_cities
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
