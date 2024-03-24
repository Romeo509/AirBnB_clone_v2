#!/usr/bin/python3
""" Start the Flask application """

from flask import Flask, request

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def greet_hbnb():
    """ Display a greeting message """
    return 'Hello HBNB!'


@app.route('/hbnb')
def display_hbnb():
    """ Display 'HBNB' """
    return 'HBNB'


@app.route('/c/<text>')
def display_c_text(text):
    """ Display 'C ' followed by the value of text """
    text = text.replace('_', ' ')
    return 'C {}'.format(text)


@app.route('/python/', defaults={'text': 'is cool'})
@app.route('/python/<text>')
def display_python_text(text):
    """ Display 'Python ' followed by the value of text """
    text = text.replace('_', ' ') if text else 'is cool'
    return 'Python {}'.format(text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
