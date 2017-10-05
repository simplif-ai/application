"""
AUTHORS: Kevin Xia

PURPOSE:
    Main body of summarizer code.

DEVELOPER NOTES:
    None
"""

# =============================================================================
# Libraries and Global Variables
# =============================================================================

import nltk
from nltk.corpus import wordnet as wn
from SummarizationModule.LexicalChain import LexChainGroup

# =============================================================================


class Summarizer:
    """ Summarizer objects generated to summarize code """

    def __init__(self, full_text):
        """ Initialize field variables """
        self.full_text = full_text

    def extract_nouns(self):
        """ Extracts and returns all nouns from a body of text """
        words = nltk.word_tokenize(self.full_text)
        tagged_words = nltk.pos_tag(words)
        nouns = []
        for (word, pos) in tagged_words:
            if pos[:2] == "NN":
                nouns.append(word)
        return nouns

    def extract_sentences(self):
        """ Extracts and returns all sentences from a body of text """
        sents = nltk.sent_tokenize(self.full_text)
        return sents

    def find_best_chains(self, num_chains):
        """ Generates chains and returns strongest chains """
        lc_group = LexChainGroup()
        nouns = self.extract_nouns()
        for noun in nouns:
            sets = wn.synsets(noun, 'n')
            if len(sets) > 0:
                ss = lc_group.get_most_relevant(sets)
                lc_group.add_to_chain(noun, ss)
        top = lc_group.get_top_chains(num_chains)
        return top

    def get_full_text(self):
        """ Getter for text """
        return self.full_text
