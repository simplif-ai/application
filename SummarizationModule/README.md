# Summarization Module
This document solely describes the codebase of the inner workings of the summarizer. For instructions on how to run
the API, please refer to the README.md in the API folder.

## LexicalChain.py
LexicalChain.py contains the code for the data structures used in the summarizer. `LexChainGroup`s store a collection
of `LexChain`s, which each contain a list of `LexWord`s contextually related to each other.

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