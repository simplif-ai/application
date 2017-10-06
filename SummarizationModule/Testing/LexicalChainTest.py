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

import sys
sys.path.append('../../')

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

    def test_simil(self):
        test_chain = LexChain()
        test_chain.add_word("person", wn.synsets("person", 'n')[0])
        test_chain.add_word("human", wn.synsets("human", 'n')[0])
        simil = test_chain.get_simil(wn.synsets("man", 'n')[0])
        self.assertGreater(simil, 0.2)

    def test_strength(self):
        test_chain = LexChain()
        test_chain.add_word("person", wn.synsets("person", 'n')[0])
        test_chain.add_word("human", wn.synsets("human", 'n')[0])
        test_chain.add_word("man", wn.synsets("man", 'n')[0])
        test_chain.add_word("person", wn.synsets("person", 'n')[0])
        strength = test_chain.get_strength()
        self.assertGreater(strength, 17.0)

    def test_score(self):
        test_chain = LexChain()
        test_chain.add_word("person", wn.synsets("person", 'n')[0])
        test_chain.add_word("human", wn.synsets("human", 'n')[0])
        test_chain.add_word("man", wn.synsets("man", 'n')[0])
        test_chain.add_word("person", wn.synsets("person", 'n')[0])
        test_chain.add_word("person", wn.synsets("person", 'n')[0])
        score = test_chain.get_score()
        self.assertGreater(score, 1.0)
        self.assertLess(score, 3.0)

    def test_key_words(self):
        test_chain = LexChain()
        test_chain.add_word("person", wn.synsets("person", 'n')[0])
        test_chain.add_word("human", wn.synsets("human", 'n')[0])
        test_chain.add_word("man", wn.synsets("man", 'n')[0])
        test_chain.add_word("person", wn.synsets("person", 'n')[0])
        test_chain.add_word("person", wn.synsets("person", 'n')[0])
        key_words = test_chain.get_key_words()
        self.assertEqual(key_words, ["person"])


class TestLexChainGroup(unittest.TestCase):
    """ Test cases for LexChainGroup """

    def test_basic(self):
        test_group = LexChainGroup()
        test_group.add_to_chain("roll", wn.synsets("roll", 'n')[0])
        wlist = test_group.get_chains()[0].get_words()
        self.assertEqual(wlist["roll"].get_word(), "roll")

    def test_relevance(self):
        test_group = LexChainGroup()
        test_group.add_to_chain("roll", wn.synsets("roll", 'n')[0])
        test_group.add_to_chain("roll", wn.synsets("roll", 'n')[0])
        test_group.add_to_chain("roll", wn.synsets("roll", 'n')[0])
        most_relevant = test_group.get_most_relevant(wn.synsets("roll", 'n'))
        self.assertEqual(most_relevant, wn.synsets("roll", 'n')[0])

    def test_strength(self):
        test_group1 = LexChainGroup()
        test_group2 = LexChainGroup()
        test_group1.add_to_chain("roll", wn.synsets("roll", 'n')[0])
        test_group1.add_to_chain("roll", wn.synsets("roll", 'n')[0])
        test_group1.add_to_chain("roll", wn.synsets("roll", 'n')[0])
        test_group2.add_to_chain("roll", wn.synsets("roll", 'n')[0])
        test_group2.add_to_chain("roll", wn.synsets("roll", 'n')[0])
        test_group2.add_to_chain("roll", wn.synsets("roll", 'n')[1])
        self.assertGreater(test_group1.get_strength(), test_group2.get_strength())

    def test_top_chains(self):
        test_group = LexChainGroup()
        test_group.add_to_chain("person", wn.synsets("person", 'n')[0])
        test_group.add_to_chain("person", wn.synsets("person", 'n')[0])
        test_group.add_to_chain("human", wn.synsets("human", 'n')[0])
        test_group.add_to_chain("man", wn.synsets("man", 'n')[0])
        test_group.add_to_chain("sausage", wn.synsets("sausage", 'n')[0])
        best_chain = test_group.get_top_chains(1)
        self.assertEqual(best_chain, [['person']])

if __name__ == "__main__":
    """ Run main if this python file is executed """
    unittest.main()
