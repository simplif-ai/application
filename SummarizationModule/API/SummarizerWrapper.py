"""
AUTHORS: Ian Renfro

PURPOSE:
    Wrapper function for the summarization module.

DEVELOPER NOTES:
    None
"""

# =============================================================================
# Libraries and Global Variables
# =============================================================================
from Summarizer import Summarizer
# =============================================================================

def wrapper(inp):
	return Summarizer(inp).rank_sentences()

def main():
	print(wrapper("hello my name is joe.  I like apple.  I like pears.  i like oranges.  Coding is fun.  Physics is terrible."))

if __name__ == "__main__":
	main()
