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

from nltk.corpus import wordnet as wn

# =============================================================================


class LexWord:
    """ Class representing individual words within chains. """

    def __init__(self, word, synset):
        """ Initialize field variables """
        self.word = word
        self.synset = synset
        self.count = 1

    def __repr__(self):
        """ String representation """
        return word

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

    def __init__(self, words):
        """ Initialize field variables """
        self.words = dict()
        if words != None:
            self.words = words

    def __repr__(self):
        """ String representation """
        wlist = []
        for word in self.words:
            wlist.append(self.words[word].getWord())
        return str(wlist)

    def add_word(self, word, synset):
        """ Adds new word along with its synset into the chain """
        if word not in self.words:
            self.words[word] = LexWord(word, synset)
        else:
            self.words[word].addCount()

    def get_words(self):
        """ Getter function for word dictionary """
        return self.words

    def get_simil(self, synset):
        """ Uses basic heuristic to compare the relevance of a synset to the chain """
        #TODO: use a better heuristic
        highest = 0
        for key in self.words:
            simil = wn.path_similarity(self.words[key].get_synset(), synset)
            if simil > highest:
                highest = simil
        return highest

    def get_strength(self):
        """ Uses basic heuristic to compute the internal strength of the chain """
        #TODO: rework this so it updates dynamically
        #TODO: use a better heuristic
        total = 0
        for key in self.words:
            total += (self.words[key].get_count() - 1) * 10
            for key2 in self.words:
                if key != key2:
                    total += 7 * wn.path_similarity(self.words[key].get_synset(), self.words[key2].get_synset())
        return total


class LexChainGroup:
    """ Class representing a possible grouping of chains """

    def __init__(self):
        """ Initialize field variables """
        pass
