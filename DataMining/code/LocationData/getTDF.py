import nltk
from ujson import loads, dumps
from datetime import datetime
import os

# ALGO:
# read all files in the location dir
# -read line by line
# --get location delhi/'new york'
# --line->json->tagged_text->
# ---all nouns in the tagged text-> add to the tdf dictionary for the- respective location
#
