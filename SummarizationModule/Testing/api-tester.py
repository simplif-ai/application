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
BASIC_PARAMS = {'text': 'hello this is a test of the api'}
BASIC_CONN = [['this is', 1, 2], ['a sample', 3, 4], ['list', 5, 6], ['for testing', 7, 8], ['json', 9, 0]]

# =============================================================================

class APItest(unittest.TestCase):

    def correctResponse(self, x):
        t = x.split(" ")
        res = []
        for x in range(len(t)):
            res.append([t[x], x * 10, x]) 
        return res

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
        self.assertEqual(arr, [ [ "I like apples.", 3, 0 ], [ "I like bananas.", 4, 1 ], [ "I like oranges.", 1, 2 ], [ "I like grapes.", 0, 3 ], [ "I love oranges.", 2, 4 ] ])


if __name__ == '__main__':
    unittest.main()
