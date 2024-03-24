#!/usr/bin/python3
""" Start the Flask application """

from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Return greeting for homepage """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    """ Return 'HBNB' """
    return "HBNB"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)