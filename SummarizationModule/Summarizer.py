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

import sys
sys.path.append('../')

import nltk
from nltk.corpus import wordnet as wn
from SummarizationModule.LexicalChain import LexChainGroup

# =============================================================================


class Summarizer:
    """ Summarizer objects generated to summarize code """

    def __init__(self, full_text):
        """ Initialize field variables """
        self.full_text = full_text
        self.sents = nltk.sent_tokenize(self.full_text)
        print(len(self.sents))

    def extract_nouns(self):
        """ Extracts and returns all nouns from a body of text """
        words = nltk.word_tokenize(self.full_text)
        tagged_words = nltk.pos_tag(words)
        nouns = []
        for (word, pos) in tagged_words:
            if pos[:2] == "NN":
                nouns.append(word)
        return nouns

    def get_sentences(self):
        """ Returns all sentences from a body of text """
        return self.sents

    def find_best_chains(self, num_chains):
        """ Generates chains and returns strongest chains """
        lc_group = LexChainGroup(chain_cap = len(self.sents) // 6 + 1)
        nouns = self.extract_nouns()
        for noun in nouns:
            sets = wn.synsets(noun, 'n')
            if len(sets) > 0:
                ss = lc_group.get_most_relevant(sets)
                lc_group.add_to_chain(noun, ss)
        top = lc_group.get_top_chains(num_chains)
        return top

    def rank_sentences(self):
        """ Ranks sentences in order of relevance and returns exportable dataset """
        top_chains = self.find_best_chains(4)
        multiplier = 1.0
        used_chains = [False] * len(top_chains)
        final_dataset = []
        weights = []
        for sent in self.sents:
            sent_words = nltk.word_tokenize(sent)
            weight = 1
            used = False
            for word in sent_words:
                for i in range(len(top_chains)):
                    if word in top_chains[i]:
                        if not used and not used_chains[i]:
                            used_chains[i] = True
                            used = True
                            weight += 10
                        else:
                            weight += 1
            weight *= multiplier
            multiplier *= 0.95
            weights.append(weight)
        ranks = [a[0] for a in sorted(enumerate(sorted(enumerate(weights), key=lambda x:x[1], reverse=True)), \
            key=lambda x:x[1][0])]
        for i in range(len(self.sents)):
            final_dataset.append([self.sents[i], ranks[i], i])
        return final_dataset

    def get_full_text(self):
        """ Getter for text """
        return self.full_text
