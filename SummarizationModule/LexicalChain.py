"""
AUTHORS: Kevin Xia

PURPOSE:
    Class definitions for lexical chain tools.

DEVELOPER NOTES:
    None
"""

# =============================================================================
# Libraries and Global Variables
# =============================================================================

import nltk

# =============================================================================


class LexWord:
    """ Class representing individual words within chains. """

    def __init__(self, word, synset):
        """ Initialize field variables """
        self.word = word
        self.synset = synset
        self.count = 1

    def add_count(self):
        """ Adds another occurrence of word """
        self.count += 1

    def get_info(self):
        """ Getter function for all fields """
        return self.word, self.synset, self.count

    def get_word(self):
        """ Getter function for word """
        return self.word

    def get_synset(self):
        """ Getter function for synset """
        return self.synset

    def get_count(self):
        """ Getter function for count """
        return self.count


class LexChain:
    """ Class representing chains of words within the same lexical context """

    def __init__(self):
        """ Initialize field variables """
        pass


class LexChainGroup:
    """ Class representing a possible grouping of chains """

    def __init__(self):
        """ Initialize field variables """
        pass
