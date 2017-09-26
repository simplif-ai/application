"""
AUTHORS: Ian Renfro

PURPOSE:
    The codebase for the Summarizer API.

DEVELOPER NOTES:
    This is written in python with flask.
"""

# =============================================================================
# Libraries and Global Variables
# =============================================================================

from flask import Flask, render_template, jsonify, request

# Create a Flask object
application = Flask(__name__)

# =============================================================================

# Create the route /summarizeTEST
@application.route('/summarizeTEST')
def summarizeTEST():
        # Send a example of what the response would generally look like
	text = [('this is', 1, 2), ('a sample', 3, 4), ('list', 5, 6), ('for testing', 7, 8), ('json', 9, 0)]
	return jsonify({'text':text})


if __name__ == '__main__':
    application.debug = True
    application.run()
