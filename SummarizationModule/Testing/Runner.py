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

from time import time
from SummarizationModule.Summarizer import Summarizer
from SummarizationModule.SummarizerTools import SummarizerTools

# =============================================================================


def main():
    """ Main method for initializing a run """

    #st = SummarizerTools()
    #print(st.extract_ppt("testppt.pptx"))


    t0 = time()
    prop = 1.0
    with open("blah.txt", 'r', encoding='utf-8') as f:
        text = f.read()
    text = text[:int(len(text) * prop)]
    print(len(text))
    tester = Summarizer(text)
    ranked = tester.rank_sentences()
    total = len(ranked)
    for sent in ranked:
        if sent[1] < total * 0.3:
            print(sent[0])
    t1 = time()
    print(t1 - t0)


if __name__ == "__main__":
    """ Run main if this python file is executed """
    main()
