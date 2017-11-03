# Summarization Module
This document solely describes the codebase of the inner workings of the summarizer. For instructions on how to run
the API, please refer to the README.md in the API folder.

## LexicalChain.py
LexicalChain.py contains the code for the data structures used in the summarizer. `LexChainGroup`s store a collection
of `LexChain`s, which each contain a list of `LexWord`s contextually related to each other.

### LexWord
`LexWord` contains the information of a single candidate word.
#### Initialization:
    LexWord(word, synset)
#### Incrementing word counter:
    add_count()
LexWord also contains getters for `word`,`synset`, and `count`.

### LexChain
`LexChain` contains a list of `LexWord`s with semantic relations.
#### Initialization:
    LexChain(words=None, length=0, strength=0, wqlen = 10)
`wqlen` represents the number of words we most recently added that we want to check for contextual relations.
#### Adding a new word to the chain:
    add_word(word, synset)
#### Check the similarity of a new synset with the chain:
    get_simil(synset)
#### Obtain strength of chain:
    get_strength()
The strength is defined as the strength of the relationship between the words within the chain.
#### Obtain score of chain:
    get_score()
The score is defined as the relative value of importance of the chain compared to other chains.
#### Obtain key words of chain:
    get_key_words()
Returns words that are representative of the chain. Chooses by returning words that have counts higher than the
mean + 0.5 * standard deviation.
#### Obtain a shallow copy of the chain:
    get_copy()

### LexChainGroup
`LexChainGroup` contains a group of `LexChain`s built together from a text.
#### Initialization:
    LexChainGroup(chains=None, chain_cap=-1)
`chain_cap` represents the maximum amount of chains that the group is willing to hold. If this cap is exceeded, the
weakest chain is dropped from the group. If this is set to -1, there is no cap.
#### Obtain most relevant synset from a group of synsets:
    get_most_relevant(synsetset)
Use this to pick the correct definition for a word with multiple definitions.
#### Add a new word to the chain group:
    add_to_chain(word, synset):
#### Obtain strength of chain:
    get_strength()
Returns the sum of strengths of all chains.
#### Obtain most relevant chains:
    get_top_chains(n)
Returns the n highest scoring chains.
#### Obtain a shallow copy of the chain group:
    get_copy()

## Summarizer.py
Summarizer.py uses the data structures in LexicalChain.py to generate a summary from a given text.

#### Example local usage of the summarizer:
    # Read the file
    with open("sample.txt", 'r', encoding='utf-8') as f:
        text = f.read()

    # Initialize and use summarizer on text
    summ = Summarizer(text)
    ranked = summ.rank_sentences()

    # Print out 20% highest priority sentences
    total = len(ranked)
    for sent in ranked:
        if sent[1] < total * 0.2:
            print(sent[0])

A runner is also included in the testing folder for convenience.