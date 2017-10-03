"""
AUTHORS: Kevin Xia

PURPOSE:
    Unit tests for LexicalChain.py

DEVELOPER NOTES:
    None
"""

# =============================================================================
# Libraries and Global Variables
# =============================================================================

import unittest
from SummarizationModule.LexicalChain import LexWord, LexChain, LexChainGroup
from nltk.corpus import wordnet as wn

# =============================================================================


class TestLexWord(unittest.TestCase):
    """ Test cases for LexWord """

    def test_basic(self):
        test_word = LexWord("ball", None)
        self.assertEqual(str(test_word), "ball")

    def test_count(self):
        test_word = LexWord("ball", None)
        self.assertEqual(test_word.get_count(), 1)
        test_word.add_count()
        test_word.add_count()
        self.assertEqual(test_word.get_count(), 3)

    def test_info(self):
        syn = wn.synsets("roll", 'n')[0]
        test_word = LexWord("roll", syn)
        res_word, res_syn, res_count = test_word.get_info()
        self.assertEqual(res_word, "roll")
        self.assertEqual(res_syn, syn)
        self.assertEqual(res_count, 1)


class TestLexChain(unittest.TestCase):
    """ Test cases for LexChain """


class TestLexChainGroup(unittest.TestCase):
    """ Test cases for LexChainGroup """


if __name__ == "__main__":
    """ Run main if this python file is executed """
    unittest.main()
