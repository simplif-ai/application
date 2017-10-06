"""
AUTHORS: Kevin Xia

PURPOSE:
    Unit tests for Summarizer.py

DEVELOPER NOTES:
    None
"""

# =============================================================================
# Libraries and Global Variables
# =============================================================================

import sys
sys.path.append('../../')

import unittest
from SummarizationModule.Summarizer import Summarizer

# =============================================================================


class TestNounExtraction(unittest.TestCase):
    """ Test cases for extract_nouns() """

    def test_basic(self):
        test_summ = Summarizer("I hit the baseball with a bat.")
        self.assertEqual(test_summ.extract_nouns(), ['baseball', 'bat'])

    def test_empty(self):
        test_summ = Summarizer("")
        self.assertEqual(test_summ.extract_nouns(), [])

    def test_saturated(self):
        test_summ = Summarizer("apple banana orange grape")
        self.assertEqual(test_summ.extract_nouns(), ['apple', 'banana', 'orange', 'grape'])

    def test_unsaturated(self):
        test_summ = Summarizer("five big quickly smelly")
        self.assertEqual(test_summ.extract_nouns(), [])


class TestSentenceExtraction(unittest.TestCase):
    """ Test cases for extract_sentences() """

    def test_basic(self):
        test_summ = Summarizer("I hit the baseball with a bat. I like food. Ms. Vincent is good at coding.")
        self.assertEqual(test_summ.extract_sentences(), ['I hit the baseball with a bat.', \
                                                         'I like food.', \
                                                         'Ms. Vincent is good at coding.'])

    def test_empty(self):
        test_summ = Summarizer("")
        self.assertEqual(test_summ.extract_sentences(), [])


if __name__ == "__main__":
    """ Run main if this python file is executed """
    unittest.main()
