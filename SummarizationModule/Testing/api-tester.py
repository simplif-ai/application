"""
AUTHORS: Ian Renfro

PURPOSE:
    The codebase for testing the Summarizer API.

DEVELOPER NOTES:
    This is written in python with unittest
"""

# =============================================================================
# Libraries and Global Variables
# =============================================================================
import unittest
import json
import requests

URL = 'https://ir.thirty2k.com/summarize'
URL_FILE = 'https://ir.thirty2k.com/upload'
BASIC_PARAMS = {'text': 'hello this is a test of the api'}
BASIC_CONN = [['this is', 1, 2], ['a sample', 3, 4], ['list', 5, 6], ['for testing', 7, 8], ['json', 9, 0]]
PDF_CORR = open('201308FCR.txt', 'r').read()
TXT_CORR = open('hello_res.txt', 'r').read()
PPTX_CORR = open('pss.txt', 'r').read()
ERR_CORR = open('error.txt', 'r').read()

# =============================================================================

class APItest(unittest.TestCase):

    def makeRequest(self, inp):
        r = requests.post(URL, data=inp)
        json_data = json.loads(r.text)
        self.assertEqual(json_data['success'], True)
        return json_data['text']

    def test_basicConnection(self):
        r = requests.get(URL+'TEST')
        json_data = json.loads(r.text)
        self.assertEqual(json_data['text'], BASIC_CONN)

    def test_basic(self):
        arr = self.makeRequest({'text':"I hit the baseball with a bat."})
        self.assertEqual(arr, [["I hit the baseball with a bat.",0,0]])

    def test_empty(self):
        arr = self.makeRequest({'text':""})
        self.assertEqual(arr, [])

    def test_sentenceCollection(self):
        arr = self.makeRequest({'text':"I like apples. I like bananas. I like oranges. I like grapes. I love oranges."})
        self.assertEqual(arr, [['I like apples.', 2, 0], ['I like bananas.', 3, 1], ['I like oranges.', 0, 2], ['I like grapes.', 4, 3], ['I love oranges.', 1, 4]])

    def test_uploadPDF(self):
        fin = open('201308FCR.pdf', 'rb')
        files = {'file': fin}
        try:
            r = requests.post(URL_FILE, files=files)
        finally:
            fin.close()
        self.assertEqual(PDF_CORR, r.text)

    def test_uploadTXT(self):
        fin = open('hello.txt', 'rb')
        files = {'file': fin}
        try:
            r = requests.post(URL_FILE, files=files)
        finally:
            fin.close()
        self.assertEqual(TXT_CORR, r.text)

    def test_uploadPPTX(self):
        fin = open('pss.pptx', 'rb')
        files = {'file': fin}
        try:
            r = requests.post(URL_FILE, files=files)
        finally:
            fin.close()
        self.assertEqual(PPTX_CORR, r.text)

    def test_uploadInvalid(self):
        fin = open('api-tester.py', 'rb')
        files = {'file': fin}
        try:
            r = requests.post(URL_FILE, files=files)
        finally:
            fin.close()
        self.assertEqual(ERR_CORR, r.text)


if __name__ == '__main__':
    unittest.main()
