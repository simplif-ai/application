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
from flask_cors import CORS
from SummarizerWrapper import wrapper
from SummarizerTools import getText
from werkzeug import secure_filename

UPLOAD_FOLDER = os.path.basename('uploads')
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'pptx'])

# Create a Flask object
application = Flask(__name__, template_folder='')
CORS(application)

application.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Form data variable name
var = 'text'

# Error Response that it returned if a request with an incorrect format is recieved
errResponse = "WELCOME to the Simplif.ai\'s API for summarization. Our full site is at %s\nThe method that you have " \
              "used, %s, is not supported. Please make a POST request. For the body of the request please " \
              "include a json variable, with the name \'text\' whose value should be the text that you want to " \
              "summarize. For example the body of the request would look like:\n{\n\t\"%s\": \"Text that you wish " \
              "to summarize\"\n}\nFor the response, the format will be an array that contains arrays of size three " \
              "for which the first index is a sentence, the second index is the strength of that sentence, " \
              "and the third index is the position of the sentence in the " \
              "original input text. For example the response " \
              "will look like:\n{\n\t\"%s\": [\n\t\t[\n\t\t\t\"this is\",\n\t\t\t1,\n\t\t\t2\n\t\t]," \
              "\n\t\t[\n\t\t\t\"a sample\",\n\t\t\t3,\n\t\t\t4\n\t\t],\n\t\t[\n\t\t\t\"list\",\n\t\t\t5," \
              "\n\t\t\t6\n\t\t],\n\t\t[\n\t\t\t\"for testing\",\n\t\t\t7,\n\t\t\t8\n\t\t],\n\t\t[\n\t\t\t\"json\"," \
              "\n\t\t\t9,\n\t\t\t0\n\t\t]\n\t]\n}"

websiteURL = "http://simplif.ai.s3-website.us-east-2.amazonaws.com/"

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
		return render_template('redirect.html')
        # If our chosen variable name is included in the form data in the body
	if var in request.form:
		return jsonify({var: wrapper(request.form[var]), 'success': True})
        # If the request is in a json format versus a form data format
	elif request.is_json:
		content = request.get_json()
		if var in content:
			return jsonify({var: wrapper(content[var]), 'success': True})
		else:
			return jsonify({'error': ("MAKE SURE TO INCLUDE A VARIABLE %s IN THE BODY\n" + (errResponse % (websiteURL, request.method))) % var, 'success': False})
			
        # If our chosen variable name is not included in the form body then send an error message
	else:
		return jsonify({'error': ("MAKE SURE TO INCLUDE A VARIABLE %s IN THE BODY\n" + (errResponse % (websiteURL, request.method))) % var, 'success': False})

# Create an Errorhandler for incorrect method requests
@application.errorhandler(405)
def wrongMethod(error):
        # Send a well formatted error message back
		return jsonify({'error': (errResponse % (websiteURL, request.method)), 'success': False})

def allowed_file(filename):
	return filename[-3:].lower() in ALLOWED_EXTENSIONS

@application.route('/upload', methods=['POST'])
def upload_file():
	if request.method == 'POST':
		file = request.files['file']
		if file and allowed_file(file.filename):
			filename = secure_filename(file.filename)
			file.save(os.path.join(application.config['UPLOAD_FOLDER'], filename))
			text = getText(os.path.join(application.config['UPLOAD_FOLDER'], filename))
			text = text.strip()
			if text == '':
				return jsonify({'error': 'We were unable to find text in the file', 'success': False})
			return jsonify({'text': wrapper(text), 'success': True}), 200
                else:
                    return jsonify({'error': 'no file found or not an allowed extension/filename', 'success': False})
        else:
            return jsonify({'error': 'must be a post request to upload a file', 'success': False})

if __name__ == '__main__':
    application.debug = True
    application.run()
