#!/usr/bin/python3
"""
Script that starts a Flask web application
"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def teardown_appcontext(self):
    """
    Teardown app context, close SQLAlchemy Session
    """
    storage.close()


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Route to display HTML page like 8-index.html
    """
    states = storage.all(State).values()
    return render_template('100-hbnb.html', states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
