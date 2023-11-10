#!/usr/bin/python3
"""
Simple Flask application returning Hello HBNB!
"""

from flask import Flask

# Create a Flask web application instance
app = Flask(__name__)

# Define a route for the root URL ('/')

@app.route('/', strict_slashes=False)
def hi_there():
    """
    Route function for the root URL.
    Returns: 'Hello HBNB!'
    """
    return 'Hello HBNB!'

# Define a route for '/hbnb'

@app.route('/hbnb', strict_slashes=False)
def hi_hbnb():
    """
    Route function for the '/hbnb' URL.
    Returns: 'HBNB'
    """
    return 'HBNB'


# Run the application if the script is executed directly
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

