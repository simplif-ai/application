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
    """ Class representing individual words within chains """

    def __init__(self, word, synset):
        """ Initialize field variables """
        self.word = word
        self.synset = synset
        self.count = 1

    def __repr__(self):
        """ String representation """
        return self.word

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

    def __init__(self, words=None, length=0, strength=0, wqlen = 10):
        """ Initialize field variables """
        self.words = dict()
        self.strength = 0
        self.length = 0
        self.q_length = wqlen
        self.word_q = []
        if words != None:
            self.words = words
            self.length = length
            self.strength = strength

    def __repr__(self):
        """ String representation """
        word_list = []
        for word in self.words:
            word_list.append(self.words[word].get_word())

        return str(word_list)

    def add_word(self, word, synset):
        """ Adds new word along with its synset into the chain """
        if word not in self.words:
            self.words[word] = LexWord(word, synset)
            self.word_q.append(word)
            for key in self.word_q:
                self.strength += 7 * wn.path_similarity(self.words[key].get_synset(), synset)
                if len(self.word_q) > self.q_length:
                    self.word_q.pop(0)
        else:
            self.words[word].add_count()
            self.strength += 10
            self.word_q.append(word)
            if len(self.word_q) > self.q_length:
                self.word_q.pop(0)
        self.length += 1

    def get_words(self):
        """ Getter function for word dictionary """
        return self.words

    def get_simil(self, synset):
        """ Uses basic heuristic to compare the relevance of a synset to the chain """
        #TODO: use a better heuristic
        highest = 0
        for key in self.word_q:
            simil = wn.path_similarity(self.words[key].get_synset(), synset)
            if simil > highest:
                highest = simil

        return highest

    def get_strength(self):
        """ Uses basic heuristic to compute the internal strength of the chain """
        #TODO: use a better heuristic
        return self.strength

    def get_score(self):
        """
        Obtains importance score of a chain

        Calculated as such:
        score = length * h_index (homogeneity)
        """
        h_index = 1 - (len(self.words.keys()) / self.length)

        return self.length * h_index

    def get_key_words(self):
        """
        Finds and returns the representative words of the chain

        Only keeps words with more than the average amount of word occurrences
        """
        #TODO: may need to filter out more than just half the words
        average = 0
        for key in self.words:
            average += self.words[key].get_count()
        average = average / len(self.words.keys())

        sd = 0
        for key in self.words:
            sd += (self.words[key].get_count() - average) ** 2
        sd = ((sd / len(self.words.keys())) ** 0.5)

        key_words = []
        for key in self.words:
            if self.words[key].get_count() >= average + 0.5 * sd:
                key_words.append(key)

        return key_words


class LexChainGroup:
    """ Class representing a possible grouping of chains """

    def __init__(self, chains=None, chain_cap=-1):
        """ Initialize field variables """
        self.chains = []
        if chains != None:
            self.chains = chains
        self.chain_cap = chain_cap

    def get_most_relevant(self, synsetset):
        """ Obtain the most relevant chain to the synset out of the chain group """
        maxscore = 0
        maxsyn = None
        for synset in synsetset:
            score = 0
            for chain in self.chains:
                simil = chain.get_simil(synset)
                if simil > score:
                    score = simil
            if score >= maxscore:
                maxscore = score
                maxsyn = synset
        return maxsyn

    def add_to_chain(self, word, synset):
        """ Add a word to one of the chains of the chain group """
        done = False
        max_simil = 0
        for chain in self.chains:
            simil = chain.get_simil(synset)
            if simil > max_simil and simil > 0.2:
                chain.add_word(word, synset)
                done = True

        if not done:
            newchain = LexChain()
            newchain.add_word(word, synset)
            self.chains.append(newchain)
            if self.chain_cap != -1 and len(self.chains) > self.chain_cap:
                min_ind = 0
                for i in range(len(self.chains)):
                    if self.chains[i].get_strength() < self.chains[min_ind].get_strength():
                        min_ind = i
                self.chains.pop(min_ind)

    def get_strength(self):
        """ Return the sum of all chains in the group """
        total = 0
        for chain in self.chains:
            total += chain.get_strength()
        return total

    def get_chains(self):
        """ Getter function for lexical chains """
        return self.chains

    def get_top_chains(self, n):
        """ Returns the most relevant chains of the group """
        scores = []
        score_map = dict()
        for chain in self.chains:
            sc = chain.get_score()
            scores.append(sc)
            score_map[sc] = chain
        scores.sort()
        schains = [score_map[x] for x in scores]
        skchains = []
        for chain in schains:
            skchains.append(chain.get_key_words())
        print(skchains[-n:])
        return skchains[-n:]
