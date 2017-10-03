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

    def test_basic(self):
        test_chain = LexChain()
        test_chain.add_word("hello", None)
        test_chain.add_word("world", None)
        wlist = test_chain.get_words()
        self.assertEqual(wlist["world"].get_word(), "world")


class TestLexChainGroup(unittest.TestCase):
    """ Test cases for LexChainGroup """

    def test_basic(self):
        test_group = LexChainGroup()
        test_group.add_to_chain("roll", wn.synsets("roll", 'n')[0])
        wlist = test_group.get_chains()[0].get_words()
        self.assertEqual(wlist["roll"].get_word(), "roll")


if __name__ == "__main__":
    """ Run main if this python file is executed """
    unittest.main()
