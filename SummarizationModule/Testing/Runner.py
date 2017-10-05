"""
AUTHORS: Kevin Xia

PURPOSE:
    Script to run summarizer. Used for testing purposes.

DEVELOPER NOTES:
    None
"""

# =============================================================================
# Libraries and Global Variables
# =============================================================================

import sys
sys.path.append('../../')

from SummarizationModule.Summarizer import Summarizer

# =============================================================================


def main():
    """ Main method for initializing a run """
    with open("sample.txt", 'r') as f:
        text = f.read()
    tester = Summarizer(text)
    print(tester.rank_sentences())


if __name__ == "__main__":
    """ Run main if this python file is executed """
    main()
