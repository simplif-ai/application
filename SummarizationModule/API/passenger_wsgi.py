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

# Import the required packages
from flask import Flask, render_template, jsonify, request

# Create a Flask object
application = Flask(__name__, template_folder='')

# Form data variable name
var = 'text'

# Error Response that it returned if a request with an incorrect format is recieved
errResponse = "WELCOME to the Simplif.ai\'s API for summarization. Our full site is at %s\nThe method that you have " \
              "used, %s, is not supported. Please make a POST request. For the body of\nthe request please " \
              "include a json variable, with the name text, and the value should be the text that\nyou want to " \
              "summarize. For example the body of the request would look like:\n{\n\t\"%s\": \"Text that you wish " \
              "to summarize\"\n}\nFor the response the format will be an array that contains arrays of size three " \
              "where the first index\nof the arrays of size three is the sentence then the next index will be the " \
              "strength of the sentence\nand the last index will contain the position of the sentence in the " \
              "original input text. The array is\nsorted by strength of the sentence. For example the response " \
              "will look like:\n{\n\t\"%s\": [\n\t\t[\n\t\t\t\"this is\",\n\t\t\t1,\n\t\t\t2\n\t\t]," \
              "\n\t\t[\n\t\t\t\"a sample\",\n\t\t\t3,\n\t\t\t4\n\t\t],\n\t\t[\n\t\t\t\"list\",\n\t\t\t5," \
              "\n\t\t\t6\n\t\t],\n\t\t[\n\t\t\t\"for testing\",\n\t\t\t7,\n\t\t\t8\n\t\t],\n\t\t[\n\t\t\t\"json\"," \
              "\n\t\t\t9,\n\t\t\t0\n\t\t]\n\t]\n}"

# TODO Website url that needs to be inserted in the future
websiteURL = "__INSERT WEBAPP URL HERE__"

# =============================================================================

# Create the route /summarizeTEST
@application.route('/summarizeTEST')
def summarizeTEST():
        # Send an example of what the response would generally look like
	text = [('this is', 1, 2), ('a sample', 3, 4), ('list', 5, 6), ('for testing', 7, 8), ('json', 9, 0)]
	return jsonify({var:text})

# Create the route /summarize for the summarization module, accept the methods GET, HEAD, and POST
@application.route('/summarize', methods=['GET', 'POST'])
def summarize():
        # If there is a GET or HEAD request then send the redirect page because it is probably done from a browser
	if request.method != 'POST':
                # TODO Create an actual redirection page
		return render_template('redirect.html')
        # If our chosen variable name is included in the form data in the body
	if var in request.form:
                # Create an example response
		t = request.form[var].split(" ")
		res = []
		for x in range(len(t)):
			res.append((t[x], x * 10, x)) 
		return jsonify({var:res})	
        # If our chosen variable name is not included in the form body then send an error message
	else:
		return "MAKE SURE TO INCLUDE A VARIABLE \"%s\" IN THE BODY\n %s" % (var, (errResponse % (websiteURL, request.method, var, var)))

# Create an Errorhandler for incorrect method requests
@application.errorhandler(405)
def wrongMethod(error):
        # Send a well formatted error message back
	return (errResponse % (websiteURL, request.method, var, var))

if __name__ == '__main__':
    application.debug = True
    application.run()
