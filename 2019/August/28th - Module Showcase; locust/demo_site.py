"""A demo site that increments a counter with every new visitor"""

from flask import Flask
app = Flask(__name__)

visitor_count = 0

@app.route('/')
def hello():
    """On page visit increments and displays visitor count"""
    global visitor_count # Grabs the visitor_count global variable
    visitor_count += 1 # Increments the visitor_count global variable
    return f'There have been: {visitor_count} visitor(s)'

if __name__ == '__main__':
    app.run()