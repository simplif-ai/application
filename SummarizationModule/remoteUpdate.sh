#!/bin/bash

# AUTHORS: Ian Renfro
#
# PURPOSE: Use for downloading files from the git on a remote server without 
#             downloading the entire repo

echo "Downloading New Version of LexicalChain.py"
wget -O LexicalChainNew.py https://raw.githubusercontent.com/simplif-ai/Application/develop/SummarizationModule/LexicalChain.py -q --show-progress
echo "Downloading New Version of Summarizer.py"
wget -O SummarizerNew.py https://raw.githubusercontent.com/simplif-ai/Application/develop/SummarizationModule/Summarizer.py -q --show-progress 
echo "Downloading New Version of Passenger_WSGI.py"
wget -O passenger_wsgiNew.py https://raw.githubusercontent.com/simplif-ai/Application/develop/SummarizationModule/API/passenger_wsgi.py -q --show-progress
echo "Finished Downloading all files"
echo "Diff'ing LexicalChain.py.  Output is in LexicalChainDiff.txt"
echo -e "Local \t\t\t\t\t\t\t\t\t\t Server\n" > LexicalChainDiff.txt 
diff -Bys LexicalChain.py LexicalChainNew.py >> LexicalChainDiff.txt
echo "Diff'ing Summarizer.py.  Output is in SummarizerDiff.txt"
echo -e "Local \t\t\t\t\t\t\t\t\t\t Server\n" > SummarizerDiff.txt 
diff -Bys Summarizer.py SummarizerNew.py >> SummarizerDiff.txt
echo "Diff'ing passenger_wsgi.py.  Output is in PassengerDiff.txt"
echo -e "Local \t\t\t\t\t\t\t\t\t\t Server\n" > PassengerDiff.txt
diff -Bys passenger_wsgi.py passenger_wsgiNew.py >> PassengerDiff.txt
echo "Finished Diff'ing all files"
