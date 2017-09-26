from flask import Flask, render_template, jsonify, request
application = Flask(__name__)

# Code Pertaining to the Summarizer API

@application.route('/summarizeTEST')
def summarizeTEST():
	text = [('this is', 1, 2), ('a sample', 3, 4), ('list', 5, 6), ('for testing', 7, 8), ('json', 9, 0)]
	return jsonify({'text':text})


if __name__ == '__main__':
    application.debug = True
    application.run()
