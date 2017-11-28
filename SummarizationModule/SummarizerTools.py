"""
AUTHORS: Kevin Xia

PURPOSE:
    Used for summarizing strange file formats.

DEVELOPER NOTES:
    None
"""

# =============================================================================
# Libraries and Global Variables
# =============================================================================

import sys
sys.path.append('../')

from pptx import Presentation
import subprocess
import time

# =============================================================================


class SummarizerTools:
    """ Summarizer Tool objects generated to deal with strange file formats """

    def __init__(self):
        """ Initialize field variables """

    def extract_ppt(self, filename):
        """ Extracts text from ppt files """
        prs = Presentation(filename)

        sents = []
        for slide in prs.slides:
            for shape in slide.shapes:
                sents.append(shape.text)

        text = ""
        for sent in sents:
            sentstr = sent.strip()
            text += sentstr
            if sentstr[-1] != '.' and sentstr[-1] != '!' and sentstr[-1] != '?':
                text += '.'
            text += ' '

        return text

    def extract_pdf(self, path):
        subprocess.Popen(["pdftotext", path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    def extract_text(self, path):
        f = open(path, 'r')
        res = f.read()
        f.close()
        return res

def getText(path):
	st = SummarizerTools()
	ext = path[-3:].lower()
	if ext == 'ppt':
		return st.extract_ppt(path)
	elif ext == 'pdf':
		st.extract_pdf(path)
		time.sleep(1)
		return st.extract_text(path[:-3] + 'txt')
	elif ext == 'txt':
		return st.extract_text(path)
