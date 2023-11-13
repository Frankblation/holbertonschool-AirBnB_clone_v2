#!/usr/bin/python3
"""
Simple Flask application returning Hello HBNB!
"""

from flask import Flask, escape, request
import html

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

# Define a route for /c/<tex>


@app.route('/c/<text>', strict_slashes=False)
def display_c_text(text):
    """
    Route function for the '/c/<text>' URL.
    Returns: 'C'
    """
    return 'C {}'.format(escape(text.replace('_', ' ')))

@app.route('/python/<text>', strict_slashes=False)
def display_python(text="is cool"):
    """
    Route function for the '/python/<text>' URL.
    Returns: 'Python ' followed by the value of the 'text' variable.
    """
    formatted_text = escape(text.replace('_', ' '))
    return 'Python {}'.format(formatted_text)

# Run the application if the script is executed directly


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
