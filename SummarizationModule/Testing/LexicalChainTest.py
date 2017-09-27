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

# =============================================================================


class TestLexWord(unittest.TestCase):
    """ Test cases for extract_nouns()"""

    def test_basic(self):
        test_word = LexWord("ball", None)
        self.assertEqual(str(test_word), "ball")

    def test_count(self):
        test_word = LexWord("ball", None)
        self.assertEqual(test_word.get_count(), 1)
        test_word.add_count()
        test_word.add_count()
        self.assertEqual(test_word.get_count(), 3)


if __name__ == "__main__":
    """ Run main if this python file is executed """
    unittest.main()
