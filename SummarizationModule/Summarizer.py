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

    def get_full_text(self):
        """ Getter for text """
        return self.full_text
