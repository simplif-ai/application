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
        pass

    def get_full_text(self):
        return self.full_text
