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
