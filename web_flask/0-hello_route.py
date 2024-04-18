#!/usr/bin/python3
""" Start the Flask application """

from flask import Flask

# Create a Flask application object named app
app = Flask(__name__)

# Define the route for /airbnb-onepage/
@app.route('/airbnb-onepage/', strict_slashes=False)
def hello_hbnb():
    """ Return Hello HBNB """
    return "Hello HBNB!"

# Ensure the Flask application is run when this script is executed directly
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
