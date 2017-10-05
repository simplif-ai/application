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
#BASIC_RESPONSE = [['hello', 0, 0], ['this', 10, 1], ['is', 20, 2], ['a', 30, 3], ['test', 40, 4], ['of', 50, 5], ['the', 60, 6], ['api', 70, 7]]

# =============================================================================

class APItest(unittest.TestCase):

    def correctResponse(self, x):
        t = x.split(" ")
        res = []
        for x in range(len(t)):
            res.append([t[x], x * 10, x]) 
        return res

    def test_basicConnection(self):
        r = requests.get(URL+'TEST')
        json_data = json.loads(r.text)
        self.assertEqual(json_data['text'], BASIC_CONN)

    def test_basicResponse(self):
        r = requests.post(URL, data=BASIC_PARAMS)
        json_data = json.loads(r.text)
        self.assertEqual(json_data['text'], self.correctResponse(BASIC_PARAMS['text']))

if __name__ == '__main__':
    unittest.main()
