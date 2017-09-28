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

from SummarizationModule.Summarizer import Summarizer

# =============================================================================


def main():
    """ Main method for initializing a run """
    tester = Summarizer("I hit a baseball with my bat.")
    print(tester.extract_nouns())


if __name__ == "__main__":
    """ Run main if this python file is executed """
    main()
