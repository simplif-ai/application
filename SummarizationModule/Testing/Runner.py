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
    tester = Summarizer("I hit a baseball with my bat. Audrey is a good coder. \
    It was a home run. The crowd cheered. I was very happy.")
    print(tester.extract_sentences())


if __name__ == "__main__":
    """ Run main if this python file is executed """
    main()
