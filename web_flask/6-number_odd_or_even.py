#!/usr/bin/python3
"""
Simple Flask application returning Hello HBNB!
"""

from flask import Flask, render_template, abort

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

# Replaces underscore with space


def replace_underscores(text):
    return text.replace('_', ' ')

# Define a route for /c/<tex>


@app.route('/c/<text>', strict_slashes=False)
def display_c_text(text):
    """
    Route function for the '/c/<text>' URL.
    Returns: 'C'
    """
    return 'C {}'.format(replace_underscores(text))

# Display's Python Text.


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def display_python_text(text="is cool"):
    """
    Route function for the '/python/<text>' URL.
    Returns: 'Python ' followed by the value of the 'text' variable.
    """
    return 'Python {}'.format(replace_underscores(text))

# Check if the value of n is a digit (numeric)


@app.route('/number/<n>', strict_slashes=False)
def n_is_number(n):
    if n.isdigit():
        return f'{n} is a number'
    abort(404)

# Check if n is an integer


@app.route('/number_template/<n>', strict_slashes=False)
def render_number_template(n):
    if n.isdigit():
        return render_template('5-number.html', n=n)
    abort(404)


@app.route('/number_odd_or_even/<n>', strict_slashes=False)
def n_number_desc(n):
    if n.isdigit():
        if int(n) % 2 == 0:
            desc = 'even'
            return render_template(
                '6-number_odd_or_even.html',
                n=n,
                desc=desc
            )
        else:
            parity = 'odd'
            return render_template(
                '6-number_odd_or_even.html',
                n=n,
                desc=desc
            )
    abort(404)
# Run the application if the script is executed directly


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
